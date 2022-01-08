from tkinter import *
import tkinter as tk
from tkinter import messagebox

# mob num window
mob_num = Tk()
mob_num.title("Mobile Number File Store")
mob_num.geometry('500x500')

name_info = StringVar()
no_info = StringVar()


# check function
def check():
    clear()
    file = open("mobile_store.txt", 'r')
    for each in reversed(file.readlines()):
        view_field.insert(0.0, each)


# clear function
def clear():
    view_field.delete(0.0, tk.END)
    name.delete(0, END)
    number.delete(0, END)


# insert function
def insert():
    file = open("mobile_store.txt", 'r')
    u_name = name_info.get()
    u_num = no_info.get()
    content = file.read()
    if u_num not in content and len(u_num) == 10 and u_num.isdigit() and u_name.isalpha():
        file = open("mobile_store.txt", 'a')
        file.write("\n"+u_name + "-->" + u_num)
        messagebox.showinfo("Added", "Information added")
    else:
        messagebox.showerror("Wrong mob_no.", "Error")


# label info for enter info
info = Label(mob_num, text="ENTER YOUR INFORMATION HERE", bg="Violet")
info.pack()


# label e_name for name
e_name = Label(mob_num, text="Enter Your Name")
e_name.place(x=50, y=50)
name = Entry(mob_num, textvar=name_info)
name.place(x=250, y=50)

# label e_num for mobile num
e_num = Label(mob_num, text="Enter Your Mobile Number")
e_num.place(x=50, y=100)
number = Entry(mob_num, textvar=no_info)
number.place(x=250, y=100)

# insert button
ins_button = Button(mob_num, text='Insert', bg="lightblue", command=insert)
ins_button.place(x=200, y=140)

# label  view_info for view info
view_info = Label(mob_num, text="View Your Information", bg="lightblue")
view_info.place(x=150, y=190)


# view field
view_field = Text(mob_num, height=10, width=40)
view_field.place(x=50, y=220)


# check button
check_button = Button(mob_num, text='Check', bg="lightgreen", command=check)
check_button.place(x=330, y=400)

# clear button
clear_button = Button(mob_num, text='Clear', bg="lightpink", command=clear)
clear_button.place(x=380, y=400)

mob_num.mainloop()
