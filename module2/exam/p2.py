import datetime


def meetup_date(year, month):
    assert year > 0
    assert 1 <= month <= 12

    new_date = datetime.date(year, month, 1)
    while new_date.strftime('%A') != 'Thursday':
        new_date += datetime.timedelta(days=1)

    new_date += datetime.timedelta(days=7)
    return new_date


print(meetup_date(2012, 3))
print(meetup_date(2015, 2))
print(meetup_date(2018, 6))
print(meetup_date(2020, 1))
