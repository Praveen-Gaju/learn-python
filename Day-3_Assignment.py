# What is the output of the expression print(-18 // 4) ?

print(-18//4)

# What is the output of print(2 * 3 ** 3 * 4) ?

print(2 * 3 ** 3 * 4)

# What is the output of print(10 - 4 * 2) ?

print(10 - 4 * 2)

# Write a python program to find minimum of two numbers. Ask numbers from user.

num1=int(input("Enter the first number:"))
num2=int(input("Enter the first number:"))

min_num=min(num1,num2)
print(min_num)

# Write a python program to convert temperature from Celsius to Fahrenheit. Ask Celsius from User.

celsius = float(input('enter temperature in celsius: '))
fahrenheit=(9/5)*celsius+32
print(f"Temperature in fahrenheit is {fahrenheit}")

# Ask 3 numbers from User and Calculate the Average.

a=float(input("Enter value of a:"))
b=float(input("Enter value of b:"))
c=float(input("Enter value of c:"))
avg=(a+b+c)/3
print(avg)


# Ask number of games played in a tournament. Ask the user number of games won and number of games loss. Calculate number of tie and total Points. (1 win= 4 points, 1 tie =2 points)

games_played=int(input("Enter no. of Games played: "))
games_won=int(input("Enter no. of Games won: "))
games_lost=int(input("Enter no. of Games lost: "))
games_tie=games_played-games_won-games_lost
game_points=(4*games_won)+(2*games_tie)
print(f"Total Tie Games are {games_tie}")
print(f"Total points are {game_points}")
