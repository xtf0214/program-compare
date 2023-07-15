from random import randint


def randPair(a, b):
    l = randint(a, b)
    r = randint(a, b)
    return (l, r) if l < r else (r, l)


def setData(writeln, id=1):
    a = randint(1, 2e9)
    b = randint(1, 2e9)
    writeln([a, b])