# a = 10
# b = 10

# # print(a//b)
# print(a**b)

# var  = "Hello world"

# if "v" and "e" in var:
#     print(True)
# else:
#     print("False")    


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# x =(factorial(5))
# print(x)

# a = 10
# b = 10
# if not(a and b == 10):
#     print(True)
# else:
#     print(False)    

# def my_function(fname, lastname):
#   print(" My name is "+fname + lastname )

# my_function("Harry", "Jack")
# my_function("Jerry", "He")
# my_function("Panda","moye")    



# class MyClass:
#     x = 6

# p1 = MyClass()
# print(p1.x)    


# a=[1,2,3,4,5,6,7,8,9,10]
# b = a[:5]
# b.reverse()
# print(b)

# output = [5,4,3,2,1]
# output = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]

# c=a[-5:]
# print(c)
# b.extend(c)
# print(b)


# var = int(input("enter the number : "))
# if var % 4 == 0:
#     print("Leap Year")
# else:
#     print("Not Leap Year") 


# a = 10
# b = 20
# if not(a or b == 10):
#     print(True)
# else:
#     print(False)    


# var = str(input("enter word : "))
# vowels = "a","e","i","o","u"
# if var in vowels:
#     print("vowels")
# elif var.isdigit():
#     print("Number")    
# else:
#     print("Consonent")   


# x = 6
# y = 12
# if x % 2 == 0 and y % 3 == 0:
#     print("Both number are divisible")
# else:
#     print("Not Divisible")


# num = int(input("Enter number : "))
# if num in range(1,10):
#     print("Possitive")
# elif num in range(-10,1):
#     print("Negative Number")    
# elif num == 0:
#     print("Number is Zero")    


# num = int(input("Enter age : "))
# if num in range(0,13):
#     print("Child")

# elif num in range(13,20):
#     print("Teeneger") 

# else:
#     print("Adult")


# num1 = float(input("Enter number : "))
# num2 = float(input("Enter number : "))
# if num1 > num2:
#     print(f"The Largest number is {num1}")
# elif num2 > num1:
#     print(f"The Largest number is {num2}")    
# else:
#     print("both number are equal")    


# num1 = float(input("Enter number : "))
# num2 = float(input("Enter number : "))
# num3 = float(input("Enter number : "))
# if num1 > num2 and num1 > num3:
#     print(f"The Largest number is {num1}")
# elif num2 > num1 and num2 > num3:
#     print(f"The Largest number is {num2}")
# elif num3 > num1 and num3 > num2:
#     print(f"The Largest number is {num3}")
# else:
#     print("All number are equal")

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)    
# x =(factorial(5))
# print(x)




# var = [1,2,3,4,5,6,7,8,9,10]
# b = var[:5]
# print(b)
# print()
# b.reverse()
# print(b)

# output = [5,4,3,2,1]
# output2 = [5,4,3,2,1,6,7,8,9,10]

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# x = 5
# print(factorial(x))


# var = str(input("Enter latter : "))
# if var.isupper():
#     print("Upper")
# else:
#     print("Lower")    


# side1 = int(input("Enter side 1 : "))
# side2 = int(input("Enter side 2 : "))
# side3 = int(input("Enter side 3 : "))

# # Check if the input values form a valid triangle
# if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
#     # Check for equilateral triangle
#     if side1 == side2 == side3:
#         print("The triangle is Equilateral.")
#     # Check for isosceles triangle
#     elif side1 == side2 or side1 == side3 or side2 == side3:
#         print("The triangle is Isosceles.")
#     # If not equilateral or isosceles, it must be scalene
#     else:
#         print("The triangle is Scalene.")
# else:
#     print("The entered sides do not form a valid triangle.")



# year = int(input("Enter year : "))

# if year % 4 == 0:
#     print(f"{year} is a leap year")
# else:
#     print("Not a leap year")    


# year = int(input("Enter year : "))

# if year % 400 == 0:
#     print(f"{year} is a leap year")
# else:
#     print("Not a leap year")



# char = str(input("Enter letter : "))
# vowles = "a","e","i","o","u","A","E","I","O","U"

# print(char)
# if char in vowles:
#     print("Vowles")
# else:
#     print("Consonent")    


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break
# #   print(x)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     # print(x)
#   if x == "banana":
#     continue
#   print(x)

# for x in range(0, 10):
#     for j in 
#     print(x)
# else:
#     print("Finally Finished")



# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]


# for x in adj:
#     for y in fruits:
#         print(x,y)


# for i in range(1, 6):
#     print('@' * i)


# for x in range(0, 10):
#     print("*" * x)
    


# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         break 
#     i += 1


# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")
# a=1001200035400062100251002251100000121

# prime_number = []
# for num in range(2, 101):
#     if all(num % i != 0 for i in range(2, num)):
#         prime_number.append(num)
# print(prime_number)        

# result = [i for i in range(1,101) if (i%2 == 0)]  
# print(result)

# result = [num for num in range(2,101) if all(num % i != 0 for i in range(2,num))]
# print(result)

# python -m jupyter notebook

# for i in range(1, 6):
#     for j in range(1, 6):
#         if i == j:
#             print(" ", end="\t")  # Print a space when i == j
#         else:
#             print(i * j, end="\t")  # Print the product of i and j
#     print()  # Move to the next line0

# from kivy.app import App
# from kivy.uix.label import Label

# class helloworld(App):
#     def build(self):
#         return Label(text = "hello world")
    

# if __name__ == "__main__":
#     helloworld().run()


# for i in range(1, 6):
#     for j in range(1, 6):
#         if i == j:
#             print(" ", end="\t")  # Print a space when i == j
#         else:
#             print(i * j, end="\t")  # Print the product of i and j
#     print()  # Move to the next line0


# import lorem

# # Generate multiple paragraphs until reaching 500 words
# words = []
# while len(words) < 500:
#     words.extend(lorem.paragraph().split())

# # Join and print exactly 500 words
# lorem_text = " ".join(words[:500])
# print(lorem_text)

# var="The quick brown fox jumps exactly right over the little lazy dog"
# var1=var.("right")
# print(var1)
# print(var.split(" "))
#print(var2)


#var="The quick brown fox jumps exactly right over the little lazy dog"
# var1=var.title()
# print(var1)
#var1="The Real World"
#var2=var1.split()
#print(var2)

# def fabonicce(n):
#     series = [0,1]
#     while len(series) < n:
#         series.append(series[-1] + series[-2])
#     return series

# n = 10
# print(fabonicce(n))

# import qrcode

# data = "https://codeinfotech.co.in/"
# qrco = qrcode.make(data)
# qrco.save("link.jpg")
# print("successfully")

var = {
    "name" : ["Nupur", "Aftab", "Sahil"],
    "id" : [i for i in range(1,101)]

}

# print(var)


# for i, v in var.items():
#     new_list = []
#     if i == "id":
#         for num in v:   
#             if num % 3 == 0 and num % 5 == 0:
#                 new_list.append(num)
#         var[i] = new_list
# print(var)

# day=int(input("enter a number "))
# match day:
#     case 1:
#         print("monday")
#     case 2:
#         print("tuesday")
#     case 3:
#         print("wednesday")
#     case 4:
#         print('thursday')
#     case 5:
#         print('friday')
#     case 6:
#         print('sat')
#     case 7:
#         print('sunday')
#     case __:
#         print('uehcru')




# var = [i for i in range(2, 101) if all(i % n != 0 for n in range(2, i))]
# print(var)

# 2. i % n != 0 for n in range(2, i): This is a generator expression that checks if i is divisible by any number n between 2 and i-1. If i is not divisible by any of these numbers, it means i is a prime number.


        
# num = 100
# while num <= 500:
#     len_digit = len(str(num))
#     armsto = sum(int(digit) ** len_digit for digit in str(num))
#     if num == armsto:
#         print(num)
#     num += 1

# num = int(input("Enter a number: "))
# original_num = num
# reversed_num = 0

# while num > 0:
#     remainder = num % 10
#     reversed_num = reversed_num * 10 + remainder
#     num = num // 10

# if original_num == reversed_num:
#     print(original_num, "is a palindrome.")
# else:
#     print(original_num, "is not a palindrome.")

# for i in range(1,11):
#     for j in range(1, i + 1):
#         print(j , end = " ")
#     print()        

# # 12.)Write a Python function to merge two dictionaries.

# d1 = {
#     "Name" : ["Aftab","ajay", "Aman"],
#     "age" : [20, 23, 24]
# }

# d2 = {
#     "Name" : ["Alam", "aman", "Sahil", "Nupur"],
#     "marks" : [78, 79, 90, 99],
#     "age" : [19, 20, 21, 22],
#     "pass" : ["yes", "no", "no", "yes"]
# }

# def fun(a, b):
#     merged = {}
#     for key in set(list(a.keys()) + list(b.keys())):
#         if key in a and key in b:
#             merged[key] = a[key] + b[key]
#         elif key in a:
#             merged[key] = a[key]
#         else:
#             merged[key] = b[key]            
#     return merged
#     # print(merged)

# print(fun(d1, d2))


# def palindrom(s):
#     if len(s) <= 1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return palindrom(s[1:-1])

# print(palindrom("Hello"))
# print(palindrom("mom"))


# var = [1,1,2,3,4,5,6,7,8]
# result = []
# # duplicates
# for i in var:
#     if var.count(i) > 1 and i not in result:
#         result.append(i)   
        

# print(result)    

var = "Python is great and Python is easy to learn. Python is popular"
var1 = var.lower()
var2 = var1.split()

result = []

for i in var2:
    if var.count(i) > 1 and i not in result:
        result.append(i)
        print(i)

print(var2)



# new_var = list(set(var))
# new_var.sort()

# if len(new_var) >= 2:
#     print(new_var[-2])

# else:
#     print()

t2 = (1)
t3=(True)
t4=(1,)
print(type(t2))
print(type(t3)) 