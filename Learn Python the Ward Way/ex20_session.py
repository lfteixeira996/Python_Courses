
from sys import argv

script, file = argv

#print the whole file
def print_lines(filename):
	print(filename.read())


#print one line
def print_one_line(filename):
	print(filename.readline())





#open file and call print_lines
filename = open(file)
#print_lines(filename)

print_one_line(filename)
filename.seek(2)
print_one_line(filename)
