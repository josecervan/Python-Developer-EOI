lista1 = [1, 4, 5, 8, 6]
lista2 = [8, 9, 1]

lista3 = list(set(lista1).intersection(lista2))
lista3.sort()

print('lista1', lista1)
print('lista2', lista2)
print('lista3', lista3)
