from collections import deque

# collections é estrutura de dados fila

fila = deque(maxlen=4)
fila.append(1)
fila.append(2)
fila.append(3)
fila.append(4)
fila.append(5)
print(fila)


print("======================= appendeleft ")
f = deque()
f.append(1)
f.append(2)
f.append(3)
f.appendleft(4) # vai adicionar mais a esquerda da fila
print(f)
f.pop()   # remove ultima da fila
f.popleft() # remova o primeiro da fila
print(f)