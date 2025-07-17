# Number of rows for the patterns
n = 5

# 1. Right Triangle
print("1. Right Triangle")
for i in range(1, n + 1):
    print("*" * i)

# 2. Inverted Right Triangle
print("\n2. Inverted Right Triangle")
for i in range(n, 0, -1):
    print("*" * i)

# 3. Left Aligned Triangle
print("\n3. Left Aligned Triangle")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)

# 4. Inverted Left Aligned Triangle
print("\n4. Inverted Left Aligned Triangle")
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * i)

# 5. Pyramid
print("\n5. Pyramid")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# 6. Inverted Pyramid
print("\n6. Inverted Pyramid")
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# 7. Diamond
print("\n7. Diamond")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# 8. Hollow Pyramid
print("\n8. Hollow Pyramid")
for i in range(1, n + 1):
    if i == 1:
        print(" " * (n - i) + "*")
    elif i == n:
        print("*" * (2 * i - 1))
    else:
        print(" " * (n - i) + "*" + " " * (2 * i - 3) + "*")

# 9. Hollow Diamond
print("\n9. Hollow Diamond")
for i in range(1, n + 1):
    if i == 1:
        print(" " * (n - i) + "*")
    else:
        print(" " * (n - i) + "*" + " " * (2 * i - 3) + "*")
for i in range(n - 1, 0, -1):
    if i == 1:
        print(" " * (n - i) + "*")
    else:
        print(" " * (n - i) + "*" + " " * (2 * i - 3) + "*")
