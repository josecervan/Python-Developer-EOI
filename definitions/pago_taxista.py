def precio_viaje_taxi(kms):
    return 4 + 0.25 * (kms * 1000 // 200)


if __name__ == '__main__':
    precio = precio_viaje_taxi(float(input('Distancia recorrida en kilómetros: ')))
    print(f'El precio del viaje es de {precio} €')
