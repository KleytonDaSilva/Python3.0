# Funções

print("------------------------ Exemplo de Funções ")

def mostrar_nome_na_tela(nome): # toda função tem DEF, nome da funcção, e nome dos parametros
    print(nome)
    return True

mostrar_nome_na_tela("Kleyton")

print("------------------------ multiplos parâmetros")
def mostrar_nome_e_sobrenome( nome, sobrenome): # nome e sobrenome, mais de um parâmetro

    print(nome, sobrenome)
    return True


mostrar_nome_e_sobrenome("Kleyton", "da Silva")

print("------------------------ multiplos retornos")

def nome_completo_usuario(codigo):
    if codigo == 10:
        return "Kleyton", "da Silva"

nome1, sobrenome1 = nome_completo_usuario(10)
print(nome1, sobrenome1)


print("------------------------ Função recursiva")
# Função recursiva é uma função que chama ela mesma repetidas vezes

def soma_dez(valor1):
    if valor1 < 100:
        return soma_dez(valor1 + 10)
    return valor1

print(soma_dez(1))

