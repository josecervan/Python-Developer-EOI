from random import sample, randint


def find_median(lst1: [int], lst2: [int]) -> float:
    l1, l2 = len(lst1), len(lst2)
    if l1 > l2:
        l1, l2 = l2, l1
        lst1, lst2 = lst2, lst1

    min_idx, median, i, j = 0, 0, 0, 0
    max_idx = l1

    while min_idx <= max_idx:
        i = int((min_idx + max_idx) / 2)
        j = int(((l1 + l2 + 1) / 2) - i)

        if i < l1 and j > 0 and lst2[j - 1] > lst1[i]:
            min_idx = i + 1

        elif i > 0 and j < l2 and lst2[j] < lst1[i - 1]:
            max_idx = i - 1

        else:
            if i == 0:
                median = lst2[j - 1]
            elif j == 0:
                median = lst1[i - 1]
            else:
                median = max(lst1[i - 1], lst2[j - 1])

            min_idx = max_idx + 1

    if (l1 + l2) % 2 == 1:
        return float(median)

    if i == l1:
        return float((median + lst2[j]) / 2)

    if j == l2:
        return float((median + lst1[i]) / 2)

    return float((median + min(lst1[i], lst2[j])) / 2)


if __name__ == '__main__':
    nums1 = sorted(sample(range(-10, 0), randint(1, 5)))
    nums2 = sorted(sample(range(0, 10), randint(1, 5)))

    print(f'nums1: {nums1}')
    print(f'nums2: {nums2}')
    print(f'population: {sorted(nums1 + nums2)}')
    print(f'median: {find_median(nums1, nums2)}')
