from operator import itemgetter
from itertools import groupby

exemplos = [('Marcos', 28),('Pedro', 19), ('João', 20),('Kleyton',36) ]

exemplos.sort(key=itemgetter(0))
print(exemplos)



#outro exemplo
from collections import defaultdict

# Lista de itens com uma chave
itens = [('A', 1), ('B', 2), ('A', 3), ('B', 4), ('C', 5), ('A', 6)]

# Criar um defaultdict para armazenar os grupos
grupos = defaultdict(list)

# Adicionar os itens aos grupos
for chave, valor in itens:
    grupos[chave].append(valor)

# Exibir os itens agrupados
for chave, grupo in grupos.items():
    print(chave, grupo)
