"""
Leia uma matrx 4x4, conte e escreve quantos valores maiores que 10 ela possui.
"""



n = 4
matrix = [[0] * n for i in range(n)]
count = 0
lista = []


#matrix com valores do user
for i in range(n):
    for j in range(n):
    	aux = int(input(f"Insira o valor [{i}][{j}]: "))
    	matrix[i][j] = aux


#procura valores maiores de 10
for i in range(n):
    for j in range(n):
    	if matrix[i][j] > 10:
    		lista.append(matrix[i][j])
    		count += 1


#print valores
print(f"Matrix: {matrix}")
print(f"Lista de valores maiores que 10: {lista}")
print(f"Numero de valores maiores que 10: {count}")


"""
#print
print(f"Matrix: {matrix}")
print(f"Numero de valores maiores que 10: {count}")
print(f"Lista de valores maiores que 10: {lista}")
"""