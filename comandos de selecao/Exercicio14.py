

print("--------------------------------------------------------")
print("Codigo   |        Descricao                | Preco (R$) ")
print("--------------------------------------------------------")
print("1        | Hamburger                       | 14,50      ")
print("2        | Chessburger                     | 15,50      ")
print("3        | Cachorro Quente                 | 10,00      ")
print("4        | Sanduiche Natural               | 13,50      ")
print("5        | Refrigerante                    |  5,00      ")
print("6        | Suco de Laranja                 |  6,00      ")
print("7        | Milk shake                      | 10,50      ")
print("8        | Sundae                          | 13,00      ")
print("9        | Casquinha                       | 10,00      ")
print("--------------------------------------------------------")

alimento = int(input("Escolha um alimento, 1 a 4: "))

if alimento == 1:
    comida = 14.5
    print("Hamburger : 14,50")
elif alimento == 2:
    comida = 15.5
    print("Chessburger : 15,50")
elif alimento == 3:
    comida = 10
    print("Cachorro Quente : 10,00")
elif alimento == 4:
    comida = 13.5
    print("Sanduiche Natural : 13,50")
else:
    print("Codigo nao existe")

bebida = int(input("Escolha uma bebida, 5 e 6 "))

if bebida == 5:
    tomar = 5.0
    print("Refrigerante  : 5,00")
elif bebida == 6:
    tomar = 6.0
    print("Suco natural : 6,00")
else:
    print("Codigo nao existe")

sobremesa = int(input("Escolha uma Sobremesa, 7 a 9: "))

if sobremesa == 7:
    posComida = 10.5
    print("Milk Shake: 10,50")

elif sobremesa == 8:
    posComida = 13.0
    print("Sundae: 13,00")
elif sobremesa == 9:
    posComida = 10.0
    print("CAasquinha : 10,00")
else:
        print("Codigo nao existe!")

total = comida + tomar + posComida

print("Total a pagar: ", total)