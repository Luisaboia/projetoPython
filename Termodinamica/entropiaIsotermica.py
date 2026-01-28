# Formula (Entropia Isotérmica com gás ideal)
# dS = n * R * ln(v2/v1)

import math # Necessário para o logaritmo natural

R = 8.314
n = float(input("Digite o número de mols: "))
v2 = float(input("Digite o volume final (m³): "))
v1 = float(input("Digite o volume inicial (m³):"))

dS = n * R * math.log(v2/v1)
print(f"A variação da entropia é, de, em média {dS:.2f} Joules/K")