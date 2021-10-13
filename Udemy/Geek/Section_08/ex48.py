"""
Faça uma funcao que recebe uma matriz 3x3 elementos.
Calcule a soma dos elementos que estao acima da diagonal principal.
"""


def special_soma(lista, cont_diag=False):
    """
    Função soma
    :param lista:
    :return: soma dos elementos a cima da diagonal principal
    """
    soma = 0
    linha = 0
    coluna = 0

    for row in lista:
        for column in row:

            if coluna > linha and not cont_diag:
                soma += column


            elif coluna >= linha and cont_diag:
                soma += column

            coluna += 1

        linha += 1
        coluna = 0

    return soma


# generate 3x3 matrix
matrix = [[valor for valor in range(1, 4)] for i in range(3)]
print(f"Matrix: {matrix}")

#call function without diagonal
print(f"Soma sem diagonal: {special_soma(matrix)}")

#call function counting diagonal
print(f"Soma com diagonal: {special_soma(matrix, True)}")

