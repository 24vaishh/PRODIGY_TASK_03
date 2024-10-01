import tkinter as tk
from tkinter import messagebox
import re

# Function to assess the strength of the password
def check_password_strength(password):
    strength = 0
    feedback = []

    # Check the length of the password
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should have at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should have at least one lowercase letter.")

    # Check for numbers
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Check for special characters
    if re.search(r'[@$!%*?&#]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one special character (@, $, !, %, *, ?, &, #).")

    # Determine overall strength
    if strength == 5:
        return "Strong", feedback
    elif strength >= 3:
        return "Moderate", feedback
    else:
        return "Weak", feedback

# Function to handle the button click
def on_submit():
    password = password_entry.get()
    strength, feedback = check_password_strength(password)

    feedback_message = "\n".join(feedback)
    if feedback_message:
        messagebox.showinfo("Password Feedback", f"Password Strength: {strength}\n\n{feedback_message}")
    else:
        messagebox.showinfo("Password Feedback", f"Password Strength: {strength}")

# Function to reset the input field
def reset_fields():
    password_entry.delete(0, tk.END)
    show_password_var.set(0)
    password_entry.config(show="*")

# Function to toggle show/hide password
def toggle_password():
    if show_password_var.get() == 1:
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

# Create the GUI window
root = tk.Tk()
root.title("Password Strength Checker")

# Add a label and entry box for password input
tk.Label(root, text="Enter your password:").grid(row=0, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.grid(row=0, column=1, padx=10, pady=10)

# Add a checkbox to show or hide the password
show_password_var = tk.IntVar()
show_password_check = tk.Checkbutton(root, text="Show Password", variable=show_password_var, command=toggle_password)
show_password_check.grid(row=1, column=1, sticky="w", padx=10)

# Add a submit button
submit_button = tk.Button(root, text="Check Strength", command=on_submit)
submit_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Add a reset button
reset_button = tk.Button(root, text="Reset", command=reset_fields)
reset_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
