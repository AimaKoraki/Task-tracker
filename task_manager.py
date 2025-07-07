import json
from datetime import datetime, timezone

# Simple CLI Todo Application
JSON_FILE = 'todo.json' 

# --- Helper Functions ---
def get_timestamp():
    """Returns the current time as a standardized string."""
    return datetime.now(timezone.utc).isoformat()

def load_todos():
    """Loads todos from the JSON file. Returns an empty list if the file doesn't exist."""
    
    try:
        with open(JSON_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_todos(todos):
    """Saves the list of todos to the JSON file."""
    with open(JSON_FILE, "w") as file:
        json.dump(todos, file, indent=2)

def get_next_id(todos):
    """Calculates the next ID for a new todo."""
    if not todos:
        return 1
    return max(todo['id'] for todo in todos) + 1


# --- Core Logic Functions ---
def add_todo(todos, title):
    """Adds a new todo to the list and saves it."""
    new_todo = {
        'id': get_next_id(todos),
        'title': title,
        'description': '',
        'status': 'pending', 
        'created_at': get_timestamp(),
        'updated_at': get_timestamp()
    }
    todos.append(new_todo)
    save_todos(todos)
    print(f"✅ Added todo: '{title}' (ID: {new_todo['id']})")

def list_todos(todos):
    """Prints all todos to the console."""
    if not todos:
        print("No todos found. Add one with the 'add' command!")
        return
    print("--- Your To-Do List ---")
    for todo in todos:
        status = todo['status'].capitalize()
        print(f"[{todo['id']}] {todo['title']} - Status: {status}")
    print("-----------------------")


def update_todo(todos, todo_id, new_title=None, new_status=None):
    """Updates the title or status of an existing todo."""
    task_found = False
    for todo in todos:
        if todo['id'] == todo_id:
            task_found = True
            if new_title is not None:
                todo['title'] = new_title
                print(f"✅ Updated title for todo {todo_id} to '{new_title}'")
            if new_status is not None:
                todo['status'] = new_status
                print(f"✅ Updated status for todo {todo_id} to '{new_status}'")

            todo['updated_at'] = get_timestamp()
            break 

    if task_found:
        save_todos(todos)
    else:
        print(f"❌ Error: Todo with ID {todo_id} not found.")


def delete_todo(todos, todo_id):
    """Deletes a todo from the list by its ID."""
    original_length = len(todos)
    new_todos = [todo for todo in todos if todo['id'] != todo_id]

    if len(new_todos) == original_length:
        print(f"❌ Error: Todo with ID {todo_id} not found.")
    else:
        save_todos(new_todos)
        print(f"✅ Deleted todo {todo_id}")
