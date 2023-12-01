"""
CRUD Operations
30/11/23
"""

import mysql.connector

# connect to the database server
try:
    conn = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root", 
        password = "u@49sql",
        database = "flights"
    )
    mycursor = conn.cursor()
    print("Connection established!")
except:
    print("Connection error")


# create a database on the server
mycursor.execute("CREATE DATABASE flights")
conn.commit()

# add database = <db-name> in the connection constructor to connect to a specific database on the server

# create a table
mycursor.execute("""
    CREATE TABLE airports(
    airport_id INTEGER PRIMARY KEY,
    code VARCHAR(10) NOT NULL,
    city VARCHAR(50) NOT NULL,
    name VARCHAR(255) NOT NULL
    )
""")
conn.commit()

# Insert data into the table
mycursor.execute("""
    INSERT INTO airports VALUES
    (1, "DEL", "New Delhi", "IGIA"),
    (2, "CCU", "Kolkata", "NSCA"), 
    (3, "BOM", "Mumbai", "CSMA")
""")
conn.commit()

# Select & Where
mycursor.execute("""
    SELECT * FROM airports
    WHERE airport_id > 1
""")
data = mycursor.fetchall()
print(data)

# looping on the resulting rows(tuples)
for i in data:
    print(i[3])

# Update
mycursor.execute("""
    UPDATE airports
    SET city = "Bombay"
    WHERE airport_id = 3
""")
conn.commit()


mycursor.execute("SELECT * FROM airports")
data = mycursor.fetchall()
print(data)

# Delete
mycursor.execute("""
    DELETE FROM airports
    WHERE airport_id = 3
""")
conn.commit()

mycursor.execute("SELECT * FROM airports")
print(mycursor.fetchall())

