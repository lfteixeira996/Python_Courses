"""
Write a program that adds up the sines (use the sin() function from the math module) of all the
numbers from 1 through 100 and prints the result.
"""

from math import sin

soma = 0
for i in range(101):
    soma += sin(i)

print("Sum = ", soma)