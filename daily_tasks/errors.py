from daily_tasks.storage import TaskStorage
from pathlib import Path
import os


file_path = Path(__file__).parent/"datas"/"tasks.json"
print(file_path)

# the file is inexistant or empty

def no_file_or_empty(func):
    def wrapper():
        if not file_path or os.path.getsize(file_path) == 0:
            print("Fichier datas/tasks.json inexistant, création du fichier")
            with open(file_path, 'x', encoding="utf-8") as file:
                file.write("[]")



    