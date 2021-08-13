"""
Faça um program que leia 2 vetores de 5 elementos. 
Crie um vetor que seja a união entre os 2 vetores anteriores, ou seja,
que contem os numeros de ambos os vetores. Nao deve conter numeros repetidos.
"""


# Le 2 vectores de 5 elementos
lista1 = []
lista2 = []

for i in range(1,6):
	aux1 = input(f"Insira o {i} valor para vetor1: ")
	aux2 = input(f"Insira o {i} valor para vetor2: ")

	lista1.append(int(aux1))
	lista2.append(int(aux2))



#cria set apartir das listas
set1 = set(lista1)
set2 = set(lista2)

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")

#vector uniao
out = set1.union(set2)

if bool(out):
	print(f"Vetor Uniao: {out}")

else:
	print("Não há Uniao!!")

