n = int(input('Número n: '))
m = int(input('Número m: '))

while n >= m:
    print('--> n debe ser menor que m')
    n = int(input('Número n: '))
    m = int(input('Número m: '))

suma = 0
while n <= m:
    suma += n
    n += 1

print('Suma:', suma)