

funcionario = input("Informe o nome do funcionario ")
salario = float(input("Informe o salario atual: "))

if salario <= 400.0:
    novo_salario = salario * 0.15 + salario
else:
    if salario > 400.0 and salario <= 700.0:
        novo_salario = salario * 0.12 + salario
    else:
        if salario > 700.0 and salario <= 1000.0:
            novo_salario = salario * 0.10 + salario
        else:
            if salario > 1000.0 and salario <= 1500.0:
                novo_salario = salario * 0.07 + salario
            else:
                if salario > 1500.0 and salario <= 2000.0:
                    novo_salario = salario * 0.04 + salario
                else:
                    print("Sem aumento no salario!")


print("Salario atual: ", novo_salario)