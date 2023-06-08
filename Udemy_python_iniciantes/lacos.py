#Laços de repetição, for ou while


print("--------------------------FOR")
for i in range (0,3):
    print(i)
print("----------------------For lista ")
lista = ['item1', 'item2']
for i in lista:
    print("Lista: ", i)

print("++++ for dicionario+++")
diciinario = { 'item1':123 , 'item2': 456}
for i in diciinario:
    print("Dicionario: ", i, diciinario[i])

print("-------------------------While")
i = 0
while i < 3:
    print(i)
    i += 1

print("-------------------------controle de laco, Break")

j = 0
while j < 30:
    if j > 2:
        break
    print(j)
    j += 1

print("-------------------------controle de laco, continua")

k = 0
while k < 3:
    k += 1
    if k == 2:
        print("é o dois ... Pulei")
        continue
    print(k)