def eco(frase):
    def inner(algo):
        return f'Repito la entrada {algo}'

    return inner(frase)

entrada = 'Hola'
print('Entrada')
print(eco('Hola'))

print(inner('Hola'))