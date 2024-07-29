#!/usr/bin/python3
"""
Extend Python script to export data in CSV format
"""
import csv
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

    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in employee_tasks:
            csv_writer.writerow([
                employee_id,
                employee_name,
                str(task['completed']),
                task['title']
            ])

    print(f"Data exported to {filename}")
