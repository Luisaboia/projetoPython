# Fórmula por condução (Lei de Fourier)
# Transmissão = (Condutividade * Delta Temperatura * Área Transversal)/Comprimento Longitudinal

k = float(input("Insira a condutividade do corpo (W/m*K): "))
dT = float(input("Insira a variação de temperatura (ambos em K ou Cº): "))
at = float(input("Insira a área transversal do corpo (m²):"))
c = float(input("Insira o comprimento do corpo (m): "))

T = (k * dT * at) / c

print(f"A taxa de transferência de calor é de, aproximadamente, {T:.2f} W")