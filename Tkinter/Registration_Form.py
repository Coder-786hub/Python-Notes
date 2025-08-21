from tkinter import *

# pip install mysql-connector-python

# import mysql.connector

# def create_database():
#     connection = mysql.connector.connect(
#         host = "localhost",
#         user = "root",
#         password = "Aftab@786"
#     )

#     cursor = connection.cursor()
#     cursor.execute("CREATE DATABASE IF NOT EXISTS NEW_DATABASE")
#     connection.close()
#     cursor.close()


# def create_table():
#     connection = mysql.connector.connect(
#         host = "localhost",
#         user = "root",
#         password = "Aftab@786",
#         database = "NEW_DATABASE"
#     )

#     cursor = connection.cursor()
#     query = """
# CREATE TABLE IF NOT EXISTS USER (ID INT AUTO_INCREMENT PRIMARY KEY,
# NAME VARCHAR(30), FATHER_NAME VARCHAR(30), MOTHER_NAME VARCHAR(30), ADDRESS VARCHAR(30), CITY VARCHAR(30), PINCODE VARCHAR(30), COUNTRY VARCHAR(30))
# """
#     cursor.execute(query)
#     connection.commit()
#     connection.close()
#     cursor.close()


# def insert_data(name, father, mother, address, city, pincode, country):
#     connection = mysql.connector.connect(
#         host = "localhost",
#         user = "root",
#         password = "Aftab@786",
#         database = "NEW_DATABASE"
#     )

#     cursor = connection.cursor()
#     query = """INSERT INTO USER (NAME, FATHER_NAME, MOTHER_NAME, ADDRESS, CITY, PINCODE, COUNTRY) 
#     VALUES (%s, %s, %s, %s, %s, %s, %s)"""
#     data_tuple = (name, father, mother, address, city, pincode, country)
#     cursor.execute(query, data_tuple)
#     connection.commit()
#     connection.close()
#     cursor.close()





def submit():
    name = name_entry.get()
    fname = f_entry.get()
    Mname = M_entry.get()
    Address = Address_entry.get()
    city = city_entry.get()
    Pincode = Pincode_entry.get()
    Country = Countryentry.get()

    # insert_data(name, fname, Mname, Address, city, Pincode, Country)

    text_area.delete(1.0, END)
    text_area.insert(END," ======== 🥰WELCOME TO PYTHON CLASS🥰 ========\n")
    text_area.insert(END, f"\nFull Name : \t\t {name}\n")
    text_area.insert(END, f"\nFather's Name :\t\t {fname}\n")
    text_area.insert(END, f"\nMother's Name : {Mname}\n")
    text_area.insert(END, f"\nAddress : {Address}\n")
    text_area.insert(END, f"\nCity Name : {city}\n")
    text_area.insert(END, f"\nPin Code : {Pincode}\n")
    text_area.insert(END, f"\nCountry : {Country}\n")
    text_area.insert(END,"\t\t\t\t\t\t\t\t🥰=========== Thank You ===========🥰\t\t\t\t\t")
    
def clear():
    name_entry.delete(0, END)
    f_entry.delete(0, END)
    M_entry.delete(0, END)
    Address_entry.delete(0, END)
    city_entry.delete(0, END)
    Pincode_entry.delete(0, END)
    Countryentry.delete(0, END)
    text_area.delete(1.0, END)

def exit():
    app.destroy()

app = Tk()
app.title("Frame")
app.geometry("1200x700+100+40")
app.config(bg  = "#0ECF82")
app.iconbitmap("icon.ico")
app.resizable(False, False)

frame = LabelFrame(app, text = "Details",bg = "#9693F6", font = ("ROBOT", 18, "bold"), fg = "gold")
frame.place(x = 10, y = 20, width = 600, height = 400)

name = Label(frame, text = "Full Name : ", bg = "#9693F6", font = "ROBOT 16 bold")
name.place(x = 10, y = 20)

name_entry = Entry(frame, font = "arial 14 bold")
name_entry.place(x = 180, y = 20)

fname = Label(frame, text = "Father Name : ", bg = "#9693F6", font = "ROBOT 16 bold")
fname.place(x = 10, y = 60)

f_entry = Entry(frame, font = "arial 14 bold")
f_entry.place(x = 180, y = 60)

Mname = Label(frame, text = "Mother Name : ", bg = "#9693F6", font = "ROBOT 16 bold")
Mname.place(x = 10, y = 100)

M_entry = Entry(frame, font = "arial 14 bold")
M_entry.place(x = 180, y = 100)

Address_name = Label(frame, text = " Address : ", bg = "#9693F6", font = "ROBOT 16 bold")
Address_name.place(x = 10, y = 140)

Address_entry = Entry(frame, font = "arial 14 bold")
Address_entry.place(x = 180, y = 140)

city_name = Label(frame, text = " City : ", bg = "#9693F6", font = "ROBOT 16 bold")
city_name.place(x = 10, y = 180)

city_entry = Entry(frame, font = "arial 14 bold")
city_entry.place(x = 180, y = 180)

Pincode_name = Label(frame, text = " Pin Code : ", bg = "#9693F6", font = "ROBOT 16 bold")
Pincode_name.place(x = 10, y = 220)

Pincode_entry = Entry(frame, font = "arial 14 bold")
Pincode_entry.place(x = 180, y = 220)

Country_name = Label(frame, text = " Country : ", bg = "#9693F6", font = "ROBOT 16 bold")
Country_name.place(x = 10, y = 260)

Countryentry = Entry(frame, font = "arial 14 bold")
Countryentry.place(x = 180, y = 260)

# OUTPUT frame
frame1 = Frame(app,  padx = 30, bg = "#CECECE")
frame1.place(x = 660, y = 20, width = 500, height = 400, )

heading = Label(frame1, text = "A.L.L   D.E.T.A.I.L.S",font = ("arial", 25, "bold"), fg = "purple",justify = "center", bg = "#CECECE" )
heading.pack()

text_area = Text(frame1, font = "ROBOT 12 bold", fg = "green")
text_area.pack()

# BTN Frame 
btn_frame = LabelFrame(app, text = "All Button", bg = "#F492F4", font = ("ROBOT", 18, "bold"), fg = "#CF0E0E")
btn_frame.place(x = 10, y = 450, width = 1150, height = 200)

submit_btn = Button(btn_frame, text = "SUBMIT", font = ("arial", 25, "bold"), bg = "blue", bd = 4, cursor = "hand2", command = submit)
submit_btn.place(x = 100, y = 40)

clear_btn = Button(btn_frame, text = "CLEAR", font = ("arial", 25, "bold"), bg = "green", bd = 4, cursor = "hand2", command = clear)
clear_btn.place(x = 500, y = 40)

exit_btn = Button(btn_frame, text = "EXIT", font = ("arial", 25, "bold"), bg = "yellow", bd = 4, cursor = "hand2", command = exit)
exit_btn.place(x = 900, y = 40)

# create_database()
# create_table()

app.mainloop()