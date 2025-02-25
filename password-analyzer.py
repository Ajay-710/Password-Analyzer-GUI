import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
import re
import random
import string

def check_password_strength(event=None):
    password = password_entry.get()
    strength, feedback = evaluate_password(password)
    
    # Update progress bar
    progress['value'] = strength
    
    # Change color based on strength
    if strength < 40:
        progress.style.configure("Strength.Horizontal.TProgressbar", foreground='red', background='red')
    elif strength < 70:
        progress.style.configure("Strength.Horizontal.TProgressbar", foreground='yellow', background='yellow')
    else:
        progress.style.configure("Strength.Horizontal.TProgressbar", foreground='green', background='green')
    
    feedback_label.config(text=feedback)

def evaluate_password(password):
    strength = 0
    feedback = ""
    
    if len(password) >= 8:
        strength += 20
    else:
        feedback += "Make your password at least 8 characters long. "
    
    if re.search(r'[A-Z]', password):
        strength += 20
    else:
        feedback += "Add at least one uppercase letter. "
    
    if re.search(r'[a-z]', password):
        strength += 20
    else:
        feedback += "Add at least one lowercase letter. "
    
    if re.search(r'[0-9]', password):
        strength += 20
    else:
        feedback += "Include at least one number. "
    
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 20
    else:
        feedback += "Use special characters like !@#$. "
    
    return strength, feedback.strip()

def generate_password():
    generated = ''.join(random.choices(string.ascii_letters + string.digits + '!@#$%^&*()', k=12))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, generated)
    check_password_strength()

def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    theme = "darkly" if dark_mode else "flatly"
    style.theme_use(theme)
    toggle_button.config(text="Dark Mode" if not dark_mode else "Light Mode")

# Initialize main window
root = tk.Tk()
root.title("Password Analyzer")
root.geometry("400x300")

# Apply ttkbootstrap theme
style = tb.Style("darkly")
dark_mode = True

frame = ttk.Frame(root, padding=20)
frame.pack(fill=tk.BOTH, expand=True)

password_label = ttk.Label(frame, text="Enter Password:")
password_label.pack(anchor='w')

password_entry = ttk.Entry(frame, width=30)
password_entry.pack(fill=tk.X, pady=5)
password_entry.bind('<KeyRelease>', check_password_strength)

progress = ttk.Progressbar(frame, length=200, mode='determinate', style="Strength.Horizontal.TProgressbar")
progress.pack(fill=tk.X, pady=5)

feedback_label = ttk.Label(frame, text="", wraplength=350, foreground='white')
feedback_label.pack(anchor='w')

generate_button = ttk.Button(frame, text="Generate Password", command=generate_password)
generate_button.pack(side=tk.LEFT, padx=5, pady=10)

toggle_button = ttk.Button(frame, text="Light Mode", command=toggle_theme)
toggle_button.pack(side=tk.RIGHT, padx=5, pady=10)

root.mainloop()
