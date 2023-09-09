


a = float(input("Informe o valor da letra A: "))
b = float(input("Informe o valor da letra B: "))
c = float(input("Informe o valor da letra C: "))

raiz = b * b - 4 * a * c

if raiz >= 0:
    print(" Valor da Raiz: ", raiz)
else:
    print("Nenhum raiz encontrada")
