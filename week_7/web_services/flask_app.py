#!flask/bin/python
from flask import Flask, jsonify, abort, request
import pymysql

# Get connection to database
def getConnection():
    cnx = pymysql.connect(user='mikkel', password='Barcelona18!', host='134.122.86.171',
                          port=3306, db='demodb', autocommit=True, cursorclass=pymysql.cursors.DictCursor)
    return cnx


app = Flask(__name__)
#app.config['ENV'] = 'development'

@app.route('/flask_app/todo/api/tasks', methods=['GET'])
def get_tasks():
    try:
        cnx = getConnection()
        cursor = cnx.cursor()
        query = "SELECT * FROM Task"
        cursor.execute(query)
        tasks = cursor.fetchall()
        return jsonify(tasks)
    finally:
        # Close connection.
        cursor.close()
        cnx.close()

def get_task_by_id(task_id):
    try:
        cnx = getConnection()
        cursor = cnx.cursor()
        query = f"SELECT * FROM Task WHERE id = {task_id}"
        cursor.execute(query)
        task = cursor.fetchone()
        return task
    finally:
        # Close connection.
        cursor.close()
        cnx.close()

@app.route('/flask_app/todo/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = get_task_by_id(task_id)
    if task == None:
        abort(404)
    return jsonify(task)

@app.route('/flask_app/todo/api/tasks', methods=['POST'])
def create_task():
    try:
        cnx = getConnection()
        cursor = cnx.cursor()
        if not request.json or not 'title' in request.json:
            abort(400)
        query = "INSERT INTO Task (title,description,done) VALUES (%s,%s,%s)"
        cursor.execute(
            query, (request.json['title'], request.json['description'], request.json['done']))
        task = get_task(cursor.lastrowid)
        return task
    finally:
        cursor.close()
        cnx.close()

@app.route('/flask_app/todo/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    try:
        cnx = getConnection()
        cursor = cnx.cursor()
        task = get_task_by_id(task_id)
        if task is None:
            abort(404)
        for key in request.json:
            task[key] = request.json[key]
        update_query = "UPDATE Task SET title=%s,description=%s,done=%s WHERE id=%s"
        cursor.execute(
            update_query, (task['title'], task['description'], task['done'], task['id']))
        return task
    finally:
        cursor.close()
        cnx.close()


@app.route('/flask_app/todo/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        cnx = getConnection()
        cursor = cnx.cursor()
        delete_query = "DELETE FROM Task WHERE id=%s"
        cursor.execute(delete_query, task_id)
        if get_task_by_id(task_id) == None:
            return jsonify(True)
        else:
            return jsonify(False)
    finally:
        cursor.close()
        cnx.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
