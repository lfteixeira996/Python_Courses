#https://holypython.com/intermediate-python-exercises/exercise-14-python-filter-function/



"""lst1=[-1000, 500, -600, 700, 5000, -90000, -17500]

print(list(map(lambda x: x * (-1), lst1)))"""


"""
This time using filter() and list() functions filter all the positive integers in the string.
"""
str1="Winter Olympics in 2022 will take place in Beijing China"

print(list(filter(lambda ch: ch.isdigit(),str1)))