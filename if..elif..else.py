# #                                Python If ... Else


#                     # Python Conditions and If statements
#                     # Python supports the usual logical conditions from mathematics:

#                     # Equals: a == b
#                     # Not Equals: a != b
#                     # Less than: a < b
#                     # Less than or equal to: a <= b
#                      # Greater than: a > b
#                     # Greater than or equal to: a >= b

# # if:-
# # These conditions can be used in several ways, most commonly in "if statements" and loops.

# # An "if statement" is written by using the if keyword.

# # Example
# # If statement:

# a = 33
# b = 200
# if b > a:
#   print("b is greater than a")



# # Elif:-

# # The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

# # Example

# a = 33
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")


# # Else:-

# # The else keyword catches anything which isn't caught by the preceding conditions.

# # Example
# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")
 



# # You can also have an else without the elif:

# # Example
# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")



# # Short Hand If:-
# # If you have only one statement to execute, you can put it on the same line as the if statement.

# # Example
# # One line if statement:

# if a > b:print("a is greater than b")



# # Short Hand If ... Else:-
# # If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:

# # Example
# # One line if else statement:

# a = 2
# b = 330
# print("A") if a > b else print("B")


# # And:-
# # The and keyword is a logical operator, and is used to combine conditional statements:

# # Example
# # Test if a is greater than b, AND if c is greater than a:

# a = 200
# b = 33
# c = 500
# if a > b and c > a:
#   print("Both conditions are True")




# # Or:-
# # The or keyword is a logical operator, and is used to combine conditional statements:

# # Example
# # Test if a is greater than b, OR if a is greater than c:

# a = 200
# b = 33
# c = 500
# if a > b or a > c:
#   print("At least one of the conditions is True")




# # Not
# # The not keyword is a logical operator, and is used to reverse the result of the conditional statement:

# # Example
# # Test if a is NOT greater than b:

# a = 33
# b = 200
# if not a > b:
#   print("a is NOT greater than b")




# # Nested If:--
# # You can have if statements inside if statements, this is called nested if statements.

# # Example
# x = 41

# if x > 10:
#   print("Above ten,")
#   if x > 20:
#     print("and also above 20!")
#   else:
#     print("but not above 20.")




# # The pass Statement:-
x=10
b=20
if x>b:
    pass

# if statements cannot be empty, but if you for some reason have an if statement
#  with no content,put in the pass statement to avoid getting an error.

# # Example:- 
# a = 33
# b = 200

# if b < a: 
#   print("b is smaller than a")
# else:
#   print("b is bigger than a")



  

# assert is used to check if a particular condition is satisfied or not.
  
# syntax:
  
# assert <condition> ,message

# if the condition is True, nothing happens.
# if the condition is False, AssertionError  will be raised.

# num=int(input("enter +ve number:"))
# assert num > 0,"please enter +ve number"

# print("Enter number is :",num)

 
# num=int(input("enter +ve number:"))
# try:
#     assert num > 0,"please enter +ve number"
#     print("Enter number is :",num)
# except:
#     print("Please enter a +ve number")




# str1="python"
# str2="python"

# assert str1==str2,"Strings are not equal"
# print("Strings are equal")





# assert "python" in "java is programming language","validation failed"
# print("pass ")