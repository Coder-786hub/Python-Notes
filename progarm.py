# Average_distance 

def calculate_average_distane(speed,time):
    average_distance = speed * time
    return average_distance
speed =  200
Time = 2
average_distance = calculate_average_distane(speed,Time)
print("The average distance of the car on mars is:",average_distance,"Meter")

# Average_speed

# Define a function to calculate the average speed of a car on mars 

def calculate_average_speed(distance,time):
    average_speed = distance / time
    return average_speed 

#  define the distance and time for the car rece 
distance = 200
# kilometeres
Time = 4
#  hours

# calculate and print the average_speed 
average_speed = calculate_average_speed(distance,Time)
print("The average speed of the car on Mars is:", average_speed,"Kilometers per hour")


# Calculate age

def calculate_age(birth_year):
    import datetime
    current_year = datetime.datetime.now().year
    age = current_year - birth_year
    # birth_year = int(input("Enter your birth year: "))
    print(age)
    return age
calculate_age(birth_year=2005)
    # return age

# Second age calculator 

import datetime

def calculate_age(birth_year):
    current_year = datetime.datetime.now().year
    age = current_year - birth_year
    return age

def main():
    # try:
    birth_year = int(input("Enter your birth year: "))
        # if birth_year > datetime.datetime.now().year:
            # print("Invalid birth year. Please enter a valid year.")
            # return
    age = calculate_age(birth_year)
    print(f"You are {age} years old.")
    # except ValueError:
        # print("Invalid input. Please enter a valid year.")

if __name__ == "__main__":
    main()


