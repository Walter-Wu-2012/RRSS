import copy
import datetime
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
        f = interpolate.interp1d(x, y[:, i], kind='cubic')
        newy[i, ...] = f(newx)

    return newx, newy

def InterpolationData(user):


    with UsingMysql(log_time=True) as um:
        # sql = "select * from mood_index where User_ID=" + user + " order by Time DESC limit 48"
        sql = "select * from mood_index where User_ID=" + user + " order by Time DESC"
        um.cursor.execute(sql)
        rows = um.cursor.fetchall()
    x = []
    y = []
    starttime = rows[len(rows) - 1]['Time']
    lasttime = rows[len(rows)-1]['Time']
    print(rows[len(rows)-1]['Time'])
    x.append(0)
    y.append([rows[len(rows)-1]['Stress'], rows[len(rows)-1]['Chaotic'], rows[len(rows)-1]['Happiness'], rows[len(rows)-1]['Energy'], rows[len(rows)-1]['Focus']])
    td = timedelta(seconds=1800)
    count = 1
    for i in range(len(rows)-2,-1,-1):
        time = rows[i]['Time']
        if time > lasttime+td:
            # print(time)
            gap = int((time - lasttime).total_seconds() / 1800) -1
            count = count + gap
        x.append(count)
        y.append([rows[i]['Stress'], rows[i]['Chaotic'], rows[i]['Happiness'], rows[i]['Energy'], rows[i]['Focus']])

        count = count+1
        lasttime = time

    newx, newy = interpolation(x, y)

    # print(newy)

    xtrue = [-1 for i in range(len(newx))]

    # print(x)

    for i in range(len(x)):
        xtrue[x[i]]=i
    # print(xtrue)

    rows = rows[::-1]
    lastsavetime = getLastSaveTime(user)
    # print(lastsavetime)
    timecounter = copy.deepcopy(starttime)
    for i in range(len(newx)):
        time = starttime+td*i
        # print(time)
        if time>lastsavetime:
            if xtrue[i] == -1:
                schedule = getschedule(time, user, timecounter)

                add_info("mood_index_interpolation", User_ID=user, Time=str(time), Title=schedule['Title'],
                         Description=schedule['Description'], Importance=schedule['Importance'], Difficulty=schedule['Difficulty'],
                         Comment=schedule['Comment'], Lasting_period=schedule['Lasting_period'], feedback=schedule['feedback'],
                         Stress=newy[0,i], Chaotic=newy[1,i], Happiness=newy[2,i], Energy=newy[3,i],
                         Focus=newy[4,i])

            else:
                timecounter = copy.deepcopy(time)
                row = rows[xtrue[i]]
                add_info("mood_index_interpolation", User_ID=row['User_ID'], Time=str(row['Time']), Title=row['Title'],
                         Description=row['Description'], Importance=row['Importance'], Difficulty=row['Difficulty'],
                         Comment=row['Comment'], Lasting_period=row['Lasting_period'], feedback=row['feedback'],
                         Stress=row['Stress'], Chaotic=row['Chaotic'], Happiness=row['Happiness'], Energy=row['Energy'],
                         Focus=row['Focus'])


def getLastSaveTime(user):
    with UsingMysql(log_time=True) as um:
        sql = "select Time from mood_index_interpolation where User_ID=" + user + " order by Time DESC limit 1"
        um.cursor.execute(sql)
        endtime = um.cursor.fetchone()
        # print(endtime)
        if endtime==None:
            endtime= datetime.datetime.strptime('1977-01-01 00:00', "%Y-%m-%d %H:%M")
        else:
            endtime = endtime["Time"]

    return endtime

def getschedule(time, user, timecounter):
    with UsingMysql(log_time=True) as um:
        sql = "select * from schedule where User_ID=" + user + " and Time<='"+str(time)+ "' and Time2>='"+str(time)+"'  order by Time DESC limit 1"
        # print(sql)
        um.cursor.execute(sql)
        rows = um.cursor.fetchall()

    if len(rows)==0:
        if time.hour>=8 and time.hour<=23:
            if timecounter.hour<8:
                timecounter = time.replace(hour=8)
                timecounter = timecounter.replace(minute=0)
            gap = (time - timecounter).total_seconds() / 3600
            schedule={'Title':'Free time', 'Description':'nothing to do', 'Importance':1, 'Difficulty':1, 'Comment':6, 'Lasting_period':gap, 'feedback':0}
        else:
            if timecounter.hour < 23 and timecounter.hour > 8:
                # print(timecounter)
                timecounter = time.replace(hour=23)-timedelta(days=1)
                timecounter = timecounter.replace(minute=0)

                # print(time)
                # print(timecounter)
                # print('---------')
            gap = (time - timecounter).total_seconds() / 3600 - 0.5
            schedule = {'Title': 'Sleep', 'Description': 'Just for sleeping', 'Importance': 1, 'Difficulty': 1,
                        'Comment': 1, 'Lasting_period': gap, 'feedback': 0}
    else:
        lastperiod = (time - rows[0]['Time']).total_seconds()/3600-0.5
        schedule = {'Title': rows[0]['Title'], 'Description': rows[0]['Description'], 'Importance': rows[0]['Importance'], 'Difficulty': rows[0]['Difficulty'],
                    'Comment': rows[0]['Comment'], 'Lasting_period': lastperiod, 'feedback': rows[0]['feedback']}
    return schedule

if __name__ == '__main__':
    InterpolationData('6')
    # show_table("mood_index")
    # r1 = datetime.datetime.strptime('2022-01-12 17:00', "%Y-%m-%d %H:%M")
    # r2 = datetime.datetime.strptime('2022-01-12 15:00', "%Y-%m-%d %H:%M")
    # r1 = datetime.datetime.strptime('2022-01-12 17:30', "%Y-%m-%d %H:%M")
    # timecounter = r1.replace(hour=8)
    # timecounter = timecounter.replace(minute=0)
    # r2 = datetime.datetime.strptime('2022-01-12 15:00', "%Y-%m-%d %H:%M")
    # print(timecounter)
    # schedule = getschedule(r1, '6', r2)
    # print(schedule)