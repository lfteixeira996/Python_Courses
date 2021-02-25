"""
Faça um program que leia um valor N inteiro e positivo, calcule e mostre o valor E, confrome a formula:

E = 1 + 1/1! + 1/2! + ... + 1/N!

"""

def factorial(x):

	ret = 1
	count=1

	while count<=x:
		ret *= count 
		count += 1

	return ret



val = int(input("Insira um valor inteiro positivo: "))



