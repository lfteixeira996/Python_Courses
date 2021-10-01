"""
Write a program that asks the user to enter a size and then draws the letter C like the one below. It’s
width and height should be equal and the size specified by the user.

*****
*
*
*
*****

"""

size = eval(input("Insert the size: "))

for i in range(size):
    print("*", end="")

print()
for i in range(size-2):
    print("*")

for i in range(size):
    print("*", end="")

