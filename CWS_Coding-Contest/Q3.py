"""
Rent Calculator
"""

monthly_rent = int(input("Enter your Monthly rent: "))
total_months = int(input("Enter the total number of Months:"))
deposit = 2 * monthly_rent  # deposit is considered as 2 months of rent

total_cost = (monthly_rent * total_months) + deposit
print("Total cost for Renting a house is:", total_cost)
