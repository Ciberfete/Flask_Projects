import sqlite3

connection = sqlite3.connect('homework5.db', check_same_thread = False)

cursor = connection.cursor()

cursor.execute(""" 
        INSERT INTO users(
            username,
            password,
            token_word) VALUES(
            'Arthas',
            'arthas',
            'frostburn' ); """)

cursor.execute(""" 
        INSERT INTO TASKS(
            ID,
            TASK_NAME,
            DAY_OF_TASK,
            PERSON_FOR_TASK) VALUES(
            100,
            'Cooking',
            'Monday',
            'Princess'); """)           

connection.commit()
cursor.close()
connection.close()