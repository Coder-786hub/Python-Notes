from tkinter import *
from tkinter import messagebox
from tkinter import ttk

win=Tk()
win.geometry("1080x1100+30+100")
win.config(bg="gold")


def submit():
    a = name.get()
    b = Gender.get()
    c = city.get()
    d = state.get()
    e = contact.get()
    f = country.get()
    g = message.get(1.0,END)


    if a=="" or b=="Choose Your Gender" or c=="" or d =="Choose Your State" or e =="" or f=="Choose Your Country" or g.strip() == "":
        messagebox.showerror("Error","All filds are required")
    else:

        textarea.delete(1.0,END) 
        textarea.insert(END,f" Name :{a}\n")
        textarea.insert(END,f"\nGender:{b}\n")
        textarea.insert(END,f'\nCity :{c}\n')
        textarea.insert(END,f'\nState :{d}\n')
        textarea.insert(END,f'\nContact: {e}\n')
        textarea.insert(END,f" \nCountry:{f}\n")
        textarea.insert(END,f"\nMessage:{g}\n")  
        textarea.insert(END,"\n\n\t\t\tThank You\n")
        messagebox.showinfo('Success','Submit Succesfully')

def clear():
    name.delete(0,END)
    Gender.set("Choose Your Gender")
    city.delete(0,END)
    state.set("Choose Your State")
    contact.delete(0,END)
    country.set("Choose Your Country")
    message.delete(1.0,END)
    textarea.delete(1.0,END)
    messagebox.showinfo("Success","Clear Successfully")



def exit():
    win.destroy()
    

label1 = Label(win,text="FORM",font="ROBOT 25 bold",bg="red",fg="black")
label1.pack(fill="x")
Frame1=LabelFrame(win,height=400,width=400,bg="red")
Frame1.place(x=30,y=50)
Frame2=LabelFrame(win,text="Details",height=400,width=400,bg="red")
Frame2.place(x=600,y=50)
Frame3=LabelFrame(win,text="Buttons",height=230,width=990,bg="red")
Frame3.place(x=50,y=490)

textarea=Text(Frame2,height=24,width=50)
textarea.pack()

name=Label(Frame1,text="Name:",font="ROBOI 15 bold",bg="red",fg="white")
name.place(x=3,y=10)

Gender=Label(Frame1,text="Gender:",font="ROBOT 15 bold",bg="red",fg="white")
Gender.place(x=3,y=50)
 

city=Label(Frame1,text="City:",font="ROBOT 15 bold ", bg="red", fg="white")
city.place(x=3,y=90)


state=Label(Frame1,text="State:",font="ROBOT 15 bold",bg="red",fg="white")
state.place(x=3,y=130)

contact=Label(Frame1,text="Contact:",font="ROBOT 15 bold",bg="red",fg="white")
contact.place(x=3,y=170)

country=Label(Frame1,text="Country:",font="ROBOT 15 bold",bg="red",fg="white")
country.place(x=3,y=210)

message=Label(Frame1,text="Message:",font='ROBOT 15 bold',bg='red',fg="white")
message.place(x=3,y=250)


name=Entry(Frame1)
name.place(x=130,y=12)

Gender=ttk.Spinbox(Frame1,values=("Male","Female","Others"),state="readonly")
Gender.set("Choose Your Gender")
Gender.place(x=130,y=50)

city=Entry(Frame1)
city.place(x=130,y=90)

state=ttk.Combobox(Frame1,values=("Himachal Pradesh","Punjab","Haryana","Others"),state="readonly")
state.set("Choose Your State")
state.place(x=130,y=130)

contact=Entry(Frame1)
contact.place(x=130,y=170)

country=ttk.Combobox(Frame1,values=('India',"England","USA","Others"),state="readonly")
country.set("Choose Your Country")
country.place(x=130,y=210)

message=Text(Frame1,height=6,width=45)
message.place(x=18,y=280)
 
#Buttons
Submit=Button(Frame3,text="SUBMIT",font="ROBOT 15 bold",width=10,cursor="hand1",command=submit)
Submit.place(x=100,y=50)

Clear=Button(Frame3,text="CLEAR",font="ROBOT 15 bold",width=10,cursor="hand1",command=clear)
Clear.place(x=380,y=50)

Exit=Button(Frame3,text="EXIT",font="ROBOT 15 bold",width=10,cursor="hand1",command=exit)
Exit.place(x=660,y=50)
win.mainloop()
