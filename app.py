from flask import Flask, render_template, request, jsonify #importing needed lybraries
import sqlite3
import database


#### BETTER TO MOVE TO DEDICATED INIT FILE 
# Database connection
conn = sqlite3.connect('./db/database.db')
c = conn.cursor()
# Create a table (if it doesn't exist)
c.execute('''CREATE TABLE IF NOT EXISTS tasks(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name varchar(255) NOT NULL,
                status char(30)
            );''')

# c.execute('''INSERT INTO tasks (name, status) VALUES ("task no.1" , "Todo");''')
conn.commit()
conn.close()
####################################################

app = Flask(__name__) #initializing app

# Delete task route and function
@app.route("/delete/<int:task_id>", methods=['POST'])
def delete(task_id):
    try:
        database.remove_task_by_id(task_id)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)

# Edit task route and function
@app.route("/edit/<int:task_id>", methods=['POST'])
def update(task_id):
    data = request.get_json()
    try:
        if "status" in data:
            database.update_status_entry(task_id, data["status"])
            result = {'success': True, 'response': 'Status Updated'}
        elif "description" in data:
            database.update_task_entry(task_id, data["description"])
            result = {'success': True, 'response': 'Task Updated'}
        else:
            result = {'success': True, 'response': 'Nothing Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)

#Create task route and function
@app.route("/create", methods=['POST'])
def create():
    data = request.get_json()
    database.insert_new_task(data['description'])
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)

# About me task route and function
@app.route("/about-me", methods=['GET'])
def about_me():
    return render_template("aboutme.html")

@app.route("/")
def home():
    tasks = database.fetch_todo()
    return render_template("index.html", taskItems=tasks) #rendering index.html file

if __name__=="__main__":
    app.run()

# GET, POST, PUT, DELETE