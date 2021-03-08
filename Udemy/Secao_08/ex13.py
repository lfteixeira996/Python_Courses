"""
Faca uma funcao que receba dois valores e um simbolo.
Este simbolo representa a função que se deseja efetuar com os numeros.

+ -> soma
- -> subtracao
/ -> divisao
* -> multiplicação
** -> elevado
"""


def calculadora(val1, val2, operation):
    if operation == '+':
        return val1 + val2
    elif operation == '-':
        return val1 - val2
    elif operation == '/':
        return val1 / val2
    elif operation == '*':
        return val1 * val2
    elif operation == '**':
        return val1 ** val2
    else:
        return "Unknown operation"


in_data = input("Insira a conta no formato <val1 val2 operação>: ")

lista = in_data.split()

out_data = calculadora(int(lista[0]), int(lista[1]), lista[2])

if out_data == "Unknown operation":
    print(out_data)

else:
    print(f"{lista[0]} {lista[2]} {lista[1]} =  {out_data}")
