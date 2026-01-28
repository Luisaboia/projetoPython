# Constante universal dos gases (R)
R = 0.082

print("=== Calculadora de Pressão ===")

# 1. Coleta de dados
n = float(input("Digite o número de mols (n): "))
temperatura_celsius = float(input("Digite a temperatura em Celsius (ºC): "))
volume = float(input("Digite o volume em Litros (V): "))

# 2. Conversão de Temperatura
temperatura_kelvin = temperatura_celsius + 273.15

# 3. P = (n * R * T) / V
pressao = (n * R * temperatura_kelvin) / volume

# 4. Exibição do resultado
print("-" * 40)
print(f"Temperatura convertida: {temperatura_kelvin:.2f} K")
print(f"A pressão calculada é: {pressao:.2f} atm")

# O código apresenta dificuldade em tratar supostas divisões feitas por zero, o que é normal.
# Uma solução é usar try: e except:, porém já irá sair do escopo do projeto.