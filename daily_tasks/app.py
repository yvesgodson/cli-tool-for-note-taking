from daily_tasks.task import Tasks
from daily_tasks.storage import TaskStorage
import json
import datetime



storage = TaskStorage()
file_path = storage.file_path
tasks = storage.load_tasks()


def yes_no_mapping(completed):
    mapping = {
        True : " Yes",
        False : "No",
    }
    return mapping[completed]


    


def add_task():
    
    next_id = 1 if not tasks else max(task["id"] for task in tasks) + 1

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    id = next_id
    title = input("Entrez la tache :\n")
    completed = False
    created_at = now

    new_task = Tasks(id= id, 
                     title = title,
                     completed = completed,
                     created_at = created_at)
    

    new_task_dict = new_task.to_dict()

    print(f"\nTache {new_task_dict["id"]} : {new_task_dict["title"]}\n")
    print(f"Completée : {yes_no_mapping(new_task_dict["completed"])}\n")
    print(f"Créée à {new_task_dict["created_at"]}")
    

    # the task is then appended in the json loaded
    tasks.append(new_task_dict)
    # and saved into the file
    storage.save_task(tasks)





def list_tasks():
    
    tasks = storage.load_tasks()
    for i in range(max(task["id"] for task in tasks)):
        print("#" * 30)
        print(f"Numéro de tache : {tasks[i]["id"]}\n")
        print(f"Tache : {tasks[i]["title"]}\n")
        print(f"Complétée : {tasks[i]["completed"]}\n")
        print(f"Créée à : {tasks[i]["created_at"]}")
        

def delete_task(id):
    with open(r'daily_tasks\datas\tasks.json', 'r') as file :
        data = json.load(file)

    data = [d for d in data if d.get("id") != id] 

    with open(r'daily_tasks\datas\tasks.json', 'w') as file :
        json.dump(data, file, indent = 4, ensure_ascii = False)
        

def mark_task_as_completed(id):
    tasks = storage.load_tasks()
    for task in tasks :
        if task["id"] == id:
            task["completed"] = True
            storage.save_task(tasks)
            print(f"Tache {id} marquée comme complétée")
            return


def display_task(id):
    tasks = storage.load_tasks()
    for task in tasks :
        if task["id"] == id :
            task_to_display = task
            print("#" * 30)
            print(f"Numéro de tache : {task_to_display["id"]}\n")
            print(f"Tache : {task_to_display["title"]}\n")
            print(f"Complétée : {task_to_display["completed"]}\n")
            print(f"Créée à : {task_to_display["created_at"]}\n")
            print("#" * 30)


#add_task()
display_task(3)
#print(storage.load_tasks())