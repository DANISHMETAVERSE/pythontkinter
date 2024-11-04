import tkinter as tk
from tkinter import messagebox, simpledialog

# Student class to store student data
class Student:
    def __init__(self, number, name, coursework1, coursework2, coursework3, exam):
        self.number = number
        self.name = name
        self.coursework = [coursework1, coursework2, coursework3]
        self.exam = exam
        self.total_coursework = sum(self.coursework)
        self.total_score = self.total_coursework + self.exam
        self.percentage = (self.total_score / 160) * 100
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.percentage >= 70:
            return 'A'
        elif self.percentage >= 60:
            return 'B'
        elif self.percentage >= 50:
            return 'C'
        elif self.percentage >= 40:
            return 'D'
        else:
            return 'F'

# Load student data from a file
def load_data():
    students = []
    try:
        with open(r"C:\Users\danish\Desktop\university\py\studentMarks.txt", 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) < 6:
                    messagebox.showwarning("Warning", f"Skipping malformed line: {line.strip()}")
                    continue
                
                number = int(parts[0])
                name = parts[1]
                coursework1 = int(parts[2])
                coursework2 = int(parts[3])
                coursework3 = int(parts[4])
                exam = int(parts[5])
                students.append(Student(number, name, coursework1, coursework2, coursework3, exam))
    except FileNotFoundError:
        messagebox.showerror("Error", "The student data file was not found.")
    except ValueError as ve:
        messagebox.showerror("Error", f"Data format error: {ve}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
    
    return students

# Main application class
class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management")
        self.students = load_data()

        # Simple menu
        self.label = tk.Label(root, text="Choose an option:", font=("Arial", 12))
        self.label.pack(pady=10)

        # Buttons for different functionalities
        tk.Button(root, text="1. View All Students", command=self.view_all_students).pack(pady=5)
        tk.Button(root, text="2. View Student Record", command=self.view_student_record).pack(pady=5)
        tk.Button(root, text="3. Show Highest Score", command=self.highest_student).pack(pady=5)
        tk.Button(root, text="4. Show Lowest Score", command=self.lowest_student).pack(pady=5)
        tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

    # Function to view all student records
    def view_all_students(self):
        all_students = ""
        total_percentage = 0

        for student in self.students:
            total_percentage += student.percentage
            all_students += f"Name: {student.name}\nNumber: {student.number}\n" \
                           f"Total Coursework: {student.total_coursework}\n" \
                           f"Exam: {student.exam}\n" \
                           f"Percentage: {student.percentage:.2f}%\n" \
                           f"Grade: {student.grade}\n" + "-"*20 + "\n"
        
        avg_percentage = total_percentage / len(self.students) if self.students else 0
        all_students += f"Total Students: {len(self.students)}\nAverage: {avg_percentage:.2f}%"
        messagebox.showinfo("All Students", all_students)

    # Function to view an individual student's record
    def view_student_record(self):
        names = [f"{i+1}. {s.name}" for i, s in enumerate(self.students)]
        names_str = "\n".join(names)
        choice = simpledialog.askinteger("Select Student", f"Choose a student:\n{names_str}")

        if choice and 1 <= choice <= len(self.students):
            student = self.students[choice - 1]
            info = f"Name: {student.name}\nNumber: {student.number}\n" \
                   f"Total Coursework: {student.total_coursework}\n" \
                   f"Exam: {student.exam}\n" \
                   f"Percentage: {student.percentage:.2f}%\n" \
                   f"Grade: {student.grade}"
            messagebox.showinfo("Student Record", info)
        else:
            messagebox.showerror("Error", "Invalid selection!")

    # Function to find and show the student with the highest score
    def highest_student(self):
        if self.students:
            best_student = max(self.students, key=lambda s: s.total_score)
            info = f"Name: {best_student.name}\nNumber: {best_student.number}\n" \
                   f"Total Coursework: {best_student.total_coursework}\n" \
                   f"Exam: {best_student.exam}\n" \
                   f"Percentage: {best_student.percentage:.2f}%\n" \
                   f"Grade: {best_student.grade}"
            messagebox.showinfo("Highest Score", info)
        else:
            messagebox.showerror("Error", "No students found!")

    # Function to find and show the student with the lowest score
    def lowest_student(self):
        if self.students:
            worst_student = min(self.students, key=lambda s: s.total_score)
            info = f"Name: {worst_student.name}\nNumber: {worst_student.number}\n" \
                   f"Total Coursework: {worst_student.total_coursework}\n" \
                   f"Exam: {worst_student.exam}\n" \
                   f"Percentage: {worst_student.percentage:.2f}%\n" \
                   f"Grade: {worst_student.grade}"
            messagebox.showinfo("Lowest Score", info)
        else:
            messagebox.showerror("Error", "No students found!")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()
