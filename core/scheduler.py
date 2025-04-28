import os

#Check if tasks.json file exists and if it does not then create it.
jsonExists = os.path.exists("../data/tasks.json")

if jsonExists == False:    
    file_path = "../data/tasks.json"
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("[]")
        print("tasks.json was created.")
else:
    print("tasks.json already exists.")
