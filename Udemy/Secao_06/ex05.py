"""
Faca um programa que peca ao usuario para digitar 10 valores e some-os.
"""

num = 1
soma = 0

while num <= 10:
	soma += int(input(f"Insira {num} valor:"))
	num += 1

print(f"Soma dos digitos: {soma}")

