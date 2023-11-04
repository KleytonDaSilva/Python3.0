contador = 1
par =0
impar=0

while contador <= 5:
    numero = int(input("Informe o valor do numero: "))

    if numero % 2 ==0:
        print("Numero e par!")
        par+=1
        contador += 1
    else:
        print("Numero e impar!")
        impar+=1
        contador += 1




print("Quantidade de numeros par: ", par)
print("Quantidade de numeros impar: ", impar)