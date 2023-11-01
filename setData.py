from random import randint
from io import TextIOWrapper


def randPair(a, b):
    l = randint(a, b)
    r = randint(a, b)
    return (l, r) if l < r else (r, l)


def setData(data: TextIOWrapper, id=1):
    writeln = lambda *args: print(*args, file=data)
    #########
    a = randint(1, 100)
    b = randint(1, 100)
    writeln(a, b)
