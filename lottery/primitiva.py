from random import randint, sample
import pdb

pdb.set_trace()

ganadores = sorted(sample(range(1, 49 + 1), 6))

comp = randint(1, 49)
reint = randint(0, 9)

print('Números ganadores:', ganadores)
print('Complementario:', comp)
print('Reintegro:', reint)
