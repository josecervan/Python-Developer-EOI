def positive(seq):
    for x in seq:
         if x > 0:
             yield x


def every_other(gen):
    for x in gen:
        yield x
        next(gen)


def twice(seq):
    for x in seq:
        yield x
        yield x


if __name__ == '__main__':

    seq = range(-5, 5)
    pos = positive(seq)
    skip = every_other(pos)
    two = twice(skip)

    for x in two:
        print(x)