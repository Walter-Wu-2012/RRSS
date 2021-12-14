# Database connector

Call the following function and change the <sql> with the sql you want to execute.

Call "um.cursor.rowcount" to know how many rows have changed by you sql.

    with UsingMysql(log_time=True) as um:
        um.cursor.execute("<sql>")
        um.cursor.rowcount

If you are use "select" sql, you need to call um.cursor.fetchone() or um.cursor.fetchall() to obtain the data into your variable

"um.cursor.fetchone()" for getting one row.
"um.cursor.fetchall()" for getting all rows.

    with UsingMysql(log_time=True) as um:
        um.cursor.execute("select count(id) as total from inventory")
        data = um.cursor.fetchall()

For more example, please check test.py