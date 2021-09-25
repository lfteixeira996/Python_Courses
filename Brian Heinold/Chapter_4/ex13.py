"""
Write a program that asks the user to enter a height and then draws a box like the one below that is
10 asterisks wide and as tall as specified by the user.
**********
**********
**********
**********
"""

print("Exercise 13")

lines = input("Insert the number of lines: ")

for i in range(0, int(lines)):
    print(10 * '*')
