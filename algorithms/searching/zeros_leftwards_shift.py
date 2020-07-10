import random


if __name__ == '__main__':

    # lst = [0,0,0,0,0,0,0,0,0,0,0,0]
    lst = [random.randint(0, 3 + 1) for _ in range(20)]

    print('i:', lst)

    n_zeros = lst.count(0)  # ocurrencias del 0
    print('n_zeros:', n_zeros)
    print('')
    reps = 0


    if any(lst):
        for _ in range(lst.count(0)):
            lst.append(lst.pop(lst.index(0)))

        # [lst.append(lst.pop(lst.index(0))) for _ in range(lst.count(0))] # solución alternativa

    print('')
    print('iteraciones:', reps)
    print('o:', lst)