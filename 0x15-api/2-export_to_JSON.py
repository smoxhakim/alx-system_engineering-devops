#!/usr/bin/python3
"""
Extend Python script to export data in CSV format
"""
import json
import requests
import sys

if __name__ == "__main__":

    employee_id = int(sys.argv[1])
    user_respons = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                                .format(employee_id))
    todos_response = requests.get("https://jsonplaceholder.typicode.com/todos")

    user = user_respons.json()
    todos = todos_response.json()

    employee_name = user['username']
    employee_tasks = [task for task in todos if task['userId'] == employee_id]

    json_data = {
        str(employee_id): [
            {
                "task": task['title'],
                "completed": task['completed'],
                "username": employee_name
            }
            for task in employee_tasks
        ]
    }

    filename = f"{employee_id}.json"
    with open(filename, 'w') as jsonfile:
        json.dump(json_data, jsonfile)

    print(f"Data exported to {filename}")
