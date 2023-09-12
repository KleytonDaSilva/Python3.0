

inicio = int(input("Informe o inicio do jogo"))
fim = int(input("Informe o fim do jogo: "))

if fim < inicio:
    total = (24 - inicio) + fim
else:
    if fim > inicio:
        total = fim - inicio
    elif fim == inicio:
        total = 24

print(" o total de horas jogadas, foram : ", total)