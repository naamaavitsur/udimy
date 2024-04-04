from tkinter import *
from tkinter import messagebox
import string
from random import choice
import pyperclip
import json

WHITE = "#F1EFEF"
BODY = "#CCC8AA"
GREY= "#7D7C7C"
BLACK = "#191717"


def add_to_txt():
    the_website = website_entry.get()
    the_password = password_entry.get()
    the_mail = mail_entry.get()
    new_data = {
        the_website: {
            "password": the_password,
            "mail": the_mail
        }
    }
    if len(the_password) == 0 or len(the_website) == 0:
        messagebox.showerror(message="Please dont leave any fild empty!")
    else:
        try:
            with open("password.json", "r") as text_file:
                # reading old data
                json_data = json.load(text_file)

        except FileNotFoundError:
            with open("password.json", "w") as text_file:
                json.dump(new_data, text_file, indent=4)

        else:
            with open("password.json", "w") as text_file:
                # update new data
                json_data.update(new_data)
                # saving updating data
                json.dump(json_data, text_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            messagebox.showinfo(message="All of the detail have been update successfully!")



def generate_password():
    all_character = string.ascii_letters + string.digits + string.punctuation
    return_generate_pass = ""
    for _ in range(15):
        chose_char = choice(all_character)
        return_generate_pass += chose_char
    password_entry.insert(END, string=return_generate_pass)
    pyperclip.copy(return_generate_pass)


def search():
    searched_word = website_entry.get()
    try:
        with open("password.json", "r") as text_file:
            # reading old data
            json_data = json.load(text_file)

    except FileNotFoundError:
        messagebox.showerror(title="error", message="no details for this website")
    if searched_word in json_data:
            searched_web = json_data[searched_word]
            searched_password = searched_web["password"]
            searched_email = searched_web["mail"]
            messagebox.showinfo(title=searched_word, message=f"The password is: {searched_password}\nThe e-mail is: {searched_email}")

    else:
            messagebox.showerror(title="error", message="no data for this website")

    website_entry.delete(0, END)


window = Tk()
window.title("Password manager")
window.config(pady=50, padx=50, bg=WHITE)
password_photo = PhotoImage(file="pass.png")
canvas = Canvas(width=600, height=600, bg=WHITE, highlightthickness=0)
canvas.create_image(350, 100, image=password_photo)
canvas.grid(row=0, column=1)

# website
website_entry = Entry(width=30)
website_entry.place(x=150, y=300)
website_entry.focus()
website_label = Label(text="Website: ", bg=WHITE)
website_label.place(x=40, y=300)

# E-mail:
mail_entry = Entry(width=50)
mail_entry.insert(END, string="naamaavit@gmail.com")
mail_entry.place(x=150, y=350)
mail_label = Label(text="Email/Username: ", bg=WHITE)
mail_label.place(x=20, y=350)

# Password
password_entry = Entry(width=30)
password_entry.place(x=150, y=400)
password_label = Label(text="Password: ", bg=WHITE)
password_label.place(x=40, y=400)
password_button = Button(text="Generate password", command=generate_password)
password_button.place(x=400, y=395)

# Add
add_button = Button(text="Add", command=add_to_txt, width=47)
add_button.place(x=150, y=450)

# search

search_button = Button(text="Search", command=search, width=16)
search_button.place(x=400, y=295)





window.mainloop()