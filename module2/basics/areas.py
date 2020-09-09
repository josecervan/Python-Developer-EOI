from math import pi, pow

triangulo = {'altura': 5, 'base': 7}
rectangulo = {'altura': 3, 'base': 6}
circulo = {'radio': 3}

areas = {"triangulo": -1, "rectangulo": -1, "circulo": -1}

areas.update({'triangulo': triangulo.get('base') * triangulo.get('altura') / 2,
              'rectangulo': rectangulo.get('base') * rectangulo.get('altura'),
              'circulo': pi * pow(circulo.get('radio'), 2)})

print(areas)