import os
import json

tasks_json_path = "../data/tasks.json"

#Opens tasks.json file, parses the json, and prints the list.
def load_tasks():
    tasks_json_path = "../data/tasks.json"
    with open(tasks_json_path, 'r') as tasks_json:
        tasks = json.load(tasks_json)
    
    for i in tasks['tasks']:
        print(i)

#Check if tasks.json file exists and if it does not then create it.
jsonExists = os.path.exists(tasks_json_path)

if jsonExists == False:    
    with open(tasks_json_path, 'w', encoding='utf-8') as tasks_json:
        tasks_json.write('{\n  "tasks": []\n}')
        print("tasks.json was created.")
else:
    print("tasks.json already exists.")

load_tasks()
