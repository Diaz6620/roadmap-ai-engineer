import json
from pathlib import Path

DATA_FILE = Path("data/tasks.json")



def load_tasks():
    if not DATA_FILE.exists():
        return {
            "next_id": 1,
            "tasks": []
        }
    
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)
    



def save_tasks(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file)