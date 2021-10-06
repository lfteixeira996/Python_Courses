"""
Write a program that generates 50 random numbers from 1 through 9. Print out all 50 numbers on the
same line. Then print out how many fives are generated.
"""
import random

count = 0

for i in range(50):
    val = random.randint(1, 9)
    if val == 5:
        count =  count +1

    print(val, end=" ")

print()
print("Number of fives = ", count)