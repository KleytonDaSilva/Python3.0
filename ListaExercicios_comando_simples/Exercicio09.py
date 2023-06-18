

aluno = input('Nome do Aluno: ')
nota1 = float(input("Primeira nota: "))
nota2 = float(input('Segunda nota:'))
nota3 = float(input('Terceira nota:'))
peso1= float(input('Peso 1'))
peso2= float(input('Peso 2'))
peso3= float(input('Peso 3'))

media = ((peso1*nota1)+ (peso2*nota2) + (peso3*nota3))
pesos = peso1 + peso2 + peso3
media_geral = media / pesos
print("Aluno: ", aluno)
print('Média: ', media)