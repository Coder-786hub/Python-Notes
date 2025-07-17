

# a=[1,2,3,4,5,6,7,8,9,10]
# b=a[:5]
# b.reverse()
# print(b)

# c=a[-5:]
# print(c)
# b.extend(c)
# print(b)


# a=1001200035400062100251002251100000121
# b=str(a)
# print(type(b))

# c=b.replace("0"," ")
# print(c)

# Que 1
'''age=int(input("Enter age: "))

if age>=18:
    print("Congratualitin, your are eligible for voting.")
else:
    print("Sorry, you are not eligible.")'''

# Que 2
# num=int(input("Enter the number: "))

# if num%2  ==0:
#     print(f"{num} is the even number.")
# else:
#     print(f"{num} is the odd number")

# Que 3
# num=int(input("Enter the number: "))

# if num % 7 ==0:
#     print(f"Yes, {num} is divisiable by 7.")
# else:
#     print(f"No, {num} is not divisiable by 7.")


# Que 4
# num=int(input("Enter the number: "))

# if num % 3 ==0:
#     print(f"Yes, {num} is divisiable by 3.")

# else:
#     print(f"No, {num} is not divisiable by 3.")


# Que 5
# year=int(input("Enter year: "))
# if year % 4 ==0:
#     print("yes")
# else:
#     print("No")

'''# Que 6
marks=int(input("Enter the marks: "))
if marks>90:
    print("A")
elif marks >80 and marks <=90:
    print("B")
elif marks >=60 and marks <=80:
    print("C")
else:
    print("D")'''


# # Que 7

# num=int(input("Enter a number from 1 to 7: "))

# if num==1 :
#     print("Sunday")

# elif num==2:
#     print("Monday")

# elif num==3:
#     print("Tuesday")

# elif num==4:
#     print("Wednesday")

# elif num==5:
#     print("Thursday")

# elif num==6:
#     print("Friday")

# elif num==7:
#     print("Saturday")

'''# Que 8

num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))

operator=input("Enter operator +,-,*,/: ")

if operator== "+" :
    result=num1 + num2
    print(result)
'''

# Que 9
# num=int(input("Enter the number: "))
# if 100<= abs(num) <=999:
#     print("yes")
# else:
#     print("No")

'''# Que 10

num1=int(input("Enter the 1st number: "))
num2=int(input("Enter the 2nd number: "))

if num1< num2:
    print(f"Yes,{num1} is the lowest number.")

elif num2 < num1:
    print(f"Yes, {num2} is the lowest number")

else:
    print("Both number are equals")'''

# Que 11

# num1=int(input("Enter the 1st number: "))
# num2=int(input("Enter the 2nd number: "))

# if num1> num2:
#     print(f"Yes,{num1} is the Largest number.")

# elif num2 > num1:
#     print(f"Yes, {num2} is the Largest number")

# else:
#     print("Both number are equals")

'''# Que 12

num1=int(input("Enter the 1st number: "))

if num1 % 2 ==0 and num1 % 3 ==0:
    print(f"The number {num1} is divisiable by 2 and 3.")

else:
    print(f"No the number {num1} is not divisiable by 2 and 3.")'''

# # Que 13

# age1=int(input("Enter the 1st people age: "))
# age2=int(input("Enter the 2st people age: "))
# age3=int(input("Enter the 3st people age: "))
# age4=int(input("Enter the 4st people age: "))

# if age1 ==18 :
#     print("No")
# elif age2 > 18:
#     print("yes he is the Youngest one")

# elif age3

# Que 14
# def get_vowels(input_string):
#     vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
#     result = []
#     result2= []
#     for char in input_string:
#         if char in vowels:
#             result.append(char)

#         else:
#             result2.append(char)
#     print(result2)

#     return result

# out = get_vowels("Aftab Alam Khan Kaise ho")
# print(out)

# Que 15
# x=int(input("Enter the number:"))
# for i in range(x):
#     for j in range(1,i +1):
#         print(j,end=" ")
#     print()


# a = ["this", "is", "a", "car"]
# b = ["are", "you", "ok"]

# var1=a[0],b[0],a[1],b[1],a[2],b[2],a[3]
# print(var1)

# Que 16
# var=int(input("Enter the number: "))

# for i in range(1,11):
#     print(f"{var} x {i} = {var * i}")

# # Que 17
# lists=[10,20,30,50,60,40,80,40,90,70,20,10,30]
# for i in lists:
#     lists.reverse()
# print(lists)

# # Que 18
# lists=[10,20,30,50,60,40,80,40,90,70,20,10,30]
# for i in lists:
#     lists.sort()
# print(lists)

# Que 19
# number = int(input("Enter a number: "))

# if number <= 1:
#     is_prime = False
# else:
#     is_prime = True
#     i = 2
#     while i * i <= number:
#         if number % i == 0:
#             is_prime = False
#             break
#         i += 1

# if is_prime:
#     print(f"{number} is a prime number.")
# else:
#     print(f"{number} is not a prime number.")


# a= [1,2,3,4,5,6,7,8]
# for i in a:
#     if i=="":
#         # pass
#         print(i)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x)


# def fun_ction():
#     print("Hello world")

# fun_ction()    


# for i in range(1, 11):
#     if i:
#         print(i)