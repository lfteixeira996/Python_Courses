"""
Criar lista com "A sua intrutora é " + nome, desde que o nome tenha menos de 5 caracteres
"""

nomes = ['Vanessa', 'Ana', 'Maria', 'luis']

print(list(map(lambda nome: f'A sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes))))
