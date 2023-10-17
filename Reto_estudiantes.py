https://replit.com/join/lrbzbmsygi-liz-sophiesophi

"""
Variables:
1. purchase amount ($) how much you paid
2. applied discount (%) how much you hot discounted
3. membership card (Yes/No) if you have one

If the purchase amount is greater than or equal to 100$.

1. ask the user for the purchase amount 
2. make a formula for discounts 
"""

purchase_amount = int(input("How much did you pay for your purchased items in dollars?"))
membership = input("Do you have a membership card?")
if membership == "yes": 
  print("You have an additional discount of 5%!")
  additional_discount = purchase_amount * 0.05
else: 
  print("You have to pay the full price, no additional discount, sorry!")

discounts = []
additional_discount = []

if purchase_amount >= 100: 
  print("But now you have a discount of 10%!")
  discount = purchase_amount * 0.1
  discounts.append(discount)
if purchase_amount <=100: 
  print("You have a disciunt of 5%!")
  discount = purchase_amount * 0.05
  discounts.append(discount)
else: 
  print("you have to pay the full price, sorry!")

final_price = purchase_amount - discounts[0]
print("Your final price is: ", final_price)

if purchase_amount <= 100: 
  final_price = purchase_amount * 0.1
  print("this is your final price", final_price)
if purchase_amount >= 100: 
  final_price = purchase_amount * 0.05
