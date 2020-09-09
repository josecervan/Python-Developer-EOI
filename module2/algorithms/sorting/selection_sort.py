import random


def min_pos(nums):
    pos = 0
    minimo = nums[pos]

    for i in range(len(nums)):
        if nums[i] < minimo:
            minimo = nums[i]
            pos = i

    return pos


def selection_sort(lst):
    sorted_list = lst.copy()
    for i in range(len(sorted_list) - 1):
        pos = min_pos(sorted_list[i:]) + i
        sorted_list[i], sorted_list[pos] = sorted_list[pos], sorted_list[i]

    return sorted_list


if __name__ == '__main__':
    for i in range(1, 1000 + 1):

        lst = random.sample(range(100), 10)

        if sorted(lst) == selection_sort(lst):
            print(str(i) + ') Ordenación correcta')
        else:
            print('sorted(lst):\n', sorted(lst))
            print('selection_sort(lst):\n', selection_sort(lst))
            print(str(i) + ') ¡Ordenación incorrecta!')
            raise Exception

    print('--')
    print('Yiiiiiiiiiiiha!')
