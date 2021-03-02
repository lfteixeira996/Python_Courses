
#import argv from sys
from sys import argv

#unpack argv
script, filename = argv
prompt = '?'

print(f"We're going to erase {filename}\nIf you don't want that, hit CTRL-C (^C).\nIf you want do that, hit RETURN.")

input(prompt)

print("Openning the file...")
target = open(filename, 'w')


print("Truncating the file. Goodbye!")
target.truncate()						#Empties the file

print("Now I'm going to ask you for three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")


print("I'm going to write these to the file.")


target.write("{}\n{}\n{}\n".format(line1, line2, line3))

print("And finally, we close it.")
target.close()



