
a = float(input("Informe o valor de A: "))
b = float(input("Informe o valor de B: "))
c = float(input("Informe o valor de C: "))
d = float(input("Informe o valor de D: "))
e = float(input("Informe o valor de E: "))
f = float(input("Informe o valor de F: "))

x = (c*e - b*f) / (a*e - b*d)
y = (a*f - c*d) / (a*e - b*d)

print("Valor de X: ", x)
print("Valor de Y: ", y)