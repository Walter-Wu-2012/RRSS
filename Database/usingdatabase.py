from Database.SqlExecuter import UsingMysql
from prettytable import PrettyTable
class user:
    "using user_ID or username to find data"
    def __init__(self, user_ID=None, username=None):
        with UsingMysql(log_time=True) as um:
            if user_ID:
                sql = "select * from User WHERE user_ID = " + str(user_ID)
                um.cursor.execute(sql)
                data = um.cursor.fetchone()
                print(data)
                self.user_ID = user_ID
                self.username = data["username"]
                self.Pwd = data["Pwd"]
                self.Birthday = data["Birthday"]
                self.Perference = data["Perference"]
                self.Gender = data["Gender"]
            if username:
                sql = "select * from User WHERE username = '" + str(username) +"'"
                um.cursor.execute(sql)
                data = um.cursor.fetchone()
                self.user_ID = data["user_ID"]
                self.username = data["username"]
                self.Pwd = data["Pwd"]
                self.Birthday = data["Birthday"]
                self.Perference = data["Perference"]
                self.Gender = data["Gender"]

class User_info:
    "using time and user_ID to find data"
    def __init__(self, time=None, user_ID=None):
        with UsingMysql(log_time=True) as um:
            sql = "select * from User_info WHERE User_ID = " + str(user_ID) + " AND Time = '" + str(time) +"'"
            um.cursor.execute(sql)
            data = um.cursor.fetchone()
            self.ID = data["ID"]
            self.Location = data["Location"]
            self.Weather = data["Weather"]
            self.Temperature = data["Temperature"]
            self.Humidity = data["Humidity"]
            self.Blood_pressure = data["Blood_pressure"]
            self.Time = data["Time"]
            self.User_ID = data["User_ID"]


class Schedule:
    "using title to find data"
    def __init__(self, time=None, user_ID=None):
        with UsingMysql(log_time=True) as um:
            sql = "select * from Schedule WHERE User_ID = " + str(user_ID) + " AND Time = '" + str(time) +"'"
            um.cursor.execute(sql)
            data = um.cursor.fetchone()
            self.ID = data["ID"]
            self.Time = data["Time"]
            self.Title = data["Title"]
            self.Description = data["Description"]
            self.Importance = data["Importance"]
            self.Difficulty = data["Difficulty"]
            self.Comment = data["Comment"]
            self.Week = data["Week"]
            self.Hour = data["Hour"]
            self.lasting_period = data["lasting_period"]
            self.User_ID = data["User_ID"]

class Mood_index:
    "using time and user_ID to find data"
    def __init__(self, time=None, user_ID=None):
        with UsingMysql(log_time=True) as um:
            sql = "select * from Mood_index WHERE User_ID = " + str(user_ID) + " AND Time = '" + str(time) +"'"
            um.cursor.execute(sql)
            data = um.cursor.fetchone()
            self.ID = data["ID"]
            self.Time = data["Time"]
            self.Stress = data["Stress"]
            self.Chaotic = data["Chaotic"]
            self.Happiness = data["Happiness"]
            self.Energy = data["Energy"]
            self.Focus = data["Focus"]
            self.User_ID = data["User_ID"]
            self.Title = data["Title"]
            self.Description = data["Description"]
            self.Importance = data["Importance"]
            self.Difficulty = data["Difficulty"]
            self.Comment = data["Comment"]
            self.Lasting_period = data["Lasting_period"]
            self.feedback = data["feedback"]




class Mood_index_test:
    "using time and user_ID to find data"
    def __init__(self, time=None, user_ID=None):
        with UsingMysql(log_time=True) as um:
            sql = "select * from Mood_index WHERE User_ID = " + str(user_ID) + " AND Time = '" + str(time) +"'"
            um.cursor.execute(sql)
            data = um.cursor.fetchone()
            self.ID = data["ID"]
            self.Time = data["Time"]
            self.Stress = data["Stress"]
            self.Chaotic = data["Chaotic"]
            self.Happiness = data["Happiness"]
            self.Energy = data["Energy"]
            self.Focus = data["Focus"]
            self.User_ID = data["User_ID"]
            self.Title = data["Title"]
            self.Description = data["Description"]
            self.Importance = data["Importance"]
            self.Difficulty = data["Difficulty"]
            self.Comment = data["Comment"]
            self.Lasting_period = data["Lasting_period"]
            self.feedback = data["feedback"]

class Prediction:
    "using time and user_ID to find data"
    def __init__(self, time=None, user_ID=None):
        with UsingMysql(log_time=True) as um:
            sql = "select * from Prediction WHERE User_ID = " + str(user_ID) + " AND Time = '" + str(time) +"'"
            um.cursor.execute(sql)
            data = um.cursor.fetchone()
            self.ID = data["ID"]
            self.Time = data["Time"]
            self.Stress = data["Stress"]
            self.Chaotic = data["Chaotic"]
            self.Happiness = data["Happiness"]
            self.Energy = data["Energy"]
            self.Focus = data["Focus"]
            self.User_ID = data["User_ID"]

# class Recommend_range:
#     "using time and user_ID to find data"
#     def __init__(self, type=None, user_ID=None):
#         with UsingMysql(log_time=True) as um:
#             sql = "select * from Recommend_range WHERE User_ID = " + str(user_ID) + " AND Type = '" + str(type) +"'"
#             um.cursor.execute(sql)
#             data = um.cursor.fetchone()
#             self.ID = data["ID"]
#             self.Type = data["Type"]
#             self.Desc1 = data["Desc1"]
#             self.Duration = data["Duration"]
#             self.Commend = data["Commend"]
#             self.Time = data["Time"]
#             self.User_ID = data["User_ID"]

class Recommend_range:
    "using time and user_ID to find data"
    def __init__(self, ID, Type, Desc1, Duration, Commend, User_ID):
            self.ID = ID
            self.Type = Type
            self.Desc1 = Desc1
            self.Duration = Duration
            self.Commend = Commend
            self.User_ID = User_ID

    def __str__(self):
        return "ID: {}, Type: {},Desc1: {},Duration: {},Commend: {},User_ID: {}".format(self.ID, self.Type, self.Desc1, self.Duration, self.Commend, self.User_ID)



def show_table(table_name=None):
    with UsingMysql(log_time=True) as um:
        sql = "select * from " + str(table_name)
        um.cursor.execute(sql)
        rows = um.cursor.fetchall()
        if len(rows)!=0:
            keys = list(rows[0].keys())
            table = PrettyTable(keys)
            for data in rows:
                values = list(data.values())
                table.add_row(values)
                # data = um.cursor.fetchone()
            print(table)

def add_info(table_name,**kwargs):
    sql1 = "INSERT INTO " + str(table_name) + "("
    sql2 = ""
    sql3 = ""
    for key, value in kwargs.items():
        sql2 = sql2 + str(key) +','
        if type(value) is str:
            sql3 = sql3 +"'" +str(value)+"'" +','
        else:
            sql3 = sql3 +str(value) +','
    sql2 = sql2[:-1]
    sql3 = sql3[:-1]
    sql = sql1 + sql2 + ') VALUES(' + sql3 +')'
    # print(sql)
    with UsingMysql(log_time=True) as um:
            um.cursor.execute(sql)

def del_info(table_name,**kwargs):
    if len(kwargs)==1:
        for key, value in kwargs.items():
            if type(value) is str:
                sql = "DELETE FROM " + table_name + " WHERE " + str(key) +"= " +"'"+ str(value)+"'"
            else:
                sql = "DELETE FROM " + table_name + " WHERE " + str(key) + "= " + str(value)
    else:
        sql1 = ""
        for key, value in kwargs.items():
            if type(value) is str:
                sql1 = sql1 + str(key) +" = " +"'"+ str(value)+"'"
            else:
                sql1 = sql1 + str(key) + " = " + str(value)
            sql1 = sql1 + " AND "
        sql = "DELETE FROM " + table_name + " WHERE " + sql1
        sql = sql[:-5]
    with UsingMysql(log_time=True) as um:
        um.cursor.execute(sql)

def get_table(table_name,**kwargs):
    content = []
    if table_name == "Recommend_range":
        with UsingMysql(log_time=True) as um:
            sql = "select * from Recommend_range WHERE User_ID = " + str(kwargs["user_ID"]) + " AND Type = '" + str(kwargs["type"]) + "'"
            um.cursor.execute(sql)
            rows = um.cursor.fetchall()
            for data in rows:
                # print(data)
                recommend1 = Recommend_range(data["ID"],data["Type"],data["Desc1"],data["Duration"],data["Commend"],data["User_ID"])
                content.append(recommend1)
        return content

    else:
        with UsingMysql(log_time=True) as um:
            sql = "select Time FROM " + str(table_name) +" where Time between  '" + str(kwargs["time1"]) + "'  and  '" + str(kwargs["time2"]) + "'"
            # sql = "select Time FROM schedule where Time between  '2021-12-21 00:00:00'  and '2021-12-30 00:00:00'"
            um.cursor.execute(sql)
            data = um.cursor.fetchone()
            if table_name == "schedule":
                while (data):
                    schedule1 = Schedule(data["Time"],user_ID = int(kwargs["user_ID"]))
                    content.append(schedule1)
                    data = um.cursor.fetchone()
            elif table_name == "mood_index":
                while (data):
                    mood1 = Mood_index(data["Time"],user_ID = int(kwargs["user_ID"]))
                    content.append(mood1)
                    data = um.cursor.fetchone()
            elif table_name == "prediction":
                while (data):
                    prediction1 = Prediction(data["Time"],user_ID = int(kwargs["user_ID"]))
                    content.append(prediction1)
                    data = um.cursor.fetchone()
            elif table_name == "user_info":
                while (data):
                    user1 = User_info(data["Time"],user_ID = int(kwargs["user_ID"]))
                    content.append(user1)
                    data = um.cursor.fetchone()

            elif table_name == "history_log":
                while (data):
                    history1 = Schedule(data["Time"],user_ID = int(kwargs["user_ID"]))
                    content.append(history1)
                    data = um.cursor.fetchone()

            return(content)





if __name__ == '__main__':
    # show_table("user_info")
    # del_info('mood_index',user_ID = 6)
    # add_info("schedule",username="Lu",user_ID = 8, Pwd = "123456")
    # user1 = user(user_ID=8,username="Lu")
    # print(user1.Pwd)
    # add_info("schedule",User_ID = 6, ID = 1, Time = "2021-12-22 17:30:00", Title = "study")
    # schedule1 = Schedule(time="2021-12-22 17:30:00",user_ID=6)
    # print(schedule1.ID)
    # add_info("mood_index",User_ID = 6, Time = "2021-12-31 18:30:00")
    # schedule = get_table("schedule",time1 = "2021-12-21 00:00:00",time2 = "2021-12-30 00:00:00", user_ID = 6)
    # print(schedule)
    # for sch in schedule:
    #     print(sch.Time)
    # add_info("user_info",Blood_pressure=" ",Heartrate = " ", Humidity = " ",Location ="  ", Temperature = " ", Time = "2021-12-30 00:00:00", User_ID=1 ,Weather= " ")
    add_info("Recommend_range", Type = 1,Desc1 = '1',Duration = 1,Commend = 1,User_ID = 6)
    # del_info('Recommend_range', user_ID=6)
    show_table("Recommend_range")

    t = get_table("Recommend_range", user_ID = 6, type='1')
    print(len(t))
    for i in range(len(t)):

        print(t[i])
