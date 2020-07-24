def test_decorator(func):
    print('start')
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('end')
        return result

    return wrapper

@test_decorator
def add_ints(a, b):
    return a + b

if __name__ == '__main__':
    # new_test = test_decorator(add_ints)
    # output = new_test(3, 5)
    # print(f'output: {output}')

    output = add_ints(3, 4)
    print(f'output: {output}')
