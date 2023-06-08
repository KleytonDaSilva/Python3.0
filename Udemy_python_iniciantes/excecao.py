# execeções
l =[1,2,3]

try:
    print(l[12])
except:
    print("Erro ao acessar a lista")

print("---------------------------- outra forma")

k =[1,3,4]
outra = None
try:
    print(k[12])
except IndexError:
    print("Erro ao acessar a lista")

print("--------------------------Finally")
j = [1,3,4]

try:
    print(j[12])
except IndexError as e:
    print("Ocorreu um erro: ", e)
finally:
    print("Liberando recurso finais")