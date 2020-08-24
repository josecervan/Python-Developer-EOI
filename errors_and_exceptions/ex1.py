a = 10
b = 0

try:
    result = a / b
except ZeroDivisionError as exception:
    print(f'ZeroDivisionError: {exception.args}')
else:
    print(result)
