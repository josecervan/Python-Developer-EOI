class Tshirt:
    def __init__(self, size='L', message='I love Python!'):
        self.size = size
        self.message = message

    def make_tshirt(self):
        print(f'Talla: {self.size}')
        print(f'Mensaje: {self.message}')


if __name__ == '__main__':

    tshirt1 = Tshirt(size='S', message='Python it!')
    tshirt2 = Tshirt(size='M', message='Py me!')
    tshirt3 = Tshirt()
    tshirt4 = Tshirt(size='XL')
    tshirt5 = Tshirt(message='High AF!')

    for tshirt in [tshirt1, tshirt2, tshirt3, tshirt4, tshirt5]:
        tshirt.make_tshirt()
