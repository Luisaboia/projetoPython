print("=== MRUV ===")

# Entrada de Dados
posicao_inicial = float(input("Posição inicial (m): "))
velocidade_inicial = float(input("Velocidade inicial (m/s): "))
aceleracao = float(input("Aceleração (m/s²): "))
tempo = float(input("Instante de tempo (s): "))

# Cálculo da Posição
posicao_final = posicao_inicial + (velocidade_inicial * tempo) + (aceleracao * (tempo ** 2) / 2)

# Cálculo da Velocidade
# Fórmula: V = V0 + a.t
velocidade_final = velocidade_inicial + (aceleracao * tempo)

# Resultados
print("-" * 40)
print(f"No tempo {tempo} segundos:")
print(f"> A posição final é:    {posicao_final:.2f} m")
print(f"> A velocidade final é: {velocidade_final:.2f} m/s")

# Movimento acelerado ou não
if velocidade_final > velocidade_inicial:
    print("(O objeto está ACELERANDO)")
elif velocidade_final < velocidade_inicial:
    print("(O objeto está FREANDO/DESACELERANDO)")
else:
    print("(Velocidade constante - Isso seria um MRU!)")