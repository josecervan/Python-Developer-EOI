colores = {'azul': 'blue',
           'rojo': 'red',
           'verde': 'green'}

try:
    color = colores['blanco']
except KeyError as exception:
    print(f'KeyError: {exception.args}')
else:
    print(color)
