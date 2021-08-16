#https://holypython.com/intermediate-python-exercises/exercise-14-python-filter-function/

################################################
#Exercise 14-a
#Using filter() function filter the list so that only negative numbers are left.

print('Exercise 14-a')
lst1=[12, -1, 9, 8, -0.5, -0.2, -100]
#Type your answer here.

lst2= list(filter(lambda x: x < 0, lst1))

print(list(lst2))

################################################
#Exercise 14-b
#Using filter function, filter the even numbers so that only odd numbers are passed to the new list.

print('Exercise 14-b')
lst1=[22, 100, 19, 13, 11, 1, 4, 66]
#Type your answer here.

lst2= list(filter(lambda x: x%2 != 0, lst1))

print(lst2)

################################################
#Exercise 14-c
#Using filter() and list() functions and .lower() method filter all the vowels in a given string.

"""print('Exercise 14-c')
str1="Winter Olympics in 2022 will take place in Beijing China"
#Type your answer here.

lst= list(filter( lambda x: x.lower().isalpha(), str1))

print(lst)"""

################################################
#Exercise 14-d
#This time using filter() and list() functions filter all the positive integers in the string.

print('Exercise 14-d')
str1="Winter Olympics in 2022 will take place in Beijing China"
#Type your answer here.

lst= list(filter( lambda x: x.isdigit(), str1))

print(lst)

################################################
#Exercise 14-e
#Using map() and filter() functions add 2000 to the values below 8000.

print('Exercise 14-e')
lst1=[1000, 500, 600, 700, 5000, 90000, 17500]
#Type your answer here.

lst2= list(map(lambda x: x+2000, filter(lambda x: x <8000, lst1)))

print(lst2)

################################################
#Exercise 14-f
#This time swap the map() and filter() functions so that map() function is inside filter() function.
#Convert a number to positive if it's negative in the list. Only pass those that are converted from
#negative to positive to the new list.

print('Exercise 14-f')
lst1=[-1000, 500, -600, 700, 5000, -90000, -17500]
#Type your answer here.

lst2=list(filter(lambda x: x>0 , map(lambda x: x*(-1), lst1)))

print(lst2)
################################################
