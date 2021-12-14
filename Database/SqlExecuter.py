from timeit import default_timer
import pymysql

host = 'test11.mysql.database.azure.com'
port = 3306
db = 'quickstartdb'
user = 'wzf'
password = 'group2!!!'


def get_connection():
    conn = pymysql.connect(host=host, port=port, db=db, user=user, password=password, charset='utf8')
    return conn

class UsingMysql(object):

    def __init__(self, commit=True, log_time=True, log_label='total time'):
        """
        :param commit: Whether to commit the transaction at the end (set to False to facilitate unit testing)
        :param log_time:  Whether to print the total running time of the program
        :param log_label:  Custom log text
        """
        self._log_time = log_time
        self._commit = commit
        self._log_label = log_label

    def __enter__(self):

        if self._log_time is True:
            self._start = default_timer()
        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        conn.autocommit = False

        self._conn = conn
        self._cursor = cursor
        return self

    def __exit__(self, *exc_info):
        if self._commit:
            self._conn.commit()
        self._cursor.close()
        self._conn.close()

        if self._log_time is True:
            diff = default_timer() - self._start
            print('-- %s: %.6f s' % (self._log_label, diff))

    @property
    def cursor(self):
        return self._cursor
