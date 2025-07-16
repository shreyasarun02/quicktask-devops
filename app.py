from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)
DATA_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(load_tasks())

@app.route('/tasks', methods=['POST'])
def create_task():
    tasks = load_tasks()
    data = request.json
    task_id = len(tasks) + 1
    data['id'] = task_id
    tasks.append(data)
    save_tasks(tasks)
    return jsonify(data), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task.update(request.json)
            save_tasks(tasks)
            return jsonify(task)
    return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t['id'] != task_id]
    if len(new_tasks) == len(tasks):
        return jsonify({'error': 'Task not found'}), 404
    save_tasks(new_tasks)
    return jsonify({'message': 'Task deleted'})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
