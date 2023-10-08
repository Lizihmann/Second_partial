https://replit.com/join/dtaeqhlyob-liz-sophiesophi

"""
Write a program that helps calculate the total nutrients in a recipe. The user should input the ingredients and their quantities, 
as well as the nutritional information per 100 grams of each ingredient. 
Then, calculate the total nutrients in the recipe considering the quantities provided by the user
"""

ingredients = int(input("Enter the number of ingredients: "))
quanitites = []
nutritional_info = []
total_nutrients = []
#I left the parenthesis open, because the number still has to be written

for i in range(ingredients):
    ingredient = input("Enter the name of the ingredient: ")
    quantity = int(input("Enter the quantity of the ingredient: "))
    nutritional_info.append(input("Enter the nutritional information of the ingredient: "))
    quanitites.append(quantity)
    total_nutrients.append(quantity * nutritional_info[i])
print(total_)

