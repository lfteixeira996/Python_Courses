"""
The Body Mass Index, BMI, is calculated as
BMI = 703w/h^2

where w is the person’s weight in pounds and h is the person’s height in inches. Write a program that
asks the user for their height their weight and prints out their BMI.

[Note: one way to compute h^2 is as h · h.]
"""

w = int(input("Insert your weight: "))
h = int(input("Insert your height: "))

BMI = 703*w/(h*h)

print(f"BMI = {BMI}")