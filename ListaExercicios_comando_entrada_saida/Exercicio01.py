
# Exercicios 01  lista

print("_______________________________________________________")
print("100 Francos franceses      |     21.55 Dólar canadenses")
print("1 Dólar Americano          |     1.06  Dólar canadenses")
print("100 Marcos alemães         |     43.20 Dólar canadenses")
print("1 Libra Inglesa            |     1.84  Dólar canadenses")
print("100 Coroas Suecas          |     24.25 Dólar canadenses")
print("100 Dracmas Gregos         |     2.95  Dólar canadenses")
print("_______________________________________________________")

total = 0
print("Conversão de moedas")
franco = float(input("Informe a quantidade de Francos para converter em Dólar canadense"))
franco = franco * 0.2155
print("Quantidade Franco Franceses : ", franco)


dolar = float(input("Informe a quantidade de Dólar  americano converter Coroas Suecas"))
dolar =  dolar * 0.2431
print("Quantidade Dólar: ", dolar )

dracmas = float(input("Informe a quantidade de Dracmas gregos converter em libra Inglesa"))
dracmas =  dracmas * 1.595
print("Quantidade de Libra ", dracmas)


dolarDo = float(input("Quantidade de Dólar Canadense para converter em  Dólar "))
dolarMa = float(input("Quantidade de Dólar Canadense para converter em  Marco Alemão "))
dolarDo =  dolarDo * 1.06
dolarMa = dolarMa * 0.432

print(" Quantidade de Dolar Americano " , dolarDo)
print("Quantidade de Marco Alemão ", dolarMa)

