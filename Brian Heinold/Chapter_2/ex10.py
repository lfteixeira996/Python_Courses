"""
Write a program that uses exactly three for loops to print the output below. It has 10 A’s, followed by
5 copies of BCD, followed by one E, followed by 15 F’s.
"""

for i in range(10):
    print("A", end="")

for i in range(5):
    print("BCD", end="")

print("E", end="")

for i in range(15):
    print("F", end="")