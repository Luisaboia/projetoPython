# Fórmula
# F = k(q1*q2/r²)

k = 9 * 10**9
q1 = float(input("Digite o valor da carga 1 em Coulombs (C): "))
q2 = float(input("Digite o valor da carga 2 em Coulombs (C): "))
r = float(input("Digite a distância entre as duas cargas (m): "))

F = k * (q1*q2/r**2)

print(f"A força elétrica é de, aproximadamente, {round(F)} N")