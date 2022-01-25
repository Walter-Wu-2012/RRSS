from Database.SqlExecuter import UsingMysql
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} == {1}".format(key, value))

greet_me(name="yasoob")
    # with UsingMysql(log_time=True) as um:
    #     um.cursor.execute("select * from user_info")
    #     data = um.cursor.fetchone()
    #     print(data)
        # cursor = um.cursor
        # cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
        # sq1 = """CREATE TABLE EMPLOYEE(NAME CHAR(20)NOT NULL,AGE INT)"""
        # cursor.execute(sq1)
        # um.close()


    # print("-- count: %d " % data['total'])

# # Create Table
#     with UsingMysql(log_time=True) as um:
#         um.cursor.execute("DROP TABLE IF EXISTS users;")
#         um.cursor.execute("CREATE TABLE users (id serial PRIMARY KEY, name VARCHAR(50), age INTEGER);")
#         um.cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s);", ("aaa", 21))
#         um.cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s);", ("bbb", 22))
#         um.cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s);", ("ccc", 23))


# # Read Data
#     with UsingMysql(log_time=True) as um:
#         um.cursor.execute("SELECT * FROM users;")
#         rows = um.cursor.fetchall()
#         print("Read", um.cursor.rowcount, "row(s) of data.")
#
#     # print(rows)
#     for row in rows:
#         print(row)


# #Update
#     with UsingMysql(log_time=True) as um:
#         um.cursor.execute("UPDATE users SET age = %s WHERE name = %s;", (24, "aaa"))
#         print("Updated", um.cursor.rowcount, "row(s) of data.")

# #Delete
#     with UsingMysql(log_time=True) as um:
#         um.cursor.execute("DELETE FROM users WHERE name=%(param1)s;", {'param1': "aaa"})
#         print("Deleted",  um.cursor.rowcount, "row(s) of data.")
