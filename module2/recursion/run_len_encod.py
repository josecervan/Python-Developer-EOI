def run_len_encod(lst):
    if lst:
        i = 1
        while i < len(lst) and lst[0] == lst[i]:
            i += 1

        return lst[0] + str(i) + run_len_encod(lst[i:])
        # return [*list([lst[0], str(i)]), *run_len_encod(lst[i:])]
    else:
        return ''


if __name__ == '__main__':
    uncoded_list = "AAAAAAAAAAAABBBBAAAAAAB"
    encoded_list = run_len_encod(uncoded_list)

    print(f'Coded list: {uncoded_list}')
    print(f'Decoded list: {encoded_list}')