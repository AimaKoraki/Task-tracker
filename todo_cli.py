import sys
import task_manager



def main():
    """
    The main function for the Command-Line Interface.
    It parses user commands and calls the appropriate functions from the task_manager.
    """
    # First, load the current list of todos. This is passed to every function that needs it.
    todos = task_manager.load_todos()

    if len(sys.argv) < 2:
        print("Usage: python todo_cli.py <command> [<args>]")
        print("Commands: add, list, update, delete, done, pending, progress")
        return

    command = sys.argv[1].lower()

    if command == 'add':
        if len(sys.argv) < 3:
            print("Usage: python todo_cli.py add <title>")
            return
        title = " ".join(sys.argv[2:])
        # Call the logic function from the other file
        task_manager.add_todo(todos, title)

    elif command == 'list':
        # Call the logic function
        task_manager.list_todos(todos)

    elif command == 'update':
        if len(sys.argv) < 4:
            print("Usage: python todo_cli.py update <id> <new_title>")
            return
        try:
            todo_id = int(sys.argv[2])
            new_title = " ".join(sys.argv[3:])
            # Call the logic function
            task_manager.update_todo(todos, todo_id, new_title=new_title)
        except ValueError:
            print(f"❌ Error: Invalid ID '{sys.argv[2]}'. ID must be a number.")

    elif command in ['done', 'progress', 'pending']:
        if len(sys.argv) < 3:
            print(f"Usage: python todo_cli.py {command} <id>")
            return
        try:
            todo_id = int(sys.argv[2])
            # Call the logic function
            task_manager.update_todo(todos, todo_id, new_status=command)
        except ValueError:
            print(f"❌ Error: Invalid ID '{sys.argv[2]}'. ID must be a number.")

    elif command == 'delete':
        if len(sys.argv) < 3:
            print("Usage: python todo_cli.py delete <id>")
            return
        try:
            todo_id = int(sys.argv[2])
            # Call the logic function
            task_manager.delete_todo(todos, todo_id)
        except ValueError:
            print(f"❌ Error: Invalid ID '{sys.argv[2]}'. ID must be a number.")

    else:
        print(f"❌ Error: Unknown command '{command}'")

# This part remains the same. It's the standard entry point for a Python script.
if __name__ == "__main__":
    main()