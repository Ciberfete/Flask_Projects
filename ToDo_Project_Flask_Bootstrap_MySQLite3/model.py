import sqlite3

def signup(username, password, token_word):
    connection = sqlite3.connect('homework5.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO users (username, password, token_word) VALUES ('{username}','{password}','{token_word}');""".format(
        username = username, password = password, token_word = token_word))
    connection.commit()
    cursor.close()
    connection.close()

def check_users():
    connection = sqlite3.connect('homework5.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("""SELECT username FROM users;""")
    db_users = cursor.fetchall()
    users = []
    for i in range(len(db_users)):
        person = [i][0]
        users.append(person)
    connection.commit()
    cursor.close()
    connection.close()
    return users

def check_pw(username):
    connection = sqlite3.connect('homework5.db', check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute("""SELECT password FROM users WHERE username = '{username}';""".format(username = username))
    password = cursor.fetchone()[0]
    connection.commit()
    cursor.close()
    connection.close()
    return password


def add_task(person, task, day):
    connection = sqlite3.connect('homework5.db', check_same_thread= False)
    cursor = connection.cursor()
    cursor.execute(
       """ 
        INSERT INTO TASKS(
            PERSON_FOR_TASK,
            TASK_NAME,
            DAY_OF_TASK) VALUES(
            '{person}', '{task}','{day}'
            );""".format( person = person, task = task, day = day))
    connection.commit()
    cursor.close()
    connection.close()   

def get_all():
    connection = sqlite3.connect('homework5.db', check_same_thread= False)
    cursor = connection.cursor()
    cursor.execute( """ SELECT * FROM TASKS; """)

    rows = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    
    return rows

def update_task(id, person, task, day):
    connection = sqlite3.connect('homework5.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(""" UPDATE TASKS set 
                                PERSON_FOR_TASK = '{person}',
                                TASK_NAME = '{task}',
                                DAY_OF_TASK = '{day}'
                            WHERE 
                                ID = '{id}'; """.format(id = id, person = person, task = task, day = day))
    connection.commit()
    cursor.close()
    connection.close()
    
    success_message = 'Your task has been updated.'     
    return success_message

def delete_task(id):
    connection = sqlite3.connect('homework5.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("""DELETE FROM TASKS WHERE ID = '{id}';""".format(id=id))
    connection.commit()
    cursor.close()
    connection.close()
    
    success_message = "Row Deleted"
    return success_message
    


