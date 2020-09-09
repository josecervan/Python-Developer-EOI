class Element:

    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print(self.name)
        print(self.symbol)
        print(str(self.number))

    def __str__(self):
        return(f'{self.name} {self.symbol} {self.number}')


if __name__ == '__main__':
    el1 = Element('Hydrogen', 'H', 1)
    print(el1)
