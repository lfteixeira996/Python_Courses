"""
This is a very simple billing program. Ask the user for a starting hour and ending hour, both given in
24-hour format (e.g., 1 pm is 13, 2 pm is 14, etc.). The charge to use the service is $5.50 per hour. Print
out the user’s total bill. You can assume that the service will be used for at least 1 hour and never
more than 23 hours. Be careful to take care of the case that the starting hour is before midnight and
the ending time is after midnight
"""

start = eval(input("Starting hour: "))
end = eval(input("Ending hour: "))

if start >= 1 and end <= 23:
    print(f"Charge: {(end-start)*5.5}")

else:
    print("Error!")