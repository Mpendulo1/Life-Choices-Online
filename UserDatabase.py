#  Mpendulo Khoza
#  Group 2
import mysql.connector
import sqlite3
def UserDatabase():
    connnection = sqlite3.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='Hospitals', auth_plugin='mysql_native_password')
    my_cursor = connnection.cursor()
    my_cursor.execute("CREATE TABLE IF NON EXISTS Users (ID INTEGER PRIMARY KEY, )")
