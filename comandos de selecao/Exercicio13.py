



empresa = float(input("Informe a poluicao da empresa A: "))


if empresa > 0.30 and empresa < 0.40:
    print("SUSPENDER AS OPERACOES! ")
else:
    if empresa >= 0.40 and empresa < 0.50:
        print("Notificacoes ")
    else:
        print("Suspender as atividades! ")
