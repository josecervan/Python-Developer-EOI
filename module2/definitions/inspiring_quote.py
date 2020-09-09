def inspiring_quote():
    print("Don't worry, be happy!")

def everything_is_ok():
    print('Keep this way!')


if __name__ == '__main__':

    feeling = str(input('How are you feeling today? '))
    while feeling not in ['good', 'bad']:
        print('Options: good or bad')
        feeling = str(input('How are you feeling today? '))

    if feeling == 'good':
        everything_is_ok()
    elif feeling == 'bad':
        inspiring_quote()

