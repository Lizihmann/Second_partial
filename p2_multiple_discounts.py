https://replit.com/join/iztbtfbhoq-liz-sophiesophi

product = float(input("Please enter the priceof your product: "))
category = input("Please enter the category (A, B, C): ")
units = int(input("Please enter the number of units purchased: "))

discount = 0
additional_discount = 0

if category == "A": 
  discount = 10

elif category == "B": 
  discount = 5

elif category == "C":
  discount = 2 

else:
  if unit == 10:
    additional_discount =+5

print("this is your final price after the discounts: ", discount)
