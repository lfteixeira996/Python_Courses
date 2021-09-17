"""
Recebe do user o nome do ficheiro e devolve o numero de letras vogais
"""

file_name = input("Insira o nome do ficheiro: ")
nb = 0
with open(file_name) as file:
    ret = file.readline()

    for i in ret:
        if i.lower() in ['a', 'e','i','o','u']:
            nb = nb+1

print("Number: ", nb)