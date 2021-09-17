"""
Faça um program no qual o usuario informa o nome do arquivo e uma palavra, e retorne
o numero de vezes que aquela palavra aparece no arquivo.
"""

palavra = input("Insira a palavra a procurar: ")

with open('poema.txt', 'r') as file:
    lines = file.readlines()
    count = 0

    for line in lines:
        if palavra in line.lower():
            count = count + 1

print("Palavra: " + palavra + " apareçe " + str(count) + " vezes!")