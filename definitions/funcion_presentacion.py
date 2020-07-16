def presentacion():

    print('Nombre:', data.get('Nombre'))
    print('Mascota', data.get('Mascota'))
    print('Edad:', data.get('Edad'))
    print('Película favorita:', data.get('Película favorita'))
    print('Libro favorito:', data.get('Libro favorito'))


if __name__ == '__main__':

    data = {'Nombre': 'Jose',
            'Mascota': False,
            'Edad': 26,
            'Película favorita': 'ESDLA',
            'Libro favorito': 'El Quijote'}

    presentacion()

