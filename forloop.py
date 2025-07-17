#                               For Loops

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

# Example:-
# Print each fruit in a fruit list:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# With the break statement we can stop the loop before it has looped through all the items:

# Example
# Exit the loop when x is "banana":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break




# With the continue statement we can stop the current iteration of the loop, and continue with the next:

# Example
# Do not print banana:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)




#   The range() Function:-
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

# Example
# Using the range() function:

for x in range(6):
  print(x)

# Example
# Using the start parameter:

for x in range(2, 6):
  print(x)



# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):

# Example
# Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)


# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

# Example
# Print all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):
  print(x)
else:
  print("Finally finished!")

# NOTE: The else block will NOT be executed if the loop is stopped by a break statement.



# Nested Loops:-
# A nested loop is a loop inside a loop.

# The "inner loop" will be executed one time for each iteration of the "outer loop":

# Example
# Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


# The pass Statement:-
# loop can not be empty:-




# for i in range(1, 6):
#     print('*' * i)




# for i in range(5, 0, -1):
#     print('*' * i)



# for i in range(6, 0, -1):
#     print(' ' * (6 - i) + '*' * i)


def add(a, b):
    result = a + b
    return result

sum = add(3,4)
print(sum)