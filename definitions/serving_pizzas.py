def make_pizza_1(*toppings, size='M'):
    return dict(size=size, toppings=list(toppings))


def make_pizza_2(*toppings, size='M', sauce='tomato', cheese='mozzarella'):
    pizza = dict(size=size, toppings=list(toppings))

    if sauce not in toppings:
        pizza.get('toppings').append(sauce)
    if cheese not in toppings:
        pizza.get('toppings').append(cheese)

    return pizza


if __name__ == '__main__':
    
    pizza1 = make_pizza_1('tomato', 'cheese', size='L')
    pizza2 = make_pizza_1('tomato', 'cheese', 'olives')
    pizza3 = make_pizza_1('tomato', 'cheese', 'onion', 'mushrooms', size='S')

    print(f'Pizza 1: {pizza1}')
    print(f'Pizza 2: {pizza2}')
    print(f'Pizza 3: {pizza3}')
    print('')

    pizza4 = make_pizza_2('olives', 'onion')
    pizza5 = make_pizza_2('ham', 'mushrooms', 'pepper')
    pizza6 = make_pizza_2('olives', 'pepper', sauce='carbonara', cheese='cheddar', size='L')

    print(f'Pizza 4: {pizza4}')
    print(f'Pizza 5: {pizza5}')
    print(f'Pizza 6: {pizza6}')
