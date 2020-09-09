import korean_name_code as code


def get_birth_date():
    while True:
        try:
            date_entry = input('> Enter a valid date in DD/MM/YYYY format: ')
            day, month, year = map(int, date_entry.split('/'))
            assert 1 <= day <= 31
            assert 1 <= month <= 12
            assert year > 0
        except ValueError:
            pass
        else:
            return day, month, str(year)


def get_korean_name(day, month, year):
    last_name = code.last_name[int(year[-1])]
    middle_name = code.middle_name[month]
    first_name = code.first_name[day]
    return last_name, middle_name, first_name


if __name__ == '__main__':
    date_tuple = get_birth_date()
    full_name_tuple = get_korean_name(*date_tuple)
    print(full_name_tuple)
