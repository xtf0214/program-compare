# https://github.com/luogu-dev/cyaron/wiki
import math
import os
import time
from random import choice, randint, random, randrange, uniform

import cyaron
from tqdm import tqdm

RED = '\033[1;31m'
GREEN = '\033[1;32m'
CLEAR = '\033[0m'


def randRegion(a: int, b: int):
    """ 返回位数属于区间[a,b)的随机数
    eg : randRegion(1, 2) in [1, 2, 3, 4, 5, 6, 7, 8, 9] """
    n = randint(a, b)
    l, r = 10**(n - 1), 10**n
    return randrange(l, r)


def randVector(Range: tuple, n: int):
    return [randint(*Range) for _ in range(n)]


def randPair(a: int, b: int):
    """ 返回大小属于区间[a,b]的随机数对 """
    l = randint(a, b)
    r = randint(a, b)
    return (l, r) if l < r else (r, l)


class ProgramCompare:

    def __init__(self, setData, std: str, cmp: str, cppstd='c++17', optimize='O2'):

        workspace = os.path.join(os.getcwd(), 'temp')
        if not os.path.exists(workspace):
            os.mkdir(workspace)
        os.chdir(workspace)

        self.setData = setData
        if std.endswith('.exe') and cmp.endswith('.exe'):
            self.std_exe = std
            self.cmp_exe = cmp
        else:
            self.std_exe = os.path.splitext(std)[0] + '.exe'
            self.cmp_exe = os.path.splitext(cmp)[0] + '.exe'
            print(GREEN + 'Compiling...' + CLEAR)
            os.system(f'g++ "{std}" -o "{self.std_exe}" -std={cppstd} -{optimize} -fexec-charset=GBK -w')
            os.system(f'g++ "{cmp}" -o "{self.cmp_exe}" -std={cppstd} -{optimize} -fexec-charset=GBK -w')
            print(GREEN + 'Succeed!' + CLEAR)

    def osCompare(self, i: int = 1):
        std_out = os.popen(self.std_exe + " < " + f'test{i}.in').read()
        cmp_out = os.popen(self.cmp_exe + " < " + f'test{i}.in').read()
        if std_out != cmp_out:
            print(RED + 'WA:' + CLEAR, f'test{i}.in')
            inputs = ''.join([i for i in open(f'test{i}.in', 'r', encoding='utf-8')])
            print('\033[1;42m' + 'input:' + CLEAR + '\n' + inputs)
            print('\033[1;43m' + 'std_out:' + CLEAR + '\n' + std_out)
            print('\033[1;44m' + 'cmp_out:' + CLEAR + '\n' + cmp_out)

    def makeData(self, i: int = 1):
        """ 使用setData()产生数据并用std_exe产生标准输出test.out """
        data = cyaron.IO(file_prefix='test', data_id=i)
        self.setData(data, i)
        data.output_gen(self.std_exe)

    def pyCompare(self, i: int = 1, data_show=True):
        """ 使用setData()产生数据并比较cmp_exe和std_exe的输出 """
        data = cyaron.IO(file_prefix='test', data_id=i, disable_output=True)
        self.setData(data, i)
        try:
            cyaron.Compare.program(self.cmp_exe, input=data, std_program=self.std_exe)
            if data_show:
                print(GREEN + 'AC:' + CLEAR, f'test{i}.in')
            return True
        except:
            if data_show:
                print(RED + 'WA:' + CLEAR, f'test{i}.in')
            return False

    def lower_bound(self, l: int = 0, r: int = 1000000):
        while r - l > 1:
            mid = (l + r) // 2
            if self.pyCompare(mid, False):
                print(GREEN + f'[{l},{mid})' + CLEAR)
                l = mid
            else:
                print(RED + f'[{mid},{r})' + CLEAR)
                r = mid
        print(GREEN + f'[{l},{r})' + CLEAR)

    def run(self, n: int, compare=True, data_show=True):
        if compare:
            for i in range(1, n + 1):
                if not self.pyCompare(i, not data_show):
                    if data_show:
                        self.osCompare(i)
        else:
            for i in tqdm(range(1, n + 1)):
                # time.sleep(math.pow(0.1, math.log10(n) + 1))
                time.sleep(0.1 / n)
                self.makeData(i)

    def clear(self):
        os.system('del *.exe')
        os.system('del *.in')
        os.system('del *.out')