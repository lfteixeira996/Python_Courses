"""
Faca um program que receba 6 numeros inteiros e mostre:

	- os numeros pares digitados
	- a soma dos numeros pares digitados
	- os numeros impares digitados
	- a quantidade de numeros impares digitados
"""

lista = []
lista_pares = []
lista_impares = []
i=1
soma_pares = 0
count_impares = 0


#le valores e preenche a lista
while i<=6:
	aux = int(input(f"Insira o {i} numero: "))
	lista.append(aux)
	i += 1

for elem in lista:
	if elem%2==0:
		lista_pares.append(elem)
		soma_pares += elem


	else:
		lista_impares.append(elem)
		count_impares += 1	


print(f"Valores inseridos: {lista}")
print(f"Valores pares inseridos: {lista_pares}")
print(f"Soma valores pares inseridos: {soma_pares}")
print(f"Valores impares inseridos: {lista_impares}")
print(f"Numero de valores impares digitados: {count_impares}")




