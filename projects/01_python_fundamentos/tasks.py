from datetime import datetime

tasks = []
next_id = 1



def create_task(user_title, user_content):
    global next_id

    task = {
        "id": next_id,
        "title": user_title,
        "content": user_content,
        "completed": False,
        "created_at": datetime.now()
    }

    tasks.append(task)

    next_id += 1

    return task





def get_tasks():
    return tasks.copy()





def get_task_by_id(task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task.copy()
    
    return None
    


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


    
