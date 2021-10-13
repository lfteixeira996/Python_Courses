"""
Faca uma função que receba a data atual e exiba-a na tela no frormato textual por extenso.
"""

dic = {"01": "Janeiro", "02": "Fevereiro", "03": "Março", "04": "Abril", "05": "Maio", "06": "Junho", "07": "Julho", "08": "Agosto", "09": "Setembro", "10":"Outubro","11":"Novembro","12":"Dezembro" }


def print_data(data):

	lista = data.split("/")

	print(f"{lista[0]} de {dic[lista[1]]} de {lista[2]}")


data = input("Insira a data: ")

print_data(data)