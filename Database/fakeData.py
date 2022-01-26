import csv
import datetime

import numpy as np

from Database.usingdatabase import add_info, get_table, show_table, del_info
#
# r1 = datetime.datetime.strptime('2022/01/13 17:00', "%Y/%m/%d %H:%M")
# for i in range(4*7*48):
#     r1 = r1 + datetime.timedelta(seconds=1800)
#     print(r1)
#     add_info("mood_index_interpolation",User_ID = 6, Time = r1.strftime("%Y/%m/%d %H:%M"), Title = "test", Description = "for test",Importance=1,Difficulty=1,Comment=1,Lasting_period=1,feedback=1,Stress=1,Chaotic=1,Happiness=1,Energy=1,Focus=1)

# add_info("schedule",User_ID = 6, Title='shopping', Description='buy food for tomorrow', Time = "2022-01-12 15:30:0",Time2 = "2022-01-12 18:00:00",Importance=3,Difficulty=1,Comment=1,feedback=0)
# schedule = get_table("mood_index",time1 = "2022-01-11 00:00:00",time2 = "2022-01-13 00:00:00", user_ID = 6)
# print(schedule)

# show_table("schedule")



# schedule = get_table("mood_index",time1 = "2022-01-11 00:00:00",time2 = "2022-01-13 00:00:00", user_ID = 6)
# print(schedule)

def csv2db(filename):

    with open(filename, encoding='utf-8-sig') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            # print(row[0].__str__())
            string = row[1].split(' ')
            y = int(string[0].split("/")[2])
            if int(float(row[0]))>990:
                d = int(string[0].split("/")[0])
                m = int(string[0].split("/")[1])
            else:
                m = int(string[0].split("/")[0])
                d = int(string[0].split("/")[1])
            h = int(string[1].split(":")[0])
            mm = int(string[1].split(":")[1])
            # print(y, m, d, h, mm, 0)
            t = datetime.datetime(y, m, d, h, mm, 0)
            print(t)
            # d = datetime.datetime.strptime(row[1], "m/d/yyyy h:m")
            add_info("mood_index", User_ID=6, Time=t.strftime('%Y-%m-%d %H:%M:%S'), Title=row[2],
                     Description=row[3], Importance=int(row[4]), Difficulty=int(row[5]), Comment=int(row[6]), Lasting_period=float(row[7]), feedback=float(row[8]),
                     Stress=float(row[9]), Chaotic=float(row[10]), Happiness=float(row[11]), Energy=float(row[12]), Focus=float(row[13]))

if __name__ == '__main__':
    # del_info('mood_index', user_ID=6)
    # csv2db('C:\\Users\\Administrator\\PycharmProjects\\RRSS\\MoodProcess\\MoodPrediction\\datasets\\lzg2.csv')
    show_table("mood_index_interpolation2")
    # del_info('mood_index_interpolation', user_ID=6)