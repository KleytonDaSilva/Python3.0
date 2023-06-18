import math

x1 = float(input('Informe x1:'))
x2 = float(input('Informe x2'))
y1 = float(input('Informe y1'))
y2 = float(input('Informe y2'))

p1= (x2*x2 - x1*x1)
p2= (y2*y2 - y1*y1)

soma = p1 + p2

d = math.sqrt(soma)

print('Coordenadas: ' , d)