"""
Faca uma funcao chamada DesenhaLinha.
Ele deve desenhar uma linha na tela usando varios simbolos de igual "===".
A funcao recebe por parametro quantos sinais de igual serao mostrados.
"""

def DesenhaLinha(numero, simbolo="="):
    print(simbolo*numero)



numero = int(input("Insira o numero de caracteres e simbolo(opcional): "))

DesenhaLinha(numero)


