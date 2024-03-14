import mysql.connector

# Establish the connection for mysql database
myConnection = mysql.connector.connect(host="localhost", user="root", password="qwe123", database="eventdb")

# To verify the connection
if myConnection.is_connected():
    print("DB connected successfully")
else:
    print("DB not connected")

# to pass the database execution using cursor
mycursor = myConnection.cursor()

# Create new table in database
'''createQuery = "create table if not exists fests (festName text, Type text, Location text);"

# execute the mysql query with cursor
mycursor.execute(createQuery)

# to save the last operation using commit
myConnection.commit()'''

# To insert new records in database
# insertQuery = "insert into fests values('{}', '{}', '{}')".format("Hackathon", "coding", "ITS") #Static data
'''insertQuery = "insert into fests values('{}', '{}', '{}')".format(input("Enter festName: "), input("Enter it's type: "), input("Enter it's location: ")) #Runtime data
mycursor.execute(insertQuery)
myConnection.commit()
'''

# Retreive records from database
'''selectQuery = "select * from fests"
mycursor.execute(selectQuery)

for fest in mycursor.fetchall():
    print(fest)
    
myConnection.commit()'''

# Retreive the specific record based on the condition using where
'''whereQuery = "select * from fests where festName='Ethical Hackona'"
mycursor.execute(whereQuery)
for fest in mycursor.fetchall():
    print(fest)
    
myConnection.commit()'''

# To update a record in the database - to change the existing record
'''updateQuery = "update fests set festName='Programmizia' where festName='Hackathon'"
mycursor.execute(updateQuery)
myConnection.commit()'''


# To delete a record from database
'''deleteQuery = "delete from fests where Type='coding'"
mycursor.execute(deleteQuery)
myConnection.commit()'''

# To delete table - drop query
dropQuery = "drop table fests"
mycursor.execute(dropQuery)
myConnection.commit()