import itertools

lista = [1,2,3]
lista2 =[4,5,6]

comb = itertools.chain(lista, lista2)

print(list(comb))

#Juntar duas listas