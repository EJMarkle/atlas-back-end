#!/usr/bin/python3
""" Returns JSONPlaceholder TODO data for a specified employee. """
import csv
import requests
import sys
""" retrieve employee todo data """


def GetEmployeeData(EmployeeID):
    url = 'https://jsonplaceholder.typicode.com'
    urlUser = f'{url}/users/{EmployeeID}'
    urlTodo = f'{url}/todos?userId={EmployeeID}'

    """ get and store user data """
    UserResponse = requests.get(urlUser)
    if UserResponse.status_code != 200:
        print(f"Error: unable to fetch user data from ID")
        return

    UserData = UserResponse.json()
    EmployeeName = UserData['name']

    """ get and store todo list data"""
    TodoResponse = requests.get(urlTodo)
    if TodoResponse.status_code != 200:
        print(f"Error: unable to fetch todo data from ID")
        return

    TodoData = TodoResponse.json()
    TotalTasks = len(TodoData)
    DoneTasks = [todo for todo in TodoData if todo['completed']]

    """ print todo list progress """
    print("Employee {} is done with tasks({}/{}):"
          .format(EmployeeName, len(DoneTasks), TotalTasks))
    for task in DoneTasks:
        print(f"\t{task['title']}")

    """ write to CSV """
    filename = f"{EmployeeID}.csv"
    with open(filename, mode='w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME',
                      'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile,
                                fieldnames=fieldnames, quoting=csv.QUOTE_ALL)

        writer.writeheader()
        for todo in TodoData:
            writer.writerow({
                'USER_ID': EmployeeID,
                'USERNAME': EmployeeName,
                'TASK_COMPLETED_STATUS': str(todo['completed']),
                'TASK_TITLE': todo['title']
            })


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Too many arguments")
        sys.exit(1)

    EmployeeID = sys.argv[1]
    try:
        EmployeeID = int(EmployeeID)
    except ValueError:
        print("Error: Employee ID must be a number")
        sys.exit(1)

    GetEmployeeData(EmployeeID)
