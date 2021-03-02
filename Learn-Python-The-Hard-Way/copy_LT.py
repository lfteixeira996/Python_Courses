
#copy the content from file in_file.txt to out_file.txt

#import argv
from sys import argv

#unpack argv
script, file_in, file_out = argv

#open file_in 
in_file = open(file_in, 'r')

out_file = open(file_out, 'w')


#copy from one to another
out_file.write(in_file.read())

print("Copy finished!")

#close files
in_file.close()
out_file.close()

