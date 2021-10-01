"""
Write a program that generates and prints 100 random numbers from 50 to 60, all on the same line,
separated by spaces
"""
import random

for i in range(100):
    print(random.randint(50, 60), end=" ")