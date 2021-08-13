

def add(a,b):
	print(f"ADDING {a} + {b}")
	return a + b


def sub(a,b):
	print(f"SUBTRACTING {a} - {b}")
	return a - b


def mult(a,b):
	print(f"MULTIPLYING {a} * {b}")
	return a * b


def div(a,b):
	print(f"DIVIDING {a} / {b}")
	return a / b

print("Let's do some math with just functions!")
print(f"Age: {add(30,5)}, Height: {sub(78,4)}, Weight: {mult(90,2)}, IQ: {div(100,2)}")

print("Here is a puzzle.")

val1 = div(50.0,2)
val2 = mult(180, val1)
val3 = sub(74, val2)
val4 = add(35, val3)

print(f"That becomes: {val4} Can you do it by hand?")