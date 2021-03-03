"""
Declare uma matrix 5x5.
Preencha com 1 a diagonal e com 0 os restantes elementos.
"""



n = 5
matrix = [[0] * n for i in range(n)]

#Insere 1 na diagonal
for i in range(n):
    for j in range(n):
    	if i==j:
    		matrix[i][j] = 1
    		break


#print valores
print(f"Matrix: {matrix}")

