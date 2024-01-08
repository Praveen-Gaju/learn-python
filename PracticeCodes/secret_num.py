"""
Guess a number

secret_number (Randomly 1 - 10)

user_number=

You won
Sorry, the number was 
"""

import random

secret_num=random.randint(1,10)
user_num=int(input("Enter your Num: "))
if user_num== secret_num :
    print("You Won")
else:
    print(f"sorry, thr number was {secret_num}")