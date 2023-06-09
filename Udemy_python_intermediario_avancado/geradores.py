#Geradores
import os

lista = [1, 2, 3, 4]

for i in lista:
    print(i)

print("--------------------")

def soletrar_palavre(palavra):
    for letra in palavra:
        yield letra
for letra in soletrar_palavre("python"):
    print(letra)