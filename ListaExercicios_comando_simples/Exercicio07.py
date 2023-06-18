nomeFun =input('Nome do funcionário: ')
hora_trab = float(input('Informe as HOras trabalhadas Mensais: '))
reeb_hora = float(input('Quanto receber por hora: '))
depende = float(input('Quatidade de dependentes: '))

dependentes = depende * 0.10
salario =  (hora_trab * reeb_hora) * dependentes
salario_bruto = hora_trab * reeb_hora + salario
print('salario bruto: ' , salario_bruto)
