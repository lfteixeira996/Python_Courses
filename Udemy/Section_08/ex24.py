"""
Escreva uma funcao que gera um triangulo de altiura e lados n e base 2*n-1.
Por exemplo, a saida para n=6:

                            *
                           ***
                          *****
                         *******
                        *********
                       ***********
"""


def print_tree(n):
    # number of spaces
    k = n - 1
    aux = 1
    # outer loop to handle number of rows
    for i in range(0, n):

        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")

        # decrementing k after each loop
        k = k - 1

        #print '*'
        print((i+aux)*'*', end=" ")
        aux +=1

        # ending line after each row
        print("\r")


val = int(input("Insira o numero de layers: "))
print_tree(val)
