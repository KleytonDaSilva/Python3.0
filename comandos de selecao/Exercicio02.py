

a = int(input("Informe o valor da letra A"))
b = int(input("Informe o valor da letra B"))
c = int(input("Informe o valor da letra C"))

if a > b:
    if a> c:
        max = a
    else:
        max = c
else:
    if b > c:
       max = b
    else:
        max = c


print("Maior entre  a , b , c " , max)