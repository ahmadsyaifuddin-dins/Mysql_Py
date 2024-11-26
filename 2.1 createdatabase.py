import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password=''
)

mycursor = mydb.cursor()
mycursor.execute('CREATE DATABASE db_penjualan_python')
print("Database Dibuat")
