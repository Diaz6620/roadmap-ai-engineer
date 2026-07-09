from tasks import create_task, get_tasks,get_task_by_id, update_task, tasks



def show_menu():
    print("\n--- TASK MANAGER ---")
    print("1. Crear tarea")
    print("2. Ver tareas")
    print("3. Buscar tarea")
    print("4. Modificar tarea")
    print("5. Salir")



def show_update_menu():
    print("\n--- MODIFICAR TAREA ---")
    print("1. Título")
    print("2. Descripción")
    print("3. Completar / Pendiente")
    print("4. Aplicar cambios")
    print("5. Salir")



def show_task(task):
    print("\n---------------------------------")
    print(f"ID: {task['id']}")
    print(f"TÍTULO: {task['title']}")
    print(f"DESCRIPCIÓN: {task['content']}") 
    if task['completed']:
        print("[X] Completada")
    else:
        print("[ ] Pendiente")
        print("---------------------------------")


def list_tasks_menu():
    print("\n--- LISTA DE TAREAS ---")

    tasks_list = get_tasks()

    if not tasks_list:
        print("No existen tareas")
        return

    for task in tasks_list:
        show_task(task)


def search_task_menu():
    print("\n--- BUSCADOR DE TAREAS ---")
    input_id = int(input("Introduce el ID: "))

    task_by_id = get_task_by_id(input_id)

    if task_by_id is None:
        print(f"No existe ninguna tarea con el ID: {input_id}")
        return
    
    show_task(task_by_id)



def find_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            return task
        
    return None



def update_menu():
    

    task_id = int(input("Introduce el ID: "))

    task_found = find_task(task_id)
        
    if task_found:
        changes = {}

        while True:
            show_update_menu()
            update_option = input("Selecciona una opción (1-5)")

            if update_option == "1":
                updated_title = input("Introduce en nuevo título: ")
                if updated_title:
                    changes['title'] = updated_title

            elif update_option == "2":
                updated_content = input("Introduce nueva descripción: ")
                if updated_content:
                    changes['content'] = updated_content

            elif update_option == "3":
                changes = {'completed': not task_found['completed']}

            elif update_option == "4":
                if not changes:
                    print("No existen cambios a aplicar")
                else:
                   task_updated = update_task(task_found, changes)
                   return show_task(task_updated)
                
            elif update_option == "5":
                break

            else:
                print("Opción inválida.")
                





def main():
    while True:
        show_menu()

        user_option = input("Selecciona una opción (1-4): ")

        if user_option == "1":
            print("\n--- CREAR TAREA ---")
            new_title = input("Introduce título: ")
            new_content = input("Introduce el contenido de la tarea: ")

            new_task = create_task(new_title, new_content)

            print("Tarea creada correctamente")
            print(f"ID: {new_task['id']}\nTÍTULO: {new_task['title']}")

        elif user_option == "2":
            list_tasks_menu()
        
        elif user_option == "3":
            search_task_menu()

        elif user_option == "4":
            update_menu()

        else:
            print("Opción inválida")





if __name__ == "__main__":
    main()
