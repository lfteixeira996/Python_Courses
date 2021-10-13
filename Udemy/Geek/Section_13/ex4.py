"""
Recebe do user o nome do ficheiro e devolve o numero de letras vogais e o numero de consoantes
"""

file_name = input("Insira o nome do ficheiro: ")
nv = 0
nc = 0
with open(file_name) as file:
    ret = file.readline()

    for i in ret:
        if i.lower() in ['a', 'e','i','o','u']:
            nv = nv+1
        else:
            nc = nc+1

print("Number vogais: ", nv)
print("Number consoantes: ", nc)
