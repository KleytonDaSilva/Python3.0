print("______________________________________")
print(" Imposto de renda 15%                 ")
print(" INSS 5%                              ")
print(" Abono 60% em cima do salario minimo  ")
print("______________________________________")


salarioMinimo = float(input( "Informe o Salario minimo do seu País: "))
salario =  float(input("Informe o salario Bruto: "))

imposto = salario * 0.15
print("Desconto do imposto de renda: ", imposto)
inss = salario * 0.05
print("Desconto do INSS: ", inss)
abono = salarioMinimo * 0.60
print("Desconto do acrescimo do abono: ", abono)

print("Salario liquido : ", (salario - imposto - inss) + abono)
