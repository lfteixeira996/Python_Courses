"""
Faca uma funcao que receba uma matrix 4x4 e retorne quantos valores maiores do que 10 ela possui.
"""

def maior_10(vetor):

    count = 0

    for linha in vetor:
        for elem in linha:
            if elem > 10:
                count += 1

    return count



#generate matrix
lista = [1, 2, 3, 4]
matrix = [[val*3 for val in lista] for i in range(4)]

#print output values
print(matrix)
print(f"Numero de valores maiores que 10: {maior_10(vetor=matrix)}")