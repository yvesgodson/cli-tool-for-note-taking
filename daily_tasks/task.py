import datetime
from daily_tasks.storage import TaskStorage
import json
import datetime
from pprint import pprint

# now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")



class Tasks:

    def __init__(self,
        id : int,
        title : str,
        completed : bool,
        created_at : datetime):


        self.id = id
        self.title = title
        self.completed = completed
        self.created_at = created_at 

    def to_dict(self):

        return {                                                       
          "id": self.id,                                             
          "title": self.title,                                       
          "completed": self.completed,                               
          "created_at": self.created_at
      }
    





class TaskManager:

    def __init__(self):
        self.storage = TaskStorage()

    def yes_no_mapping(self, completed):
        return "Yes" if completed else "No"

    def input_task(self):
        while True:
            title_input = input("Entrez votre tache : ").strip()
            if title_input:
                return title_input
            print("La tache ne peut pas être vide")
    # add a task
    def add_task(self):
        tasks = self.storage.load_tasks()
        next_id = 1 if not tasks else max(t["id"] for t in tasks) + 1
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        new_task = Tasks(
            id=next_id,
            title=self.input_task(),          
            completed=False,
            created_at=now,
        )
        new_task_dict = new_task.to_dict()

        print("#" * 30)
        print("\n")
        print(f"Tache {new_task_dict['id']} : {new_task_dict['title']}")
        print(f"Complétée : {self.yes_no_mapping(new_task_dict['completed'])}")  
        print(f"Créée à {new_task_dict['created_at']}")
        print("\n")
        print("#" * 30)

        tasks.append(new_task_dict)
        self.storage.save_task(tasks)

    # list_tasks
    def list_tasks(self):
        tasks = self.storage.load_tasks()
        if len(tasks) == 0 :
            print("Pas de tache à lister ")
        else :
            for i in range(len(tasks)):
                print("\n")
                print("#" * 30)
                print("\n")
                print(f"Numéro de tache : {tasks[i]['id']}\n")
                print(f"Tache : {tasks[i]['title']}\n")
                print(f"Complétée : {tasks[i]['completed']}\n")
                print(f"Créée à : {tasks[i]['created_at']}")
                #print("\n")

    # delete task
    def delete_task(self, id):
        with open(r'daily_tasks\datas\tasks.json', 'r', encoding="utf-8") as file:
            data = json.load(file)
        new_data = [d for d in data if d.get("id") != id]
        if len(new_data) == len(data):
            print(f"Pas de tache d'id {id} à supprimer")
            return
        with open(r'daily_tasks\datas\tasks.json', 'w', encoding="utf-8") as file:
            json.dump(new_data, file, indent=4, ensure_ascii=False)
        print(f"Tache {id} supprimée")

    # mark as completed

    def mark_task_as_completed(self, id):
        tasks = self.storage.load_tasks()
        for task in tasks:
            if task["id"] == id:
                task["completed"] = True
                self.storage.save_task(tasks)
                print(f"Tache {id} marquée comme complétée")
                return
        print(f"Aucune tâche trouvée avec l'id {id}.")


    def display_task(self, id):
        tasks = self.storage.load_tasks()
        task_to_display = None
        for task in tasks :
            if task["id"] == id :
                task_to_display = task
                break
        # the task don't exist
        if task_to_display is None :
            print(f"La tache d'id {id} n'existe pas")
            return
        print("#" * 30)
        print("\n")
        print(f"Numéro de tache : {task_to_display["id"]}\n")
        print(f"Tache : {task_to_display["title"]}\n")
        print(f"Complétée : {task_to_display["completed"]}\n")
        print(f"Créée à : {task_to_display["created_at"]}\n")
        print("#" * 30)



