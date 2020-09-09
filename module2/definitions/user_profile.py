def register_user(f_name, l_name, **kwargs):
    full_name = {'f_name': f_name,
                 'l_name': l_name}

    return {**full_name, **kwargs}


if __name__ == '__main__':

    user1 = register_user('John', 'Doe', age=63)
    user2 = register_user('Jane', 'Doe', age=45, city='NY', hobbies=['reading', 'Python'])
    user3 = register_user('Judy', 'Doe')

    print(user1)
    print(user2)
    print(user3)
