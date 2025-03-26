import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []
        
        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)
        
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(side="left", padx=5)
        
        self.edit_button = tk.Button(root, text="Edit Task", command=self.edit_task)
        self.edit_button.pack(side="left", padx=5)
        
        self.complete_button = tk.Button(root, text="Mark Completed", command=self.mark_completed)
        self.complete_button.pack(side="left", padx=5)
        
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side="left", padx=5)
    
    def add_task(self):
        task_text = simpledialog.askstring("Add Task", "Enter task:")
        if task_text:
            due_date = simpledialog.askstring("Task Date", "Enter due date (YYYY-MM-DD HH:MM):")
            try:
                due_date_obj = datetime.strptime(due_date, "%Y-%m-%d %H:%M")
                task_entry = f"{task_text} (Due: {due_date_obj})"
                self.tasks.append(task_entry)
                self.update_listbox()
            except ValueError:
                messagebox.showerror("Error", "Invalid date format!")
    
    def edit_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0]
            new_task_text = simpledialog.askstring("Edit Task", "Edit task:", initialvalue=self.tasks[selected_task_index])
            if new_task_text:
                self.tasks[selected_task_index] = new_task_text
                self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Select a task to edit!")
    
    def mark_completed(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0]
            self.tasks[selected_task_index] = "✔ " + self.tasks[selected_task_index]
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Select a task to mark as completed!")
    
    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0]
            del self.tasks[selected_task_index]
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Select a task to delete!")
    
    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
