"""
Faça um programa que receba como entrada o ano corrente e o nome de dois arquivos:
um de entrada e outro de saida. Cada linha do arquivo de entrada contem o nome de
uma pessoa (ocupando 40 caracteres) e o seu ano de nascimento. O programa devera
ler o arquivo de entrada e gerar um arquivo de saide onde aparece o nome da pessoa
seguida por uma string que representa a sua idade.

    - Se a idade for meno do que 18 anos, escreve "menor de idade"
    - Se a idade for maior do que 18 anos, escreva "maior de idade"
    - Se a idade for igual a 18 anos, escreva "entrando na maior idade"
"""
from datetime import date
def str_age(ano):
    today = date.today()

    age = today.year - int(ano)

    if age < 18:
        return 'menor de idade'

    elif age > 18:
        return 'maior de idade'

    return "entrando na maior idade"


with open('ex15_input.txt', 'r') as input:
    with open('ex15_output.txt', 'w') as output:
            input_line = input.readlines()              #read lines of input file

            #write each line on output file
            for line in input_line:
                name = line[0:40]
                ano = line[40:]

                output.write(name)
                output.write(str_age(ano))
                output.write('\n')

