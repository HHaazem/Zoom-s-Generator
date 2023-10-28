import random
import tkinter as tk
from tkinter import messagebox

def generate_password():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()"

    all_characters = lower + upper + numbers + symbols
    password_length = 16
    password = "".join(random.sample(all_characters, password_length))
    return password

def save_password():
    website = website_entry.get()
    password = generate_password()
    
    with open("passwords.txt", "a") as file:
        if file.tell() != 0:
            file.write("\n")
        file.write(website + " " + password)

    messagebox.showinfo("Password Generator", f"Password for {website} has been saved to 'passwords.txt'")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and configure UI elements
website_label = tk.Label(root, text="Website or Service:")
website_label.pack()

website_entry = tk.Entry(root)
website_entry.pack()

generate_button = tk.Button(root, text="Generate and Save Password", command=save_password)
generate_button.pack()

# Start the Tkinter main loop
root.mainloop()