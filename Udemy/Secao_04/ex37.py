"""
Faça um prgrama que leia o valor de um produto e imprima o valor com desconto, tendo em vista que o k desconto foi de 12%
"""


valor_str = input("Insira o valor do produto: ")

desconto = 12/100 #12%

valor_desconto = int(valor_str) - int(valor_str)*desconto

print(f"Valor do produto: {valor_str}")
print(f"Desconto aplicado: 12%")
print(f"Valor com desconto: {valor_desconto}")