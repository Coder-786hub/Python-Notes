# # x =  int(input("Enter the number"))
# # for i in range(1,x+1):
# #     print(" "*(x-i) + "@" * (2 *i - 1))
# # for i in range(x,0,-1):
# #     print(" " * (x-i) + "@" * (2 * i - 1))

# # x = int(input("Enter the number ="))
# # for i in range(x):
# #     print("#"*i)
# # for i in range(x,0,-1):
# #     print("@"*i)

# # x = int(input("Enter the number"))
# # for i in range(x,0,-1):
# #     print(" "*(x-i),"*"*i)
# # for i in range(x,0,-1):
# #     print()


# '''x = int(input("how many students are here "))
# result = []
# for  i in range(x):
#     name = input("My name is =")
#     age = input("My age is =")
#     gender = input("My gender is =")
#     location = input("My location is =")
#     details =[name,age,gender,location]
#     # print(details)
#     result.append(details)
# print(result)'''

x = int(input("enter the number"))
# for i in range(x):
#     print("","*"*i)
for i in range(x,0,-1):
    print(" "*(x-i),"*"*i)
# # for i in range(1,x+1):
# # print(" "*(x-i) + "*" * (2* i -1))
# # for i in range(x,0,-1):
# #     print(" "*(x-i) + "*" * (2 * i -1))
# # for i in range(1,x+1):
# #     print(" "*(x-i) + "*" * (2* i -1))
# # for i in range(x,0,-1):
# #     print(" "*(x-i) + "*" * (2 * i -1))

# '''x = int(input("Enter the number"))
# result = []
# for i in range(x):
#     name = input("My name is =:- ")
#     age = input("My age is =:- ")
#     gender = input("My gender is =:- ")
#     location = input("My location is =:- ")
#     Details = [name,age,gender,location]
#     result.append(Details)
# print(result)'''

# x = (input("Enter the number =:- "))
# for i in range(x):
#     print(""*x,"@"*i)
# # for i in range(x,0,-1):
# #     print(" "*(x-i),"@"*i)
# # for i in range(1,x+1):
# #     print(" "*(x-i) + "@" * (2 * i -1))
# # for i in range(x,0,-1):
# #     print(" "*(x-i) + "@" * (2*i-1))

# # for i in range(1,10):
# #     print(i)

# # num = 1
# # for i in range(1,6):
# #     for j in range(i):
# #         print(num,end=" ")
# #         num+=1
# #     print()





# # a = 1
# # for i in range(1,10):
# #     for j in range(i):
# #         print(a, end=" ")
# #         a+=1
# #     print()
# # for i in range(10,0,-1):
# #     for j in range(i-1):
# #         print(a,end=" ")
# #         a+=1
# #     print()

# # z = int(input("enter the number"))
# # for i in range(1,z-1):
# #     for j in range(i):
# #         print(z,end=" ")
# #         z+=1
# #     print()


# # class myclass:
# #     x=5
# # p1 = myclass
# # print(p1.x)

# # class person:
# #     def __init__(self, name, age):
# #         self.n = name
# #         self.a = age
# # p1= person("john",36)
# # print(p1.n)
# # print(p1.a)

# '''class Details:
#     def __init__(abc,name,age):
#         abc.n=name
#         abc.a=age
# p1=Details("John",17)
# print(p1.n)
# print(p1.a)'''


# # class person:
# #     def __init__(self,name,age):
# #         self.n=name
# #         self.a=age
# #     def __str__(self):
# #         return f"{self.n}({self.a})"
# # p1 = person("aftab",19)
# # print(p1)
        
# '''class person:
#     def __init__(self,name,age):
#         self.n=name
#         self.a=age
#     def __str__(self):
#         return f"{self.n}({self.a})"
#     def myfuncion(self):
#         print("Hello my name is =:- " +self.n)
#         print("And my age is :- " +str(self.a))
# p1=person("Aftab",17)
# p1.myfuncion()'''


# # class person:
# #     def __init__(self,
# #                  name,
# #                  age,
# #                  gender,
# #                  location,
# #                  curlocation):
# #         self.name= name
# #         self.age = age
# #         self.gender= gender
# #         self.location = location
# #         self.Curlocation= curlocation
# #     def __str__(self):
# #         return f"{self.name}({self.age})({self.age})({self.gender})({self.Curlocation})"
# #     def myfunction(self):
# #         print("My Name is =:- " +self.name)
# #         print("My Age is =:- " +str(self.age))
# #         print("My Gender is =:- " +self.gender)
# #         print("My Location is =:- " +self.location)
# #         print("My Current Location is =:- " +str(self.Curlocation))
# # p1 = person("Aftab",19,"Male","Uttar-Pradesh","4901,New maloya Colony Chandigarh")
# # p1.myfunction()

# '''def aftabagecal(y, m, d):
#     import datetime
#     today = datetime.datetime.now().date()
#     dob = datetime.date(y, m, d)
#     age = int((today - dob).days/365.25)
#     print(age)
# aftabagecal(2005, 7, 10)'''







# # class person:
# #     def __init__(self,name,age,gender,location): 
# #         pass

# '''class person:
#     def __init__(self,fname,lname):
#         self.fname= fname
#         self.lname= lname
#     def printname(abc):
#         print(abc.fname,abc.lname)
#         abc.graduation = 2021
# class student(person):
#     def __init__(xyz,firstname,lastname):
#         person.__init__(xyz,firstname,lastname)
# class kdk(person):
#     def __init__(aft,fstname,lstname,year):
#         super().__init__(fstname,lstname)
#         aft.graduationyear= year
# z = kdk("My first name is aman",",And my last name is khan",2019)
# y = person("Sahil", "khan")
# x = student("Aftab","alam")
# z.printname()
# y.printname()
# x.printname()
# print(x.graduation)
# print("My Graduation year is ",z.graduationyear)'''


# # class person:
# #     def __init__(self,name,age,gender,location):
# #         self.name = name
# #         self.age = age
# #         self.gender = gender
# #         self.location = location
# #     def printname(abc):
# #         print(abc.name,abc.age,abc.gender,abc.location)
# # class student(person):
# #     def __init__(xyz,name, age ,gender,location):
# #         person.__init__(xyz,name,age,gender,location)
# # class kdk(person):
# #     def __init__(aft,name, age ,gender,location):
# #         super().__init__(name, age ,gender,location)
# #         aft.graduationyear = 2019
# # x = person("My name is Aftab alam, And my Last name is Alam","My age is (18).","My Gender is Male.", "My Current Location is Chandigarh.")
# # y = student("My name is Sahil Khan, And my Last name is Alam","My age is (18).","My Gender is Male.", "My Current Location is Uttar_Pradesh.")
# # z = kdk("My name is Aftab alam, And my Last name is Alam","My age is (18).","My Gender is Male.", "My Current Location is Chandigarh.")
# # x.printname()
# # y.printname()
# # z.printname()
# # print("My Graduation year is",z.graduationyear)





# # x = int(input("How many students are here "))
# # result = []
# # for i in range(x):
# #     name = input("My name is:-")
# #     age = input("My age is:-")
# #     gender= input("my gender is:-")
# #     location= input("My location is:-")
# #     details = [name,age,gender,location]
# #     result.append(details)
# # print(result)

# '''class mycalss:
#     def __init__(self,name,age):
#         self.name= name
#         self.age= age 

#     # def __str__(self):
#     #     return f"{self.name}({self.age})"
#     def mufunction(self):
#         print("My name is " +self.name)
#         self.mygender = "male"
# x = mycalss("aftab",34)
# # print(x.name)
# x.mufunction()
# print("My gender is",x.mygender)
# print(x.age)
# pass'''

# # class person:
# #     def __init__(self,name,age,gender,location,father_name,mother_name,Address):
# #         self.name = name
# #         self.age = age
# #         self.gender = gender
# #         self.location = location
# #         self.father = father_name
# #         self.mother= mother_name
# #         self.address = Address

# #     def printname(self):
# #         print(self.name,self.age,self.gender,self.location,self.father,self.mother,self.address)
# #         self.year=2019
# # class aft(person):
# #     def __init__(abc, name, age, gender, location, father_name, mother_name,Address):
# #         person.__init__(abc,name, age, gender, location, father_name, mother_name,Address)
# #         abc.graduationyear=2019
# # class student(person):
# #     def __init__(self, name, age, gender, location, father_name, mother_name,Address):
# #         super().__init__(name, age, gender, location, father_name, mother_name,Address)
# #         self.year=2019
# # class Data(person):
# #     def __init__(xyz, name, age, gender, location, father_name, mother_name,Address):
# #         person.__init__(xyz,name, age, gender, location, father_name, mother_name,Address)
# #         xyz.month = "July"
# # x = person("My name is aftab alam","I am 18 year old.","My gender is male.","I belongs from Uttar-Pradesh.","My father name is Rukhsar Ahmad","and My mother name is Fatima Begam","My Address is #4901 maloya colony Chandigarh")
# # y = student("My name is aftab alam","I am 18 year old.","My gender is male.","I belongs from Uttar-Pradesh.","My father name is Rukhsar Ahmad","and My mother name is Fatima Begam","My Address is #4901 maloya colony Chandigarh")
# # z = aft("My name is aftab alam","I am 18 year old.","My gender is male.","I belongs from Uttar-Pradesh.","My father name is Rukhsar Ahmad","and My mother name is Fatima Begam ","maloya colony Chandigarh")
# # m = Data("My name is aftab alam","I am 18 year old.","My gender is male.","I belongs from Uttar-Pradesh.","My father name is Rukhsar Ahmad","and My mother name is Fatima Begam","CHnadgarh")
# # x.printname()
# # y.printname()
# # z.printname()
# # m.printname()
# # print(z.graduationyear)
# # print(x.year)
# # print(y.year)
# # print(m.month)

# '''
# txt = "Aftab Sahil Aman"
# x = txt.split()
# print(x)'''


# # a = "akhil#aftab#sahil#aman"
# # x = a.split("#", 3)
# # print(x)

# # z = "Hello my name is, aftab, and my last name is,alam"
# # b = z.split(", ")
# # print(z)


# # mytuple = ("apple", "banana", "cherry")
# # # myit = iter(mytuple)

# # # print(next(myit))
# # # print(next(myit))
# # # print(next(myit))
# # for x in mytuple:
# #     print(x)


# '''class Person:
#   def __init__(self,name,age):
#     self.a = name
#     self.b = age

#   def __str__(self):
#     return f"{self.a}({self.b})"

# p1 = Person("John", 36)
# print(p1)

# class person:
#     def __init__(self,name,age):
#         self.n=name
#         self.a=age
#     def __str__(self):
#         return f"{self.n}({self.a})"
# p1 = person("aftab",19)
# print(p1)'''


# # class MyNumbers:
# #   def __iter__(self):
# #     self.a = 1
# #     return self

# #   def __next__(self):
# #     # if self.a <= 20:
# #     x = self.a
# #     self.a += 1
# #     return x
# '''else:
#     raise StopIteration
#     for x in myiter:
#         print(x)'''

# # myclass = MyNumbers()
# # myiter = iter(myclass)


# # result =[]

# # for _ in range(5):
# #   result.append(next(myiter))

# # for i in reversed(result):
# #   print(" "*(len(result) - i - 1) + " ".join(result[:i+1]))

  
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))

# '''class MyNumbers:
#     def __init__(self):
#         self.a = "aftab"

#     def __iter__(self):
#         return self

#     def __next__(self):
#         x = self.a
#         self.a += " aftab "
#         return x

# myclass = MyNumbers()
# myiter = iter(myclass)

# result = []
# for _ in range(3):
#     result.append(next(myiter))

# for i in range(len(result)):
#     print(" " * (len(result) - i - 1) + " ".join(result[:i+1]))'''

# # class mynumber:
# #     def __iter__(self):
# #         self.a = 1
# #         return self
# #     def __next__(self):
# #         x  = self.a
# #         self.a +=1
# #         return x
# # myclass = mynumber()
# # myiter = iter(myclass)
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))

# '''class person:
#     def __init__(self,name,age,gender):
#         self.name =name
#         self.age = age
#         self.gender = gender

#     def __str__(self):
#         return f"{self.name}({self.age})({self.gender})"
    
# p1 =person("Aftab alam",18,"male")
# print(p1)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name}({self.age})"

# p1 = Person("John", 36)

# print(p1)

# class Person:
#     def __init__(self, name, age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def myfunction(self):
#         print("Hello my name is " +self.name,", And my age is " +str(self.age),", And my gender is ",self.gender,".")
# p1 = Person("John", 36,"Male")

# print(p1)
# p1.myfunction()

# class person:
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def printname(self):
#         print(self.name,self.age,self.gender)
#         # self.location = "Uttar_Pradesh"
# class student(person):
#     def __init__(self,fname,lname,age,location):
#         super().__init__(fname,lname,age)
#         self.location  = location
# p1 = person("Aftab alam",18,"male")
# p3 = student("Alam",18,"male","Chnadigarh")
# p1.printname()
# p3.printname()
# p1.printname()
# print(p3.location)
# # print(p1.location)'''


# '''class Mynumber:
#     def __iter__(self):
#         self.a = "*"
#         return self
#     def __next__(self):
#         x = self.a
#         self.a = "*"
#         return x
# myclass = Mynumber()
# myiter = iter(myclass)
# result  = []
# for _ in range(10):
#     result.append(next(myiter))
# for i in range(len(result)):
#     print(" " * (len(result) - i - 1) + " ".join(result[:i+1]))'''

# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))


# # class MyNumbers:
# #   def __iter__(self):
# #     self.a = "aftab"
# #     return self

# #   def __next__(self):
# #     # if self.a <= 20:
# #         x = self.a
# #         self.a += "aftab"
# #         return x
# # myclass = MyNumbers()
# # myiter = iter(myclass)


# # result =[]

# # for _ in range(5):
# #   result.append(next(myiter))

# # for x in reversed(result):
# # #   print(" "*(len(result) - i - 1) + " ".join(result[:i+1]))
# #   print(" " * (len(result) - i - 1) + " ".join(map(str, result[:i+1])))


# # class mynumber:
# #    def __iter__(self):
# #       self.a = 1
# #       return self
# #    def __next__(self):
      

# '''class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("This is for Drive!")

# class Boat:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("This is for Sail!")

# class Plane:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("This is for Fly!")

# car1 = Car("Ford", "Mustang")       #Create a Car class
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
# plane1 = Plane("Boeing", "747")     #Create a Plane class

# for x in (car1, boat1, plane1):
# #   print(x.brand)
#   print("The Brand name is "+x.brand+",","And the Model name is "+x.model,".")
#   x.move()'''

# # class person:
# #   def __init__(self,name,age):
# #     self.name= name
# #     self.age= age
# #   def move(self):
# #     print("Employee 1")
# # class Employee1(person):
# #   pass
# # class Employee2(person):
# #   def move(self):
# #     print("Employee2")
# # class Employee3(person):
# #   def move(self):
# #     print("Employee3")
# # a = Employee1("Aman",19)
# # b = Employee2("Sahil",20)
# # c = Employee3("Sahid",21)
# # for x in (a,b,c):
# #   print("Employe name is "+x.name,",")
# #   print("And age is "+str(x.age))
# #   x.move()


# '''class animals:
#   def speak(self):
#     print("Animal speaks")
# class dog(animals):
#   def speak(self):
#     print("Dog Barks")
# class cat(animals):
#   def speak(self):
#     print("Cat meows")
# animals  = [dog(),cat()]
# for animal in animals:
#   animal.speak()'''


# # class men:
# #   def angry(self):
# #     print("men become angry")
# # class women(men):
# #   def angry(self):
# #     print("Women are very clever")
# # men = [men(),women()]
# # for x in men:
# #   x.angry()

# '''class after:
#   def noon(self):
#     print("Good Morning")
# class morning(after):
#   def noon(self):
#     print("Good after noon")
# class evening(after):
#   def noon(self):
#     print("Good evening")
# Noon = [morning(),evening()]
# for i in Noon:
#   i.noon()'''

# # import threading

# # def print_numbers():
# #     for i in range(5):
# #         print(threading.current_thread().name,i)

# # thread1 = threading.Thread(target=print_numbers, name='Thread 1')
# # thread2 = threading.Thread(target=print_numbers, name='Thread 2')

# # thread1.start()
# # thread2.start()

# # thread1.join()
# # thread2.join()

# # print("Both threads have finished.")

# '''import tkinter as tk
# from tkinter import scrolledtext

# class ChatApp:
#     def __init__(self, master):
#         self.master = master
#         master.title("Chat App")

#         self.message_history = []

#         self.message_area = scrolledtext.ScrolledText(master, width=40, height=10)
#         self.message_area.pack(padx=10, pady=10)

#         self.input_field = tk.Entry(master, width=40)
#         self.input_field.pack(padx=10, pady=(0, 10))

#         self.send_button = tk.Button(master, text="Send", command=self.send_message)
#         self.send_button.pack(padx=10)

#     def send_message(self):
#         message = self.input_field.get()
#         self.input_field.delete(0, tk.END)
#         self.message_history.append("You: " + message)
#         self.update_message_area()

#     def update_message_area(self):
#         self.message_area.config(state=tk.NORMAL)
#         self.message_area.delete(1.0, tk.END)
#         for msg in self.message_history:
#             self.message_area.insert(tk.END, msg + "\n")
#         self.message_area.config(state=tk.DISABLED)
        
# def main():
#     root = tk.Tk()
#     app = ChatApp(root)
#     root.mainloop()

# if __name__ == "__main__":
#     main()'''



# '''import tkinter as tk

# class VirtualKeyboard:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Virtual Keyboard")
        
#         self.entry_widget = tk.Entry(self.root, width=50)
#         self.entry_widget.pack(pady=10)
        
#         self.create_keyboard()

#         self.shift_active = False
#         self.caps_lock_active = False
        
#         self.root.bind("<KeyPress>", self.physical_key_pressed)
#         self.root.bind("<KeyRelease>", self.key_released)
    
#     def create_keyboard(self):
#         keyboard_frame = tk.Frame(self.root)
#         keyboard_frame.pack()

#         keyboard_frame.configure(bg="lightgrey")  # Set the background color of the keyboard frame

#         self.keys = [
#             ("`", "~"), ("1", "!"), ("2", "@"), ("3", "#"), ("4", "$"), ("5", "%"), ("6", "^"), ("7", "&"), ("8", "*"), ("9", "("), ("0", ")"), ("-", "_"), ("=", "+"), ("Backspace", "Backspace"),
#             ("Tab", "Tab"), ("q", "Q"), ("w", "W"), ("e", "E"), ("r", "R"), ("t", "T"), ("y", "Y"), ("u", "U"), ("i", "I"), ("o", "O"), ("p", "P"), ("[", "{"), ("]", "}"), ("\\", "|"),
#             ("CapsLock", "CapsLock"), ("a", "A"), ("s", "S"), ("d", "D"), ("f", "F"), ("g", "G"), ("h", "H"), ("j", "J"), ("k", "K"), ("l", "L"), (";", ":"), ("'", "\""), ("Enter", "Enter"),
#             ("Shift", "Shift"), ("z", "Z"), ("x", "X"), ("c", "C"), ("v", "V"), ("b", "B"), ("n", "N"), ("m", "M"), (",", "<"), (".", ">"), ("/", "?"), ("↑", "↑"),
#             ("Ctrl", "Ctrl"), ("Fn", "Fn"), ("Alt", "Alt"), ("Space", "Space"), ("AltGr", "AltGr"), ("Menu", "Menu"), ("Ctrl", "Ctrl"),
#             ("←", "←"), ("↓", "↓"), ("→", "→"),
#             ("Insert", "Insert"), ("Home", "Home"), ("PgUp", "PgUp"),
#             ("NumLock", "NumLock"), ("/", "/"), ("*", "*"), ("-", "-"),
#             ("7", "Home"), ("8", "↑"), ("9", "PgUp"), ("+", "+"),
#             ("4", "←"), ("5", " "), ("6", "→"),
#             ("1", "End"), ("2", "↓"), ("3", "PgDn"),
#             ("0", "Insert"), (".", "Delete")
#         ]

#         for key in self.keys:
#             key_frame = tk.Frame(keyboard_frame)
#             key_frame.grid(row=self.keys.index(key)//14, column=self.keys.index(key)%14)

#             key_button = tk.Button(key_frame, text=key[0], width=3, padx=3, pady=3)
#             key_button.pack(expand=True, fill="both")

#             if key[0] in ("Enter", "Shift", "CapsLock", "Tab", "Backspace", "Clear", "↑", "Ctrl", "Fn", "Alt", "Space", "AltGr", "Menu", "←", "↓", "→", "Insert", "Home", "PgUp", "NumLock", "/", "*", "-", "+", "End", "PgDn", "Delete"):
#                 key_button.bind("<Button-1>", self.handle_special_key)
#             else:
#                 key_button.bind("<Button-1>", self.handle_key)
    
#     def handle_key(self, event):
#         key = event.widget["text"]
#         self.entry_widget.insert(tk.END, key)
    
#     def handle_special_key(self, event):
#         key = event.widget["text"]
#         if key == "Enter":
#             self.entry_widget.insert(tk.END, "\n")
#         elif key == "Backspace":
#             self.entry_widget.delete(len(self.entry_widget.get()) - 1)
#         elif key == "Clear":
#             self.entry_widget.delete(0, tk.END)
#         elif key == "Tab":
#             self.entry_widget.insert(tk.END, "\t")
#         elif key == "Shift":
#             self.shift_active = not self.shift_active
#         elif key == "CapsLock":
#             self.caps_lock_active = not self.caps_lock_active
#         elif key == "↑":
#             # Implement functionality for arrow keys if needed
#             pass
#         elif key == "Ctrl":
#             # Implement functionality for Ctrl key
#             pass
#         elif key == "Fn":
#             # Implement functionality for Fn key
#             pass
#         elif key == "Alt":
#             # Implement functionality for Alt key
#             pass
#         elif key == "Space":
#             self.entry_widget.insert(tk.END, " ")
#         elif key == "AltGr":
#             # Implement functionality for AltGr key
#             pass
#         elif key == "Menu":
#             # Implement functionality for Menu key
#             pass
#         elif key == "←":
#             # Implement functionality for left arrow key
#             pass
#         elif key == "↓":
#             # Implement functionality for down arrow key
#             pass
#         elif key == "→":
#             # Implement functionality for right arrow key
#             pass
#         elif key == "Insert":
#             # Implement functionality for Insert key
#             pass
#         elif key == "Home":
#             # Implement functionality for Home key
#             pass
#         elif key == "PgUp":
#             # Implement functionality for Page Up key
#             pass
#         elif key == "NumLock":
#             # Implement functionality for Num Lock key
#             pass
#         elif key == "/":
#             # Implement functionality for numeric keypad slash key
#             pass
#         elif key == "*":
#             # Implement functionality for numeric keypad asterisk key
#             pass
#         elif key == "-":
#             # Implement functionality for numeric keypad minus key
#             pass
#         elif key == "+":
#             # Implement functionality for numeric keypad plus key
#             pass
#         elif key == "End":
#             # Implement functionality for End key
#             pass
#         elif key == "PgDn":
#             # Implement functionality for Page Down key
#             pass
#         elif key == "Delete":
#             # Implement functionality for Delete key
#             pass
#         self.toggle_caps_lock()
#         self.toggle_shift()
    
#     def physical_key_pressed(self, event):
#         if event.keysym != "Shift_L" and event.keysym != "Shift_R":
#             self.entry_widget.insert(tk.END, event.char)
    
#     def toggle_caps_lock(self):
#         if self.caps_lock_active:
#             for key_frame in self.root.winfo_children():
#                 for key_button in key_frame.winfo_children():
#                     if key_button["text"] not in ("Enter", "Shift", "CapsLock", "Tab", "Backspace", "Clear", "↑", "Ctrl", "Fn", "Alt", "Space", "AltGr", "Menu", "←", "↓", "→", "Insert", "Home", "PgUp", "NumLock", "/", "*", "-", "+", "End", "PgDn", "Delete"):
#                         key_button.config(text=key_button["text"].upper())
#         else:
#             for key_frame in self.root.winfo_children():
#                 for key_button in key_frame.winfo_children():
#                     if key_button["text"] not in ("Enter", "Shift", "CapsLock", "Tab", "Backspace", "Clear", "↑", "Ctrl", "Fn", "Alt", "Space", "AltGr", "Menu", "←", "↓", "→", "Insert", "Home", "PgUp", "NumLock", "/", "*", "-", "+", "End", "PgDn", "Delete"):
#                         key_button.config(text=key_button["text"].lower())
    
#     def toggle_shift(self):
#         if self.shift_active:
#             for key_frame in self.root.winfo_children():
#                 for key_button in key_frame.winfo_children():
#                     if key_button["text"] not in ("Enter", "Shift", "CapsLock", "Tab", "Backspace", "Clear", "↑", "Ctrl", "Fn", "Alt", "Space", "AltGr", "Menu", "←", "↓", "→", "Insert", "Home", "PgUp", "NumLock", "/", "*", "-", "+", "End", "PgDn", "Delete"):
#                         key_button.config(text=key_button["text"].upper())
#         else:
#             for key_frame in self.root.winfo_children():
#                 for key_button in key_frame.winfo_children():
#                     if key_button["text"] not in ("Enter", "Shift", "CapsLock", "Tab", "Backspace", "Clear", "↑", "Ctrl", "Fn", "Alt", "Space", "AltGr", "Menu", "←", "↓", "→", "Insert", "Home", "PgUp", "NumLock", "/", "*", "-", "+", "End", "PgDn", "Delete"):
#                         key_button.config(text=key_button["text"].lower())
    
#     def key_released(self, event):
#         if event.keysym == "Shift_L" or event.keysym == "Shift_R":
#             self.shift_active = False
#         self.toggle_shift()

# if __name__ == "__main__":
#     root = tk.Tk()
#     keyboard = VirtualKeyboard(root)
#     root.mainloop()'''


# # x = int(input("enter the number"))
# # for i in range(x):
# #     print("","*"*i)
# # for i in range(x,0,-1):
# #     print(" "*(x-i),"*"*i)
# # for i in range(1,x+1):
# #     print(" "*(x-i) + "*" * (2* i -1))
# # for i in range(x,0,-1):
# #     print(" "*(x-i) + "*" * (2 * i -1))
# # for i in range(1,x+1):
# #     print(" "*(x-i) + "*" * (2* i -1))
# # for i in range(x,0,-1):
# #     print(" "*(x-i) + "*" * (2 * i -1))

# # x = int(input("Enter the number"))
# # for i in range(x,0,1):
# #     print(" "*(x-i),"*"*i)
# # for i in range(x,0,-1):
# #     print()


# # l1= [1,2,3,4,5]
# # l2=[8,9,10,11,12]

# # l3=l1 + l2

# # d={"One":l1[0],
# #    "Two":l1[1],
# #    "Three":l1[2],
# #    "Four":l1[3],
# #    "Five":l1[4],
# #    "Six":l1[5],
# #    "Seven":l1[6],
# #    "Eight":l2[0],
# #    "Nine":l2[1],
# #    "Ten":l2[2],
# #    "Eleven":l2[3],
# #    "Twelve":l2[4],
# #    "Thirteen":l2[5],
# #    "Fourteen":l2[6],
# #    }

# # d ={l1[0]:l2[0],
# #     l1[1]:l2[1],
# #     l1[2]:l2[2],
# #     l1[3]:l2[3],
# #     l1[4]:l2[4],
# #         }
# # print(d)
# # print(d["One"])


# # l1 =[1,2,3,4,5]
# # l2 = [6,7,8,9,10]
# # l3 =l1+l2
# # d ={"key":l1[0:5],
# #     "Key2":l2[0:5]}
# # l3.append(d)
# # print(d)

# # T1 =(1,2,3,)
# # T2 =(1,2,3,)
# # T3 =(1,2,3,)
# # T4 =(1,2,3,)
# # T5 =(1,2,3,)
# # iter(T1)

# # def __new__(
# #             cls,
# #             iter1: Iterable[T1],
# #             iter2: Iterable[T2],
# #             iter3: Iterable[T3],
# #             iter4: Iterable[T4],
# #             iter5: Iterable[T5],
# #             /,
# #             *,
# #             strict: bool = ...,
# #         ) -> zip[tuple[T1, T2, T3, T4, T5]]


# # a={1,2,3,4,5,6}
# # b={1,2,3,4,5,6,7,8,9,10}
# # commanvalue=a.intersection(b)
# # print(commanvalue)
# a={1,2,3,4,5,6}
# b=[1,2,3,4,5,6,7,8,9,10]

# print()
# # # c =a & b
# # print(c)

# from tkinter import *
# from tkcalendar import DateEntry
# from tkinter import ttk
# import mysql.connector 
# from tkinter import messagebox

# # Function to submit form data to the data base

# def submit():
#     try:
#         customer_name =et_customer.get()
#         dob=et_dob.get()
#         father_name=et_father.get()
#         adress=et_Address.get()
#         state=state_.get()
#         postoffice=et_post_office.get()
#         pincode=et_pin_code.get()
#         district=dist1.get()
#         mobileno=et_mobile_no.get()
#         meterno=et_meter_no.get()
#         accountno=et_account_no.get()
#         oldue=et_old_due.get()
#         oldreading=et_old_reading.get()
#         newreading=et_new_reading_date.get()
#         totaldays=et_total_days_reading.get()
#         oldreadingdate=et_old_reading.get()
#         newreadingdate=et_new_reading.get()
#         totalconsumption=et_total_consmption.get()
#         unitrate=et_unit_rate.get()
#         charge=et_charges.get()
#         totalamount=et_total_amount.get()
#         billduedate=et_bill_due_date
        
# # Check if any field is empty
        
#         if not all([customer_name,dob,father_name,adress,state,postoffice,pincode,district,mobileno,meterno,accountno,oldue,oldreading,newreading,totaldays,oldreadingdate,newreadingdate,totalconsumption,unitrate,charge,totalamount,billduedate]):
#             messagebox.showerror('Error', "All fields are mandatory")
#             return
        
#         # Insert data into the database
        
#         add_data(customer_name,dob,father_name,adress,state,postoffice,pincode,district,mobileno,meterno,accountno,oldue,oldreading,newreading,totaldays,oldreadingdate,newreadingdate,totalconsumption,unitrate,charge,totalamount,billduedate)
        
#         messagebox.showinfo('Success', "Data submitted successfully!")
#     except Exception as e:
#         messagebox.showerror('Error', str(e))

# # Function to create the database
# def create_database():
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="vinit1234"
#     )
#     cursor = conn.cursor()
#     cursor.execute("CREATE DATABASE IF NOT EXISTS haryana electricity bill")
#     conn.close()

# # Function to create the table

# def create_table():
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="vinit1234",
#         database="haryana electricity bill"
#     )

#     cursor = conn.cursor()
#     cursor.execute('''CREATE TABLE IF NOT EXISTS BHARAT_RAILWAY (
#         Customer_name varchar(50),dob int,father_name varchar(50),address varchar(50),state_ varchar(50),post_office varchar(50),
#          pin_code int,district varchar(50),mobile_no bigint,meter_no bigint,account_no bigint,old_due bigint ,old_reading_date bigint,
#          new_reading_date bigint,total_days_reading int,old_reading bigint,new_reading bigint,total_consumption bigint,unit_rate int,
#          charges bigint,total_amount bigint,bill_due_date bigint
        
#     )''')
#     conn.commit()
#     conn.close()
        
#     #  Function to add data to the table
    
# def add_data(customer_name,dob,father_name,adress,state,postoffice,pincode,district,mobileno,meterno,accountno,oldue,oldreading,newreading,totaldays,oldreadingdate,newreadingdate,totalconsumption,unitrate,charge,totalamount,billduedate):
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="vinit1234",
#         database="INDIA_IRCTC"
#     )
#     cursor = conn.cursor()
#     cursor.execute('''INSERT INTO customer_name,dob,father_name,adress,state,postoffice,pincode,district,mobileno,meterno,accountno,oldue,oldreading,newreading,totaldays,oldreadingdate,newreadingdate,totalconsumption,unitrate,charge,totalamount,billduedate]):
#     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', 
#     (customer_name,dob,father_name,adress,state,postoffice,pincode,district,mobileno,meterno,accountno,oldue,oldreading,newreading,totaldays,oldreadingdate,newreadingdate,totalconsumption,unitrate,charge,totalamount,billduedate))
#     conn.commit()
#     conn.close()
        
        
        
        
# root=Tk()


# root.title("Haryana bijli board")
# # root.iconbitmap("bulb.ico")
# root.geometry("2000x850")

# f=LabelFrame(root,height=60,width=1000,font=("bold"),bg="#1E3D81").pack(fill=X)
# f1=Label(f,text="ELECTRICITY BILL",font=("arial 20 bold"),width=25,bg="#6CBCE0").place(x=550,y=12)

# f2=LabelFrame(root,width=80,height=700,bg="#006CB1").place(x=10,y=70)

# text = "ELECTRICITY BILL"

# # Add individual labels for each character inside f2
# for a, char in enumerate(text):
#     label =Label(f2, text=char, bg="#006CB1", fg="white", font=("Helvetica", 20))
#     label.place(x=40, y=170 + a*30)


# f3=LabelFrame(root,width=80,height=700,bg="#006CB1").place(x=1445,y=70)

# for a, char in enumerate(text):
#     label =Label(f3, text=char, bg="#006CB1", fg="white", font=("Helvetica", 20))
#     label.place(x=1470, y=170 + a*30)

# f4=LabelFrame(root,height=250,width=1335,bg="#6CBCE0").place(x=100,y=72)

# e=Label(f4,text="Customer Detail",bg="#6CBCE0",font=("bold")).place(x=111,y=76)
# e1=Label(f4,text="Customer name",font=("arial 11 bold"),bg="#6CBCE0").place(x=222,y=140)
# et_customer=Entry(f4).place(x=355,y=145)

# e2=Label(f4,text="D.O.B",bg="#6CBCE0",font=("arial 11 bold")).place(x=680,y=140)
# et_dob=DateEntry(f4,width=17).place(x=750,y=142)

# e3=Label(f4,text="Father name",bg="#6CBCE0",font=("arial 11 bold")).place(x=1080,y=140)
# et_father=Entry(f4).place(x=1200,y=144)

# e4=Label(f4,text="Address",bg="#6CBCE0",font=("arial 11 bold")).place(x=222,y=200)
# et_Address=Entry(f4).place(x=355,y=205)

# e5=Label(f4,text="State",bg="#6CBCE0",font=("arial 11 bold")).place(x=680,y=200)

# state=StringVar()
# state_=ttk.Combobox(f4,width=17,height=5,text=state)
# state_["state"]="readonly"
# state_["values"]=("Haryana")
# state_.place(x=750,y=202)
# state_.current(0)

# e6=Label(f4,text="Post office",bg="#6CBCE0",font=("arial 11 bold")).place(x=1080,y=200)
# et_post_office=Entry(f4).place(x=1200,y=204)

# e7=Label(f4,text="Pin code",bg="#6CBCE0",font=("arial 11 bold")).place(x=222,y=260)
# et_pin_code=Entry(f4).place(x=355,y=260)

# e8=Label(f4,text="District",bg="#6CBCE0",font=("arial 11 bold")).place(x=680,y=260)
# # et_distt=Entry().place(x=750,y=260)

# et_distt=StringVar()
# dist1=ttk.Combobox(f4,width=17,text=et_distt)
# dist1["state"]="readonly"
# dist1["values"]=("Yamunanagar","Ambala","Gurugram","Hisar","Jind")
# dist1.place(x=750,y=260)
# dist1.current()


# e=Label(f4,text="Mobile No",bg="#6CBCE0",font=("arial 11 bold")).place(x=1080,y=260)
# et_mobile_no=Entry(f4).place(x=1200,y=260)




# f5=LabelFrame(root,height=250,width=1335,bg="#6CBCE0").place(x=100,y=333)

# e9=Label(f5,text="Bill detail",bg="#6CBCE0",font=("bold")).place(x=111,y=345)
# e10=Label(f5,text="Meter No",bg="#6CBCE0",font=("arial 11 bold")).place(x=200,y=400)
# et_meter_no=Entry(f5).place(x=355,y=400)

# e11=Label(f5,text="Account No",bg="#6CBCE0",font=("arial 11 bold")).place(x=590,y=400)
# et_account_no=Entry(f5).place(x=744,y=400)

# e12=Label(f5,text="Old Due",bg="#6CBCE0",font=("arial 11 bold")).place(x=1040,y=400)
# et_old_due=Entry(f5).place(x=1200,y=400)

# e13=Label(f5,text="Old Reading Date",bg="#6CBCE0",font=("arial 11 bold")).place(x=200,y=460)
# et_old_reading_date=Entry(f5).place(x=355,y=460)

# e14=Label(f5,text="New Reading Date",bg="#6CBCE0",font=("arial 11 bold")).place(x=590,y=460)
# et_new_reading_date=Entry(f5).place(x=744,y=460)

# e15=Label(f5,text="Total Days Reading",bg="#6CBCE0",font=("arial 11 bold")).place(x=1040,y=460)
# et_total_days_reading=Entry(f5).place(x=1200,y=460)

# e16=Label(f5,text="Old Reading ",bg="#6CBCE0",font=("arial 11 bold")).place(x=200,y=520)
# et_old_reading=Entry(f5).place(x=355,y=520)

# e17=Label(f5,text="New Reading",bg="#6CBCE0",font=("arial 11 bold")).place(x=590,y=520)
# et_new_reading=Entry(f5).place(x=744,y=520)

# e18=Label(f5,text="Total Consumption",bg="#6CBCE0",font=("arial 11 bold")).place(x=1040,y=520)
# et_total_consmption=Entry(f5).place(x=1200,y=520)

# f6=LabelFrame(root,height=100,width=1335,bg="#6CBCE0").place(x=100,y=594)
# f7=Label(f6,text="Amount",bg="#6CBCE0",font=("bold")).place(x=111,y=606)
# A=Label(f6,text="Unit Rate",bg="#6CBCE0",font=("arial 11 bold")).place(x=230,y=645)
# et_unit_rate=Entry(f6).place(x=355,y=645)

# A1=Label(f6,text="Charges",bg="#6CBCE0",font=("arial 11 bold")).place(x=625,y=645)
# et_charges=Entry(f6).place(x=744,y=645)

# A2=Label(f6,text="Total Amount",bg="#6CBCE0",font=("arial 11 bold")).place(x=1070,y=645)
# et_total_amount=Entry(f6).place(x=1200,y=645)

# f8=LabelFrame(root,width=450,height=55,font=("arial 11 bold"),bg="#006CB1").place(x=984,y=705)

# var=Label(f8,text="Bill due date",bg="#006CB1",font=("arial 12 ")).place(x=1068,y=720)
# et_bill_due_date=Entry(f8).place(x=1198,y=723)

# var3=Button(root,text="Submit",bg="#6CBCE0",font=("arial 13 bold")).place(x=730,y=730)

# f9=LabelFrame(root,width=450,height=55,font=("arial 11 bold"),bg="#006CB1").place(x=100,y=705)
# var4=Label(f9,text="HARYANA BIJLI VITRAN NIGAM",bg="#006CB1",font=("bold")).place(x=175,y=717)
    
    
# root.mainloop()


