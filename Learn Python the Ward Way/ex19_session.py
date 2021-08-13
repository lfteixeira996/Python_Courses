

def cheese_and_crackers(cheeses, crackers):
	print(f"You have {cheeses} cheeses!")
	print(f"You have {crackers} boxes of crackers!")
	print("Man that's enough for a party!")
	print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variable from our script:")
cheese = 10
box = 50
cheese_and_crackers(cheese, box)

print("We can even do math inside too:")
cheese_and_crackers(20 + 10, 10 + 1)

print("And we can combine the two, variables and math:")
cheese_and_crackers(cheese + 100, box + 1000)






