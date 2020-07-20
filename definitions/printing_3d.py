def print_design(design):
    print(f'Printing now: {design}')


def store_printed_design(design):
    printed_designs.append(design)


def print_log(designs):
    print('\nPrinted 3D designs:')
    for design in designs:
        print(f'\t--> {design}')


if __name__ == '__main__':

    unprinted_designs = ['colgante', 'funda de móvil', 'figura robot']
    printed_designs = list()

    for design in unprinted_designs:
        print_design(design)
        store_printed_design(design)

    print_log(printed_designs)
