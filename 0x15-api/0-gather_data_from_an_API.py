#!/usr/bin/python3
"""model doc"""
import requests
import sys

"""using this REST API, for a given employee ID"""

if __name__ == "__main__":

    employee_id = int(sys.argv[1])
    user_respons = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                                .format(employee_id))
    todos_response = requests.get("https://jsonplaceholder.typicode.com/todos")

    user = user_respons.json()
    todos = todos_response.json()
    employee_name = user['name']
    employee_tasks = [task for task in todos if task['userId'] == employee_id]

    total_tasks = len(employee_tasks)
    completed_tasks = [task for task in employee_tasks if task['completed']]
    n_completed_tasks = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, n_completed_tasks, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
