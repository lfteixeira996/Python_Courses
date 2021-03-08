"""
Faça uma função que recebe, 2 vetores de 10 elementos inteiros e que
calcule e retorne o vetor união dos dois primeiros
"""
import random

def uniao(list1, list2):
    return list1.union(list2)


vetor1 = []
vetor2 = []
n = 10

for i in range(0,n):
    vetor1.append(random.randint(0,100))
    vetor2.append(random.randint(0, 100))

print(vetor1)
print(vetor2)


print(list(uniao(set(vetor1), set(vetor2))))