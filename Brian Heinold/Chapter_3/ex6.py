"""
Write a program that prints out the numbers from 1 to 20 and their square roots, rounded to 4 decimal
places, with the square root of the number being on the same line as the number.
"""
from math import sqrt

for i in range(1, 21):
    print(f"{i} {round(sqrt(i), 4)}")