"""
Peça ao usuario para digitar tres valores inteiros e imprima a soma deles
"""
import sys

soma = 0

for aux in range(1,4):
	val_str = input(f"Insira o valor {aux}: ")
	soma += int(val_str)

print(f"Soma dos valores: {soma}")