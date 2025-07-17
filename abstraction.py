

"""
Abstraction in Python is a fundamental concept in object-oriented programming that helps in hiding the complex implementation details and showing only the necessary features of an object. This makes the code more modular and easier to manage
"""


def calculate_area(shape, *args):
    if shape == "circle":
        return 3.14 * args[0] ** 2
    elif shape == "rectangle":
        return args[0] * args[1]
    elif shape == "triangle":
        return 0.5 * args[0] * args[1]
    else:
        return "Unknown shape"

# Using the calculate_area function
circle_area = calculate_area("circle", 5)
rectangle_area = calculate_area("rectangle", 4, 6)
triangle_area = calculate_area("triangle", 3, 4)

print(f"Circle area: {circle_area}")
print(f"Rectangle area: {rectangle_area}")
print(f"Triangle area: {triangle_area}")