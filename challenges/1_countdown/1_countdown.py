class Countdown:
    def __init__(self, top):
        self.top = top

    def __iter__(self):
        yield from range(self.top, 0, -1)


def countdown(top):
    yield from range(top, 0, -1)


if __name__ == '__main__':

    TOP = 100

    # Con clases
    for i in Countdown(TOP):
        print(i)


    # Sin clases
    # for i in countdown(TOP):
    #     print(i)

