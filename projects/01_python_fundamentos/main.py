from tasks import create_task, get_tasks,get_task_by_id, update_task, delete_task, tasks



def show_menu():
    print("\n--- TASK MANAGER ---")
    print("1. Crear tarea")
    print("2. Ver tareas")
    print("3. Buscar tarea")
    print("4. Modificar tarea")
    print("5. Salir")



def show_update_menu():
    task_id = int(input("Introduce un ID: "))

    task_found = get_task_by_id(task_id)

    if not task_found:
        print(f"No existe ninguna tarea con el ID {task_id}")
        return

    changes = {}

    while True: 
        print("\n--- MODIFICAR TAREA ---")
        print("1. Título")
        print("2. Descripción")
        print("3. Completar / Pendiente")
        print("4. Aplicar cambios")
        print("5. Salir")

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
            changes = changes['completed'] = not task_found['completed']
        elif update_option == "4":
            if not changes:
                print("No existen cambios a aplicar")
            else:
                task_updated = update_task(task_id, changes)
                print("Tarea actualizada:")
                show_task(task_updated)
                return

        elif update_option == "5":
            break

        else:
            print("Opción inválida.")



def delete_task_menu():
    task_id = int(input("Introduce el ID: "))

    task_to_delete = get_task_by_id(task_id)

    if not task_to_delete:
        print(f"No existe ninguna tarea con el ID {task_id}")
        return
    
    show_task(task_to_delete)

    print("¿Esta seguro que desea eliminar la tarea?")

    while True:
        user_option = input("s/n: ").lower()

        if user_option == "n":
            print("Cancelado.")
            break
        elif user_option == "s":
            task_deleted = delete_task(task_to_delete)
            print("Tarea eliminada correctamente:")
            show_task(task_deleted)

            break
        else:
            print("Opción inválida...")
    
    



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

        elif user_option == "4":
            show_update_menu()

        elif user_option == "5":
            delete_task_menu()

        else:
            print("Opción inválida")





if __name__ == "__main__":
    main()
