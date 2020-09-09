print(complex(2, 3))
print(type(complex(2, 3)))
print('--')

print(complex('2+3j'))
print(type(complex('2+3j')))
print('--')

print(complex(2, 3) == complex('2+3j'))
print('--')

print(complex(2, 0))
print(type(complex(2, 0)))
print('--')

print(complex(0, 3))
print(type(complex(0, 3)))
print('--')

print(complex('2'))
print(type(complex('2')))
print('--')

print(complex('3j'))
print(type(complex('3j')))
print('--')

try:
    print(complex('2 + 3j'))
except:
    pass
