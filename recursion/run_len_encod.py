def run_len_encod(lst):
    if lst:
        last_symbol = lst[0]
        i = 1
        while i < len(lst) and last_symbol == lst[i]:
            i += 1

        return last_symbol + str(i) + run_len_encod(lst[i:])

    else:
        return ''


if __name__ == '__main__':
    uncoded_list = "AAAAAAAAAAAABBBBAAAAAAB"
    encoded_list = run_len_encod(uncoded_list)

    print(f'Coded list: {uncoded_list}')
    print(f'Decoded list: {encoded_list}')