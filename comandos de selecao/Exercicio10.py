


nome = input("Informe o nome do Funcionario: ")
hora_extra = float(input("Informe as Horas Extras: "))
faltas = int(input("Informe numero de faltas: "))


hora = hora_extra - 2/3 * faltas

if hora > 40:
    print(" Grafiticacao de 1000,00")
else:
    if hora < 30 and hora <= 40:
        print(" Grafiticacao de 800,00")
    else:
        if hora < 20 and hora <= 30:
            print(" Grafiticacao de 600,00")
        else:
            if hora < 10 and hora <= 20:
                print(" Grafiticacao de 400,00")
            else:
                print(" Grafiticacao de 200,00")