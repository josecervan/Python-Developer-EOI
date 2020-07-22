def run_len_decod(lst):
    if lst:
        symbol = lst[0]
        reps = lst[1]
        return symbol * int(reps) + run_len_decod(lst[2:])

    else:
        return ''


if __name__ == '__main__':
    coded_list = ["A", 12, "B", 4, "A", 6, "B", 1]
    decoded_list = run_len_decod(coded_list.copy())

    print(f'Coded list: {coded_list}')
    print(f'Decoded list: {decoded_list}')