"""
Recebe do user o nome do ficheiro e devolve o numero de linhas do mesmo
"""

file_name = input("Insira o nome do ficheiro: ")

with open(file_name) as file:
    ret = file.readlines()
    print("Number of lines: ", len(ret))