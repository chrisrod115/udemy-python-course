from tkinter import *
import random as rnd
import string
from tkinter import messagebox
import pyperclip

# ---------------------------- CONSTANTS ------------------------------- #
PRINTABLE = ''.join(char for char in string.printable if char not in string.whitespace)
EMAIL = "chrisrod@gmail.com"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pwd():
    password = ''.join(rnd.choice(PRINTABLE) for _ in range(10))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    password = password_entry.get()

    if len(website) == 0 and len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"Website: {website.capitalize()} \nEmail: {EMAIL}\nPassword: {password}\n")
        if is_ok:
            with open("password_file.txt", "a") as file:
                file.write(f"Website: {website.capitalize()} | Email/Username: {EMAIL} | Password: {password}\n")
            clear_text()
            website_entry.focus()


def clear_text():
    website_entry.delete(0, END)
    password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, EMAIL)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", width=10, command=gen_pwd)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=33, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
