'''
# Establish the connection
import mysql.connector

myconnection = mysql.connector.connect(host="localhost", username="root", password="qwe123", database="eventdb")

if myconnection.is_connected():
    print("db connected")
else:
    print("db not connected")
    
# iterative enhancement model -> software engineering topic for presentation without making ppt.
'''

'''
13 march 2024
MySQL + Python -> xampp
               -> mysql server {recommended}
               
               
Mobile App development -> swift ios, kotlin
                       -> react native - js, flutter - dart {recommended}
'''

'''
Task -> create a database dbName -> Startup, Table Name -> Employees, Column Names -> empname, empPosition, empsalary, empemail, empdept
Table Name -> Department, Column Names -> deptname, deptid
-> create db
-> create table
-> insert 50 records - 1 time execution using loop

-- master data -> collection of complete data. eg. marketing, developer, admin, hr , management department.

-> find 2nd higest paid employee
-> find 3rd lowest paid employee
-> find employee name who got same salary
-> find highest paid employee in every department
-> find empid who work in same department

use mysql server {recommended}
'''

# MongoDB -> will discuss soon

'''
------Machine Learning------
ML identify the problem and on the basis of this it makes future prediction

ML Techniques/problems -> Supervised -> regression, classification
                       -> Unsupervised -> clustering

-- Unsupervised ML techniques/problems will solve the problem by using making groups called clustering
        -> K-mean -> k-mean is unsupervised ML technique which work on groups or datapoints by making clustering
        
-- Supervised ML techniques/problems will work on data set based on relationship.
    -> Regression -> The regression technique will work on dataset to find the relationship and plot the graph also predict the future data.
        -> Linear regression -> The linear regression will find the relatioship in b/w the dataset or datapoint and draw the linear graph based on the dataset also predict the new data
    -> Classification -> 
        -> Logistic regression -> It solves classification problems
        -> 
        
-- Decision Tree -> It will help you to make the decision based on the previous dataset. eg. status of student to get pass or fail

-- Train or Test -> The train or test is a technique to measure the performance or accuracy of given model
ML models -> 
'''

