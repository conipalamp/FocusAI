import json

# Archivo donde guardaremos las tareas
TASKS_FILE = "tasks.json"

def load_tasks():
    """Carga las tareas desde el archivo JSON."""
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Si no hay archivo, devuelve una lista vacía

def save_tasks(tasks):
    """Guarda las tareas en el archivo JSON."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    """Añade una nueva tarea a la lista."""
    tasks = load_tasks()
    task = {"description": description, "completed": False}
    tasks.append(task)
    save_tasks(tasks)

def list_tasks():
    """Lista todas las tareas guardadas."""
    tasks = load_tasks()
    return tasks

def complete_task(index):
    """Marca una tarea como completada."""
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)

def delete_task(index):
    """Elimina una tarea."""
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        del tasks[index]
        save_tasks(tasks)
