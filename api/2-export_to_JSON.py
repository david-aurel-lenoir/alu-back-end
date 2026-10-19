#!/usr/bin/python3
"""Export employee TODO data to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"
    user = requests.get(base_url + "/users/" + str(employee_id)).json()
    url = base_url + "/todos"
    todos = requests.get(url, params={"userId": employee_id}).json()
    username = user.get("username")
    task_list = []
    for task in todos:
        task_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })
    data = {str(employee_id): task_list}
    filename = str(employee_id) + ".json"
    with open(filename, "w") as jsonfile:
        json.dump(data, jsonfile)
