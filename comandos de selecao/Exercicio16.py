
sexo = input("Informe o sexo, M e F: ")
altura = float(input("Informe a altura: "))

if sexo == "m":
    total =  (72.7 * altura) - 58
elif sexo == "f":
    total = (62.1 * altura) -44.7
else:
    print("Sexo nao encontrado!")


print("Peso ideal : ", total)