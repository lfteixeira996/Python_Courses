"""
Escreva um program que, dada a idade de um nadador, classifique-o em uma das seguintes categorias:

	|---------------------------|
	|  Categoria  | Idade 		|
	|-------------|-------------|
	| Infantil A  | 5 a 7		|
	| Infantil B  | 8 a 10		|
	| Juvenil A   | 11 a 13		|
	| Juvenil B   | 14 a 17		|
	| Sénior      | > 18		|
	|---------------------------|

"""

age_str = input("Insert the age: ")

age_int = int(age_str)

if age_int >= 5 and age_int <= 7:
	print("Infantil A")


elif age_int >= 8 and age_int <=10:
	print("Infantil B")

elif age_int >= 11 and age_int <=13:
	print("Juvenil A")

elif age_int >= 14 and age_int <=17:
	print("Juvenil B")

else:
	print("Sénior")	


