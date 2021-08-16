#https://holypython.com/intermediate-python-exercises/exercise-13-python-map-function/

################################################
#Exercise 13-a
#Write a map function that adds plus 5 to each item in the list.

print('Exercise 13-a')
#Type your answer here.

lst1=[10, 20, 30, 40, 50, 60]

lst2=list(map(lambda x: x+5, lst1))

print(lst2)

################################################
#Exercise 13-b
#Write a map function that returns the squares of the items in the list.
print('Exercise 13-b')
#Type your answer here.

lst1=[10, 20, 30, 40, 50, 60]

lst2=list(map(lambda x: x**2, lst1))

print(lst2)

################################################
#Exercise 13-c
#Write a map function that adds "Hello, " in front of each item in the list.
#Type your answer here.

print('Exercise 13-c')
lst1=["Jane", "Lee", "Will", "Brie"]

lst2=list(map(lambda x: 'Hello, '+x, lst1))

print(lst2)

################################################
#Exercise 13-d
#Using map() function and len() function create a list that's consisted of lengths of each
#element in the first list.

print('Exercise 13-d')
#Type your answer here.

lst1=["Alpine", "Avalanche", "Powder", "Snowflake", "Summit"]

lst2=list(map(lambda x: len(x), lst1))

print(lst2)

################################################
#Exercise 13-e
#Using map() function and lambda add each elements of two lists together. Use a lambda with two arguments.

print('Exercise 13-e')
lst1=[100, 200, 300, 400, 500]
lst2=[1,10,100,1000,10000]


#Type your answer here.

lst3=list(map(lambda x, y: x+y, lst1, lst2))


print(lst3)

################################################
#Exercise 13-f
#Using map() function and lambda and count() function create a list which
#consists of the number of occurence of letter: a.

print('Exercise 13-f')
lst1=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
#Type your answer here.

lst2=list(map(lambda x: x.count('a'), lst1))


print(lst2)

################################################
#Exercise 13-g
#Using map() function and lambda and count() function
#create a list consisted of the number of occurence of both letters: A and a.

print('Exercise 13-g')
lst1=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
#Type your answer here.

lst2=list(map(lambda ch: ch.lower().count('a'), lst1))


print(lst2)
