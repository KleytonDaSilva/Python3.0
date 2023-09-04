salarioBruto = float(input("Informe o salario Bruto do Funcionario"))

previdencia =  salarioBruto * 0.1

alimentacao = salarioBruto * 0.3

salarioBruto =  salarioBruto - previdencia - alimentacao


print("Desconto da Previdencia Social:", previdencia)
print("Desconto com vale Alimentacao:", alimentacao)
print("Salario liquido do funcionario:", salarioBruto)

