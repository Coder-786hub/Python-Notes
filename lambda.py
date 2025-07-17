# Python Lambda

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.


# Syntax:-
# lambda arguments : expression
# The expression is executed and the result is returned:

# Example:-
# Add 10 to argument a, and return the result:

x = lambda a : a + 10
print(x(5))


# Lambda functions can take any number of arguments:

# Example
# Multiply argument a with argument b and return the result:

x = lambda a, b : a * b
print(x(5, 6))


# Example
# Summarize argument a, b, and c and return the result:

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.

# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def myfunc(n):
  return lambda a : a * n


# Use that function definition to make a function that always doubles the number you send in:

# Example

def myfunc(n):
  return lambda a : a * n

x = myfunc(2)

print(x(10))


'''
The code defines a function myfunc that takes an argument n. Inside the myfunc function, it returns a lambda function that takes an argument a and multiplies it by n. This returned lambda function forms a closure with the n argument of the myfunc function, which means it can access the value of n even after myfunc has finished executing.

After defining the myfunc function, the code calls it with an argument of 2 and assigns the returned lambda function to the variable x. This means that x now holds a reference to a lambda function that multiplies its input by 2.

Finally, the code calls x(10), which invokes the lambda function stored in x with an argument of 10. The lambda function multiplies this argument by 2 and returns the result, which is 20. The print statement then outputs 20 to the console.
'''



# Or, use the same function definition to make a function that always triples the number you send in:

# Example
def myfunc(n):
  return lambda a : a * n

x = myfunc(3)

print(x(11))




# Or, use the same function definition to make both functions, in the same program:

# Example
def myfunc(n):
  return lambda a : a * n

x = myfunc(2)
y = myfunc(3)

print(x(11))
print(y(11))


# Use lambda functions when an anonymous function is required for a short period of time.

# Example: Filter even numbers using a lambda function within a function
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def filter_even(numbers):
#     even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
#     return even_numbers

# result = filter_even(numbers)
# print(result)  # Output: [2, 4, 6, 8, 10]

#---------------------------------------------------------------------#


# Map Function -------------------------------------------------------------------
# map() applies a given function to each item in an iterable (like a list) and returns a map object (which can be converted to a list).

# Syntax:
# map(function, iterable)


# Example:
# Use map with a lambda to square each number in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# In this example:
# lambda x: x ** 2 is applied to each element in numbers.
# map() returns a map object, which we convert to a list to see the result.


# Filter Function
# filter() applies a function to each item in an iterable and returns only the items where the function returns True.
# Syntax:
# filter(function, iterable)

# Example:
# Use filter with a lambda to get even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]

# In this example:
# lambda x: x % 2 == 0 checks if each number in numbers is even.
# filter() returns only the items where the condition is True, which we convert to a list.








# the map() funxtion applies a function to each item in an iterable(like a list) and returns map object
# syntax
        # map(function, iterable)

# exmple
# number = [1,2,3,4,5,6,7]
# squarred_number = map(lambda x: x **2, number)
# print(list(squarred_number))


# the filter() function filter the elements of based on condition defined in function

# syntax
# filter(function, iterable)

# exmple

# number = [1,2,3,4,5,6,7,8,9,10]
# even_number = filter(lambda x: x %2 == 0, number)
# print(list(even_number))