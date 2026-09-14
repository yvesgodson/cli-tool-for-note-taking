from pathlib import Path
import json



class TaskStorage:
    
    def __init__(self):
        self.file_path = Path(__file__).parent/"datas"/"tasks.json"
        

    def load_tasks(self):
        with self.file_path.open('r', encoding="utf-8") as file:
            return json.load(file)
        
    def save_task(self, tasks):
        with self.file_path.open('w', encoding="utf-8") as file:
            json.dump(tasks, file, indent = 4, ensure_ascii= False)