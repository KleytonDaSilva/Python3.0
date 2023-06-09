# if , else e eliff
print("------------------- estrutura")
a =123
if a == 1:
    print("Valor de a é igual a 1")
elif a == 2:
    print("Valor de a é igual a 2")
else:
    print("Valor de a  não é igual a 1 nem 2")


print("------------------- escopo ou bloco")
# bloco ou escopo

c = 1
b = 2

if c == 1:
    d = 3
    #Aqui eu consigo acessar as varaveis: c,b e d
    print(c,b, d)
elif c == 2:
    d = 4
    # Aqui eu consigo acessar as variaveis c,b e d
    print(c, b, d)
else:
    e = 5
    #aqui eu consigo acessar as variaveis a, b e e
    print(a,b,e)

