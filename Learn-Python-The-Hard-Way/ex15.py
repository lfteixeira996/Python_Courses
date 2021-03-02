
#import argv
from sys import argv

#unpack argv
script, filename = argv

#open the file with "filename"
txt = open(filename)

print(f"Here's your file {filename}: ")
print(txt.read())						#at the time that the reading initiates the print prints what is read


print("Type the filename again: ")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())						#at the time that the reading initiates the print prints what is read

txt.close()
txt_again.close()
