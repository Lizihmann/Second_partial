"""
Create a program that records the customers who enter a store and how many of them buy wands. 
You should record which customers bought which wands. 
The wand options are: 1. Elder Wand, 2. Hawthorn Wand, 3. Willow Wand, and 4. Holly Wand.
"""

client = input("Does a client come in? (Yes/No): ")
buy = input("Do they but something? (Yes/No): ")

total_clients = 0

option = input("What wand did you buy?")
wand = ["Elder Wand (1)", "Hawthorn Wand (2)", "Willow Wand (3)", "Holly Wand (4)"]

while client == "Yes":
    if buy == "Yes":
        wand = input("Which wand did they buy? (Elder Wand, Hawthorn Wand, Willow Wand, or Holly Wand): ")
        if wand == "Elder Wand":
            print("You bought an Elder Wand")
        elif wand == "Hawthorn Wand":
            print("You bought a Hawthorn Wand")
        elif wand == "Willow Wand":
            print("You bought a Willow Wand")
        elif wand == "Holly Wand":
            print("You bought a Holly Wand")
        else:
            print("You did not buy a wand")
    else:
      print("You did not buy anything")

print("What a great day for Ollivanders!")
