#https://holypython.com/intermediate-python-exercises/exercise-12-python-zip-function/

#Exercise 12-a:

print("Exercise 12-a")

lst1=[19542209, 4887871, 1420491, 626299, 1805832, 39865590]
lst2=["New York", "Alabama", "Hawaii", "Vermont", "West Virginia",  "California"]

#Type your answer here.
lst3=list(zip(lst1, lst2))

print(lst3)

#################################

#Exercise 12-b: 
print("Exercise 12-b")

lst1=["Energy", "Agriculture", "Industry", "Technology", "Finance", "Forestry", "Transport"]

#Type your answer here.
rng1= range(1, 8)

lst= list(zip(lst1, rng1))

print(lst)

#################################

#Exercise 12-c: 
print("Exercise 12-c")

lst1=["Netflix", "Hulu", "Sling", "Hbo"]
lst2=[198, 166, 237, 125]

#Type your answer here.
points= dict(zip(lst1, lst2))

print(points)

#################################

#Exercise 12-d: 
print("Exercise 12-d")
lst1=["Mike", "Danny", "Jim", "Annie"]
lst2=[4, 12, 7, 19]

#Type your answer here.
sorted_lst= sorted(list(zip(lst1, lst2)))

print(sorted_lst)




