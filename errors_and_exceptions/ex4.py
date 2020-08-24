x = 20
y = "15"

try:
    resultado = x + y
except TypeError as exception:
    print(f'TypeError: {exception.args}')
else:
    print(resultado)
