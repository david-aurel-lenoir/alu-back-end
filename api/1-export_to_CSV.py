#!/usr/bin/python3
"""Export employee TODO data to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"
    user = requests.get(base_url + "/users/" + str(employee_id)).json()
    url = base_url + "/todos"
    todos = requests.get(url, params={"userId": employee_id}).json()
    username = user.get("username")
    filename = str(employee_id) + ".csv"
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
