
#import packages
from sys import argv
from os.path import exists

#unpack argv
script, from_file, to_file = argv
prompt = '>'

print(f"Copying from {from_file} to {to_file}")

#we could do these two lines in one
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input(prompt)

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()


