#!/usr/bin/python3
""" Returns JSONPlaceholder TODO data for a specified employee. """
import sys
import requests
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
    print(f"Employee {EmployeeName} is done with tasks ({len(DoneTasks)}/
          {TotalTasks}):")
    for task in DoneTasks:
        print(f"\t{task['title']}")


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
