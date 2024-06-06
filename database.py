# These functions are started from app.py

import sqlite3

# reads database and selects all tasks
def fetch_todo():
    conn = sqlite3.connect('./db/database.db')
    query_results = conn.execute("Select * from tasks;").fetchall()
    conn.close()
    todo_list = []
    for result in query_results:
        item = {
            "id": result[0],
            "name": result[1],
            "status": result[2]
        }
        todo_list.append(item)
    return todo_list

# connects to database and updates tasks
def update_task_entry(task_id, text):
    conn = sqlite3.connect('./db/database.db')
    c = conn.cursor()
    c.execute("UPDATE tasks SET name = ? WHERE id = ?", (text, task_id))
    conn.commit()
    conn.close()

# Connects to database and updates status
def update_status_entry(task_id, text):
    conn = sqlite3.connect('./db/database.db')
    c = conn.cursor()
    c.execute('UPDATE tasks set status = ? WHERE id = ?', (text, task_id))
    conn.commit()
    conn.close()

# Connects to database and creates new task
def insert_new_task(text):
    conn = sqlite3.connect('./db/database.db')
    query = 'Insert Into tasks (name, status) VALUES ("{}", "{}");'.format(
        text, "Todo")
    conn.execute(query)
    conn.commit()
    query_results = conn.execute("Select last_insert_rowid();")
    query_results = [x for x in query_results]
    task_id = query_results[0][0]
    conn.commit()
    conn.close()

    return task_id

# Deletes task
def remove_task_by_id(task_id):
    """ remove entries based on task ID """
    conn = sqlite3.connect('./db/database.db')
    query = 'Delete From tasks where id={};'.format(task_id)
    conn.execute(query)
    conn.commit()
    conn.close()
