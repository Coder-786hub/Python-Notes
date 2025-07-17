# # The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.

# # Function Polymorphism
# # An example of a Python function that can be used on different objects is the len() function.

# # String
# # For strings len() returns the number of characters:

# # Example
# # x = "Hello World!"

# # print(len(x))

# #  ============================ Polymorphism ===========================================


class lady():
    def fun(self):
        print("lady")
# class office(lady):
    def office(self):
        print("Employee")
# class home(lady):
    def home(self):
        print("Wife")
class mom(lady):
    def mom(self):
        print("Mother")

        

# obj = mom()
# obj.fun()
# obj.office()
# obj.home()                        
# obj.mom()



a = "hello world"

print(len(a))