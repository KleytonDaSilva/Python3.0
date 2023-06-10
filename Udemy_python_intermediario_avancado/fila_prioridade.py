# algoritmo de caminho minimo, algoritmo de draskan
import heapq
# Importando o módulo heapq para utilizar a funcionalidade de fila de prioridade
import heapq

# Definindo a classe PriorityQueue para implementar uma fila de prioridade
class PriorityQueue:
    """
    Classe que implementa uma fila de prioridade utilizando o módulo 'heapq'.
    """

    def __init__(self):
        """
        Inicializa a fila de prioridade vazia e o contador de índice.
        """
        self.queue = []     # Lista que armazena os elementos da fila de prioridade
        self._index = 0     # Contador de índice para desempatar elementos com a mesma prioridade

    def push(self, item, priority):
        """
        Insere um item na fila de prioridade.
        Parâmetros:
            - item: o item a ser inserido na fila de prioridade.
            - priority: a prioridade associada ao item.
        """
        heapq.heappush(self.queue, (-priority, self._index, item))    # Insere o item na fila de prioridade usando o módulo heapq
        self._index += 1     # Incrementa o contador de índice para desempatar elementos

    def pop(self):
        """
        Remove e retorna o item com a maior prioridade da fila.
        Retorna:
            - O item com a maior prioridade.
        """
        return heapq.heappop(self.queue)[-1]     # Remove e retorna o último elemento do tupla armazenada na fila de prioridade


# Definindo a classe Pessoa para representar uma pessoa
class Pessoa:
    """
    Classe que representa uma pessoa com um atributo 'name'.
    """

    def __init__(self, name):
        """
        Inicializa a pessoa com o nome fornecido.
        """
        self.name = name

    def __repr__(self):
        """
        Retorna o nome da pessoa ao chamar a função 'repr' ou 'print' na instância.
        """
        return self.name


# Criando uma instância da classe PriorityQueue
q = PriorityQueue()

# Adicionando instâncias da classe Pessoa à fila de prioridade
q.push(Pessoa('Kleyton'), 36)
q.push(Pessoa('Amanda'), 34)
q.push(Pessoa('Beatriz'), 8)
q.push(Pessoa('Alencar'), 63)
q.push(Pessoa('Margarete'), 60)


print(q.pop())