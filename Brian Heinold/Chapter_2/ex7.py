"""
Write a program that uses a for loop to print out the first 20 perfect squares, all on the same line. The
first few are 1, 4, 9, 16, 25, . . . .
"""

for i in range(1, 21):
   print(pow(i, 2), end=" ")