import mysql.connector as mc

mydb = mc.connect(
    host="localhost",
    user="root",
    password="JaswindaR@2105",
    database="theComplainEngine",
)

cursor = mydb.cursor()

cursor.execute("SELECT * FROM Student")

rows = cursor.fetchall()

for row in rows:
    print(row)
