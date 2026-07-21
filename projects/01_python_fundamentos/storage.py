import json
from pathlib import Path
import exceptions

DATA_FILE = Path("data/tasks.json")



def load_tasks():
    if not DATA_FILE.exists():
        initialize_storage()
    
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            content = file.read()

            if not content.strip():
                raise exceptions.StorageEmptyError("El archivo de tareas está vacío.")

            return json.loads(content)

    except json.JSONDecodeError as error:
        raise exceptions.DataLoadError("El archivo contiene datos inválidos.") from error
        
    except OSError as error:
        raise exceptions.DataLoadError("Error al acceder al archivo.") from error
        
    
    



def save_tasks(data):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file)

    except OSError as error:
        raise exceptions.DataSaveError("No se pudo excribir el archivo de tareas") from error
    
    except TypeError as error:
        raise exceptions.DataSaveError("Los datos tienen un formato no válido para guardarse") from error





def initialize_storage():
    try:
        DATA_FILE.parent.mkdir(exist_ok=True)
    
    
        initial_state = {
            "next_id": 1,
            "tasks": []
        }

        save_tasks(initial_state)

        return initial_state

    except (OSError, exceptions.DataSaveError) as error:
        raise exceptions.DataLoadError("No se pudo preparar el almacenamiento") from error


        
    