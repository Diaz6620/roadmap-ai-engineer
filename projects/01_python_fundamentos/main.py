from tasks import create_task, get_tasks,get_task_by_id, tasks



def show_menu():
    print("\n--- TASK MANAGER ---")
    print("1. Crear tarea")
    print("2. Ver tareas")
    print("3. Buscar tarea")
    print("4. Salir")



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

        else:
            print("Opción inválida")





if __name__ == "__main__":
    main()
