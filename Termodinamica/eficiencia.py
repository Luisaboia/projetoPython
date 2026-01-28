# Fórmula
# n = 1 - Tf/Tq

tf = float(input("Insira a temperatura fria (K): "))
tq = float(input("Insira a temperatura quente (K): "))

n = 1 - (tf/tq)
nPorcentagem = n * 100
print(f"A eficiência da máquina térmica é de, aproximadamente, {nPorcentagem:.2f}%")