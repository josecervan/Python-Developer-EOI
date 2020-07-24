from functools import reduce
from random import sample

# Aportaciones trimestrales
aportaciones = sample(range(1, 100), 10)

# Saldo final
saldo_final = round(reduce(lambda x, y: x * 1.03 + y * 1.01, aportaciones, 0), 2)

# Beneficios
beneficios = round(saldo_final - sum(aportaciones), 2)

# Informe
print(f'Aportaciones: {aportaciones}')
print(f'Total de aportaciones: {sum(aportaciones)}')
print(f'Saldo final: {saldo_final}')
print(f'Beneficios: {beneficios}')

# acumulado = 0
# for aportacion in aportaciones:
#      acumulado = acumulado * 1.03 + aportacion * 1.01
#
# print(f'Saldo final: {round(acumulado, 2)}')
