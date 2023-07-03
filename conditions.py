"""
Conditional Statement
1.If Statement
2.if-else 
3.elif
"""

# age as input

age=int(input("Enter your age: "))
if age>18:
    print ("You are adult")
else : 
    print ("you are child")


# Maximum of 2 numbers

num1=int(input("Enter Num1: "))
num2=int(input("Enter Num2: "))
if num1>num2:
    print("num1 is greater")
elif num2>num1:
    print("num2 is greater")
else:
    print("Both are equal")


"""
Ask age from user.

18 above -> Adult
13-17 -> Teenager
13 below -> Child
"""

age=int(input("Enter your age: "))
if (age>18):
    print("Adult")
elif (age >= 13 and age <=18):
    print("Teenager")
else:
    print("Child")