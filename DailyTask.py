import tkinter as tk
from tkinter import messagebox
import json
import datetime

# Load previous tasks from a file
def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Save tasks to a file
def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

# Get tomorrow's date
def get_tomorrow_date():
    return (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

# Add task for tomorrow
def add_task():
    task = task_entry.get()
    if task:
        tomorrow = get_tomorrow_date()
        if tomorrow not in tasks:
            tasks[tomorrow] = {"completed": [], "pending": []}
        tasks[tomorrow]["pending"].append(task)
        save_tasks(tasks)
        task_entry.delete(0, tk.END)
        update_task_lists()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Complete task
def complete_task():
    selected_task = pending_listbox.curselection()
    if selected_task:
        task = pending_listbox.get(selected_task)
        tomorrow = get_tomorrow_date()
        if tomorrow in tasks and task in tasks[tomorrow]["pending"]:
            tasks[tomorrow]["pending"].remove(task)
            tasks[tomorrow]["completed"].append(task)
            save_tasks(tasks)
            update_task_lists()
        else:
            messagebox.showwarning("Task Error", "Selected task is not in the pending list.")
    else:
        messagebox.showwarning("Selection Error", "Please select a task to complete.")

# Update the task lists in the GUI
def update_task_lists():
    tomorrow = get_tomorrow_date()
    
    # Clear both listboxes
    pending_listbox.delete(0, tk.END)
    completed_listbox.delete(0, tk.END)

    if tomorrow in tasks:
        # Add pending tasks to the pending listbox
        for task in tasks[tomorrow]["pending"]:
            pending_listbox.insert(tk.END, task)
        
        # Add completed tasks to the completed listbox
        for task in tasks[tomorrow]["completed"]:
            completed_listbox.insert(tk.END, task)
    else:
        pending_listbox.insert(tk.END, "No tasks for tomorrow.")
        completed_listbox.insert(tk.END, "No completed tasks.")

# Create the main window
root = tk.Tk()
root.title("Daily Task Planner")

# Load tasks from file
tasks = load_tasks()

# Create a label for the task entry
task_label = tk.Label(root, text="Enter a task for tomorrow:")
task_label.pack(pady=10)

# Create an entry widget for tasks
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=5)

# Add task button
add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_button.pack(pady=5)

# Frame for holding both listboxes
listbox_frame = tk.Frame(root)
listbox_frame.pack(pady=10)

# Create a listbox to display pending tasks
pending_listbox = tk.Listbox(listbox_frame, width=50, height=10)
pending_listbox.pack(side=tk.LEFT, padx=5)

# Create a listbox to display completed tasks
completed_listbox = tk.Listbox(listbox_frame, width=50, height=10)
completed_listbox.pack(side=tk.LEFT, padx=5)

# Complete task button
complete_button = tk.Button(root, text="Complete Task", width=20, command=complete_task)
complete_button.pack(pady=5)

# Update task lists initially
update_task_lists()

# Run the main event loop
root.mainloop()
