"""
Faça um programa que leia um numero inteiro positivo par N e imprima todos os numeros pares de 0 ate N em ordem decrescente.
"""


val = 3

while val%2 != 0:

	val= int(input("Insira um numero par: "))


for i in range(val, -1, -2):
	print(f"{i}")	