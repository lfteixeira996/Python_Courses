"""
Faça um programa que receba dois arquivos do usuario, e crie um terceiro arquivo com
o conteudo dos dois primeiros juntos (o conteudo do primeiro seguido do conteudo do
segundo.
"""

with open('poema.txt', 'r') as file1:
    with open('poema2.txt', 'r') as file2:
        with open('ex9_output.txt', 'w') as file3:
            file3.write(file1.read())
            file3.write(file2.read())