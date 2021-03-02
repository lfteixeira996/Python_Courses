

#import argv
from sys import argv

#unpack argv
scriptName, fileName = argv

print(f"We will read the file {fileName}")

#open the file
file = open(fileName)


print("Content of the file: ")

print(file.read())

#closes de file
file.close()
