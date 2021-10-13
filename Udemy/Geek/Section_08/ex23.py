"""
Escreva uma funcao que gera um triangulo lateral de altura 2*n-1 e n largura.
Por exemplo, a saida para n=4:

*
**
***
****
***
**
*

"""


def print_tree(n):

    for i in range(1, n+1):
        #print '*'
        print(i*'*')

    for i in range(n-1, 0, -1):
        #print '*'
        print(i*'*')



val = int(input("Insira o numero de layers: "))
print_tree(val)
