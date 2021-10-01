"""
The distance between two numbers on the number line is the absolute value of the difference of the
two numbers. For instance, the distance between 3 and 7.2 is |3 − 7.2| = 4.2. Write a program that
asks the user for two numbers and prints out the distance between them.
"""

val1 = eval(input("First number: "))
val2 = eval(input("Second number: "))

print(abs(val1-val2))