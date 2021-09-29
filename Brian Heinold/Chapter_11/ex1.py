"""
Create a dictionary whose keys are the strings 'abc', 'def', 'ghi', 'jkl', and 'mno' and whose
corresponding values are 7, 11, 13, 17, and 19. Then write dictionary code that does the following:

(a) Print the value in the dictionary associated with the key 'def'.
(b) Use the keys() method to print out all the keys.
(c) Loop over the dictionary and print out all the keys and their associated values.
(d) Use an if statement to check if the dictionary contains the key 'pqr' and print out an appropriate
message indicating whether it does or doesn’t.
(e) Change the value associated with the key 'abc' to 23 and then print out all the values in the
dictionary using the values() method.

"""

#create dictionary
dict = {
    'abc': 7,
    'def': 11,
    'ghi': 13,
    'jkl': 17,
    'mno': 19
}

# alinea a
print(f"key 'def' = ", dict['def'])

# alinea b
print(f"All keys: ", dict.keys())

# alinea c
for i in dict.keys():
    print(f"Key = {i} and value = {dict[i]}")

# alinea d
if 'pqr' in dict.keys():
    print("The key exists!")

else:
    print("The key doesn't exist!")

# alinea e
dict["abc"] = 23
for i in dict.values():
    print(i)