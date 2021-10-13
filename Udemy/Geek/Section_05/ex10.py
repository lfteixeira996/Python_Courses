"""
Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,utilizando as seguintes formulas:

Homens: (72.7*h) - 58
Mulheres: (62.1*h) - 44.7
"""
import readchar


h_str = input("Insert the heigh: ")

print("Insert the gender M(men) or W(woman):  ")
s = readchar.readchar()

h_val = float(h_str)



if s == 'W':
	Peso_ideal = (62.1*h_val)-44.7
	print(f"Output: {Peso_ideal}")

elif s=="M":
	Peso_ideal = (72.7*h_val)-58
	print(f"Output: {Peso_ideal.2}")

else:
	print("Invalid gender inserted! Exit!")