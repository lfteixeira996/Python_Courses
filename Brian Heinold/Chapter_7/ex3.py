"""
Write a program that creates the list L = [1,2,3,4,5].
    (a) Attempt to make a copy of the list by using copy= L. Then set the first item in L to 999, and print out copy.
    (b) Set L back to [1,2,3,4,5], make a proper copy of L, set the first item in L to 9, and print out copy.
"""
# a
L = [1, 2, 3, 4, 5]

copy = L
L[0] = 999

print(copy)

# b
L = [1, 2, 3, 4, 5]
copy = []

for i in L:
    copy.append(i)

print(copy)

