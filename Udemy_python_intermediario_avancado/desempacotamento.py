#desempacotar
x,y,z = [1,2,3]

print(x)
print(y)
print(z)
print("-------------------------------------")

_,k,p = [1,2,3] # _ ele descarta o elemento
print(p)
print(k)


print("-------------------------------------")

lista = [9,4,5,15,20]
*n1, n2 = lista # * ele guardou os 4 primeiros elementos para n1 e reservou o elemento 20 para n2

print(n1)


notas = [9,7,8,5,10]

m1, *m2, m3 = notas # descartando a primeira e a ultima nota, ficando somente com as 3 do meio
firts, *_, last = notas # pegando somente a primeira nota e a ultima, descartando as demais

print(m2)
print(firts, last)