from ProgramCompare import *


def setData(data: cyaron.IO, i):
    white = data.input_write
    whiteln = data.input_writeln

    N = 10
    n = randint(1, N)
    n = N
    whiteln(n)
    whiteln(sum(cyaron.Vector.random(n, [(0, n)]), []))
    p = randint(1, N)
    whiteln(p)
    for _ in range(p):
        l, r = randPair(1, n)
        whiteln(l, r, randint(1, 100))
    q = randint(1, N)
    whiteln(q)
    whiteln(sum(cyaron.Vector.random(q, [(0, n)]), []))


std_code = r'D:\Code\CPP\Debug\std.cpp'
cmp_code = r'D:\Code\CPP\Debug\cmp.cpp'
cmp = ProgramCompare(setData, std_code, cmp_code)

cmp.run(5, compare=False)
# cmp.lower_bound()

time.sleep(2)
cmp.clear()