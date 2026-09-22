from pathlib import Path
import json
import os



class TaskStorage:

    
    def __init__(self):
        self.file_path = Path(__file__).parent/"datas"/"tasks.json"
        

    def load_tasks(self):
        if os.stat(self.file_path).st_size == 0 :
            with self.file_path.open('w', encoding="utf-8") as file:
                file.write('[]')
        
        with self.file_path.open('r', encoding="utf-8") as file:
            return json.load(file)

        
    def save_task(self, tasks):
        
        with self.file_path.open('w', encoding="utf-8") as file:
            json.dump(tasks, file, indent = 4, ensure_ascii= False)


            ####

    # def load_tasks(self):
        
    #     file_path = r'daily_tasks\datas\tasks.json' 
        
    #     # Vérifier si le fichier existe et n'est pas vide
    #     if not os.path.exists(file_path) or os.stat(file_path).st_size == 0:
    #         return []
        
    #     try:
    #         with open(file_path, 'r', encoding="utf-8") as file:
    #             return json.load(file)
    #     except json.JSONDecodeError:
    #         # Si le fichier est corrompu ou vide, on retourne une liste vide
    #         return []