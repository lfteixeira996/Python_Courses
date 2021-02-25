"""
Leia a temperatura em graus F e apresente-a convertida em graus C.
A formula de conversao é: C = 5.0*(F-32.0)/9.0, sendo C a temperatura em Celsius e F a temperatura em Fahrnheit.
"""


temp_str = input("Insira a temperatura em Fahrnheit: ")

temp_F = float(temp_str)

#conversion
temp_C = 5.0*(temp_F-32.0)/9.0

print(f"{temp_F} Fahrnheit corresponde a {temp_C} Celsius")
