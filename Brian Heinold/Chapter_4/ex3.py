"""
Ask the user to enter a temperature in Celsius. If the temperature is less than or equal to 0, print
“Warning: Low temperature.” If the temperature is between 0 and 35, print ”Temperature is okay.”
Otherwise, print out “Warning: High temperature.”
"""

temp = eval(input("Insert temperature: "))

if temp <= 0:
    print("Warning: Low temperature.")

elif 0 < temp <= 35:
    print("Temperature is okay.")

else:
    print("Warning: High temperature.")