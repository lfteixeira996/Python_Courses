"""
Leia um valor de area em hectares e apresente-o convertido em metros quadrados.
A formula de conversao é: M = H*10000, sendo M a area em metros quadrados e H a area em hectares.
"""


area_str = input("Insira a area H: ")

area_H = float(area_str)

#conversion
area_M= area_H*10000

print(f"{area_H} hectares corresponde a {area_M} metros quadrados")
