# Importa funciones y decorator
import decs

# Importa paquetes
from random import sample
from numpy import random

# Ejecuta 'N_PRUEBAS' pruebas
N_PRUEBAS = 10
for _ in range(N_PRUEBAS):
    # Lista de números enteros positivos aleatorios
    positives = random.choice(range(100 + 1), size=10)

    # Lista de números enteros negativos aleatorios
    negatives = random.choice(range(-10, 0), size=2)

    # Lista de números reales aleatorios
    floats = random.uniform(low=-10.0, high=10.0, size=2)

    # Muestra aleatorio de la combinación de las lista anteriores
    population = sample([*positives, *negatives, *floats], 3)

    # Validación de números
    print(f'Population: {decs.get_numbers(*population)}')
    print('--')
