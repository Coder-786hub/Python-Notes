# Python Inheritance

# Python Inheritance:- 
# # Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.

# Create a Parent Class:-
# Any class can be a parent class, so the syntax is the same as creating any other class:-

# Example:-
# Create a class named Person, with firstname and lastname properties, and a printname method:

# class Person:
#   def _init_(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

# x = Person("John", "Doe")
# x.printname()


# Create a Child Class:-
# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

# Example
# Create a class named Student, which will inherit the properties and methods from the Person class:

# class Person:
#   def _init_(self, fname, lname):
#     self.firstname = fname
# self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)
# class Student(Person):
#   pass

# x = Student("harry", "kumar")
# x.printname()



# Now the Student class has the same properties and methods as the Person class.

# Example
# Use the Student class to create an object, and then execute the printname method:

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   pass

# x = Student("harry", "kumar")
# x.printname()


# Add the _init_() Function
# So far we have created a child class that inherits the properties and methods from its parent.

# We want to add the _init_() function to the child class (instead of the pass keyword)

# Example
# Add the _init_() function to the Student class:

# class Student(Person):
#   def _init_(self, fname, lname):
    

#     #add properties etc.
# When you add the _init() function, the child class will no longer inherit the parent's __init_() function.

# To keep the inheritance of the parent's _init() function, add a call to the parent's __init_() function:

# Example
#     class Person:
#         def _init_(self, fname, lname):
#           self.firstname = fname
#           self.lastname = lname

#         def printname(self):
#           print(self.firstname, self.lastname)

#     class Student(Person):
#         def _init_(self, fname, lname):
#           Person._init_(self, fname, lname)

#     x = Student("harry", "kumar")
#     x.printname()



# Now we have successfully added the _init() function, and kept the inheritance of the parent class, aznd we are ready to add functionality in the __init_() function.


# Use the super() Function:-
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

# Example
# class Person:
#   def _init_(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def _init_(self, fname, lname):
#     super()._init_(fname, lname)

# x = Student("harry", "kumar")
# x.printname()


# By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

# Add Properties
# Example
# Add a property called graduationyear to the Student class:

# class Person:
#   def _init_(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def _init_(self, fname, lname):
#     super()._init_(fname, lname)
#     self.graduationyear = 2019

# x = Student("harry", "kumar")
# print(x.graduationyear)



# In the example below, the year 2019 should be a variable, and passed into the Student class when 
# creating student objects. To do so, add another parameter in the _init_() function:

# Example
# Add a year parameter, and pass the correct year when creating objects:

# class Person:
#   def _init_(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def _init_(self, fname, lname, year):
#     super()._init_(fname, lname)
#     self.graduationyear = year

# x = Student("Mike", "kumar", 2019)
# print(x.graduationyear) 



# Add Methods
# # # # Example
# # # # Add a method called welcome to the Student class:

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year

#   def welcome(self):
#     print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# x = Student("Mike", "Kumar", 2019)
# x.welcome()

  
# # # # If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.


# Types of Inheritence

# ========================================Single Inheritence=============================

# class father():
#     def fun(self):
#         print("father")
# class son(father):
#     def fun1(self):
#         print("Son")
# obj=son()
# obj.fun()
# obj.fun1()


# =======================================Multiple Inheritence=============================

# class father():
#     def fun(self):
#         print("father")
# class son1(father):
#     def fun1(self):
#         print("Son1")
# class son2(father):
#     def fun2(self):
#         print("Son2")    
# obj=son2()
# obj.fun()
# obj.fun2()


# ========================================= Multilevel Inheritence ============================

# class father():
#     def fun(self):
#         print("father")
# class son1(father):
#     def fun1(self):
#         print("Son")
# class son1_1(son1):
#     def fun3(self):
#         print("son1_1")
                        
# obj=son1_1()
# obj.fun()
# obj.fun1()
# obj.fun3()


# # # # ================================= Heirarchy Inheritence ===========================


# class father():
#     def fun(self):
#         print("father")
# class son1(father):
#     def fun1(self):
#         print("Son")
# class son2(father):
#     def fun2(self):
#         print("son2")
# class son1_1(son1):
#     def fun3(self):
#         print("son1_1")
# class son1_2(son1):
#     def fun4(self):
#         print("Son1_2")
# class son2_1(son2):
#     def fun5(self):
#         print("Son2_1")
# class son2_2(son2):
#     def fun6(self):
#         print("son2_2")                                
# obj=son2_1()
# obj.fun()
# obj.fun2()
# obj.fun5()


# # # # ========================================== Hybrid Inheritence =================================

# class grandparentes():
#     def fun(self):
#         print("Grandparentes")
# class dad(grandparentes):
#     def fun1(self):
#         print("Dad")
# class mom(grandparentes):
#     def fun2(self):
#         print("Mom")
# class superchild(mom,dad):
#     def fun3(self):
#         print("SuperChild")

# obj = superchild()
# obj.fun()
# obj.fun1()
# obj.fun2()
# obj.fun3()