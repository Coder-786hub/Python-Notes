import tkinter as tk

def clear():
    input_field.delete(0, tk.END)

def delete_character():
    current_text = input_field.get()
    if current_text:
        new_text = current_text[:-1] 
        input_field.delete(0, tk.END)  
        input_field.insert(0, new_text)  

def button_click(number):
    current = input_field.get()
    input_field.delete(0, tk.END)
    input_field.insert(0, current + str(number))


def calculate():
    current = input_field.get()
    try:
        result = eval(current)
        input_field.delete(0, tk.END)
        input_field.insert(0, str(result))
    except Exception as e:
        input_field.delete(0, tk.END)
        input_field.insert(0, "Error")

root=tk.Tk()
root.geometry("336x503")
root.title("call_by_aftab")

label = tk.Label(root, text="CALCULATOR", font=("Times", 16, ""), background="black", foreground="white")
label.pack(fill="x", pady=(10, 0),ipady=4)

input_field = tk.Entry(root, background="grey", font=("Helvetica", 30))
input_field.pack(fill="x", pady=(1, 1))

clean=tk.Button(root, text="Clear",font=("",18,"bold"),background="green",command=clear)
clean.place(x=5,y=98)

lable1=tk.Label(root, text="aftab",font=("Times", 16, ""))
lable1.place(x=140,y=110)

delete_button = tk.Button(root, text="<Edit",font=("",18,"bold"),background="lightgrey", command=delete_character)
delete_button.place(x=245,y=98)


buttons=[
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '.', '0', '=', '+'
]

row_val = 150
col_val = 0

for button_text in buttons:
    tk.Button(root, text=button_text,font=("",30,"bold"), background="lightgrey",padx=20, pady=20, command=lambda b=button_text: button_click(b) if b != '=' else calculate()).place(x=col_val*85, y=row_val, width=80, height=80)
    col_val += 1
    if col_val > 3:
        col_val = 0  
        row_val += 90



root.mainloop()