



a = int(input("Informe o valor da letra A: "))
b = int(input("Informe o valor da letra B: "))
c = int(input("Informe o valor da letra C: "))

if a > b or a > c:
    maximo = a
elif b > a or b > c:
    maximo = b
else:
    maximo = c

print("Maior entre A, B, C:", maximo)