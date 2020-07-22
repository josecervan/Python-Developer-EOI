def read_value():
    value = input('Value: ')
    if value != '':
        return float(value) + read_value()
    else:
        return 0.0


if __name__ == '__main__':
    print(f'Sum: {read_value()}')
