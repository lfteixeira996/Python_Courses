"""
Leia 2 vetores de inteiros x e y, cada um com 5 elementos.
Calcule e mostre os vetores resultantes em cada caso abaixo:

	-	soma entre x e y: soma de cada elemento de x com o correspondente em y
	-	produto entre x e y: multiplicação de cada elemento de x com o correspondente em y
	-	diferença entre x e y: todos os elementos de x que nao existam em y
	-	intersecao entre x e y: apenas os elementos que parecem nos dois vetores
		uniao entre x e y: todos os elementos de x e y (não repetidos)   
"""


# Le 2 vectores de 5 elementos
x = []
y = []
soma = []
mult = []
dif = []

for i in range(1,6):
	aux1 = input(f"Insira o {i} valor para x: ")
	aux2 = input(f"Insira o {i} valor para y: ")

	x.append(int(aux1))
	y.append(int(aux2))


for i in range(0,5):
	soma.append(x[i] + y[i])
	mult.append(x[i] * y[i])


for i in x:
	if i in y:
		break;

	else:
		dif.append(i)	
	




#cria set apartir das listas
setx = set(x)
sety = set(y)
inter = setx.intersection(sety)
uni = setx.union(sety)





print(f"Vetor x: {x}")
print(f"Vetor y: {y}")
print(f"Vetor Soma: {soma}")
print(f"Vetor Produto: {mult}")
print(f"Vetor diferença: {dif}")
print(f"Vetor Interseção: {list(inter)}")
print(f"Vetor União: {list(uni)}")






"""
#vector uniao
out = set1.union(set2)

if bool(out):
	print(f"Vetor Uniao: {out}")

else:
	print("Não há Uniao!!")

"""