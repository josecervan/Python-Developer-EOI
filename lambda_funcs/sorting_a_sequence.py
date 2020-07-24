notas = [{'nombre': 'Lola', 'final': 9},
         {'nombre': 'Javier', 'final': 9.2},
         {'nombre': 'Marta', 'final': 9.5}]


if __name__ == '__main__':
    nombres_ordenados = sorted(notas, key=lambda nota: nota.get('nombre'))
    notas_ordenadas = sorted(notas, key=lambda nota: nota.get('nombre'))
    minima = min(notas, key=lambda nota: nota.get('final'))
    maxima = max(notas, key=lambda nota: nota.get('final'))
    print(f'Notas: {notas}')
    print(f'Por nombre: {nombres_ordenados}')
    print(f'Por nota: {notas_ordenadas}')
    print(f'Nota mínima: {minima}')
    print(f'Nota mínima: {maxima}')

