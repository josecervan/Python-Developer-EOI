class Fib:
    def __init__(self, n_terms):
        self.n_terms = n_terms
        self.prev = 1
        self.post = 0
        self.item_n = self.prev + self.post
        self.items = list()

    def __iter__(self):
        self.reps = 0
        return self

    def __next__(self):
        if self.reps < self.n_terms:
            self.item_n = self.calc_item_n(self.prev, self.post)
            self.items.append(self.item_n)
            self.prev = self.post
            self.post = self.item_n

            self.reps += 1
            return self
        raise StopIteration

    def calc_item_n(self, prev, post):
        return prev + post


if __name__ == '__main__':

    N = 6
    sucesion = Fib(N)

    it = iter(sucesion)

    for i in it:
        print(sucesion.item_n)

    print(sucesion.items)


# a_{n+1} = a_n + a_{n-1}
#
# a_0 = 0, a_1 = 1
#
# n = 1:  0 + 1 = 1
# n = 2:  1 + 1 = 2
# n = 3:  1 + 2 = 3
# n = 4:  3 + 2 = 5
# n = 5:  3 + 5 = 8
#                 13
#                 21
#                 34
#                 55
#                 ...

# ant1 = 1
# ant2 = 0
# 
# N = 15
# 
# for _ in range(N):
#     item_n = ant1 + ant2
#     print(item_n)
# 
#     ant2 = ant1
#     ant1 = item_n


