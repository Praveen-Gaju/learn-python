"""
rock paper scissors
"""

import random

options = ["rock", "paper", "scissors"]
system_choice = random.choice(options)
user_choice = input("Enter your choice in rock, paper, scissors: ").lower()
if system_choice == user_choice:
    print("Tie Game")
elif system_choice == "rock" and user_choice == "paper":
    print("You Won the Game")
elif system_choice == "rock" and user_choice == "scissors":
    print("You Won the Game")
elif system_choice == "paper" and user_choice == "rock":
    print("I Won the Game")
elif system_choice == "paper" and user_choice == "scissors":
    print("I Won the Game")
elif system_choice == "scissors" and user_choice == "rock":
    print("You Won the Game")
elif system_choice == "scissors" and user_choice == "paper":
    print("I Won the Game")


import random


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"


def play_game():
    choices = ["rock", "paper", "scissors"]

    print("Let's play Rock-Paper-Scissors!")
    print("Choose one: rock, paper, scissors")

    while True:
        player_choice = input("Your turn: ").lower()
        if player_choice in choices:
            break
        else:
            print("Invalid choice. Please try again.")

    computer_choice = random.choice(choices)

    print("Computer's choice:", computer_choice)
    print(determine_winner(player_choice, computer_choice))


play_game()
