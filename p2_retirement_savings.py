https://replit.com/join/kbkhabwxip-liz-sophiesophi

"""
PMT is the required monthly payment
FV is the desired retirement amount
r is the monthly interest rate (annual return divided by 12, expressed as a decimal)
n is the number of monthly payments in retirement (year of retirement multiplied by 12)
t is the number of years until retirement

STEPS 
1. enter the current age
2. enter the age you want to retire
3. enter your desired retirement amount
4. calculate how much they should save monthly, considering an expected annual investment return 
"""

current_age = int(input("Enter your current age: "))
retirement_age = int(input("Enter the age you want to retire: "))
desired_retirement_amount = int(input("Enter your desired retirement amount: "))

monthly_savings = (int(desired_retirement_amount))*12/100

print("You need to save about", monthly_savings, "per month, to reach your retirement goal")
