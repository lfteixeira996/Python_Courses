"""
Faça um program que receba dois numeros e mostre qual deles é o maior
"""


val1_str = input("Insira o primeiro valor: ")
val2_str = input("Insira o segundo valor: ")

#convert values to integers
val1 = int(val1_str)
val2 = int(val2_str)

if val1 > val2:
	print(f"Value {val1} is the biggest!")

else:
	print(f"Value {val2} is the biggest!")
