import random
import tkinter as tk
from tkinter import messagebox

class MathQuizApp:
    def __init__(self, master):
        self.master = master
        master.title("Math Quiz")

        self.score = 0
        self.current_question = 0

        self.menu_frame = tk.Frame(master)
        self.quiz_frame = tk.Frame(master)

        self.display_menu()

    def display_menu(self):
        self.menu_frame.pack()
        tk.Label(self.menu_frame, text='DIFFICULTY LEVEL (1-4):').pack()
        self.difficulty_var = tk.IntVar()
        tk.Entry(self.menu_frame, textvariable=self.difficulty_var).pack()
        tk.Button(self.menu_frame, text="Start Quiz", command=self.start_quiz).pack()

    def start_quiz(self):
        self.diff = self.difficulty_var.get()
        if self.diff not in [1, 2, 3, 4]:
            messagebox.showerror("Error", "Invalid choice. Please enter 1, 2, 3, or 4")
            return

        self.menu_frame.pack_forget()
        self.quiz_frame.pack()
        self.current_question = 0
        self.score = 0
        self.ask_question()

    def ask_question(self):
        if self.current_question < 10:
            n1 = self.randomInt()
            n2 = self.randomInt()
            self.operation = random.choice(['+', '-'])
            self.correct_ans = eval(f"{n1} {self.operation} {n2}")

            self.question_label = tk.Label(self.quiz_frame, text=f"{n1} {self.operation} {n2} = ?")
            self.question_label.pack()

            self.answer_var = tk.StringVar()
            answer_entry = tk.Entry(self.quiz_frame, textvariable=self.answer_var)
            answer_entry.pack()
            answer_button = tk.Button(self.quiz_frame, text="Submit", command=self.check_answer)
            answer_button.pack()
        else:
            self.display_results()

    def randomInt(self):
        if self.diff == 1:
            return random.randint(0, 9)
        elif self.diff == 2:
            return random.randint(10, 99)
        elif self.diff == 3:
            return random.randint(100, 999)
        elif self.diff == 4:
            return random.randint(1000, 9999) #extra level for those brainy ones :)

    def check_answer(self):
        try:
            user_ans = int(self.answer_var.get())
            if user_ans == self.correct_ans:
                self.score += 10
                messagebox.showinfo("Result", "Correct!")
            else:
                messagebox.showinfo("Result", f"Incorrect! The correct answer was {self.correct_ans}.")
            self.current_question += 1
            self.ask_question()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def display_results(self):
        self.quiz_frame.pack_forget()
        messagebox.showinfo("Quiz Complete", f"Your final score: {self.score} / 100")
        self.reset_quiz()

    def reset_quiz(self):
        self.menu_frame.pack_forget()
        self.display_menu()

if __name__ == "__main__":
    root = tk.Tk()
    app = MathQuizApp(root)
    root.mainloop()
