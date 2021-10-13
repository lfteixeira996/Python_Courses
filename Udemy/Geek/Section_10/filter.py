"""
Example how to use Filter()
"""

import statistics

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Valores = {valores}")

#calcula media
media = statistics.mean(valores)
print(f"Media = {media}")

#Filtar valores superiores á media
res = filter(lambda valor: valor>media, valores)

print(f"Valores filtrados = {list(res)}")
