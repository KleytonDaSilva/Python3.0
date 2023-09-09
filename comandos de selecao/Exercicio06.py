


a = float(input("Informe o valor da letra A: "))
b = float(input("Informe o valor da letra B: "))
c = float(input("Informe o valor da letra C: "))

if a > b and a > c:
    if b > c :
        max = a
        med = b
        men = c
    else:
        max = c
        med = a
        men = b
else:
    if b > c:
        max = b
        med = c
        men = a
    else:
        max = c
        med= a
        men = b

opcao = int(input("Escolha opcao de 1 a 3"))

if opcao == 1:
    print(" Ordem crescente ", men, med, max)
elif opcao == 2:
    print(" Ordem decrescente: ", max, med, men)
else:
    print(" Maior valor no meio ", med, max, men)

