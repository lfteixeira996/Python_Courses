"""
If you have a right triangle that is x units wide and y units tall, then using atan2(y,x) from the math
module finds one of the triangle’s angles. It returns the result in radians. The degrees() function can
convert the result to degrees. Write a program that asks the user to enter a width and a height and
prints out the angle returned by atan2, but in degrees and rounded to one decimal place.
"""
import math

wide = eval(input("Wide: "))
tall = eval(input("Tall: "))

radius = math.atan2(wide, tall)

print(round(math.degrees(radius), 1))

