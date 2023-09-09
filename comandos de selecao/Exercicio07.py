


x = float(input("Informe o lado X: "))
y = float(input("Informe o lado y: "))
z = float(input("Informe o lado Z: "))

if x != y and y != z:
    print("Triangulo Escaleno")
elif x == y and x == z and y == z:
    print("Triangulo equilatero")
else:
    print("Triangulo isosceles")