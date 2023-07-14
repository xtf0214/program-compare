from io import TextIOWrapper
from random import randint


def setData(file: TextIOWrapper, id=1):
    write = lambda *x: file.write(' '.join([str(i) for i in x]) + ' ')
    writeln = lambda *x: file.write(' '.join([str(i) for i in x]) + '\n')
    ###################
    a = randint(1, 2e9)
    b = randint(1, 2e9)
    writeln(a, b)