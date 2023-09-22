

print(" Codigo |_______________________________| preco unitario")
print(" 100    |_______________________________| 13,00         ")
print(" 101    |_______________________________| 12,50         ")
print(" 102    |_______________________________| 12,00         ")
print(" 103    |_______________________________| 12,25         ")
print(" -------------------------------------------------------")


quantidade_item = int(input("Informe a quantidade de lanches: "))
codigo = int(input("Informe o codigo do lanche: "))

if quantidade_item == 5 and codigo == 100:
    total = 13 * 4
    print("Promocao! compre 5 e pague 4!")
    print("Total: ", total)
elif quantidade_item == 5 and codigo == 101:
    total = 12.5 * 4
    print("Promocao! compre 5 e pague 4!")
    print("Total: ", total)
elif quantidade_item == 5 and codigo == 102:
    total = 12 * 4
    print("Promocao! compre 5 e pague 4!")
    print("Total: ", total)
elif quantidade_item == 5 and codigo == 103:
    total = 12.25 * 4
    print("Promocao! compre 5 e pague 4!")
    print("Total: ", total)

else:
    print("Codigo errado!")


