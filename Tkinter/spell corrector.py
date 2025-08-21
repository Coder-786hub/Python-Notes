from tkinter import *
from textblob import TextBlob
def correction():
    input_word= word_entry.get()
    text_blob=TextBlob(input_word)
    corrected_word=str(text_blob.correct())
    word2_entry.delete(0,END)
    word2_entry.insert(10,corrected_word)

def claer():
    word_entry.delete(0,END)
    word2_entry.delete(0,END)
    

root=Tk()
root.title("Spell Corrector")
root.geometry("500x300")

Label(root,text="Welcome to Spell Corrector Application",font=("arial",12,"bold"),bg="red",fg="black",bd=2).place(x=120,y=10)

word_label=Label(root,text="Input Word",font=("arial",12,"bold"),bg="green",fg="black",bd=2).place(x=10,y=50)
word_entry=Entry(root,bd=2,font=("arial",12,"bold"))
word_entry.place(x=150,y=50)

Button(root,text="Correction",font=("arial",12,"bold"),bg="red",fg="black",bd=2,command=correction).place(x=185,y=90)


word2_label=Label(root,text="Corrected Word",font=("arial",12,"bold"),bg="green",fg="black",bd=2).place(x=10,y=150)
word2_entry=Entry(root,bd=2,font=("arial",12,"bold"))
word2_entry.place(x=150,y=150)

Button(root,text="Clear",font=("arial",12,"bold"),bg="blue",fg="black",bd=2,command=claer).place(x=190 ,y=200)


root.mainloop()