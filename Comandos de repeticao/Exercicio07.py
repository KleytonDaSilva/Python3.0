contador = 0
contador_mulher = 0
total = 0
total_home = 0
while contador < 5:

    sexo = input("Imforme sexo: ")

    if sexo == "f" or sexo =="F":
        altura = float(input("Informe a altura: "))
        total = altura + total
        contador_mulher+=1
        contador +=1
    else:
        altura_home = float(input("Informe a altura:"))
        total_home = altura_home + total
        contador+=1


print("Media da altura das mulheres: ", total / contador_mulher)
print("Media de altura da turma " ,  total + total_home / contador)