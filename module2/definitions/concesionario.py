def make_car(*args, **kwargs):
    if len(args) == 2:
        car = {'brand': args[0],
               'model': args[1]}

        return {**car, **kwargs}
    
    
if __name__ == '__main__':
    
    car1 = make_car('seat', 'leon', color='yellow', tinted_windows=True, doors=5)
    car2 = make_car('bmw', '320d', color='black', fuel='diesel', doors=5, tinted_windows=False)
    car3 = make_car('renault', 'capture')
    car4 = make_car('audi')
    car5 = make_car('dacia', 'logan', fuel='petrol', doors=3)

    print(car1)
    print(car2)
    print(car3)
    print(car4)
    print(car5)
