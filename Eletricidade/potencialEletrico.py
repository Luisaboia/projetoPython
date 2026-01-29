# Fórmulas
# V = U/q, U = (k * Q * q)/d

k = 9 * 10**9
Q = float(input("Insira o valor da carga geradora em Coulombs (C): "))
q = float(input("Insira o valor da carga de prova em Coulombs (C): "))
d = float(input("Insira a distância entre elas (m): "))

# Energia Potencial Elétrica
U = (k * Q * q)/d

# Potencial Elétrico
V = U/q

print(f"A Energia Potencial é, aproximadamente: {round(U)} J")
print(f"O Potencial Elétrico é, aproximadamente: {round(V)} V")