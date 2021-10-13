"""
Faça um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos juntamente com o  maior, menor e media dos valores.
"""

lista = []
aux=0

#le valores e preenche a lista
while aux<5:
	var = int(input("Insira um valor: "))
	lista.append(var)
	aux += 1

#ordena a lista
lista.sort()

#sabendo que a lista esta ordenada, sabemos que o primeiro elemento é o minimo e o ultimo o maximo
minimo = lista[0]
maximo = lista[len(lista)-1] 
media = 0

for elem in lista:
	media += elem	


media = media/len(lista)

print(f"Valores inseridos: {lista}")
print(f"Valor Minimo: {minimo}")
print(f"Valor Maximo: {maximo}")
print(f"Media: {media}")
