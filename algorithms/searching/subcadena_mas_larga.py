import random
import string


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for _ in range(length))
    return result_str


def subcadena_mas_larga(entrada):

    cad_activa = list()
    subcadenas = list()

    for c in entrada:

        if c in cad_activa:
            subcadenas.append(''.join(cad_activa))

            corte = cad_activa.index(c) + 1
            cad_activa = cad_activa[corte:]

        cad_activa += c
        print(cad_activa)

    subcadenas.append(''.join(cad_activa))

    longest = max(subcadenas, key=len)
    return longest


if __name__ == '__main__':

    length = random.randint(1, 20)
    secuencia = get_random_string(length)
    secuencia = 'pwwkew'
    sub_mas_larga = subcadena_mas_larga(secuencia)

    print('Secuencia aleatoria de longitud ' + str(length) + ':', secuencia)
    print('Subcadena más larga sin repetición:', sub_mas_larga)
    print('Longitud de la subcadena más larga:', len(sub_mas_larga))

