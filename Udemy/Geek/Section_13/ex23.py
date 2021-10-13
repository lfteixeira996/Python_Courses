"""
Escreva um program que leia a profissao e o tempo de serviço (em anos) de cada um
dos 5 funcionarios de uma empresa e armazene-os no arquivo "emp.txt". Cada linha
do arquivo corresponde aos dados de um funcionario.
"""


with open('emp.txt', 'w') as file:
    for i in range(1, 3):
        name = input("Insira o nome: ")
        anos = input("Insira os anos de servico: ")

        file.write('O ' + name)
        file.write(' ')
        file.write('tem ' + anos + ' de servico\n')