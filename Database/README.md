# Database connector
##get data from table
###user table
    "using username or user_ID to find data"
*for example:*

user1 = user(user_ID = 5)

print(user1.username)
###user_info table
    "using time and user_ID to find data"
*for example:*

show_table("user_info")

user1 = User_info(time="202112262107", user_ID=6)

###schedule table
    "using title and user_ID to find data"
schedule1 = Schedule(title="shopping", user_ID=6)
print(schedule1.Time)
###schedule table
    "using time and user_ID to find data"
mood_index = Mood_index(time="20210909", user_ID=6)
print(mood_index.Time)
###Prediction table
    "using time and user_ID to find data"
prediction = Prediction(time="20210909", user_ID=6)
print(prediction.Time)
###recommend_range table
    "using time and user_ID to find data"
recommend_range = Recommend_range(time="202112262107", user_ID=6)
print(recommend_range.Desc1)
##show table
we can use the function show_table to check the table we want
##delete data from table
we can use the function del_table to delete the data we want
##add data from table
we can use the function add_table to add the data we want




