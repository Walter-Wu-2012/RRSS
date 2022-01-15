import datetime

from Database.usingdatabase import add_info, get_table

r1 = datetime.datetime.strptime('2022/01/13 16:30', "%Y/%m/%d %H:%M")
for i in range(7*2):
    r1 = r1 + datetime.timedelta(seconds=1800)
    print(r1)
    add_info("mood_index",User_ID = 6, Time = r1.strftime("%Y/%m/%d %H:%M"), Title = "test", Description = "for test",Importance=1,Difficulty=1,Comment=1,Lasting_period=1,feedback=1,Stress=1,Chaotic=1,Happiness=1,Energy=1,Focus=1)

# schedule = get_table("mood_index",time1 = "2022-01-11 00:00:00",time2 = "2022-01-13 00:00:00", user_ID = 6)
# print(schedule)