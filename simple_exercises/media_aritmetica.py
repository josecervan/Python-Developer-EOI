cuantos = int(input('¿Cuántos números quieres introducir? '))

numeros = list()
for num in range(cuantos):
  numeros.append(float(input('Número ' + str(num + 1) + ': ')))

print('Media aritmética:', sum(numeros)/len(numeros))
