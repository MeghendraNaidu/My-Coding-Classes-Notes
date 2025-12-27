import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "banksystem",
    port = 3306,
    autocommit = False
)

# print(conn.is_connected())

cur = conn.cursor()
cur.execute("show tables")
# print(cur.fetchall())
# print(cur.fetchone())
# print(cur.fetchone())
print(cur.fetchmany())


cur.close()
conn.close()