import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        task_listbox.delete(task_listbox.curselection()[0])
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete!")

def update_task():
    try:
        selected = task_listbox.curselection()[0]
        new_task = task_entry.get()
        if new_task:
            task_listbox.delete(selected)
            task_listbox.insert(selected, new_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to update!")

def clear_tasks():
    task_listbox.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Button(frame, text="Add", command=add_task, width=12).grid(row=0, column=0, padx=5)
tk.Button(frame, text="Update", command=update_task, width=12).grid(row=0, column=1, padx=5)
tk.Button(frame, text="Delete", command=delete_task, width=12).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame, text="Clear", command=clear_tasks, width=12).grid(row=1, column=1, padx=5, pady=5)

task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

root.mainloop()

