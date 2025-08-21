from tkinter import *
from tkinter import messagebox
import mysql.connector
import random

import Database 




# Database setup
# def create_database():
#     connection = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="Aftab@786"
#     )
#     cursor = connection.cursor()
#     cursor.execute("CREATE DATABASE IF NOT EXISTS RestaurantDB")
#     connection.close()
#     cursor.close()

# def create_table():
#     connection = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="Aftab@786",
#         database="RestaurantDB"
#     )
#     cursor = connection.cursor()
#     query = """
#     CREATE TABLE IF NOT EXISTS Bills (
#         Bill_No INT AUTO_INCREMENT PRIMARY KEY,
#         Customer_Name VARCHAR(50),
#         Customer_Contact VARCHAR(15),
#         Item VARCHAR(50),
#         Quantity INT,
#         Cost DECIMAL(10, 2),
#         Total DECIMAL(10, 2)
#     )"""
#     cursor.execute(query)
#     connection.commit()
#     connection.close()
#     cursor.close()

# def insert_data(bill_no, name, contact, item, quantity, cost, total):
#     connection = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="Aftab@786",
#         database="RestaurantDB"
#     )
#     cursor = connection.cursor()
#     query = """INSERT INTO Bills (Bill_No, Customer_Name, Customer_Contact, Item, Quantity, Cost, Total) \
#     VALUES (%s, %s, %s, %s, %s, %s, %s)"""
#     data = (bill_no, name, contact, item, quantity, cost, total)
#     cursor.execute(query, data)
#     connection.commit()
#     connection.close()
#     cursor.close()

# GUI Functions
def submit():
    bill_no = bill_no_var.get()
    name = name_entry.get()
    contact = contact_entry.get()
    item = item_entry.get()
    quantity = int(quantity_entry.get())
    cost = float(cost_entry.get())
    total = quantity * cost

    # insert_data(bill_no, name, contact, item, quantity, cost, total)

    result_text.delete(1.0, END)
    result_text.insert(END, f"Bill No: {bill_no}\n")
    result_text.insert(END, f"Customer Name: {name}\n")
    result_text.insert(END, f"Contact: {contact}\n")
    result_text.insert(END, f"Item: {item}\n")
    result_text.insert(END, f"Quantity: {quantity}\n")
    result_text.insert(END, f"Cost per Item: {cost}\n")
    result_text.insert(END, f"Total: {total}\n")

    messagebox.showinfo("Success", "Data inserted successfully!")

def clear():
    name_entry.delete(0, END)
    contact_entry.delete(0, END)
    item_entry.delete(0, END)
    quantity_entry.delete(0, END)
    cost_entry.delete(0, END)
    result_text.delete(1.0, END)

def exit_app():
    app.destroy()

# Application Setup
app = Tk()
app.title("Restaurant Management System")
app.geometry("900x600")
app.config(bg="#F0F0F0")

# Variables
bill_no_var = IntVar(value=random.randint(1000, 9999))

# Frames
input_frame = LabelFrame(app, text="Input Details", font=("Arial", 14), bg="#E8E8E8")
input_frame.place(x=20, y=20, width=400, height=350)

output_frame = Frame(app, bg="#E8E8E8")
output_frame.place(x=450, y=20, width=400, height=350)

button_frame = Frame(app, bg="#F0F0F0")
button_frame.place(x=20, y=400, width=830, height=150)

# Input Fields
Label(input_frame, text="Bill No:", font=("Arial", 12), bg="#E8E8E8").grid(row=0, column=0, padx=10, pady=10, sticky=W)
bill_no_entry = Entry(input_frame, textvariable=bill_no_var, font=("Arial", 12), state="readonly")
bill_no_entry.grid(row=0, column=1, padx=10, pady=10)

Label(input_frame, text="Customer Name:", font=("Arial", 12), bg="#E8E8E8").grid(row=1, column=0, padx=10, pady=10, sticky=W)
name_entry = Entry(input_frame, font=("Arial", 12))
name_entry.grid(row=1, column=1, padx=10, pady=10)

Label(input_frame, text="Contact:", font=("Arial", 12), bg="#E8E8E8").grid(row=2, column=0, padx=10, pady=10, sticky=W)
contact_entry = Entry(input_frame, font=("Arial", 12))
contact_entry.grid(row=2, column=1, padx=10, pady=10)

Label(input_frame, text="Item:", font=("Arial", 12), bg="#E8E8E8").grid(row=3, column=0, padx=10, pady=10, sticky=W)
item_entry = Entry(input_frame, font=("Arial", 12))
item_entry.grid(row=3, column=1, padx=10, pady=10)

Label(input_frame, text="Quantity:", font=("Arial", 12), bg="#E8E8E8").grid(row=4, column=0, padx=10, pady=10, sticky=W)
quantity_entry = Entry(input_frame, font=("Arial", 12))
quantity_entry.grid(row=4, column=1, padx=10, pady=10)

Label(input_frame, text="Cost per Item:", font=("Arial", 12), bg="#E8E8E8").grid(row=5, column=0, padx=10, pady=10, sticky=W)
cost_entry = Entry(input_frame, font=("Arial", 12))
cost_entry.grid(row=5, column=1, padx=10, pady=10)

# Output Field
result_text = Text(output_frame, font=("Arial", 12), width=40, height=20)
result_text.pack(pady=10)

# Buttons
Button(button_frame, text="Submit", font=("Arial", 14), command=submit, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=20, pady=20)
Button(button_frame, text="Clear", font=("Arial", 14), command=clear, bg="#FF9800", fg="white").grid(row=0, column=1, padx=20, pady=20)
Button(button_frame, text="Exit", font=("Arial", 14), command=exit_app, bg="#F44336", fg="white").grid(row=0, column=2, padx=20, pady=20)

# Database Initialization
# create_database()
# create_table()

# Start Application
app.mainloop()
