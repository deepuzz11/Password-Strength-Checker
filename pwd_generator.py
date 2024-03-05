import random
import string
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import re

def generate_password(length):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def check_strength(password):
    # Check password strength
    if len(password) < 8:
        return "Weak"
    elif re.search("[a-z]", password) is None or re.search("[A-Z]", password) is None or re.search("[0-9]", password) is None or re.search("[!@#$%^&*()_+}{\":?><]", password) is None:
        return "Medium"
    else:
        return "Strong"

def generate_password_gui():
    try:
        password = password_entry.get()
        
        strength = check_strength(password)
        
        if strength == "Weak":
            # Display a generated strong password
            generated_password = generate_password(12)
            generated_password_label.config(text="Generated Strong Password: " + generated_password)
            generated_password_frame.pack(pady=padding_y)
        else:
            messagebox.showinfo("Password Strength", "Your password is strong!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create a tkinter window
window = tk.Tk()
window.title("Password Generator")

# Add padding
padding_y = 10
padding_x = 20

# Create a label for instructions
instruction_label = tk.Label(window, text="Enter your desired password:", font=("Helvetica", 12))
instruction_label.pack(pady=padding_y)

# Create an entry for the password
password_entry = tk.Entry(window, font=("Helvetica", 12), show="*")
password_entry.pack(pady=padding_y)

# Create a button to check the password strength
check_strength_button = tk.Button(window, text="Check Strength", font=("Helvetica", 12), command=generate_password_gui)
check_strength_button.pack(pady=padding_y)

# Create a frame to display a generated strong password
generated_password_frame = ttk.Frame(window)
generated_password_label = tk.Label(generated_password_frame, text="", font=("Helvetica", 12), wraplength=400)
generated_password_label.pack(pady=padding_y)

# Center the window
window.update_idletasks()
width = window.winfo_width()
height = window.winfo_height()
x_offset = (window.winfo_screenwidth() - width) // 2
y_offset = (window.winfo_screenheight() - height) // 2
window.geometry(f"{width}x{height}+{x_offset}+{y_offset}")

# Run the tkinter event loop
window.mainloop()


