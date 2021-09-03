#https://holypython.com/intermediate-python-exercises/exercise-15-python-sorted-function/

#Exercise 15-a
#Using sorted() function, sort the list in ascending order.

lst1=[500, 1000, 400, 40000, 999, 2, 0.5, 17]

#Type your answer here.
lst2=sorted(lst1)

print(lst2)


#Exercise 15-b
#Using sorted() function, sort the list from a to z.

lst1=["zebra", "bird", "ant", "porcupine", "giraffe"]

#Type your answer here.
lst2=sorted(lst1)

print(lst2)


#Exercise 15-c
#Using sorted() function sort the list from z to a.
lst1=["zebra", "bird", "ant", "porcupine", "giraffe"]

#Type your answer here.
lst2=sorted(lst1, reverse=True)

print(lst2)


#Exercise 15-d
#Using sorted() function sort the list in descending order.
lst1=[500, 1000, 400, 40000, 999, 2, 0.5, 17]

#Type your answer here.
lst2=sorted(lst1, reverse=True)

print(lst2)


#Exercise 15-e
#Using len function and sorted() function, sort the list based on the length of the strings (In ascending order).
lakes1=["Malawi", "Medicine", "Tahoe", "Moraine", "Upper Arrow", "Plitvice", "Edith", "Emerald"]

#Type your answer here.
lakes2=sorted(lakes1, key=lambda lake: len(lake))

print(lakes2)

#Exercise 15-f
#Using len function and sorted() function, sort the list based on the length of the strings this time in descending order.

lakes1=["Malawi", "Medicine", "Tahoe", "Moraine", "Upper Arrow", "Plitvice", "Edith", "Emerald"]

#Type your answer here.
lakes2=sorted(lakes1, key=lambda lake: len(lake), reverse=True)

print(lakes2)


#Exercise 15-g
#Using lambda and sorted() function, sort the list based on last characters of the items from z to a.
lakes1=["Malawi", "Medicine", "Tahoe", "Moraine", "Upper Arrow", "Plitvice", "Edith", "Emerald"]

#Type your answer here.
lakes2=sorted(lakes1, key=lambda lake: lake[-1], reverse=True)

print(lakes2)


#Exercise 15-h
#Using lambda and sorted() function, sort the list based on the remainder from dividing each element to 5 (From greater to smaller).

lst1=[1000, 50, 66, 101, 333, 9999, 19, 300, 200, 250]

#Type your answer here.
lst2=sorted(lst1, key=lambda lst: lst%5, reverse=True)

print(lst2)





