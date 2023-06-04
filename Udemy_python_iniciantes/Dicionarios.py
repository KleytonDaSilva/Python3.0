#dicionarios

dicionario = {}
dicionario['item'] = 'conteudo' #indice e uma string
dicionario[0] = 'outro conteudo' #indice e um inteiro

print(dicionario)

# manipulando USANDO LEN E KEYS

print(dicionario.keys()) #indices do dicionario
print(len(dicionario)) #tamanho do conteudo


#Martriz esparsas

matriz_lista = [[0,0,2],[0,4,5],[0,0,0]]

#usando dicionario
matriz_dicionario = {(0,2): 2, (1,1): 4, (1,2): 5} #(0,2) posição X e Posição Y : 2 valor naquela posição XY
print(matriz_dicionario[0,2])


#Pratica

dicionario2= {'item1': 'primeiro', 'item2': 'segundo'}
print(dicionario2)

print(len(dicionario2)) #tamanho
print(dicionario2.keys())