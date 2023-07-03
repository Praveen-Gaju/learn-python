"""
You are tasked with creating a "7 Up or Down" game where the user has to guess whether a randomly generated number is above, below, or equal to 7. 
Your program should use the random module to generate a random number between 1 and 13 (inclusive). The user should then be prompted to make 
their guess. If the user's guess matches the random number, they win! Otherwise, they lose.
Here are the specific requirements for your program:
1. Your program should generate a random number between 1 and 13 (inclusive)using the random module.
2. Your program should prompt the user to enter their guess (above, below,or equal to 7) and store it in a variable.
3. Your program should compare the user's guess to the random number and print "You win!" if they guessed correctly, or "Sorry, you lose." 
if they guessed incorrectly.
4. Your program should handle invalid user input (e.g. if the user enters "between" instead of "above" or "below").
"""
import random

random_num = random.randint(1, 13)
guess = input("Is the number above, below, or equal to 7? ")

if guess == "above":
    if random_num > 7:
        print("You Win!")
    else:
        print("Sorry, You lose.")

elif guess == "below":
    if random_num < 7:
        print("You Win!")
    else:
        print("Sorry, You lose.")

elif guess == "equal to":
    if random_num == 7:
        print("You Win!")
    else:
        print("Sorry, You lose.")
else:
    print("Invalid Inut")
