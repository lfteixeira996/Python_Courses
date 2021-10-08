"""
Write a program that asks the user to enter 10 numbers between 0 and 100.
After all the numbers are entered, of all the numbers that the user enters that are between 50 and 100,
print out the smallest one. If none are in that range, then print out a message indicating that fact.
"""

lst = []
count = 0

while (1):

    val = eval(input("Insert a value between 0 and 100: "))

    if val >= 0 and val <= 100:
        lst.append(val)
        count += 1

    if count == 10:
        break






