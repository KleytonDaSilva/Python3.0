

m1 = float(input("Informe o valor de M1: "))
m2 = float(input("Informe o valor de M2: "))
m3 = float(input("Informe o valor de M3: "))

r13 = float(input("Informe o valor de R13: "))
r23 = float(input("Informe o valor de R23: "))
r12 = float(input("Informe o valor de R12: "))

e = 6.67 *(m1 * m2 + m1 * m3 + m2 + m3) / ( r12 + r13 + r23)

print("Energia de coesao: ", e)