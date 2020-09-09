factorial = lambda x: x * factorial(x - 1) if x > 0 else 1

for i in range(11):
    print(f'{i}! = {factorial(i)}')