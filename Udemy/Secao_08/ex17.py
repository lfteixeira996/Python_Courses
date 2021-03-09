"""
Faca um funcao que recebe dois valores inteiros positivos e retorne a soma dos N numeros inteiros existentes entre eles.
"""

def soma(a, b):
    soma = 0
    for i in range(a, b+1):
        soma += i

    return soma


#Read values
str = input("Insira dois valores: ")
str = str.split()

print(f"soma dos valores de {str[0]} a {str[1]} = {soma(int(str[0]), int(str[1]))}")
