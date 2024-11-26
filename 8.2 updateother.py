import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3306",
    database="db_penjualan_python"
)

mycursor = mydb.cursor()
sql = "UPDATE kategori SET name=%s where id = %s"
adr = ("Drinks", "2")
mycursor.execute(sql, adr)

mydb.commit()
print(mycursor.rowcount, "record(s) Updated")