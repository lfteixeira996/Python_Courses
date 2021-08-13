"""
Faça um programa para converter uma letra maiúscula em letra minúscula. 
Use a tabela ASCII para resolver  problema.
"""
import readchar

print("Insira um caracter maiúsculo: ")
ch_M = readchar.readchar()


#Metodo Pedido
#Conversão
#ch_m = chr(ord(ch_M)+32)


#Metodo Alternativo
ch_m = ch_M.lower()


print(f"Caracter inserido: {ch_M} (Maiúscula)")
print(f"Caracter convertido: {ch_m} (Minúscula)")