"""
An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. A leap year contains a leap day.
Two conditions are used to identify leap years:
· If the year can be evenly divided by 4, it is then a leap year.
· But if year is evenly divided by 4 and also by 100, then it is NOT a leap year.
· But if year is evenly divided by 4 and also by 400, then it is a leap year.
This means the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.
Ask a year input from user. And tell if the year entered by user is leap or not.
"""

year = int(input("Enter year: "))

if year % 4 == 0:  # if the year is divisible by 4 or not
    if year % 100 == 0:  # if the year is divisible by 100 or not
        if year % 400 == 0:  # if the year is divisible by 400 or not
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
