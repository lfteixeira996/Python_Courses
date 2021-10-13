"""
Leia a nota e o numero de faltas de um aluno, e escreva seu conceito.
De acordo com a tabela abaixo, quando o aluno tem mais de 20 faltas ocorre uma redução de conceito.

	|------------------------------------------------------------
	|	Nota 		|	até 20 faltas	|	acima 20 faltas		|
	|------------------------------------------------------------	
	| 9.0 ate 10.0	|			A 		|		B				|
	| 7.5 ate 8.9	|			B 		|		C 				|
	| 5.0 ate 7.4	|			C 		|		D 				|
	| 4.0 ate 4.9	|			D 		|		E 				|
	| 0.0 ate 3.9	|			E 		|		E 				|
	|------------------------------------------------------------

"""


nota_str = input("Insira a nota: ")
nota = float(nota_str)

faltas_str = input("Insira o numero de faltas: ")
faltas = int(faltas_str)

nota_new = 'A'

if (nota>=9.0) and (nota<=10.0):
	if faltas<=20:
		nota_new = 'A'

	else:
		nota_new = 'B'


elif (nota>=7.5) and (nota<=8.9):
	if faltas<=20:
		nota_new = 'B'

	else:
		nota_new = 'C'


elif (nota>=5.0) and (nota<=7.4):
	if faltas<=20:
		nota_new = 'C'

	else:
		nota_new = 'D'


elif (nota>=4.0) and (nota<=4.9):
	if faltas<=20:
		nota_new = 'D'

	else:
		nota_new = 'E'

else:
	nota_new = 'E'


print(f"De acordo com o numero de faltas a nota é: {nota_new}")