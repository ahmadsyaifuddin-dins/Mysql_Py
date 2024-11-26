import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3306",
    database="db_penjualan_python"
)

mycursor = mydb.cursor()
sql = "SELECT * FROM kategori where id = %s"
no = ("1",)
mycursor.execute(sql, no)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)