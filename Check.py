import mysql.connector as mysql

con=mysql.connect(host="localhost", user='root', password='root', database='db')
print(con.is_connected())
