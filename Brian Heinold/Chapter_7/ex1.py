"""
Write a program that asks the user to enter a list of at least five integers. Do the following:
(a) Print out the total number of items in the list.
(b) Print out the fourth item (index 3) in the list.
(c) Print out the last three items in the list.
(d) Print out all the items in the list except the first two.
(e) Print out the list in reverse order.
(f) Print out the largest and smallest values in the list.
(g) Print out the sum of all the values in the list.
(h) If the list contains a zero, print out the index of the first zero in the list, and otherwise print out
a message saying there are no zeroes.
(i) Sort the list and print out the list after sorting.
(j) Delete the first item from the (now sorted) list and print out the new list.
(k) Change the second-to-last item in the list to 9876 and print out the new list.
(l) Append the value -500 to the end of the list and print out the new list.
"""

n = eval(input("Insert the number of elements: "))
lst = []

for i in range(n):
    val = eval(input("Element: "))
    lst.append(val)

# a
print("Print out the total number of items in the list: ", n)

# b
print("Print out the fourth item (index 3) in the list: ", lst[3])

# c
print("Print out the last three items in the list: ", lst[n-3:])

# d
print("Print out all the items in the list except the first two: ", lst[2:])

# e
print("Print out the list in reverse order: ", lst[::-1])

# f
print("Print out the largest and smallest values in the list: ", max(lst), min(lst))

# g
print("Print out the sum of all the values in the list: ", sum(lst))

# h
print("If the list contains a zero, print out the index of the first zero in the list, and otherwise print out a message saying there are no zeroes.")
if 0 in lst:
    print("Index: ", lst.index(0))

else:
    print("There are no zeros!!")

# i
print("Sort the list and print out the list after sorting: ", lst.sort())

# j
lst.pop(0)
print("Delete the first item from the (now sorted) list and print out the new list: ", lst)

# k
lst[n-2] = 9876
print("Change the second-to-last item in the list to 9876 and print out the new list: ",lst)

# l
lst.append(-500)
print("Append the value -500 to the end of the list and print out the new list:", lst)