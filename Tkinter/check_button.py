from tkinter import *
from tkinter  import ttk
root=Tk()

root.title("TikTok")
root.iconbitmap("icon.ico")
root.maxsize(width=500,height=360)
root.minsize(width=480, height=270)

def fun():
    print(checkbtn1.get())
    print(checkbtn2.get())

checkbtn1= IntVar()
checkbtn2= IntVar()

select= Checkbutton(root,text="Male",variable=checkbtn1,onvalue=1,offvalue=0)
select.pack()

select= Checkbutton(root,text="Female",variable=checkbtn2,onvalue=1,offvalue=0)
select.pack()

btn=Button(root,text="Submit",command=fun)
btn.pack()

root.mainloop()