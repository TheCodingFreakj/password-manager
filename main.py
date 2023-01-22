import os
import sys
from tkinter import *
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox
import random
import string
import json

dir_path = os.path.join(os.path.dirname(__file__), 'data.json')


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def get_random_string(length=10):
    # With combination of lower and upper case
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    # print random string
    entry_password.insert(0, result_str)
    # pyperclip.copy(entry_password)


def check_password():
    e_website = entry_website.get()

    with open(dir_path, 'r') as f:
        the_data = json.load(f)
        if e_website.lower() in map(str.lower, the_data.keys()):
            email_entered = the_data[ e_website ][ "password" ]
            messagebox.showinfo(title="Password Retrieved", message=f"This is your password {email_entered}")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def get_value():
    e_website = entry_website.get()
    e_name = entry_name.get()
    e_pass = entry_password.get()
    new_data = {e_website: {
        "email": e_name,
        "password": e_pass
    }}
    if len(e_pass) == 0 or len(e_name) == 0 or len(e_website) == 0:
        messagebox.showinfo(title="Oops", message="Enter all the fields")
    else:
        is_okay = messagebox.askokcancel(title=e_website,
                                         message=f"These are the details: \n Email {e_name} \n Password{e_pass}\n Is it Okay To Save?")
        if is_okay:
            try:
                with open(dir_path, 'r') as f:
                    the_data = json.load(f)
                    the_data.update(new_data)
                with open(dir_path, 'w') as f:
                    json.dump(the_data, f, indent=4)
            except:
                with open(dir_path, 'w') as f:
                    json.dump(new_data, f, indent=4)
            finally:
                entry_website.delete(0, END)
                entry_password.delete(0, END)
# ---------------------------- Path ------------------------------- #
def resourcePath(relativePath):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        basePath = sys._MEIPASS
    except Exception:
        basePath = os.path.abspath(".")

    return os.path.join(basePath, relativePath)
# ---------------------------- UI SETUP ------------------------------- #
win = Tk()
win.title("Password Manager")
win.config(padx=20, pady=34)
win.resizable(False, False)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("./Images/company-logo.png").resize((400, 300)))
# Constructing the first image, frame1
frame1 = Label(win, image=img, padx=15, pady=15)
frame1.grid(row=0, column=0, sticky="we")
# Constructing the second frame, frame2
frame2 = Label(win, text="Website", font='Aerial 15', padx=15, pady=15)

# Displaying the frame2 in row 0 and column 1
frame2.grid(row=1, column=0, sticky="w")
Button(
    win,
    text='Search Website',
    command=check_password,
    font='Arial 14'
).grid(row=1, column=2)
# Constructing the third frame, frame3
frame3 = Label(win, text="Username/Email", font='Aerial 15', padx=15, pady=15)

# Displaying the frame2 in row 0 and column 1
frame3.grid(row=2, column=0, sticky='w')

# Constructing the fourth frame, frame4
frame4 = Label(win, text="Password", font='Aerial 15', padx=15, pady=15)
0
# Displaying the frame2 in row 0 and column 1
frame4.grid(row=3, column=0, sticky='w')

entry_website = Entry(win, width=60)
entry_website.grid(row=1, column=1, ipadx=12, ipady=12)

entry_name = Entry(win, width=60)
entry_name.grid(row=2, column=1, ipadx=12, ipady=12)
entry_name.insert(END, "pallavidapriya75@gmail.com")

entry_password = Entry(win, width=60)
entry_password.grid(row=3, column=1, ipadx=12, ipady=12)

Button(
    win,
    text='Login',
    command=get_value,
    font='Arial 14'
).grid(row=4)

Button(
    win,
    text='Generate Password',
    command=get_random_string,
    font='Arial 14'
).grid(row=4, column=2)

win.mainloop()
