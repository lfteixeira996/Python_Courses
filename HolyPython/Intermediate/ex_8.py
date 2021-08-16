#https://holypython.com/intermediate-python-exercises/exercise-8-python-for-loop/

################################################
#Exercise 8-a
#Write a for loop so that every item in the list is printed.

print("Exercise 8-a")
lst=["koala", "cat", "fox", "panda", "chipmunk", "sloth", "penguin", "dolphin"]
#Type your answer here.

for item in lst:
    print(item)

################################################
#Exercise 8-b
#Write a for loop which print "Hello!, " plus each name in the list. i.e.: "Hello!, Sam"

print("Exercise 8-b")
lst=["Sam", "Lisa", "Micha", "Dave", "Wyatt", "Emma", "Sage"]
#Type your code here.

for item in lst:
    print("Hello!,"+item)

################################################
#Exercise 8-c
#Write a for loop that iterates through a string and prints every letter.

print("Exercise 8-c")
str="Antarctica"
#Type your code here.

for ch in str:
    print(ch)

################################################
#Exercise 8-d
#Type a code inside the for loop so that counter variable named c is increased by one each time loop iterates.
#Can you guess how many times it will add 1?.
print("Exercise 8-d")

str="Civilization"

c=0
for i in str:
#Type your answer here.
    c += 1

print(c)

################################################
#Exercise 8-e
#Using a for loop and .append() method append each item with a Dr. prefix to the lst.
print("Exercise 8-e")

lst1=["Phil", "Oz", "Seuss", "Dre"]
lst2=[]
#Type your answer here.

for item in lst1:
    lst2.append('Dr.'+item)

print(lst2)

################################################
#Exercise 8-f
#Write a for loop which appends the square of each number to the new list.
print("Exercise 8-f")

lst1=[3, 7, 6, 8, 9, 11, 15, 25]
lst2=[]
#Type your answer here.

for i in lst1:
    lst2.append(i**2)

print(lst2)

################################################
#Exercise 8-g
#Write a for loop using an if statement, that appends each number to the new list if it's positive.
print("Exercise 8-g")
lst1=[111, 32, -9, -45, -17, 9, 85, -10]
lst2=[]
#Type your answer here.

for i in lst1:
    if i>0:
        lst2.append(i)

print(lst2)

################################################
#Exercise 8-h
#Using for loop and if statement, append the value minus 1000 for each key to the new list if the value is
#above 1000. i.e.: if the value is 1500, 500 should be added to the new list.

print("Exercise 8-h")
dict={"z1":900, "t1": 1100, "p1": 2300, "r1": 1050, "k1": 3200, "g1": 400}
lst=[]
#Type your answer here.

for i in dict:
    if dict[i] > 1000:
        lst.append(dict[i]-1000)

print(lst)

################################################
#Exercise 8-i
#Write a for loop which appends the type of each element in the first list to the second list.

print("Exercise 8-i")
lst1=[3.14, 66, "Teddy Bear", True, [], {}]
lst2=[]
#Type your answer here.

for i in lst1:
    lst2.append(type(i))

print(lst2)




