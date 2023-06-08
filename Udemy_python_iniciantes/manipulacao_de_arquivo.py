# lendo um arquivo em disco
import os

arquivo = open('nome_do_arquivo.txt','w')
arquivo.write("Informarções do arquivo morto")
arquivo.close()

arquivo = open('nome_do_arquivo.txt', 'r')


# gravando um arquivo em disco

arquivo_gravacao = open("arquivo.txt", "w")
arquivo_gravacao.write("python é legal")
arquivo_gravacao.close()

arquivo = open("arquivo.txt", 'rb')
print(arquivo.read())

print("---------------------------- entendendo um pouco sobre o modulo")

if os.path.exists('nome_arquivo.txt'):
    arquivo = open('nome_arquivo.txt', 'r')
    print (arquivo.read())
    arquivo.close()

else:
    print ('Arquivo não existe')


print("--------------------------- cudir, abspath e join")

print (os.path.curdir)
print (os.path.abspath(os.path.curdir))
print(os.path.join(os.path.abspath((os.path.curdir))), 'nome_aquivo.txt')