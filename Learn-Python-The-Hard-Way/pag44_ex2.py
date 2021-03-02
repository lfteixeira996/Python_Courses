

from sys import argv

#read one value from argv
name, read_value = argv


#read values until number of values reach the one from argv
for x in range(int(read_value)):
	
	to_print = input("Insert the value: ")

	print("Inserted value: ", to_print)


