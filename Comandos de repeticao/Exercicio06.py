alunos = 1
contador_maior =0
contador_menor =0
while alunos <=5:

    nome = input("Informe o Nome do aluno: ")
    idade =int(input("Informe a idade do aluno: "))

    if idade >= 18:
        print("Aluno : ", nome)
        print("Idade : ", idade)
        contador_maior +=1
        alunos += 1
    else:
        print("Menor de idade")
        contador_menor+=1
        alunos += 1


print("Quantidades de alunos maiores de 18 " , contador_maior)
print("Quantidade de alunos menores de 18 " , contador_menor)