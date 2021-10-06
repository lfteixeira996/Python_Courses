"""
Ask the user for a length in feet. Then ask them which unit they want to convert to (inches, centimeters, or meters)
and print out the converted value. There are 12 inches in a foot, 30.48 cm in a foot,
and .3048 meters in a foot. If the unit chosen is not one of the above, then print out an error message.
"""

len = eval(input("Insert the length: "))

unit = input("Insert the Unit: ")

if unit == "inches":
    print("Result in inches: ", len*12)

elif unit == "centimeters":
    print("Result in centimeters: ", (len*30.48))

elif unit == "meters":
    print("Result in meters: ", (len*0.3048))

else:
    print("Error!")
