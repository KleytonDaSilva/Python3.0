# ordenamento

lista = [10.5,11,3,20,18]


print(sorted(lista))  # Ordena a lista em ordem crescente

tupla = ['python', 'java', 'Go']

print(sorted(tupla))  # Ordena a tupla em ordem alfabética

dicionario = {1: 'b', 2: 'a', 3: 'c'}

print(sorted(dicionario))  # Ordena as chaves do dicionário em ordem crescente



class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return self.nome
def pelo_nome(pessoa):
        return pessoa.nome
def pelo_idade(pessoa):
    return pessoa.idade

p1 = Pessoa('Marco', 28)
p2 = Pessoa('Gabriel', 30)
p3 = Pessoa('Ana', 25)

pessoas = [p1,p2,p3]


print(sorted(pessoas, key=pelo_nome))  # Ordena a lista de pessoas pelo nome
print(sorted(pessoas, key=pelo_idade))  # Ordena a lista de pessoas pela idade
print(sorted(pessoas, key=pelo_idade, reverse=True))  # Ordena a lista de pessoas pela idade em ordem decrescente