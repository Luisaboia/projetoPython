import numpy as np
import matplotlib.pyplot as plt

# Entrada de Dados
def obter_float(mensagem):
    while True:
        try:
            val = float(input(mensagem))
            if val <= 0:
                print("Por favor, digite um valor positivo.")
                continue
            return val
        except ValueError:
            print("Valor inválido.")

print("--- Cálculo de Variação de Entropia (Isotérmica) ---")
n = obter_float("Digite o número de mols (n): ")
v1 = obter_float("Digite o volume inicial (m³): ")
v2_alvo = obter_float("Digite o volume final desejado (m³): ")

R = 8.314

# Definição do Domínio
# Criamos um intervalo de volumes para mostrar a evolução da função.
# Vamos de 50% do volume inicial até 150% do volume final desejado.
v_continuo = np.linspace(v1 * 0.5, v2_alvo * 1.5, 500)

# dS em função do volume 'v' variando
dS_continuo = n * R * np.log(v_continuo / v1)

dS_final = n * R * np.log(v2_alvo / v1)
plt.figure(figsize=(10, 6))

# Curva logarítmica
plt.plot(v_continuo, dS_continuo, label=r'$\Delta S = nR \ln(V/V_1)$', color='purple', linewidth=2)

# Linha de referência no Volume Inicial (onde dS = 0)
plt.axvline(x=v1, color='gray', linestyle='--', alpha=0.5, label='Volume Inicial ($V_1$)')
plt.axhline(y=0, color='gray', linestyle='--', alpha=0.5)

# Ponto específico escolhido pelo usuário
plt.scatter([v2_alvo], [dS_final], color='red', zorder=5)
plt.annotate(f'Seu Ponto\n{dS_final:.2f} J/K', 
             (v2_alvo, dS_final), 
             textcoords="offset points", 
             xytext=(0,10), 
             ha='center')

# Preenchimento para representar a integral (área visual)
# Preencher entre V1 e o V2 alvo para destacar a variação acumulada
plt.fill_between(v_continuo, dS_continuo, where=((v_continuo >= min(v1, v2_alvo)) & (v_continuo <= max(v1, v2_alvo))),
                 color='purple', alpha=0.1)

plt.title(f'Variação da Entropia em Expansão/Compressão Isotérmica (n={n} mol)')
plt.xlabel('Volume (m³)')
plt.ylabel('Variação de Entropia $\Delta S$ (J/K)')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

print(f"\nResultado Pontual: A variação de entropia para {v2_alvo} m³ é de {dS_final:.2f} J/K.")
print("O gráfico mostra como a entropia evolui de forma logarítmica.")

plt.show()