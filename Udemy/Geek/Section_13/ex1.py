"""
Escreve um program que:
    a) Crie/abra um arquivo texto de nome "arq.txt"
    b) Permita que o usuario grave diversos caracteres nesse arquivo, ate que o usuario insira '0'
    c) feche o arquivo
"""


with open('arq.txt', 'w') as file:
    while True:
        ch = input("Insira o char: ")

        if ch != '0':
            file.write(ch)
        else:
            break


