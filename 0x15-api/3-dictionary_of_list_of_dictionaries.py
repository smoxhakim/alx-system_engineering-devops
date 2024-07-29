#!/usr/bin/python3
"""
Extend Python script to export data for all employees in JSON format
"""
import json
import requests

if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    users = users_response.json()
    todos = todos_response.json()

    # Prepare the JSON data
    json_data = {}

    for user in users:
        user_id = str(user['id'])
        username = user['username']
        user_tasks = [task for task in todos if task['userId'] == user['id']]

        json_data[user_id] = [
            {
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            }
            for task in user_tasks
        ]

    # Create JSON file
    filename = "todo_all_employees.json"
    with open(filename, 'w') as jsonfile:
        json.dump(json_data, jsonfile)

    print(f"Data exported to {filename}")
