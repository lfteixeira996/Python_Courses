"""
The file expenses.txt has a bunch of expenses, each an integer, one on each line. Write a program
that reads the file and prints out how many expenses are over $2000. Print all of them on the same
line.
"""

with open("expenses.txt") as file:
    for line in file:
        if int(line.strip()) > 2000:
            print(line.strip(), end=' ')

