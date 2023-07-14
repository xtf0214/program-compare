from ProgramCompare import *
from tqdm import tqdm


def setData(data: cyaron.IO = cyaron.IO, id=1):
    write = data.input_write
    writeln = data.input_writeln
    ##########
    a = randint(1, 7)
    b = randint(1, 7)
    writeln(a, b)


def printData(i=1):
    writeln = print
    ##########


def outData(i=1):
    with open(f'output{i}.out', 'w') as f:
        write = lambda x: f.write(str(x) + ' ')
        writeln = lambda x: f.write(str(x) + '\n')
        #########


std = r'D:\Code\CPP\Debug\compare\std.cpp'
cmp = r'D:\Code\CPP\Debug\compare\cmp.cpp'
compare = ProgramCompare(setData, std, cmp, cppstd='c++17')

# ######## make data
# compare.makeData(1e1)
# compare.makeData(1e2)
# compare.makeData(1e3)
# compare.makeData(1e4)
# compare.makeData(1e5)

######### find the first error
# cmp.lower_bound(1, int(1e8))

######### brute test until error
compare.run(10, compare=True, show_input=False, show_output=False)

input(GREEN + 'finish!\n' + CLEAR)
compare.clear()