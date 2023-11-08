https://replit.com/join/hhodxosuur-liz-sophiesophi
"""
Write a program that detects if 'Alexa' is written in a text. If you type more than once, the program should respond "Hey, just say my name once." Tip: use the split() functions to separate the text and count() to identify the times Alexa says.
"""

name = input("Say Something so her: ")

count = 0

for word in name.split():
  if word == "Alexa":
    count += 1
    
if count > 1:
  print("Hey, just say my name once!")

