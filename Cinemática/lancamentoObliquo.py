import math

# Constante da gravidade
g = 10

print("=== Lançamento Oblíquo ===")

# Entradas
v0 = float(input("Velocidade inicial (m/s): "))
angulo_graus = float(input("Ângulo de lançamento (em graus): "))

# Graus -> Radianos
# O computador só entende radianos nas funções trigonométricas
angulo_rad = math.radians(angulo_graus)

# Decomposição dos Vetores
# V0x = V0 * cos(theta)
# V0y = V0 * sen(theta)
v0x = v0 * math.cos(angulo_rad)
v0y = v0 * math.sin(angulo_rad)

# Tempo de subida
tempo_total = (2 * v0y) / g

# Altura Máxima
altura_maxima = (v0y ** 2) / (2 * g)

# Alcance Horizontal
alcance = v0x * tempo_total

# Saída
print("-" * 40)
print(f"RESULTADOS PARA O ÂNGULO DE {angulo_graus}°:")
print(f"> Componente X (Velocidade constante): {v0x:.2f} m/s")
print(f"> Componente Y (Velocidade inicial vertical): {v0y:.2f} m/s")
print("-" * 40)
print(f"Tempo total de voo:  {tempo_total:.2f} s")
print(f"Altura máxima:       {altura_maxima:.2f} m")
print(f"Distância alcançada: {alcance:.2f} m")