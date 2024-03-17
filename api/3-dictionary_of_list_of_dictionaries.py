#!/usr/bin/python3
"""Exports JSONPlaceholder TODO data for all employees."""
import json
import requests
import sys


def GetAllEmployeesData():
    """Define the base URL for JSONPlaceholder API"""
    url = 'https://jsonplaceholder.typicode.com/users'
    
    """Fetch all employees data"""
    response = requests.get(url)
    
    """Check if the request was successful"""
    if response.status_code != 200:
        print("Error: unable to fetch user data from ID")
        return

    """Parse the JSON response to extract employee information"""
    employees = response.json()
    
    """Initialize dictionary to store all employee tasks"""
    all_tasks = {}
    
    """Iterate over each employee"""
    for employee in employees:
        EmployeeID = str(employee['id'])
        EmployeeName = employee['name']

        """Construct URL to fetch employee's TODO data"""
        urlTodo = f"https://jsonplaceholder.typicode.com/todos?userId={EmployeeID}"
        
        """Fetch TODO data for the current employee"""
        todo_response = requests.get(urlTodo)
        
        """Check if the request was successful"""
        if todo_response.status_code != 200:
            print(f"Error: unable to fetch TODO data for employee {EmployeeID}")
            continue

        """Parse the JSON response to extract employee's TODO list"""
        todos = todo_response.json()
        
        """List to store individual tasks for the current employee"""
        employee_tasks = []
        
        """Iterate over each task"""
        for todo in todos:
            task_details = {
                "task": todo['title'],
                "completed": todo['completed'],
                "username": EmployeeName
            }
            employee_tasks.append(task_details)
        
        """Store tasks for the current employee in the dictionary"""
        all_tasks[EmployeeID] = employee_tasks

    """Write all employee tasks to a JSON file"""
    filename = "todo_all_employees.json"
    with open(filename, mode='w') as jsonfile:
        json.dump(all_tasks, jsonfile)


GetAllEmployeesData()
