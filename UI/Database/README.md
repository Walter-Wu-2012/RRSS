# --Database connector--

# USER Table

##select one row
"using user_ID to get one user data from user table"

input: userID

output: user instance

*for example:*

    user1 = user(user_ID = 5)

    print(user1.username)


##delete data from user table
we can use the function del_table to delete the data we want
input: table name,

*for example:*

    del_info('user',user_ID = 5)

##add data from table
we can use the function add_table to add the data we want
*for example:*

    add_info("user",username="Lu",user_ID = 1, Pwd = "123456", Birthday = "2012.12.12",Gender ="male", Perference = "touching fish")


#--------------------------
#user_info table
##select one row
"using user_ID and time to get one user_info data from user_info table"

input: userID, time

output: user_info instance

*for example:*

    user1 = user_info(user_ID = 5,time = "2021-12-21 00:00:00")

    print(user1.username)

## select multiple rows

*for example:*

    user_info1= get_table("user_info",time1 = "2021-12-21 00:00:00",time2 = "2021-12-30 00:00:00", user_ID = 6)



##delete data from user_info table
we can use the function del_table to delete the data we want
input: table name,condition(Blood_pressure,Heartrate,humidity,ID,Location,Temperature,Time,User_ID,Weather) 
(for condition, you can use some of them, just choose the conditions you need and input them.)
*for example:*

    del_info('user_info',user_ID = 5)
or
    
    del_info('user_info',ID = 5,Location = "tokyo")

##add data from table
we can use the function add_table to add the data we want
input: table name,condition(Blood_pressure,Heartrate,humidity,Location,Temperature,Time,User_ID,Weather) 
(for condition, you can use some of them, just choose the conditions you need and input them.)
    
    add_info("user_info",Blood_pressure=" ",Heartrate = " ", Humidity = " ",Location ="  ", Temperature = " ",Time = " "%datatime format, User_ID=  ,Weather= " ")


#--------------------------
#schedule table
##select one row
    "using user_ID and time to get one  data from schedule table"
input: userID and time

output: schedule instance

*for example:*

    schedule1 = schedule(user_ID = 5,time = "2021-12-21 00:00:00")

    print(schedule1.Time)

## select multiple rows

*for example:*

    schedule = get_table("schedule",time1 = "2021-12-21 00:00:00",time2 = "2021-12-30 00:00:00", user_ID = 6)



##delete data from schedule table
we can use the function del_table to delete the data we want
input: table name,condition(comment,difficulty,time,ID,title,User_ID) 
(for condition, you can use some of them, just choose the conditions you need and input them.)
*for example:*

    del_info('schedule',user_ID = 5)
or
    
    del_info('schedule',ID = 5,time = "2021-12-21 00:00:00")

##add data from table
we can use the function add_table to add the data we want
input: table name,condition(comment,description,difficulty,hour,importance,time,title,User_ID,week,lasting period) 
(for condition, you can use some of them, just choose the conditions you need and input them.)

    add_info("schedule",comment = " ",description= " ",difficulty= " ",hour= " ",importance= " ",time= " ",title= " ",User_ID= ,week= " ",lasting period= " ")


#--------------------------
#mood_index table
##select one row
    "using user_ID and time to get one  data from mood_index table"
input: userID and time

output: mood_index instance

*for example:*

    mood = mood_index(user_ID = 5,time = "2021-12-21 00:00:00")

    print(mood.Time)

## select multiple rows

*for example:*

    mood = get_table("mood_index",time1 = "2021-12-21 00:00:00",time2 = "2021-12-30 00:00:00", user_ID = 6)



##delete data from mood_index table
we can use the function del_table to delete the data we want
input: table name,condition(focus,energy,time,ID,happiness,User_ID) 
(for condition, you can use some of them, just choose the conditions you need and input them.)
*for example:*

    del_info('mood_index',user_ID = 5)
or
    
    del_info('mood_index',ID = 5,time = "2021-12-21 00:00:00")

##add data from table
we can use the function add_table to add the data we want
input: table name,condition(chaotic,energy,happiness,focus,stress,time,happiness,User_ID) 
(for condition, you can use some of them, just choose the conditions you need and input them.)

    add_info("mood_index",chaotic= " ",energy= " ",happiness= " ",focus= " ",stress= " ",time= " ",happiness= " ",User_ID= " ")


#------------------------------------------------
#prediction table
##select one row
    "using user_ID and time to get one  data from prediction table"
input: userID and time

output: prediction instance

*for example:*

    pre1 = prediction(user_ID = 5,time = "2021-12-21 00:00:00")

    print(pre1.Time)

## select multiple rows

*for example:*

    pre = get_table("prediction",time1 = "2021-12-21 00:00:00",time2 = "2021-12-30 00:00:00", user_ID = 6)



##delete data from prediction table
we can use the function del_table to delete the data we want
input: table name,condition(focus,energy,time,ID,happiness,User_ID) 
(for condition, you can use some of them, just choose the conditions you need and input them.)
*for example:*

    del_info('prediction',user_ID = 5)
or
    
    del_info('prediction',ID = 5,time = "2021-12-21 00:00:00")

##add data from table
we can use the function add_table to add the data we want
input: table name,condition(chaotic,energy,happiness,focus,stress,time,happiness,User_ID) 
(for condition, you can use some of them, just choose the conditions you need and input them.)
    
    add_info("prediction",chaotic= " ",energy= " ",happiness= " ",focus= " ",stress= " ",time= " ",happiness= " ",User_ID= " ")


#------------------------------------------------
#recommend_range table
##select one row
    "using user_ID and type to get one  data from prediction table"
input: userID and type

output: recommend_range instance

*for example:*

    recomm = recommend_range(user_ID = 5,time = "2021-12-21 00:00:00")

    print(recomm.Time)

## select multiple rows

*for example:*

    recommend_ran = get_table("recommend_range",time1 = "2021-12-21 00:00:00",time2 = "2021-12-30 00:00:00", user_ID = 6)



##delete data from recommend_range table
we can use the function del_table to delete the data we want
input: table name,condition(commend,Duration,ID,User_ID) 
(for condition, you can use some of them, just choose the conditions you need and input them.)
*for example:*

    del_info('recommend_range',user_ID = 5)
or
    
    del_info('recommend_range',ID = 5,time = "2021-12-21 00:00:00")

##add data from table
we can use the function add_table to add the data we want
input: table name,condition(commend,desc1,Duration,User_ID,Type) 
(for condition, you can use some of them, just choose the conditions you need and input them.)
   
    add_info("recommend_info",commend= " ",desc1= " ",Duration= " ",User_ID= " ",Type= " ")


#-----------------------------------


#show table
we can use the function show_table to check the table we want

input:table name

*for example:*

    show_table("schedule")




