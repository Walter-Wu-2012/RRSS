import datetime

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

# del_info('mood_index_interpolation',user_ID = 6)

show_table("mood_index_interpolation2")
schedule = get_table("mood_index",time1 = "2022-01-11 00:00:00",time2 = "2022-01-13 00:00:00", user_ID = 6)
print(schedule)
