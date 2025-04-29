import os
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta
tasks_json_path = "../data/tasks.json"


#Opens tasks.json file and parses it to a dictionary.
def load_tasks():
    tasks_json_path = "../data/tasks.json"

    with open(tasks_json_path, 'r') as tasks_json:
        tasks_dic = json.load(tasks_json)
        return tasks_dic

#Adds a new tasks to tasks.json.
def add_task():
    tasks_json_path = "../data/tasks.json"
    current_date_time = datetime.now()

#Get all input from user.
    task_name = input("Please enter new task name: ")

    task_complete = False

    task_create_date = current_date_time

    print("Please enter the due date of this task: ")
    due_months = input("Months: ")
    due_weeks = input("Weeks: ")
    due_days = input("Days: ")
    due_hours = input("Hours: ")
    task_due_date = task_create_date + relativedelta(months=+int(due_months), weeks=+int(due_weeks), days=+int(due_days), hours=+int(due_hours))

    task_details = input("Please enter details required to complete this task: ")
    
    task_category = input("Please pick a category for this task: \n 0) Work \n 1) Study \n 2) Project \n 3) Errand \n 4) Family/Friends \n 5) Personal Life \n 6) Other \n Category: ")
    if task_category == 0:
        task_category = "Work"
    elif task_category == 1:
        task_category = "Study"
    elif task_category == 2:
        task_category = "Project"
    elif  task_category == 3:
        task_category = "Errand"
    elif task_category == 4:
        task_category = "Family/Friends"
    elif task_category == 5:
        task_category = "Personal Life"
    else:
        task_category = "Other"
    
    task_priority = input("Please set a priority for this task: \n 0) Low \n 1) Medium \n 2) High \n Priority: ")
    if task_priority == 2:
        task_priority = "High"
    elif task_priority == 1:
        task_priority = "Medium"
    else:
        task_priority = "Low"
    
    task_reminder_time = task_priority
    if task_priority == "High":
        task_reminder_time = task_due_date - relativedelta(weeks=1)
    elif task_priority == "Medium":
        task_reminder_time = task_due_date - relativedelta(days=3)
    else:
        task_reminder_time = task_due_date - relativedelta(days=1)

    task_last_update = current_date_time

#Convert all times to strings.
    task_create_date = task_create_date.isoformat()
    task_due_date = task_due_date.isoformat()
    task_reminder_time = task_reminder_time.isoformat()
    task_last_update = task_last_update.isoformat()

#Load task dictionary and append with new user data.
    new_task = {
        "task_name": task_name,
        "task_complete": task_complete,
        "task_create_date": task_create_date,
        "task_due_date": task_due_date,
        "task_details": task_details,
        "task_category": task_category,
        "task_priority": task_priority,
        "task_reminder_time": task_reminder_time,
        "task_last_update": task_last_update
    }
    task_dic = load_tasks()
    task_dic["tasks"].append(new_task)

    with open(tasks_json_path, 'w', encoding="utf-8") as tasks_json:
        json.dump(task_dic, tasks_json)
        print("Scheduler: New tasks added.")


print("Scheduler: Starting...")

#Check if tasks.json file exists and if it does not then create it.
jsonExists = os.path.exists(tasks_json_path)

if jsonExists == False: 
    print("Scheduler: tasks.json does not exist.")   
    with open(tasks_json_path, 'w', encoding='utf-8') as tasks_json:
        tasks_json.write('{\n  "tasks": []\n}')
        print("Scheduler: tasks.json created.")
else:
    print("Scheduler: tasks.json already exists.")

add_task()
