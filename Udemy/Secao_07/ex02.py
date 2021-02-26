"""
crie um programa que lê 6 inteiros e de seguida imprime no ecra
"""


lista = []
i=0

while i<6:
	val = int(input("Insira um valor: "))
	lista.append(val)
	i +=1


print(f"Valores inseridos: {lista}")
