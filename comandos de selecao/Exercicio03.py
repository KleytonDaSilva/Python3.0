


a = float(input("Informe o valor da letra A: "))
b = float(input("Informe o valor da letra B: "))
c = float(input("Informe o valor da letra C: "))

if a > b:
    if a > c:
        max = a
        media1= b
        media2 = c
    else:
        max = c
        media1= b
        media2 = a
else:
    if b > c:
        max = b
        media1= a
        media2 = c
    else:
        max = c
        media1= b
        media2 = a

media_ponderada = (max * 5 + media1 * 2.5  + media2 * 2.5) / 10

print("Maior nota: ", max)
print("Media ponderada: ", media_ponderada)