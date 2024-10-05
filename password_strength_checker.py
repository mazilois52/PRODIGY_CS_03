import re
import tkinter as tk
from tkinter import StringVar

def assess_password_strength(password):
    strength = 0

    # Criteria checks
    if len(password) >= 8:
        strength += 1  # Length criteria
    if re.search(r'[a-z]', password):
        strength += 1  # Lowercase
    if re.search(r'[A-Z]', password):
        strength += 1  # Uppercase
    if re.search(r'\d', password):
        strength += 1  # Number
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1  # Special character

    # Feedback based on strength score
    if strength <= 2:
        return 'Weak'
    elif 3 <= strength <= 4:
        return 'Medium'
    elif strength == 5:
        return 'Strong'


def update_strength_label(event=None):
    password = password_var.get()
    feedback = assess_password_strength(password)
    strength_label.config(text=f"Password strength: {feedback}")


# Initialize the Tkinter window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")

# Create a label, entry, and result label
password_var = StringVar()
tk.Label(root, text="Enter your password:", font=('Helvetica', 12)).pack(pady=10)
password_entry = tk.Entry(root, textvariable=password_var, font=('Helvetica', 12), show="*")
password_entry.pack(pady=5)

# Label to display password strength
strength_label = tk.Label(root, text="Password strength: ", font=('Helvetica', 12), fg="blue")
strength_label.pack(pady=10)

# Bind the input event to update strength in real time
password_entry.bind("<KeyRelease>", update_strength_label)

# Run the Tkinter event loop
root.mainloop()