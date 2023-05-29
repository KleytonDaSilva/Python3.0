

nomeFunc = input("Informe o nome do funcionario: ")
horasTraba = float(input("Informe as horas trabalhadas mensais: "))
valorHoras = float(input("Valor por hora trabalhada : "))
dependentes = float(input("Número de dependentes: "))

salario = horasTraba * valorHoras
salarioBru = salario + (dependentes *(salario * 0.1))

print("Salario Bruto: ", salarioBru)