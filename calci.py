import tkinter as tk
from tkinter import messagebox

def on_click(event):
    text = event.widget.cget("text")  # Get button text
    if text == "=":  # Evaluate expression
        try:
            result = eval(str(entry_var.get()))  # Calculate
            entry_var.set(result)
        except Exception:
            messagebox.showerror("Error", "Invalid Expression")
            entry_var.set("")
    elif text == "C":  # Clear input
        entry_var.set("")
    else:  # Append button text to input
        entry_var.set(entry_var.get() + text)

def key_press(event):
    key = event.char  # Get pressed key
    if key in "0123456789+-*/().":  # Allow only valid characters
        entry_var.set(entry_var.get() + key)
    elif key == "\r":  # Press Enter to evaluate
        try:
            result = eval(str(entry_var.get()))
            entry_var.set(result)
        except Exception:
            messagebox.showerror("Error", "Invalid Expression")
            entry_var.set("")
    elif key == "\x08":  # Backspace to delete last character
        entry_var.set(entry_var.get()[:-1])

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Create entry field
entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font=("Arial", 18), justify="right")
entry.pack(fill="both", ipadx=8, ipady=8, padx=10, pady=10)
entry.bind("<Key>", key_press)  # Bind keyboard input

# Create button grid
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

button_frame = tk.Frame(root)
button_frame.pack()

for row in buttons:
    frame = tk.Frame(button_frame)
    frame.pack(side="top", fill="both")
    for char in row:
        btn = tk.Button(frame, text=char, font=("Arial", 18), width=5, height=2)
        btn.pack(side="left", expand=True, fill="both")
        btn.bind("<Button-1>", on_click)  # Bind button clicks

# Run the application
root.mainloop()
