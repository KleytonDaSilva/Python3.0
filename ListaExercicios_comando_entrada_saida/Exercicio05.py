nome = input("Informe NOme do Aluno: ")
matematica = float(input("Informe a nota de Matematica: "))
portugues = float(input("Informe a nota de Português: "))
conhecimento = float(input("Informe a nota de Conhecimento Gerais: "))

media = (matematica + portugues + conhecimento) / 3

print("Aluno : ", nome)
print("Nota de Matemática: ", matematica)
print("Nota de Português : ", portugues)
print("Nota de Conhecimento Gerais: ", conhecimento)
print("Média do Aluno: ", media)