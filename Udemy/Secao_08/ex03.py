"""
Faça uma funcção para verificar se um numero é positivo ou negativo.
Sendo que o valor de retorn sera 1 se positivo, -1 se negativo e 0 se for igual a 0.
"""


def positivo_ou_negativo(valor):
	
	if valor > 0:
		return 1

	elif valor < 0:
		return -1

	else:
		return 0	
	



val = int(input("Insira um valor: "))

print(f"Analise do numero {val} é {positivo_ou_negativo(val)}")
