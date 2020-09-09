def reverse(x: int) -> int:
    if x > 0:
        num = x
        n_digits = 0
        while num > 0:
            num = num // 10
            n_digits += 1

        result = 0
        for i in range(n_digits - 1, -1, -1):
            digit = x % 10
            result += digit * 10 ** i
            x = x // 10

        if result > 2 ** 31 - 1:
            return 0

        return result

    if x < 0:
        x2 = abs(x)
        num = x2
        n_digits = 0
        while num > 0:
            num = num // 10
            n_digits += 1

        result = 0
        for i in range(n_digits - 1, -1, -1):
            digit = x2 % 10
            result += digit * 10 ** i
            x2 = x2 // 10

        result = -result
        if result < - 2 ** 31:
            return 0

        return result

    if x == 0:
        return 0


if __name__ == '__main__':
    number = randint(- 2 ** 31, 2 ** 31 - 1)
    rev = reverse(number)
    print(f'number: {number}, reversed: {rev}')
