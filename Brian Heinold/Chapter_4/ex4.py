"""
Ask the user to enter a number of days. If the user enters 28 or 29, the program should print out
”Feb”. If they enter 30, the program should print out “Apr, Jun, Sep, Nov”. If they enter 31, the
program should print out “Jan, Mar, May, Jul, Aug, Oct, Dec”. For any other entry, the program
should print out “Error”.
"""

days = eval(input("Days: "))

if days==28 or days==29:
    print("Feb")

elif days==30:
    print("Apr, Jun, Sep, Nov")

elif days==31:
    print("Jan, Mar, May, Jul, Aug, Oct, Dec")

else:
    print("Error")