def todo_OK():
    return True


def fallo():
    return False


if __name__ == '__main__':

    if todo_OK():
        print('TODO OK')
    else:
        pass

    if not fallo():
        print('FALLO')
    else:
        pass
        
        
