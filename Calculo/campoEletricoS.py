try:
    import numpy as np
    import matplotlib.pyplot as plt
except ImportError:
    print("Erro: numpy ou matplotlib não estão instalados.")
    exit()

def obter_dados():
    try:
        Q_input = float(input("Digite a carga do objeto em Coulombs (ex: 1^-6 para 1µC): "))
        return Q_input
    except ValueError:
        print("Valor inválido. Usando carga padrão de 1^-6 C.")
        return 1e-6

Q = obter_dados()
k = 9 * 10**9
d = np.linspace(0.1, 5, 500) 

# Campo Elétrico: E proporcional a 1/d²
E = (k * abs(Q)) / d**2

# Potencial Elétrico (Conceito de Integral de E): V proporcional a 1/d
# V = integral(E) dr = kQ/d
V = (k * Q) / d
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plotagem do Campo Elétrico (Eixo Y da esquerda)
color = 'tab:red'
ax1.set_xlabel('Distância (m)')
ax1.set_ylabel('Campo Elétrico |E| (N/C)', color=color)
ax1.plot(d, E, color=color, linewidth=2, label='Campo Elétrico ($1/d^2$)')
ax1.tick_params(axis='y', labelcolor=color)
ax1.grid(True, linestyle='--', alpha=0.6)

# Criação do segundo eixo Y para o Potencial (Eixo Y da direita)
ax2 = ax1.twinx()  
color = 'tab:blue'
ax2.set_ylabel('Potencial Elétrico V (Volts)', color=color)
ax2.plot(d, V, color=color, linewidth=2, linestyle='-.', label='Potencial Elétrico ($1/d$)')
ax2.tick_params(axis='y', labelcolor=color)

# Títulos e Ajustes
plt.title(f'Campo vs. Potencial (Carga Q = {Q} C)')
fig.tight_layout()  

print(f"\nCálculo realizado para o intervalo de distância de {d[0]}m a {d[-1]}m.")
print("O gráfico foi gerado.")

plt.show()