https://replit.com/join/fehsmltgre-liz-sophiesophi

#I will enter the weight in kilograms, the duration of the exercise and the type of exercise
weight = int(input("Enter your weight in kilograms: "))
duration = int(input("Enter the duration of the activity in minutes: "))
type = input("Enter the type of exercise (running, swimming, cycling, etc.): ")

#now I will create a formula to calculate the amount of calories burned in the exercise
calories = (int(duration)*int(3.5)*int(weight))/20

#I calculated it by multiplying the weight with the duration and dividing it by 20

print("You burned around", calories, "calories while", type)
