def catalogar(lst):
    for item in lst:
        print(f"{type(item).__name__}: {item}")


def check_wheels(lst, n_wheels=2):
    print('--')
    print("Checking vehicles with {} wheel/s".format(n_wheels))
    print('--')
    for item in lst:
        if item.ruedas == n_wheels:
            print(f"{type(item).__name__}: {item}")
