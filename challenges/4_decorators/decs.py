def validator(func):
    def wrapper(*args, **kwargs):
        # Contadores
        negs = 0
        floats = 0
        i = 0

        # Se ejecuta mientras no haya negativos y no enteros
        while i < len(args) and (negs == 0 or floats == 0):
            if args[i] < 0:
                negs += 1
            if isinstance(args[i], float):
                floats += 1

            i += 1

        if negs > 0:
            print('Al menos, hay un número negativo')
        if floats > 0:
            print('Al menos, hay un número no entero')

        # Llamada a la función
        result = func(*args, **kwargs)

        return result

    return wrapper


@validator
def get_numbers(*numbers):
    # Sólo devuelve números en formato lista
    return list(numbers)
