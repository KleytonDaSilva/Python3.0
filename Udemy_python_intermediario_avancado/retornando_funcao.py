# funções = posso criar função dentro de função
def pai(num):

	def filho1(): # função chamada "pai" que vai passar um número chamado "num"
		print('Oi, eu sou o filho1')

	def filho2():
		print('Oi, eu sou o filho2')

	try:
		assert num == 20
		return filho1
	except AssertionError:
		return filho2


f1 = pai(10)
f2 = pai(20)

f1()
f2()