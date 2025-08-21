from tkinter import *
from tkinter import ttk
from googletrans import LANGUAGES,Translator
# pip install googletrans==4.0.0-rc1


# function 
def translatoor():
    translate=Translator()
    translate_text=translate.translate(text=input_textarea.get(1.0,END),
    src=Input_combobox.get(),dest=Output_combobox.get())
    Output_textarea.delete(1.0,END)
    Output_textarea.insert(END,translate_text.text)


root=Tk()
root.title("Language Translator")
root.geometry("1540x800+0+0")
root.configure(background="lightblue")

Label(root,text="Langugae Translator",font=("arial",22,"bold"),bd=8,bg="lightyellow",fg="black").place(x=640,y=10)

# =========================================Input Language==============================

Input_Frame= LabelFrame(root, text="Input Language", font=20, bd=2, width=700, bg="pink", fg="black",height=500, relief=GROOVE)
Input_Frame.place(x=50, y=100)

input_label=Label(Input_Frame,text="Input Language",font=("arial",15,"bold"),bd=2,bg="lightblue",fg="black")
input_label.place(x=10,y=10)

# language=list(LANGUAGES.values())
Input_combobox =ttk.Combobox(Input_Frame, values=list(LANGUAGES.values()),state="readonly")
Input_combobox.place(x=200, y=10)
Input_combobox.set("Select Language")

input_textarea=Text(Input_Frame)
input_textarea.place(x=20,y=50)

# ===========================================Output Language=======================================================

Output_Frame= LabelFrame(root, text="Output Language", font=20, bd=2, width=700, bg="pink", fg="black",height=500, relief=GROOVE)
Output_Frame.place(x=800, y=100)

Output_label=Label(Output_Frame,text="Output Language",font=("arial",15,"bold"),bd=2,bg="lightblue",fg="black")
Output_label.place(x=10,y=10)

# language=list(LANGUAGES.values())
Output_combobox =ttk.Combobox(Output_Frame, values=list(LANGUAGES.values()),state="readonly")
Output_combobox.place(x=200, y=10)
Output_combobox.set("Select Language")

Output_textarea=Text(Output_Frame)
Output_textarea.place(x=20,y=50)

translate_btn=Button(root,text="Translate",bd=3,fg="black",bg="light green",font=("arial",22,"bold"),command=translatoor)
translate_btn.place(x=720,y=640)

root.mainloop()