# Establish the connection
import mysql.connector

myconnection = mysql.connector.connect(host="localhost", username="root", password="qwe123", database="eventdb")

if myconnection.is_connected():
    print("db connected")
else:
    print("db not connected")
    
# iterative enhancement model -> software engineering topic for presentation without making ppt.
