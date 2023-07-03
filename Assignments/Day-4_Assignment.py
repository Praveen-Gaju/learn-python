"""
Write a program that asks the user for their favorite color and prints out a message depending on the color they choose. For example: 
"Red is a bold color!" or "Blue is a calm color!". Use at least 3 different colors in your program.
"""

color=input("Enter your favorite color ")
if color == "red":
    print("Red is a bold color!")
elif color == "blue":
    print("Blue is a calm color!")
elif color == "green":
    print("You Loves environment")


"""
Write a program that asks the user for a number and prints out whether the number is positive, negative, or zero
"""

num=int(input("Enter the Number: "))
if num == 0:
    print ("Zero")
if num < 0:
    print("Negative")
if num > 0:
    print("Positive")



"""
Write a program that asks the user for a letter grade (A, B, C, D, or F) and prints out the corresponding GPA. For example, 
an A should print out as 4.0, a B as 3.0, and so on
"""

grade = input('Enter letter grade:')
if grade == "A":
    print("Grade is 4.0")
elif grade == "B":
    print("Grade is 3.0")
elif grade == "C":
    print("Grade is 2.0")
elif grade == "D":
    print("Grade is 1.0")
elif grade == "F":
    print("Grade is 0.0")

"""
Ask 4 ages from user (age1, age2, age3, age4). Print out which age is the youngest.
"""

age1= int(input("Enter age1: "))
age2= int(input("Enter age2: "))
age3= int(input("Enter age3: "))
age4= int(input("Enter age4: "))

young_age=min(age1, age2, age3, age4)

print(f"The Youngest is {young_age}")


"""
Python Program to Generate a Random Number
"""

import random
num = random.randint(1,10)
print(num)