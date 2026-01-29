# Fórmula (Campo elétrico de uma carga puntiforme)
# E = (k * |Q|)/d²

Q = float(input("Digite a carga do objeto em Coulombs (C): "))
d = float(input("Digite a distância entre a carga e o ponto em metros (m): "))
k = 9 * 10**9

# abs() irá ter a mesma função que o módulo
E = (k * abs(Q))/d**2

print(f"O campo elétrico é de {round(E)} N/C.")