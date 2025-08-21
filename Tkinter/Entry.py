# tkinter entry
# The tkinter entry box lets you input text in your desktop software. Usually an entry box (input field) comes with a label, that’s because without labels its not clear what the user should type there.

# You can add more than one input field. The input field can show latin character but also other types of input (like passwords)


# tkinter entry
# The tkinter entry box lets you type in the GUI. The code below adds an entry box to the GUI. The first parameter is what to add, the text parameter defines what to place next to it.


 
from tkinter import *

# top = Tk()

# top.geometry("200x200")
# L1 = Label(top, text="Label")
# L1.pack()

# E1 = Entry(top, bd=5, font = "arial 15 bold")
# E1.pack()
# top.mainloop()

# tkinter entry

# tkinter entry password
# The tkinter entry can be plain text but it also supports password input. By changing the parameter show, you can make it look like anything you want.
 
# import tkinter as tk
 
# window = tk.Tk()
# window.title('My Window')
# window.geometry('500x300') 
 
# e1 = tk.Entry(window, show=None, font=('Arial', 14))  
# e2 = tk.Entry(window, show='*', font=('Arial', 14))   
# e1.pack()
# e2.pack()
 
# window.mainloop()


from tkinter import * 

def button():
    e = E1.get()
    print(e)
    btn.config(text = "Click Me")

top = Tk()

top.geometry("500x400")
top.title("Form")
top.config(bg = "#B0E9EB")
L1 = Label(top, text="User Name", fg = "green", font = ("ROBOT", 20, "bold"),bg = "#B0E9EB")
L1.pack(pady = 10)

E1 = Entry(top, bd=5, font = "arial 15 bold")
E1.pack(pady = 20)

L1 = Label(top, text="Password", fg = "blue", font = ("ROBOT", 20, "bold"), bg = "#B0E9EB")
L1.pack(pady = 10)

E1 = Entry(top, border=5, font = "arial 15 bold", show = "*")
E1.pack(pady = 20)

btn = Button(top, text = "Button", font=("arial", 35, "bold"), border = 4, background = "red", foreground = "white", command = button, cursor = "hand2")
btn.pack(pady = 10)

top.mainloop()