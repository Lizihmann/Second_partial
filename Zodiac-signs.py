https://replit.com/join/kfnuynhjuf-liz-sophiesophi

"""
Write a Python program that prompts the user to enter their birthdate (in the format: MM/DD/YYYY).
2. Calculate their zodiac sign based on their birthdate.
3. Display the determined zodiac sign to the user.
4. Make sure to handle invalid inputs gracefully (e.g., non-numeric characters or out-of-range dates).
5. Test your program with different birth dates to ensure accuracy.

Hint: You can use conditional statements and date ranges to determine the zodiac sign.

Example Output:
- Enter your birthdate (MM/DD/YYYY): 07/22/1995
- Your zodiac sign is Cancer.

Aries: March 21 - April 19
Taurus: April 20 - May 20
Gemini: May 21 - June 20
Cancer: June 21 - July 22
Leo: July 23 - August 22
Virgo: August 23 - September 22
Libra: September 23 - October 22
Scorpio: October 23 - November 21
Sagittarius: November 22 - December 21
Capricorn: December 22 - January 19
Aquarius: January 20 - February 18
Pisces: February 19 - March 20
"""

birthdate = int(input("Please enter your birthdate in the format (MM/DD/YYYY):")
#S1. I firstly ask for the date of birth of the user.
                
print("The Zodiacs are: Cancer, Aries, Virgo, Leo, Aquarius,  Pisces, Scorpio, Sagittarius, Capricorn, and Libra")
#S2. I provide the information of the Zodiac signs
                
if birthdate == "March 21" and "April 19":
    print("Your zodiac sign is Aries")
                
elif birthdate == "April 20" and "May 20":
    print("Your zodiac sign is Taurus")

elif birthdate == "May 21" and "June 20":
    print("Your zodiac sign is Gemini")

elif birthdate == "June 21" and "July 22":
    print("Your zodiac sign is Cancer")

elif birthdate == "July 23" and "August 22": 
  print("Your zodiac sign is Leo")

elif birthdate == "August 23" and "September 22": 
  print("Your zodiac sing is Virgo")

elif birthdate == "September 23" and "October 22": 
  print("Your zodiac sign is Libra")

elif birthdate == "October 23" and "November 21": 
  print("Your zodiac sign is Scorpio")

elif birthdate == "November 22" and "December 21": 
  print("Your zodiac sign is Sagittarius")

elif birthdate == "December 22" and "January 19": 
  print("Your zodiac sign is Capricorn")

elif birthdate == "January 20" and "February 18": 
  print("Your zodiac sign is Aquarius")

elif birthdate == "February 19" and "March 20": 
  print("Your zodiac sign is Pisces")

