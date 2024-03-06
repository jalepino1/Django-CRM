import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Henrycrawley15!',
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE CRMdb")