from datetime import datetime
from copy import deepcopy

tasks = []
next_id = 1



def initialize_tasks(data):
    global tasks
    global next_id

    tasks = data["tasks"]
    next_id = data["next_id"]




def get_state():
    return {
        "next_id": next_id,
        "tasks": deepcopy(tasks)
    }



def create_task(user_title, user_content):
    global next_id

    task = {
        "id": next_id,
        "title": user_title,
        "content": user_content,
        "completed": False,
        "created_at": datetime.now().isoformat()
    }

    tasks.append(task)

    next_id += 1

    return task




def get_tasks():
    return tasks.copy()

    



def update_task(task_id, changes):
    task = get_task_by_id(task_id)

    if not task:
        return None
    
    task.update(changes)
    return task
    



            
def delete_task(task):
    if not task:
        return None
    
    tasks.remove(task)
    return task






def get_task_by_id(task_id):
    for t in tasks:
        if t['id'] == task_id:
            return t

    return None 


