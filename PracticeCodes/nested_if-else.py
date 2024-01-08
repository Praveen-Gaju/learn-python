"""
Nested If-else
"""

age = int(input("Enter your age: "))
if age >= 14:
    if age >= 18:
        print("Adult")
    else:
        print("Teenager")
elif age > 1 and age <= 13:
    print("Child")
else:
    print("Invalid age")
