"""
Develop a program that calculates the percentage error of an LM35 temperature sensor in a laboratory. 
The program must detect and store raw data, ultimately displaying the percentage of times that the sensor gave values outside the expected range (between 10 and 40 degrees Celsius).
"""

temperature_readings = int(input("Please enter the number of temperature readings: "))

temperature_list = []
for i in range(temperature_readings):
    temperature = int(input("Please enter the temperature reading: "))
    temperature_list.append(temperature)
    if temperature >=40: 
      print("The temperature reading is within the normal range.")
    elif temperature <=10:
      print("The temperature reading is within the normal range.")
print(temperature_list)
