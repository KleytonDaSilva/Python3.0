


matricula = int(input("Informe a matricula do aluno: "))
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))

aproveitamento = (nota1 * 5 + nota2 * 2 + nota3 * 3)/ 10


if aproveitamento >= 9.0:
    print("Matricula do aluno: ", matricula)
    print("Primeira nota : " , nota1)
    print("Segunda nota : ", nota2)
    print("Terceira nota : " , nota3)
    print("Media de aproveitamento : ", aproveitamento)
    print(" conceito A")
    print(" Aprovado ")
else:
    if aproveitamento >= 7.5 and aproveitamento < 9.0:
        print("Matricula do aluno: ", matricula)
        print("Primeira nota : ", nota1)
        print("Segunda nota : ", nota2)
        print("Terceira nota : ", nota3)
        print("Media de aproveitamento : ", aproveitamento)
        print(" conceito B")
        print(" Aprovado ")
    else:
        if aproveitamento >= 6.0 and aproveitamento < 7.5:
            print("Matricula do aluno: ", matricula)
            print("Primeira nota : ", nota1)
            print("Segunda nota : ", nota2)
            print("Terceira nota : ", nota3)
            print("Media de aproveitamento : ", aproveitamento)
            print(" conceito C")
            print(" Aprovado ")
        else:
            if aproveitamento >= 4.0  and aproveitamento < 6.0:
                print("Matricula do aluno: ", matricula)
                print("Primeira nota : ", nota1)
                print("Segunda nota : ", nota2)
                print("Terceira nota : ", nota3)
                print("Media de aproveitamento : ", aproveitamento)
                print(" conceito D")
                print(" Reprovado ")
            else:
                print("Matricula do aluno: ", matricula)
                print("Primeira nota : ", nota1)
                print("Segunda nota : ", nota2)
                print("Terceira nota : ", nota3)
                print("Media de aproveitamento : ", aproveitamento)
                print(" conceito E")
                print(" Reprovado ")
