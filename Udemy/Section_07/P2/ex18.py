"""
Faça um programa que permita ao usuario entrar com uma matriz 3x3 de numeros inteiros.
Em, seguida gera um array unidimensional pela soma dos numeros de cada coluna da matriz e mostrar esse array.
"""

n=3
matrix = [[0] * n for i in range(n)]
lista = []
soma = 0

#fill the matrix
for i in range(n):
	for j in range(n):
		aux = int(input(f"Insira o valor [{i}][{j}]: "))
		matrix[i][j] = aux


for j in range(n):
	for i in range(n):
		soma += matrix[i][j]

	lista.append(soma)	
	soma = 0


print(matrix)
print(lista)	