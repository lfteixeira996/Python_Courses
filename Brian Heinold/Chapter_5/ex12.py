"""
Write a program that generates 20 random numbers from 1 through 10. Print all of the generated
numbers on the same line. Just once, after all the numbers have been printed, print out whether or
not the same number was ever generated twice in a row. [Hint: use a variable to keep track of the
most recently generated number.]
"""

from random import randint

lst = []

for i in range(10):
    lst.append(randint(1, 10))

print(lst)




