

#this function receives a pointer
def print_two(*args):
	arg1, arg2 = args
	print(f"arg1: {arg1}, arg2: {arg2}")


#this function receives two parameters
def print_again(arg1, arg2):
	print(f"arg1: {arg1}, arg2: {arg2}")



#this function receives one parameter
def print_one(arg1):
	print(f"arg1: {arg1}")


#no argument
def print_nothing():
	print("Nothing to print")


print_two("Zed", "Shaw")
print_again("Zed", "Shaw")
print_one("First!")
print_nothing()