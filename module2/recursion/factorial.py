def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    elif n in (0, 1):
        return 1


if __name__ == '__main__':

    for i in range(6):
        print(f'{i}! = {factorial(i)}')
