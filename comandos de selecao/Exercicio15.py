

print("Menu:")
print("1. Opção T")
print("2. Opção Q")
print("3. Opção R")

escolha = input("Escolha uma opção: ")

if escolha == "t":
    print("Você escolheu a Opção T, Area de um triangulo.")
    b = float(input("Informe a Base: "))
    a = float(input("Informe a Altura: "))
    area = (b * a)/ 2
    print("Area do triangulo: ", area)

elif escolha =="q":

    print("Você escolheu a Opção Q, Area de um quadrado.")
    l = float(input("Informe o Lado: "))
    area = l * l
    print("Area do triangulo: ", area)
elif escolha == "r":

    print("Você escolheu a Opção R, Area de um retangulo.")
    b = float(input("Informe a Base: "))
    a = float(input("Informe a Altura: "))
    area = b * a
    print("Area do triangulo: ", area)
else:
    print("Opcao invalida!!!")