import tkinter as tk
from tkinter import messagebox
import task_manager 

class TaskTrackerApp:
    def __init__(self, root):
        """
        Initialize the Task Tracker application.
        This is the main constructor for the GUI.
        """
        self.root = root
        self.root.title("Task Tracker GUI")
        self.root.geometry("500x550")
        self.root.resizable(False, False)

        
        self.filter_frame = tk.Frame(root, pady=5)
        self.filter_frame.pack(fill='x', padx=10)

        self.list_frame = tk.Frame(root)
        self.list_frame.pack(fill='both', expand=True, padx=10)

        self.input_frame = tk.Frame(root, pady=10)
        self.input_frame.pack(fill='x', padx=10)

        self.action_frame = tk.Frame(root, pady=10)
        self.action_frame.pack(fill='x', padx=10)


       

        # Filter buttons
        tk.Button(self.filter_frame, text="All", command=self.refresh_listbox).pack(side='left', padx=2)
        tk.Button(self.filter_frame, text="Pending", command=lambda: self.refresh_listbox('pending')).pack(side='left', padx=2)
        tk.Button(self.filter_frame, text="In Progress", command=lambda: self.refresh_listbox('progress')).pack(side='left', padx=2)
        tk.Button(self.filter_frame, text="Done", command=lambda: self.refresh_listbox('done')).pack(side='left', padx=2)
        
        # Listbox with a Scrollbar
        self.tasks_listbox = tk.Listbox(self.list_frame, height=15, selectmode=tk.SINGLE, font=("Helvetica", 12))
        self.scrollbar = tk.Scrollbar(self.list_frame, orient=tk.VERTICAL, command=self.tasks_listbox.yview)
        self.tasks_listbox.config(yscrollcommand=self.scrollbar.set)
        
        self.scrollbar.pack(side='right', fill='y')
        self.tasks_listbox.pack(side='left', fill='both', expand=True)

        # Input entry for adding/updating tasks
        tk.Label(self.input_frame, text="Task Title:", font=("Helvetica", 10)).pack(side='left')
        self.task_entry = tk.Entry(self.input_frame, width=45, font=("Helvetica", 12))
        self.task_entry.pack(side='left', fill='x', expand=True)

        # Main action buttons
        self.add_button = tk.Button(self.action_frame, text="Add Task", command=self.add_task_command)
        self.add_button.pack(side='left', padx=5, pady=5)

        self.update_button = tk.Button(self.action_frame, text="Update Selected", command=self.update_task_command)
        self.update_button.pack(side='left', padx=5, pady=5)

        self.delete_button = tk.Button(self.action_frame, text="Delete Selected", command=self.delete_task_command)
        self.delete_button.pack(side='left', padx=5, pady=5)


     
        self.tasks_listbox.bind("<<ListboxSelect>>", self.on_task_select)

    
        self.refresh_listbox()


  
    def refresh_listbox(self, status_filter=None):
        """Clears and re-populates the listbox with tasks from the JSON file."""
        self.tasks_listbox.delete(0, tk.END)  # Clear all items
        todos = task_manager.load_todos()
        for task in todos:
            if status_filter is None or task['status'] == status_filter:
                display_text = f"[{task['id']}] [{task['status']}] - {task['title']}"
                self.tasks_listbox.insert(tk.END, display_text)


    # --- Command functions for buttons ---
    def add_task_command(self):
        """Handles the 'Add Task' button click."""
        title = self.task_entry.get()
        if not title:
            messagebox.showwarning("Input Error", "Task title cannot be empty.")
            return
        
        todos = task_manager.load_todos()
        task_manager.add_todo(todos, title) 
        self.task_entry.delete(0, tk.END)  
        self.refresh_listbox() 
        messagebox.showinfo("Success", "Task added successfully!")

    def update_task_command(self):
        """Handles the 'Update Selected' button click."""
        task_id = self.get_selected_task_id()
        if task_id is None:
            return 
        
        new_title = self.task_entry.get()
        if not new_title:
            messagebox.showwarning("Input Error", "New title cannot be empty.")
            return

        todos = task_manager.load_todos()
        task_manager.update_todo(todos, task_id, new_title=new_title)
        self.task_entry.delete(0, tk.END)
        self.refresh_listbox()
        messagebox.showinfo("Success", f"Task {task_id} updated.")

    def delete_task_command(self):
        """Handles the 'Delete Selected' button click."""
        task_id = self.get_selected_task_id()
        if task_id is None:
            return

        
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete task {task_id}?"):
            todos = task_manager.load_todos()
            task_manager.delete_todo(todos, task_id)
            self.refresh_listbox()
            messagebox.showinfo("Success", f"Task {task_id} deleted.")

    # --- Event handler and helper method ---
    def on_task_select(self, event):
        """Fills the entry box with the title of the selected task."""
        # Check if anything is selected
        selection_indices = self.tasks_listbox.curselection()
        if not selection_indices:
            return

        selected_text = self.tasks_listbox.get(selection_indices[0])
        
        # Parse the title from the display string: "[id] [status] - title"
        try:
            title = selected_text.split(' - ', 1)[1]
            self.task_entry.delete(0, tk.END)
            self.task_entry.insert(0, title)
        except IndexError:
            # This handles cases where the format might be unexpected
            pass

    def get_selected_task_id(self):
        """Helper function to get the ID of the currently selected task."""
        try:
            selection_indices = self.tasks_listbox.curselection()
            if not selection_indices:
                messagebox.showerror("Selection Error", "Please select a task from the list first.")
                return None
            
            selected_text = self.tasks_listbox.get(selection_indices[0])
            # Parse the ID from the string: "[id] ..."
            task_id = int(selected_text.split('[', 1)[1].split(']', 1)[0])
            return task_id
        except (IndexError, ValueError):
            messagebox.showerror("Error", "Could not parse the task ID.")
            return None


# --- Main execution block ---
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskTrackerApp(root)
    root.mainloop()