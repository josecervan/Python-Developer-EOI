def run_len_decod(lst):
    if lst:
        return [*list(lst[0] * lst[1]), *run_len_decod(lst[2:])]
    else:
        return ''

if __name__ == '__main__':
    coded_list = ["A", 12, "B", 4, "A", 6, "B", 1]
    decoded_list = run_len_decod(coded_list.copy())

    print(f'Coded list: {coded_list}')
    print(f'Decoded list: {decoded_list}')
