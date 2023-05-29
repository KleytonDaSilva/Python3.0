import math

a = float(input("Informe Lado A do triangulo: "))
b = float(input("Informe Lado B do triangulo: "))
c = float(input("Informe Lado C do triangulo: "))

p = (a + b +c)/ 2
ponto =p  * (p -a) * (p - b) * ( p - c)
areaTriangulo = float(ponto) ** 2.0

print("Área do Triangulo: " ,  areaTriangulo)