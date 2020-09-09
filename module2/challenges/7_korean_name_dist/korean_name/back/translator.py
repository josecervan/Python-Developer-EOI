from tkinter import END


def get_birth_date(date, label):

    msg = ''

    try:
        day, month, year = map(int, date.get().split('/'))

        assert 1 <= day <= 31
        assert 1 <= month <= 12
        assert year > 0

    except:
        msg = 'Enter a valid dd/mm/yyyy format date'
    else:
        korea_name = get_korean_name(day, month, str(year))
        msg = 'Your birth date ({}) becomes in your korean name:\n{} {} {}'.format(date.get(),
                                                                                  korea_name[0],
                                                                                  korea_name[1],
                                                                                  korea_name[2])
    date.delete(0, END)
    label.config(text=msg)


def get_korean_name(day, month, year):
    from korean_name.data.source_data import last_name, middle_name, first_name

    last_name = last_name[int(year[-1])]
    middle_name = middle_name[month]
    first_name = first_name[day]

    return last_name, middle_name, first_name
