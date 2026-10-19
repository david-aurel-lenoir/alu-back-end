#!/usr/bin/python3
"""Gather employee TODO data from REST API."""
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get(base_url + "/users/" + str(employee_id)).json()
    todos = requests.get(base_url + "/todos",
                         params={"userId": employee_id}).json()

    employee_name = user.get("name")
    total_tasks = len(todos)
    done_task = [task for task in todos if task.get("completed")]
    number_done = len(done_task)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_done, total_tasks))

    for task in done_task:
        print("\t {}".format(task.get("title")))
