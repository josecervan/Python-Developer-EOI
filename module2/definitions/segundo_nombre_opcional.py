def cap_full_name(fname, fsurname, msurname, sname=None):
    if sname == None:
        return f'{fname.capitalize()} {fsurname.capitalize()} {msurname.capitalize()}'

    return f'{fname.capitalize()} {sname.capitalize()} {fsurname.capitalize()} {msurname.capitalize()}'


if __name__ == '__main__':

    nombre1 = cap_full_name('juan', 'rebolledo', 'lópez', 'antonio')
    nombre2 = cap_full_name('miranda', 'gálvez', 'aranda')
    nombre3 = cap_full_name('luis', 'malik', 'moreno', 'fernando')

    print(nombre1)
    print(nombre2)
    print(nombre3)
