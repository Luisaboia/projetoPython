print("=== Colisões em uma dimensão ===")
print("Atenção: Use sinal NEGATIVO (-) se o objeto estiver indo para a esquerda.")

# Entradas
m1 = float(input("Massa do objeto 1 (kg): "))
v1_inicial = float(input("Velocidade inicial do obj 1 (m/s): "))

m2 = float(input("Massa do objeto 2 (kg): "))
v2_inicial = float(input("Velocidade inicial do obj 2 (m/s): "))

print("\nTipo de Colisão (Coeficiente de Restituição 'e'):")
print("Digite 1 para Elástica (conserva energia - ex: bilhar)")
print("Digite 0 para Perfeitamente Inelástica (bate e gruda)")
print("Digite entre 0 e 1 para Parcialmente Elástica")

# Coeficiente de Restituição
e = float(input("Valor de 'e': "))

# Cálculos
# Calcular a Quantidade de Movimento Total
q_total = (m1 * v1_inicial) + (m2 * v2_inicial)

# Calcular as velocidades finais
v1_final = (q_total + m2 * e * (v2_inicial - v1_inicial)) / (m1 + m2)

# Sabendo V1 final, usamos a definição do 'e' para achar V2 final
# Vf2 = Vf1 + e*(V1_ini - V2_ini)
v2_final = v1_final + e * (v1_inicial - v2_inicial)

# Resultados das colisões
print("-" * 40)
print(f"Velocidade final do objeto 1: {v1_final:.2f} m/s")
print(f"Velocidade final do objeto 2: {v2_final:.2f} m/s")

# Resultado da situação
if v1_final == v2_final:
    print("Resultado: Os objetos colidiram e seguiram GRUDADOS.")
else:
    print("Resultado: Os objetos se separaram após a colisão.")

# Energia Cinética para perca de Energia
ec_antes = 0.5 * m1 * v1_inicial**2 + 0.5 * m2 * v2_inicial**2
ec_depois = 0.5 * m1 * v1_final**2 + 0.5 * m2 * v2_final**2
perda = ec_antes - ec_depois

if perda > 0.1:
    print(f"Energia dissipada (perdida): {perda:.2f} Joules")
else:
    print("Energia Cinética conservada (Colisão Elástica).")