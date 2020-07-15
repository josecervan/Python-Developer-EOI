
    def __init__(self, n_terms):
        self.n_terms = n_terms
        self.prev = 0
        self.post = 1

    def __iter__(self):
        for _ in range(self.n_terms):
            self.prev, self.post = self.post, self.prev + self.post
            yield self.prev


class FibMax:
    def __init__(self, top):
        self.top = top
        self.prev = 0
        self.post = 1

    def __iter__(self):
        while self.prev <= self.top:
            yield self.prev
            self.prev, self.post = self.post, self.prev + self.post


if __name__ == '__main__':

    N = 10      # Número de términos de la sucesión
    TOP = 55    # Valor máximo de los términos de la sucesión

    # Con clase FibTop
    # for term in FibTop(N):
    #     print(term)

    # Con clase FibMax
    for term in FibMax(TOP):
        print(term)



