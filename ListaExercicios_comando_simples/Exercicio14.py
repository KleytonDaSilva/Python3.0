

a = float(input("Informe o valor de A: "))
b = float(input("Informe o valor de B: "))

maiorA = (a + b + abs(a) * (a - b)) / 2
maiorB = (a + b + abs(b) * (a - b)) / 2

print("Valor de A: ", maiorA)
print("Valor de B: ", maiorB)