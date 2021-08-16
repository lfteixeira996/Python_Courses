#https://holypython.com/intermediate-python-exercises/exercise-9-python-while-loop/

################################################
#Exercise 9-a
#Write a while loop that adds all the numbers up to 100 (inclusive).

print("Exercise 9-a")
counter = 0
total = 0

# Construct your while loop here.
while counter < 101:
    total += counter

    counter += 1

print(total)

################################################
#Exercise 9-b
#Using while loop, if statement and str() function;
#iterate through the list and if there is a 100, print it with its index number. i.e.:
#"There is a 100 at index no: 5"
print("Exercise 9-b")
lst = [10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
# Type your code here.

i = 0
while i < len(lst):
    if lst[i] == 100:
        print("There is a 100 at index no: " + str(i))

    i += 1

################################################
#Exercise 9-c
#Using while loop and an if statement write a function named name_adder which appends
#all the elements in a list to a new list unless the element is an empty string: "".

print("Exercise 9-c")
lst1 = ["Joe", "Sarah", "Mike", "Jess", "", "Matt", "", "Greg"]

# Type your code here.
def name_adder(list):
    ret = []
    i = 0

    while i < len(lst1):
        if lst1[i] != "":
            ret.append(lst1[i])

        print(lst1[i])
        i += 1

    return ret


print(name_adder(lst1))

################################################
#Exercise 9-d
#This time inside a function named name_adder, write a while loop that stops appending
#items to the new list as soon as it encounters an empty string: "".
#And prints "There is an empty string and returns the new list."
print("Exercise 9-d")


lst1=["Sam", "", "Ben", "Olivia", "Alicia"]
i=0
def name_adder(list):
    i = 0
    new_list = []
    while i < len(list):
        if list[i] != "":
            new_list.append(list[i])
        else:
            break
        i = i+1
    return new_list

print(name_adder(lst1))