import tkinter as tk
from tkinter import messagebox

# Sample quiz data
quiz_data = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Rome", "Berlin"], "answer": "Paris", "type": "single"},
    {"question": "Select prime numbers:", "options": ["2", "3", "4", "5"], "answer": ["2", "3", "5"], "type": "multi"},
    {"question": "Fill in the blank: The sun rises in the _____.", "answer": "east", "type": "fill"}
]

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.current_question = 0
        self.score = 0
        self.user_answers = []
        self.create_widgets()
        self.load_question()

    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="", font=("Arial", 14), wraplength=400, justify="left")
        self.question_label.pack(pady=10)
        
        self.options_frame = tk.Frame(self.root)
        self.options_frame.pack()
        
        self.next_button = tk.Button(self.root, text="Next", command=self.next_question)
        self.next_button.pack(pady=10)

    def load_question(self):
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        
        question_data = quiz_data[self.current_question]
        self.question_label.config(text=question_data["question"])
        
        if question_data["type"] == "single":
            self.var = tk.StringVar()
            for option in question_data["options"]:
                rb = tk.Radiobutton(self.options_frame, text=option, variable=self.var, value=option)
                rb.pack(anchor="w")
        elif question_data["type"] == "multi":
            self.vars = {}
            for option in question_data["options"]:
                self.vars[option] = tk.BooleanVar()
                cb = tk.Checkbutton(self.options_frame, text=option, variable=self.vars[option])
                cb.pack(anchor="w")
        elif question_data["type"] == "fill":
            self.entry = tk.Entry(self.options_frame)
            self.entry.pack()

    def next_question(self):
        question_data = quiz_data[self.current_question]
        user_answer = None

        if question_data["type"] == "single":
            user_answer = self.var.get()
        elif question_data["type"] == "multi":
            user_answer = [key for key, var in self.vars.items() if var.get()]
        elif question_data["type"] == "fill":
            user_answer = self.entry.get().strip().lower()

        self.user_answers.append(user_answer)

        if question_data["type"] == "single" and user_answer == question_data["answer"]:
            self.score += 1
        elif question_data["type"] == "multi" and set(user_answer) == set(question_data["answer"]):
            self.score += 1
        elif question_data["type"] == "fill" and user_answer == question_data["answer"].lower():
            self.score += 1

        self.current_question += 1
        if self.current_question < len(quiz_data):
            self.load_question()
        else:
            self.show_result()

    def show_result(self):
        messagebox.showinfo("Quiz Completed", f"Your score: {self.score}/{len(quiz_data)}")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()
