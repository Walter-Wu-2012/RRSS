from Database.SqlExecuter import UsingMysql
from prettytable import PrettyTable
class user:
    "using user_ID or username to find data"
    def __init__(self, user_ID, username, Pwd, Birthday, Perference, Gender ):
        self.user_ID = user_ID
        self.username = username
        self.Pwd = Pwd
        self.Birthday = Birthday
        self.Perference = Perference
        self.Gender = Gender
    def __str__(self):
        return "user_ID: {}, username: {},Pwd: {},Birthday: {},Perference: {},Gender: {}".format(self.user_ID, self.username, self.Pwd, self.Birthday, self.Perference, self.Gender)




class User_info:
    "using time and user_ID to find data"
    def __init__(self, ID, Location, Weather, Temperature,Humidity,Blood_pressure,Time,User_ID):
        self.ID = ID
        self.Location = Location
        self.Weather = Weather
        self.Temperature = Temperature
        self.Humidity = Humidity
        self.Blood_pressure = Blood_pressure
        self.Time = Time
        self.User_ID = User_ID

    def __str__(self):
        return "ID: {}, Location: {},Weather: {},Temperature: {},Humidity: {},Blood_pressure: {},Time: {},User_ID: {}".format(self.ID, self.Location, self.Weather, self.Temperature, self.Humidity, self.Blood_pressure,self.Time,self.User_ID)

class Schedule:
    "using title to find data"
    def __init__(self, ID, Time, Title, Description, Importance, Difficulty, Comment, Time2, User_ID, feedback):
        self.ID = ID
        self.Time = Time
        self.Title = Title
        self.Description = Description
        self.Importance = Importance
        self.Difficulty = Difficulty
        self.Comment = Comment
        self.Time2 = Time2
        self.User_ID = User_ID
        self.feedback = feedback

    def __str__(self):
        return "ID: {}, Time: {},Title: {},Description: {},Importance: {},Difficulty: {},Comment: {},Time2: {},User_ID: {},feedback: {}".format(
            self.ID, self.Time, self.Title, self.Description, self.Importance, self.Difficulty, self.Comment, self.Time2,
            self.User_ID, self.feedback)


class Mood_index:
    "using time and user_ID to find data"
    def __init__(self, ID,Time,Stress,Chaotic,Happiness,Energy,Focus,User_ID,Importance,Difficulty,Comment,Lasting_period):
        self.ID = ID
        self.Time = Time
        self.Stress = Stress
        self.Chaotic = Chaotic
        self.Happiness = Happiness
        self.Energy = Energy
        self.Focus = Focus
        self.User_ID = User_ID
        self.Importance = Importance
        self.Difficulty = Difficulty
        self.Comment = Comment
        self.Lasting_period = Lasting_period
    def __str__(self):
        return "ID: {}, Time: {},Stress: {},Chaotic: {},Happiness: {},Energy: {},Focus: {},User_ID: {},Importance: {},Difficulty: {},Comment: {},Lasting_period: {}".format(
            self.ID, self.Time, self.Stress, self.Chaotic, self.Happiness, self.Energy, self.Focus, self.User_ID,
            self.Importance,self.Difficulty,self.Comment,self.Lasting_period)



class Prediction:
    "using time and user_ID to find data"
    def __init__(self, ID, Time, Stress, Chaotic, Happiness, Energy, Focus, User_ID):
        self.ID = ID
        self.Time = Time
        self.Stress = Stress
        self.Chaotic = Chaotic
        self.Happiness = Happiness
        self.Energy = Energy
        self.Focus = Focus
        self.User_ID = User_ID
    def __str__(self):
        return "ID: {}, Time: {},Stress: {},Chaotic: {},Happiness: {},Energy: {},Focus: {},User_ID: {}".format(self.ID, self.Time, self.Stress, self.Chaotic, self.Happiness, self.Energy, self.Focus, self.User_ID)


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
            sql = "select * FROM " + str(table_name) +" where Time between  '" + str(kwargs["time1"]) + "'  and  '" + str(kwargs["time2"]) + "'"
            # sql = "select Time FROM schedule where Time between  '2021-12-21 00:00:00'  and '2021-12-30 00:00:00'"
            print(sql)
            um.cursor.execute(sql)
            rows = um.cursor.fetchall()
            if table_name == "Schedule":
                for data in rows:
                    schedule = Schedule(data["ID"], data["Time"], data["Title"], data["Description"],
                                                 data["Importance"], data["Difficulty"],data["Comment"],data["Time2"],data["User_ID"],data["feedback"])
                    content.append(schedule)
                    # ID, Time, Title, Description, Importance, Difficulty, Comment, Week, Hour, Time2, User_ID
            elif table_name == "Mood_index":
                for data in rows:
                    mood = Mood_index(data["ID"], data["Time"], data["Stress"], data["Chaotic"],
                                                 data["Happiness"], data["Energy"],data["Focus"],data["User_ID"],data["Importance"],data["Difficulty"],data["Comment"],data["Lasting_period"])
                    content.append(mood)
            elif table_name == "Mood_index_interpolation":
                for data in rows:
                    mood = Mood_index(data["ID"], data["Time"], data["Stress"], data["Chaotic"],
                                                 data["Happiness"], data["Energy"],data["Focus"],data["User_ID"],data["Importance"],data["Difficulty"],data["Comment"],data["Lasting_period"])
                    content.append(mood)
            elif table_name == "Mood_index_interpolation2":
                for data in rows:
                    mood = Mood_index(data["ID"], data["Time"], data["Stress"], data["Chaotic"],
                                                 data["Happiness"], data["Energy"],data["Focus"],data["User_ID"],data["Importance"],data["Difficulty"],data["Comment"],data["Lasting_period"])
                    content.append(mood)
            elif table_name == "prediction":
                print(len(rows))
                for data in rows:
                    prediction = Prediction(data["ID"], data["Time"], data["Stress"], data["Chaotic"],
                                        data["Happiness"], data["Energy"], data["Focus"], data["User_ID"])
                    content.append(prediction)
            elif table_name == "User_info":
                for data in rows:
                    user = User_info(data["ID"], data["Location"], data["Weather"], data["Temperature"],
                                            data["Humidity"], data["Blood_pressure"], data["Time"], data["User_ID"])
                    content.append(user)
            elif table_name == "History_log":
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
    # add_info("Recommend_range", Type = 1,Desc1 = '1',Duration = 1,Commend = 1,User_ID = 6)
    # del_info('Recommend_range', user_ID=6)
    # del_info("User_info",Time = "2021-12-21 00:00:00", Stress =1, Chaotic =1, Happiness=1, Energy=1, Focus=1, User_ID=6)
    show_table("Mood_index_interpolation")
    #
    t = get_table("Mood_index_interpolation2",time1 = "2021-12-21 00:00:00",time2 = "2022-01-13 00:00:00", user_ID = 6)
    print(len(t))
    for i in range(len(t)):

        print(t[i])
