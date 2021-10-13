"""
Crie uma função que receba como parametro um valor inteiro e gere como saida n linhas com pontos de exclamação, 
conforme o exemplo abaixo (n=5):

!
!!
!!!
!!!!
!!!!!

"""



def print_linhas(n):

	for i in range(1, n+1):
		print(i*"!")



print_linhas(10)