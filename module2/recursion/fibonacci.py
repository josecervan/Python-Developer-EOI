def fibonacci(n):
    if n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)
    elif n in (0, 1):
        return n


def fibonacci2(n):
    if n != 0:
        return _fib(n, 1, 0, 1)

    return 0

def _fib(n, m, fibm_minus1, fibm):
    if n != m:
        return _fib(n, m + 1, fibm, fibm_minus1 + fibm)

    return fibm

if __name__ == '__main__':

    N = 5
    # print(f'Fibonacci sequence ({N} terms)')
    # for i in range(N):
    #     print(f'F_{i} = {fibonacci(i)}')

    print(f'Fibonacci sequence ({N} terms)')
    for i in range(N):
        print(f'F_{i} = {fibonacci2(i)}')
