'''
Fest -> Table Name
    -> Student Name
    -> dept
    -> email
    -> mobile
    -> eventName
'''

# cmd_mysql.py should by the name.... -> but name could be anything

# Establish the connection
import mysql.connector

my_connect = mysql.connector.connect(host="localhost", username="root", password="qwe123qwe", database="eventdb")
if my_connect.is_connected():
    print("DB connected")
else:
    print("DB not connected")
    