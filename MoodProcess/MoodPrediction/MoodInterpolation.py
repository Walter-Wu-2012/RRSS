from scipy import interpolate

from Database.SqlExecuter import UsingMysql


def interpolation(x, y, xnew):
    f = interpolate.interp1d(x, y, kind='quadratic')
    ynew = f(xnew)

def Interpolation(user):
    with UsingMysql(log_time=True) as um:
        sql = "select Time from mood_index where User_ID=" + int(user) + " order by Time DESC limit 48"
        um.cursor.execute(sql)
        endtime = um.cursor.fetchone()['Time']


if __name__ == '__main__':
    Interpolation('6')