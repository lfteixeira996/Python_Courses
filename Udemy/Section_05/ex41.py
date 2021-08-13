"""
Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação de acordo com a tabela abaixo:

	|-----------------------------------------------|
	|	IMC			|	classificação 				|
	|-----------------------------------------------|
	| 	<18.5		|	Abaixo do peso 				|
	|	18.6 - 24.9	|	Saudável					|
	|	25 - 29.9	|	Peso em excesso				|
	|	30 - 34.9	|	Obsidade Grau I 			|
	|	35 - 39.9	|	Obsidade Grau II (severa)	|
	|	>= 40		|	Obsidade Grau III (mórbida)	|
	|-----------------------------------------------|

"""

weight_str = input("Insert your weight: ") 
weight_val = float(weight_str)

height_str = input("Insert your height: ") 
height_val = float(height_str)


#IMC Calculation
IMC = weight_val/(height_val**2)



if IMC <  18.5:
 	print("Abaixo do peso")

elif IMC >= 18.6 and IMC <= 24.9:
 	print("Saudável")

elif IMC >= 25 and IMC <= 29.9:
 	print("Peso em excesso")

elif IMC >= 30 and IMC <= 34.9:
 	print("Obsidade Grau I")

elif IMC >= 35 and IMC <= 39.9:
 	print("Obsidade Grau II")

else:
	print("Obsidade Grau III")
 	







  	