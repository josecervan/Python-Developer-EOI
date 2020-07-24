def sandwich(func):
    def wrapper(*args, **kwargs):
        print('\n=== REBANADA SUPERIOR ===')
        result = func(*args, **kwargs)
        print('=== REBANADA INFERIOR ===')
        return result

    return wrapper


@sandwich
def relleno(ingrs):
    print(' / '.join(ingrs))


if __name__ == '__main__':

    print(f'Introduzca 3 ingredientes\n')
    ingredients = list()
    while len(ingredients) < 3:
        ingredients.append(input(f'Ingrediente {len(ingredients) + 1}: '))

    # sandwich(relleno)
    # new(ingredients)
    relleno(ingredients.copy())
