import sqlite3

connection = sqlite3.connect('homework5.db', check_same_thread= False)

cursor = connection.cursor()

cursor.execute(""" CREATE TABLE users (
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username VARCHAR(20),
    password VARCHAR(32) NOT NULL,
    token_word VARCHAR(20) ); """ )


cursor.execute(
   """ CREATE TABLE TASKS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    PERSON_FOR_TASK VARCHAR(20),
    TASK_NAME VARCHAR(20) NOT NULL,
    DAY_OF_TASK VARCHAR(20) ); """
)    

connection.commit()

cursor.close()

connection.close()    