def person_name(first_name, last_name):
    person = {'first': first_name,
              'last': last_name}
    return person


def build_person(first_name, last_name, age = None):
    person = {'first': first_name,
              'last': last_name}
    if age:
        person.update({'age': age})

    return person


if __name__ == '__main__':
    
    person1 = person_name('Carmen', 'Sevilla')
    person2 = person_name('Philip', 'Glass')
    person3 = build_person('Jose', 'Cerván', 26)
    person4 = build_person('Elena', 'Ruiz')

    print(person1)
    print(person2)
    print(person3)
    print(person4)
