import mysql.connector

mydb = mysql.connector.connect(host = 'localhost',user = 'Hasan',passwd='hb90903290')
mycursor = mydb.cursor()

mycursor.execute('shuw databases')

for i in mycursor:
    print(i)