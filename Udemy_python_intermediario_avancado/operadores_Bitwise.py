#operadores bit a bit

n1 = 10
n2 = 5
n3 = 6

print(bin(n1))
print(bin(n2))
print(bin(n3))

r = n1 & n2
re= n1 & n3
print(r)
print(re)


# Operador bit a bit OR (|)
result_or = 10 | 5  # Resultado: 15 (0b1111)

# Operador bit a bit XOR (^)
result_xor = 10 ^ 5  # Resultado: 15 (0b1111)

# Operador bit a bit NOT (~)
result_not = ~10  # Resultado: -11 (Complemento de 2 de 10)

# Operador de deslocamento à esquerda (<<)
result_left_shift = 10 << 2  # Resultado: 40 (0b101000)

# Operador de deslocamento à direita (>>)
result_right_shift = 10 >> 2  # Resultado: 2 (0b10)
