import numpy as np

ganadores = sorted(np.random.choice(np.arange(1, 49 + 1), 7, replace=False))
complementario = ganadores[-1]
reintegro = np.random.choice(np.arange(0, 9 + 1), 1)

ganadores = np.delete(ganadores, len(ganadores) - 1)

print('Números ganadores:', ganadores)
print('Complementario:', complementario)
print('Reintegro:', reintegro)
