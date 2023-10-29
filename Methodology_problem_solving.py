https://replit.com/join/shovqnomek-liz-sophiesophi

"""
Solving a problem with methodology.
The problem: Chemistry rally/competition on Monday
1. asking if they studied
2. asking if they payed attention
3. the topics for the competition
4. asking if they studied and payed attention
5. asking about the difficulty level from 1 to 5
"""
study = input("Did you study for the chemistry rally? Answer with Yes/No")
#S1. asking the student if they studied for the rally using input function

attention = ("Did yiu pay attention in class to understand the topics? Answer Yes/No")
#S2. asking the student if they paid attention using input function

print("Nomenclature name and classification")
#S3. the topics of the competition

if study == "yes" and attention == "yes": 
#S4. if the student studied and paid attention, using condition
  print("Try to research in other sources thatyiu might mnow and maybe ask for help of a friend or your tutor.")
  print("make a study guide alone or with a friend")
  print("review all of your resources on how to determine the nomenclature")
elif study == "yes" and attention == "no": 
#S5. if the student studied but didn't pay attention, using conditionals
  print("Please pay more attention in class, student! Its important for this competition!")
elif study == "no" and attention == "yes": 
#S6. if the student hasn't studied but payed attention, using conditionals
  print("You should definetely study! Go on!")
elif study == "no" and attention == "no": 
#S7. they didn't study and didn't pay attention, using conditionals
  print("It's bad... you will not win this competition!")

difficulty_level = int(input("On a scale of 1 to 5, give me the number of how difficult it is for you to understand and learn nomenclature: "))
#S8. asking about the difficulty level using the input function

if difficulty_level == "5": 
#S9. asking the first difficulty level with a conditional
  print("It looks really bad with nomenclature for you, doesnt it?")
  print("try to review the topics again with an app of a tutor or friend")
  #proposing a solution with the print function
elif difficulty_level == "4":
  print("Okay, you seem to struggle a bit, still")
  print("try to understand with online videos or an app")
elif difficulty_level == "3":
  print("Okay, youre in the middle: Not 100% shure but 50-50")
  print("Study with a friend and dont be scared asking for help here, okay?")
elif difficulty_level == "2": 
  print("Great, you seem to get it quite well!")
  print("Still you can reviwe the topics again, to be 100% shure :)")
elif difficulty_level == "1":
  print("Wow, you definetely got it!")
  print("You dont need any more help, you are 100% sure of what you're doing! Great Job!")
#difficulty_level 1 is the easiest and difficulty_level 5 is the hardest
#Asking these questions by using conditionals
