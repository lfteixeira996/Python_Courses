"""
One way to solve math equations is by trial and error. Computers can help with that. The equation
21x^2 − x^3 + 21904 = 0 has an integer solution between 1 and 100. Use a for loop and an if statement
to find it.
"""

for i in range(1, 101):

    if 21*i**2 - i**3 + 21904 == 0:
        print("x=", i)
        break