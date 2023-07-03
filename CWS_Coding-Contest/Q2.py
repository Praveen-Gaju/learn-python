"""
Ask a number from user. Print 'Yes' if the number is divisible by 2,3 but not 8. Otherwise print 'No'

"""

num = int(input("Enter the number: "))
if num % 2 == 0 and num % 3 == 0 and num % 8 != 0:
    print("Yes")
else:
    print("No")
