import datetime
from daily_tasks.storage import TaskStorage
import json
import datetime
from rich.console import Console
from rich.panel import Panel



console = Console()


class Tasks:

    console = Console()

    def __init__(self,
        id : int,
        title : str,
        completed : bool,
        created_at : datetime,
        ):


        self.id = id
        self.title = title
        self.completed = completed
        self.created_at = created_at 
        self.console = Console()

    def to_dict(self):

        return {                                                       
          "id": self.id,                                             
          "title": self.title,                                       
          "completed": self.completed,                               
          "created_at": self.created_at
      }
    


###########################################################################


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
            console.print("La tache ne peut pas être vide")
    # add a task
    def add_task(self, title = None):
        tasks = self.storage.load_tasks()
        next_id = 1 if not tasks else max(t["id"] for t in tasks) + 1
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        final_title = title if title is not None else self.input_task()

        new_task = Tasks(
            id=next_id,
            title=final_title,      
            completed=False,
            created_at=now,)
        new_task_dict = new_task.to_dict()

        # console.print("#" * 30)
        # console.print("\n")
        # console.print(f"Tache {new_task_dict['id']} : {new_task_dict['title']}")
        # console.print(f"Complétée : {self.yes_no_mapping(new_task_dict['completed'])}")  
        # console.print(f"Créée à {new_task_dict['created_at']}")
        # console.print("\n")
        # console.print("#" * 30)
        
        ###

        panel = Panel(f"{new_task_dict['title']}\nComplétée : {self.yes_no_mapping(new_task_dict['completed'])}", title = f"Tache {new_task_dict['id']} ", subtitle = f"Créé à {new_task_dict['created_at']}")
        print("\n")
        console.print(panel)
        print("\n")
        tasks.append(new_task_dict)
        self.storage.save_task(tasks)

    # list_tasks
    def list_tasks(self):
        tasks = self.storage.load_tasks()
        if len(tasks) == 0 :
            console.print("Pas de tache à lister ")
        else :
            for i in range(len(tasks)):
                # console.print("\n")
                # console.print("#" * 30)
                # console.print("\n")
                # console.print(f"Numéro de tache : {tasks[i]['id']}\n")
                # console.print(f"Tache : {tasks[i]['title']}\n")
                # console.print(f"Complétée : {tasks[i]['completed']}\n")
                # console.print(f"Créée à : {tasks[i]['created_at']}")

                ###

                panel = Panel(f"{tasks[i]['title']}\nComplétée : {self.yes_no_mapping(tasks[i]['completed'])}", title = f"Tache {tasks[i]['id']} ", subtitle = f"Créé à {tasks[i]['created_at']}")
                console.print(panel)
                print("\n \n \n")


    # delete task
    def delete_task(self, id):
        tasks = self.storage.load_tasks()
        new_data = [t for t in tasks if t.get("id") != id]
        if len(new_data) == len(tasks):
            console.print(f"Pas de tache d'id {id} à supprimer")
            return
        self.storage.save_task()
        console.print(f"Tache {id} supprimée")

    # mark as completed

    def mark_task_as_completed(self, id):
        tasks = self.storage.load_tasks()
        for task in tasks:
            if task["id"] == id:
                task["completed"] = True
                self.storage.save_task(tasks)
                console.print(f"Tache {id} marquée comme complétée")
                return
        console.print(f"Aucune tâche trouvée avec l'id {id}.")


    def display_task(self, id):
        tasks = self.storage.load_tasks()
        task_to_display = None
        for task in tasks :
            if task["id"] == id :
                task_to_display = task
                break
        # the task don't exist
        if task_to_display is None :
            console.print(f"La tache d'id {id} n'existe pas")
            return
        # console.print("#" * 30 )
        # console.print(f"\nNuméro de tache : {task_to_display['id']}\n")
        # console.print(f"Tache : {task_to_display['title']}\n")
        # console.print(f"Complétée : {task_to_display['completed']}\n")
        # console.print(f"Créée à : {task_to_display['created_at']}\n")
        # console.print("#" * 30)
        print("\n")
        panel = Panel(f"{task_to_display['title']}\nComplétée : {self.yes_no_mapping(task_to_display['completed'])}", title = f"Tache {task_to_display['id']} ", subtitle = f"Créé à {task_to_display['created_at']}")
        console.print(panel)
        print("\n")



