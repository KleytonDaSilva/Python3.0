import heapq

# prioridade na fila

idade = [15,10,20,18,25,8,19]
print(heapq.nsmallest(3, idade)) #heapq.nsmallest(3,idade) vai pegar as três menos idade do vetor

print(heapq.nlargest(4,idade)) #heapq.nlargest(4,idade) vai pegar as 4 maiores idade do vetor

print(heapq.heapify(idade)) # vai trazer o vetor na ordem do menor para o maior

print(heapq.heappop(idade)) # heappop retira o menor numero

print(heapq.heappush(idade,8)) #adiciona um numero no vetor idade

