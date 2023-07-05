import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    port='3306',
)

mydb = database.cursor()

mydb.execute('CREATE DATABASE captain')
print("Database created!")
