import random


class Lista:

    def __init__(self, lista):
        self.lista = lista

    def __str__(self):
        return str(self.lista)

    def __len__(self):
        return len(self.lista)

    def __add__(self, other):
        return self.lista + other.lista

    def __mul__(self, other):
        return self.lista * len(other.lista)

    def __lt__(self, other):
        return len(self.lista) < len(other.lista)

    def __gt__(self, other):
        return len(self.lista) > len(other.lista)

    def __eq__(self, other):
        return self.lista == other.lista

if __name__ == '__main__':

    randlist_a = random.sample(range(50), random.randint(1, 10))
    list_a = Lista(randlist_a)

    randlist_b = random.sample(range(50), random.randint(1, 10))
    list_b = Lista(randlist_b)

    print(list_a, len(list_a))
    print(list_b, len(list_b))
    print('--')
    print(list_a + list_b)
    print(list_a * list_b)
    print(list_a < list_b)
    print(list_a > list_b)
    print(list_a == list_b)
