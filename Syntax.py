# Python Syntax

# >>> print("Hello, World!")
# Hello, World!
# On this page

# Execute Python Syntax
# Python Indentation
# Python Variables
# Python Comments


# Python Indentation
# Indentation refers to the spaces at the beginning of a code line.

# Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

# Python uses indentation to indicate a block of code.

# ExampleGet your own Python Server
# if 5 > 2:
#   print("Five is greater than two!")
# Python will give you an error if you skip the indentation:

# Example
# Syntax Error:

# if 5 > 2:
# print("Five is greater than two!")
# The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.

# Example
# if 5 > 2:
#  print("Five is greater than two!") 
# if 5 > 2:
#         print("Five is greater than two!") 
# You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:

# Example
# Syntax Error:

# if 5 > 2:
#  print("Five is greater than two!")
#         print("Five is greater than two!")


# Python Variables
# In Python, variables are created when you assign a value to it:

# Example
# Variables in Python:

# x = 5
# y = "Hello, World!"s
# Python has no command for declaring a variable.

# You will learn more about variables in the Python Variables chapter.

# Comments
# Python has commenting capability for the purpose of in-code documentation.

# Comments start with a #, and Python will render the rest of the line as a comment:

# Example
# Comments in Python:

# #This is a comment.
# print("Hello, World!")



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"
  
p1 = Person("John", 36)
print(p1)

