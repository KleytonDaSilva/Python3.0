


print("Categoria  |   % de aumento sobre salario atual")
print("-----------------------------------------------")
print("A,C,F,H    |              10                   ")
print("B,D,E,G    |              15                   ")
print("I,K ate R  |              20                   ")
print("J,S ate Z  |              25                   ")
print("-----------------------------------------------")

nome = input("Informe o nome do funcionario: ")
salario =  float(input("Informe o salario do funcionario: "))
categoria = input("Informe a categoria do funcionario: ")

if categoria == "a" or categoria == "c" or categoria == "f" or categoria == "h":
    salario = salario * 0.10 + salario
    print("Funcionario: ", nome)
    print("Salario atual :", salario )
    print("Categoria: " , categoria)
elif categoria == "b" or categoria == "d" or categoria == "e" or categoria == "g":
    salario = salario * 0.15 + salario
    print("Funcionario: ", nome)
    print("Salario atual :", salario )
    print("Categoria: " , categoria)
elif categoria == "i" or categoria == "k" or categoria == "m" or categoria == "r":
    salario = salario * 0.20 + salario
    print("Funcionario: ", nome)
    print("Salario atual :", salario)
    print("Categoria: ", categoria)
elif categoria == "j" or categoria == "s" or categoria == "v" or categoria == "z":
    salario = salario * 0.25 + salario
    print("Funcionario: ", nome)
    print("Salario atual :", salario )
    print("Categoria: " , categoria)
else:
    print("Codigo invalido!")