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
                self.user_ID = user_ID
                self.username = data["username"]
                self.Pwd = data["Pwd"]
                self.Birthday = data["Birthday"]
                self.Perference = data["Perference"]
                self.Gender = data["Gender"]
            if username:
                sql = "select * from User WHERE username = '" + str(username) +"'"
                print(sql)
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
    def __init__(self, title=None, user_ID=None):
        with UsingMysql(log_time=True) as um:
            sql = "select * from Schedule WHERE User_ID = " + str(user_ID) + " AND Title = '" + str(title) +"'"
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

class Recommend_range:
    "using time and user_ID to find data"
    def __init__(self, time=None, user_ID=None):
        with UsingMysql(log_time=True) as um:
            sql = "select * from Recommend_range WHERE User_ID = " + str(user_ID) + " AND Time = '" + str(time) +"'"
            um.cursor.execute(sql)
            data = um.cursor.fetchone()
            self.ID = data["ID"]
            self.Type = data["Type"]
            self.Desc1 = data["Desc1"]
            self.Duration = data["Duration"]
            self.Commend = data["Commend"]
            self.Time = data["Time"]
            self.User_ID = data["User_ID"]

def show_table(table_name=None):
    with UsingMysql(log_time=True) as um:
        sql = "select * from " + str(table_name)
        um.cursor.execute(sql)
        data = um.cursor.fetchone()
        keys = list(data.keys())
        table = PrettyTable(keys)
        while(data):
            values = list(data.values())
            table.add_row(values)
            data = um.cursor.fetchone()
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


if __name__ == '__main__':
    # show_table("user_info")
    # del_info('user',username="Lu",user_ID = 6)
    # add_info("user",username="Lu",user_ID = 6, Pwd = "123456")
    show_table("schedule")
