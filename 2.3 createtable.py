import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='db_penjualan_python'
)

mycursor = mydb.cursor()
mycursor.execute('CREATE TABLE kategori(id int(9) primary key, name varchar(50))')
print("berhasil ditambahkan")
