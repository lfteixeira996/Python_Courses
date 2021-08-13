"""
Faça uma função que receba a distancia em Km e a quantidade de litros de gasolina consumidos por um carro em um
percurso, calcule o consumo em km/l e escreva uma uma mensagem de acordo com a tabela:


    |-----------------|-------------------------------|
    |    CONSUMO      |  (Km/l)  |       MENSAGEM     |
    |-----------------|----------|--------------------|
    |    menor que    |     8    |  Venda o carro!    |
    |    entre        |  8 a 12  |  economico         |
    |    maior que    |    12    |  super economico   |
    |-----------------|-------------------------------|

"""


def km_l(km, litros):
    """
    Função
    :param km: kilometros
    :param litros: combustivel consumido
    :return: combustivel consumido por km
    """
    km_litros = km/litros

    if km_litros < 8:
        return "Venda o carro!"

    elif km_litros >= 8 and km_litros <= 12:
        return "Economico!"

    else:
        return "Super Económico!"



km = float(input("Insira o numero de Kms: "))
litros = float(input("Insira o numero de litros: "))

print(f"Retorno da função: {km_l(km, litros)}")
