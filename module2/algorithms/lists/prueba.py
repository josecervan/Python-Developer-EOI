import random


# lst = [0,0,0,0,0,0,0,0,0,0,0,0]
lst = [random.randint(0, 3 + 1) for _ in range(20)]

print('i:', lst)
print('')

n_zeros = lst.count(0)  # ocurrencias del 0
reps = 0

if any(lst):
    while reps < n_zeros:
        lst.remove(lst[lst.index(0)])
        lst.append(0)
        reps += 1

print('n_zeros:', n_zeros)
print('')
print('iteraciones:', reps)
print('o:', lst)