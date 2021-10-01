"""
Write a program that asks the user for two numbers x and y and then prints out the result of x^y
"""

x = eval(input("First value: "))
y = eval(input("Second value: "))

print("Result: ", pow(x,y))

#or

print("Result: ", x**y)