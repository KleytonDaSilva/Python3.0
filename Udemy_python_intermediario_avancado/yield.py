import os
def gerador():
    for i in range(5):
        yield i

g = gerador()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g)) 


print('============================= exemplo chatgpt')

def gerador():
    yield 1
    yield 2
    yield 3

# Utilizando o gerador
gen = gerador()
print(next(gen))  # Saída: 1
print(next(gen))  # Saída: 2
print(next(gen))  # Saída: 3
