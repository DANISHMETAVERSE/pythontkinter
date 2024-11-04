import tkinter as tk
import random

def load_jokes(filename):
    jokes = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split('?')
                if len(parts) == 2:
                    jokes.append(parts)
        if not jokes:
            print("Warning: No jokes found in the file.")
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    return jokes

def tell_joke():
    if not jokes:
        joke_label.config(text="No jokes available!")
        punchline_button.config(state=tk.DISABLED)
        return

    setup, punchline = random.choice(jokes)
    joke_label.config(text=setup)
    punchline_button.config(state=tk.NORMAL)
    punchline_button['command'] = lambda: show_punchline(punchline)

def show_punchline(punchline):
    joke_label.config(text=punchline)
    punchline_button.config(state=tk.DISABLED)

def create_gui():
    global joke_label, punchline_button
    root = tk.Tk()
    root.title("Alexa's Joke")
    
    joke_label = tk.Label(root, text="Alexa, Tell me a Joke!", font=("Arial", 14), wraplength=300)
    joke_label.pack(pady=20)

    tell_joke_button = tk.Button(root, text="Tell me a joke", command=tell_joke, font=("Arial", 12))
    tell_joke_button.pack(pady=10)

    punchline_button = tk.Button(root, text="Show punchline", state=tk.DISABLED)
    punchline_button.pack(pady=10)

    quit_button = tk.Button(root, text="Quit", command=root.quit, font=("Arial", 12))
    quit_button.pack(pady=20)

    root.mainloop()

# Load jokes from the file
jokes = load_jokes(r"C:\Users\danish\Desktop\university\py\jokes.txt")
create_gui()
