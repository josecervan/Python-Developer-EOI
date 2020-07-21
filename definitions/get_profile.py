MAX_SPORTS = 5


def get_profile(name, age, *sports, **awards):
    if not isinstance(age, int) or len(sports) > MAX_SPORTS:
        raise ValueError

    return {'name': name,
            'age': age,
            'sports': list(sports),
            'awards': awards
            }


if __name__ == '__main__':

    print(get_profile('tim', 36))
    print('')
    print(get_profile('tim', 36, 'tennis', 'basketball'))
    print('')
    print(get_profile('tim', 36, 'tennis', 'basketball', aw1='helped out team in crisis', aw2='good helper'))
