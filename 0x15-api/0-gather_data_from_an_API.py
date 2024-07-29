#!/usr/bin/python3
import requests
import sys
"""using this REST API, for a given employee ID"""


employee_id = int(sys.argv[1])
user_response = requests.get("https://jsonplaceholder.typicode.com/users/{employee_id}")
todos_response = requests.get("https://jsonplaceholder.typicode.com/todos")

if user_response.status_code != 200 or todos_response.status_code != 200:
    print("Error fetching data from the API")
    sys.exit(1)

user = user_response.json()
todos = todos_response.json()
employee_name = user['name']
employee_tasks = [task for task in todos if task['userId'] == employee_id]

total_tasks = len(employee_tasks)
completed_tasks = [task for task in employee_tasks if task['completed']]
n_completed_tasks = len(completed_tasks)


print(f"Employee {employee_name} is done with tasks\
      ({n_completed_tasks}/{total_tasks}):")
for task in completed_tasks:
    print(f"\t {task['title']}")
