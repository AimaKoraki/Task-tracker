# Task Tracker CLI & GUI 
(https://roadmap.sh/projects/task-tracker)

A simple, lightweight, and dependency-free command-line and graphical application to manage your to-do list. Built with pure Python, this tool helps you track tasks by adding, updating, and deleting them directly from your terminal or a simple GUI, with all data stored locally in a `todo.json` file.

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## Features

- **No External Dependencies**: Built entirely with Python's standard library.
- **Persistent Storage**: Tasks are saved in a `todo.json` file in the same directory.
- **Full CRUD Functionality**: Create, Read, Update, and Delete tasks.
- **Task Statuses**: Mark tasks as `pending`, `progress`, or `done`.
- **Dual Interface**:
  - **CLI**: A robust command-line interface for terminal power-users.
  - **GUI**: A user-friendly graphical interface for easy interaction.

---

## Prerequisites

- Python 3.x

---

## Setup & Installation

1.  **Clone the repository** or download the files into a new directory:
    ```bash
    git clone (https://github.com/AimaKoraki/Task-tracker.git)
    cd <your-repository-folder>
    ```

2.  That's it! No installation is needed. The `todo.json` data file will be created automatically the first time you add a task.

---

## How to Use the CLI (`todo_cli.py`)

Run all commands from your terminal in the project directory.

### Add a Task

To add a new task, use the `add` command followed by the task title.
```bash
python todo_cli.py add "Buy groceries for the week"
```

### List All Tasks

To see all your current tasks, their IDs, and their statuses:
```bash
python todo_cli.py list
```
### Update a Task Tasks

To change a task's title::
```bash
python todo_cli.py update <ID> "New task title"
```

To change a task's status:
Use the done, progress, or pending commands followed by the task ID.
```bash
python todo_cli.py done 1
python todo_cli.py progress 2
```

### Delete a Task
To permanently remove a task, use the delete command with the task's ID:
```bash
python todo_cli.py delete <ID>
```

---

###How to Use the GUI (todo_gui.py)
To run the graphical interface, execute the todo_gui.py script:

```bash
python todo_gui.py
```

This will open a window where you can:
- **View all tasks in a scrollable list.
- **Filter tasks by status by clicking the filter buttons at the top.
- **Add a new task by typing in the entry box and clicking "Add Task".
- **Update a task by clicking it in the list (its title will appear in the entry box), editing the title, and clicking "Update Selected".
- **Delete a task by selecting it from the list and clicking "Delete Selected".

---

###File Structure

.
├── todo_cli.py      # The command-line interface script.
├── todo_gui.py      # The graphical user interface script.
├── task_manager.py  # The core backend logic for managing tasks.
├── todo.json        # The JSON file where tasks are stored.
└── README.md        # This file.

