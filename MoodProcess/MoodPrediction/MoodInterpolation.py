import copy
from datetime import timedelta

import numpy as np
from scipy import interpolate

from Database.SqlExecuter import UsingMysql
from Database.usingdatabase import show_table, add_info


def interpolation(x, y):
    x = np.array(x)
    y = np.array(y)
    newx = []
    for i in range(int(x[-1]) + 1):
        newx.append(i)
    newx = np.array(newx)
    newy = np.zeros([5, newx.shape[0]])
    for i in range(5):
        f = interpolate.interp1d(x, y[:, i], kind='quadratic')
        newy[i, ...] = f(newx)

    return newx, newy

def InterpolationData(user):


    with UsingMysql(log_time=True) as um:
        sql = "select * from mood_index where User_ID=" + user + " order by Time DESC limit 48"
        um.cursor.execute(sql)
        rows = um.cursor.fetchall()
    x = []
    y = []
    starttime = rows[len(rows) - 1]['Time']
    lasttime = rows[len(rows)-1]['Time']
    x.append(0)
    y.append([rows[len(rows)-1]['Stress'], rows[len(rows)-1]['Chaotic'], rows[len(rows)-1]['Happiness'], rows[len(rows)-1]['Energy'], rows[len(rows)-1]['Focus']])
    td = timedelta(seconds=1800)
    count = 1
    for i in range(len(rows)-2,-1,-1):
        time = rows[i]['Time']
        if time > lasttime+td:

            gap = int((time - lasttime).total_seconds() / 1800) -1
            count = count + gap
        x.append(count)
        y.append([rows[i]['Stress'], rows[i]['Chaotic'], rows[i]['Happiness'], rows[i]['Energy'], rows[i]['Focus']])

        count = count+1
        lasttime = time

    newx, newy = interpolation(x, y)

    # print(newy)

    xtrue = [0 for i in range(len(newx))]

    print(x)

    for i in range(len(x)):
        xtrue[x[i]]=i
    print(xtrue)


    lastsavetime = getLastSaveTime(user)
    timecounter = copy.deepcopy(starttime)
    for i in range(len(x)):
        time = starttime+td*i
        if time>lastsavetime:
            if xtrue[i] == 0:
                schedule = getschedule(time, user, timecounter)
                add_info("mood_index", User_ID=user, Time=time, Title=schedule['Title'],
                         Description=schedule['Description'], Importance=schedule['Importance'], Difficulty=schedule['Difficulty'],
                         Comment=schedule['Comment'], Lasting_period=schedule['Lasting_period'], feedback=schedule['feedback'],
                         Stress=newy[0,i], Chaotic=newy[1,i], Happiness=newy[2,i], Energy=newy[3,i],
                         Focus=newy[4,i])

            else:
                timecounter = copy.deepcopy(time)
                row = rows[xtrue[i]]
                add_info("mood_index", User_ID=row['User_ID'], Time=row['Time'], Title=row['Title'],
                         Description=row['Description'], Importance=row['Importance'], Difficulty=row['Difficulty'],
                         Comment=row['Comment'], Lasting_period=row['Lasting_period'], feedback=row['feedback'],
                         Stress=row['Stress'], Chaotic=row['Chaotic'], Happiness=row['Happiness'], Energy=row['Energy'],
                         Focus=row['Focus'])


def getLastSaveTime(user):
    with UsingMysql(log_time=True) as um:
        sql = "select Time from mood_index_interpolation where User_ID=" + int(user) + " order by Time DESC limit 1"
        um.cursor.execute(sql)
        endtime = um.cursor.fetchone()['Time']

    return endtime

def getschedule(time, user, timecounter):
    with UsingMysql(log_time=True) as um:
        sql = "select * from schedule where User_ID=" + int(user) + " order by Time DESC limit 1"
        um.cursor.execute(sql)
        rows = um.cursor.fetchall()

    if len(rows)==0:
        gap = (time - timecounter).total_seconds()/3600
        if time.hour>=8 and time.hour<=23:
            schedule={'Title':'Free time', 'Description':'nothing to do', 'Importance':1, 'Difficulty':1, 'Comment':6, 'Lasting_period':gap, 'feedback':0}
        else:
            schedule = {'Title': 'Sleep', 'Description': 'Just for sleeping', 'Importance': 1, 'Difficulty': 1,
                        'Comment': 1, 'Lasting_period': gap, 'feedback': 0}
    return schedule

if __name__ == '__main__':
    # InterpolationData('6')
    show_table("mood_index")