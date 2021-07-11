#  Mpendulo Khoza
#  Group 2
import mysql.connector
import sqlite3
def UserDatabase():
    connection = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='LifeChoicesOnline', auth_plugin='mysql_native_password')
    my_cursor = connection.cursor()
    sql = ("CREATE TABLE IF NOT EXISTS Admin ()")
def AddRecord(ID, Name , Surname , PhoneNumber , IdentityNumber , KiName , KinNumber ):
    connection = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='LifeChoicesOnline', auth_plugin='mysql_native_password')
    my_cursor = connection.cursor()
    my_cursor.execute("INSERT INTO Admin VALUES (NULL, ?,?,?,?,?,?,?)", ID, Name, Surname , PhoneNumber , IdentityNumber , KiName , KinNumber)
    connection.commit()
    connection.close()

def viewRecord():
    connection = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='LifeChoicesOnline', auth_plugin='mysql_native_password')
    my_cursor = connection.cursor()
    my_cursor.execute("SELECT * FROM Login")
    rows = my_cursor.fetchall()
    connection.close()
    return rows

def deleteRecord(id):
    connection = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='LifeChoicesOnline', auth_plugin='mysql_native_password')
    my_cursor = connection.cursor()
    my_cursor.execute("DELETE FROM Login WHERE id=?", (id,))
    connection.commit()
    connection.close()

def searchRecord(ID = "", Name = "", Surname = "", PhoneNumber = "", IdentityNumber = "", KinName = "", KinNumber = ""):
    connection = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='LifeChoicesOnline', auth_plugin='mysql_native_password')
    my_cursor = connection.cursor()
    my_cursor.execute("SELECT * FROM Login WHERE ID=? OR FirstNAme=? OR Surname=? OR PhoneNumber=? OR Identity=? OR KiName=? OR KinNumber=?", (ID, Name, Surname, PhoneNumber , IdentityNumber, KinName, KinNumber))
    rows = my_cursor.fetchall()
    connection.close()
    return rows

def updateRecord(id, ID = "", Name = "", Surname = "", PhoneNumber = "", IdentityNumber = "", KinName = "", KinNumber = ""):
    connection = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='LifeChoicesOnline', auth_plugin='mysql_native_password')
    my_cursor = connection.cursor()
    my_cursor.execute("UPDATE Login SET ID=? OR NAme=? OR Surname=? OR PhoneNumber=? OR IdentityNumber=? OR KiName=? OR KinNumber=?", (id,ID, Name, Surname, PhoneNumber, IdentityNumber, KinName, KinNumber))
    connection.commit()
    connection.close()
