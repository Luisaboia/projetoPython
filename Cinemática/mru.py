def posicao_mru(posicao_inicial, velocidade, tempo):
    return posicao_inicial + velocidade * tempo

posicao_inicial = float(input("Digite a posicao inicial: "))
velocidade = float(input("Qual a velocidade?: "))
tempo = float(input("E o intervalo de tempo?: "))

resultado = posicao_mru(posicao_inicial, velocidade, tempo)

print(f"A posição final é: {resultado} m")