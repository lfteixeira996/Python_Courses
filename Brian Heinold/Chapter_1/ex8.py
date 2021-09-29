"""
Write a program that asks the user to enter five numbers (use five input statements). Then print out
those numbers all on the same line, with each number separated from the others by exactly three
spaces. Use the sep optional argument to the print statement to do this.
"""

no_1 = int(input("Insert 1st number: "))
no_2 = int(input("Insert 2nd number: "))
no_3 = int(input("Insert 3th number: "))
no_4 = int(input("Insert 4th number: "))
no_5 = int(input("Insert 5th number: "))

print(no_1, no_2, no_3, no_4, no_5, sep='   ')