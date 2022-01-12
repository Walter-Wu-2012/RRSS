from torch.utils.data import dataset
from Database.SqlExecuter import UsingMysql
from datetime import datetime, date, timedelta

from Database.usingdatabase import get_table


class MoodDataLoader(dataset.Dataset):

    def __init__(self, table, user):
        super(MoodDataLoader, self).__init__()
        self.timelist = self.getTotalList(table, user)
        self.table = table
        self.user = user

    def __getitem__(self, index):
        time = self.img_info[index]
        starttime = time - timedelta(days=7)+timedelta(seconds=1810)
        endtime = time + timedelta(days=7)+timedelta(seconds=1810)

        data = get_table(self.table, time1 = starttime,time2 = endtime, user_ID = self.user)

    def __len__(self):
        return len(self.timelist)

    def getTotalList(self, table, user):
        with UsingMysql(log_time=True) as um:
            sql = "select Time from "+table+" where User_ID="+int(user)+" order by id DESC limit 1"
            um.cursor.execute(sql)
            endtime = um.cursor.fetchone()['Time']

            sql = "select Time from " + table + " where User_ID=" + user + " order by id ASC limit 1"
            um.cursor.execute(sql)
            starttime = um.cursor.fetchone()['Time']

        gap = (endtime - starttime).total_seconds()/3600

        if gap<=(2*7*24):
            return False

        starttime = starttime + timedelta(days=7)
        endtime = endtime - timedelta(days=7)

        timelist = []
        # starttime = starttime + timedelta(seconds=1800)
        while(starttime<endtime):
            timelist.append(starttime)
            starttime = starttime + timedelta(seconds=1800)

        return timelist



if __name__ == '__main__':
    with UsingMysql(log_time=True) as um:
        # sql = "select * from Mood_index order by id DESC limit 1"
        table = 'Mood_index'
        user = '6'
        sql = "select Time from " + table + " where User_ID=" + user + " order by id DESC limit 1"
        # sql = "select * from Mood_index where User_ID=6 order by id ASC limit 1"
        um.cursor.execute(sql)
        endtime = um.cursor.fetchone()['Time']

        sql = "select Time from " + table + " where User_ID=" + user + " order by id ASC limit 1"
        # sql = "select * from Mood_index where User_ID=6 order by id ASC limit 1"
        um.cursor.execute(sql)
        starttime = um.cursor.fetchone()['Time']

        gap = (endtime - starttime).total_seconds()/3600

        print(gap)

        timelist = []
        while (starttime < endtime):
            timelist.append(starttime)
            starttime = starttime + timedelta(seconds=1800)

        print(timelist)
