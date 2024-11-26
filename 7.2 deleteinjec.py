import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3306",
    database="db_penjualan_python"
)

mycursor = mydb.cursor()
sql = "DELETE FROM kategori where id = %s"
adr = ("3",)
mycursor.execute(sql, adr)

mydb.commit()
print(mycursor.rowcount, "record(s) deleted")