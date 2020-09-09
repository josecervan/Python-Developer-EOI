class Counter:
    def __init__(self, size):
        self.size = size

    def __iter__(self):
        num = 1
        while num <= self.size:
            yield num
            num += 1

    def reverse(self):
        val = self.size
        while val > 0:
            yield val
            val -= 1


if __name__ == '__main__':

    counter = Counter(10)

    for i in counter.reverse():
        print(i)

        