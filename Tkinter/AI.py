from tkinter import *
import google.generativeai as genai

api = "AIzaSyD8FrLR6bmeG6NFEztRtvdfoPH-FGIkaHc"

genai.configure(api_key= api)

# Use correct model name
model = genai.GenerativeModel('gemini-1.5-flash')

# response = model.generate_content("Explain how AI works?")

def AI():
    query = user_entry.get().lower()
    response = model.generate_content(query)
    area.insert(END, f"{response.text}\n")
    print(response.text)



app = Tk()
app.geometry("1200x700+20+60")
app.resizable(0, 0)


heading = Label(app, text = "Aftab AI", font = "robot 35 bold", fg = "green", bg = "blue", justify = "center")
heading.pack(fill = "x")

frame = Frame(app, width = 1200, height = 580, bg = "#cbf5f1")
frame.place(x = 0, y = 60)




Label(frame, text = "What you want : ", bg = "#cbf5f1", fg = "green", font = "arial 18 bold").place(x = 10, y = 10)

user_entry = Entry(frame, font = "arial 18 bold", justify = "left", width = 65)
user_entry.place(x = 220, y = 10)

btn = Button(frame, text = "GET", font = "arial 20 bold", fg = "red", bg = "#cbf5f1", command = AI)
btn.place(x = 1100, y = 2)



scroll = Scrollbar(frame)
scroll.place(x = 1170, y = 60)


area = Text(frame, width = 145, height = 60, yscrollcommand = Y)
area.place(x = 0, y = 60)
scroll.config(command = area.yview)

app.mainloop()