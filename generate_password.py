import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    character_set = ""
    if use_upper:
        character_set += string.ascii_uppercase
    if use_lower:
        character_set += string.ascii_lowercase
    if use_digits:
        character_set += string.digits
    if use_special:
        character_set += string.punctuation
    
    if not character_set:
        messagebox.showwarning("Error", "Please select at least one character type")
        return ""

    return ''.join(random.choice(character_set) for _ in range(length))

def generate_and_display_password():
    length = int(length_entry.get())
    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digits_var.get()
    use_special = special_var.get()

    password = generate_password(length, use_upper, use_lower, use_digits, use_special)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

root = tk.Tk()
root.title("Генератор пароля/ів")

tk.Label(root, text="Довжина пароля:").grid(row=0, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_var = tk.BooleanVar()

tk.Checkbutton(root, text="Великі літери", variable=upper_var).grid(row=1, column=0, sticky="w")
tk.Checkbutton(root, text="Малі літери", variable=lower_var).grid(row=2, column=0, sticky="w")
tk.Checkbutton(root, text="Цифри", variable=digits_var).grid(row=3, column=0, sticky="w")
tk.Checkbutton(root, text="Спеціальні символи", variable=special_var).grid(row=4, column=0, sticky="w")

tk.Button(root, text="Згенерувати пароль", command=generate_and_display_password).grid(row=5, column=0, columnspan=2)

password_entry = tk.Entry(root, width=40)
password_entry.grid(row=6, column=0, columnspan=2)

root.mainloop()