"""
Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui.
"""


lista = []
pares = []
aux=0
count = 0

while aux<10:
	var = int(input("Insira um valor: "))
	lista.append(var)
	aux += 1


for elem in lista:
	if elem%2==0:
		pares.append(elem) 	
		count += 1

print(f"Valores inseridos: {lista}")
print(f"Numero de valores pares: {count}")
print(f"Valores pares: {pares}")
