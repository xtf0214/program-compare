# https://github.com/luogu-dev/cyaron/wiki
import math
import os
import time
from random import choice, randint, random, randrange, uniform

import cyaron
from tqdm import tqdm


def randRegion(a, b):
    """ 返回位数属于区间[a,b]的随机数
    eg : randRegion(1, 2) in [1, 2, 3, 4, 5, 6, 7, 8, 9] """
    n = randint(a, b)
    l, r = 10**(n - 1), 10**n
    return randrange(l, r)


def randPair(a, b):
    """ 返回大小属于区间[a,b]的随机数对 """
    l = randint(a, b)
    r = randint(a, b)
    return (l, r) if l < r else (r, l)


class ProgramCompare:

    def __init__(self, setData, std: str, cmp: str, cppstd='c++17', optimize='O2'):
        self.setData = setData
        if std.endswith('.exe') and cmp.endswith('.exe'):
            self.std_exe = std
            self.cmp_exe = cmp
        else:
            self.std_exe = os.path.splitext(std)[0] + '.exe'
            self.cmp_exe = os.path.splitext(cmp)[0] + '.exe'
            print('\033[1;32mCompiling...\033[0m')
            os.system(f'g++ "{std}" -o "{self.std_exe}" -std={cppstd} -{optimize} -fexec-charset=GBK -w')
            os.system(f'g++ "{cmp}" -o "{self.cmp_exe}" -std={cppstd} -{optimize} -fexec-charset=GBK -w')
            print('\033[1;32mSucceed!\033[0m')

    def osCompare(self, i=1):
        input_file = os.path.join(os.getcwd(), f'test{i}.in')
        std_out = os.popen(self.std_exe + " < " + input_file).read()
        cmp_out = os.popen(self.cmp_exe + " < " + input_file).read()
        if std_out != cmp_out:
            print("\033[1;31mWA:\033[0m:", input_file)
            print("\033[1;44mstd_out:\033[0m\n" + std_out)
            print("\033[1;43mcmp_out:\033[0m\n" + cmp_out)

    def makeData(self, i=1):
        """ 使用setData()产生数据并用std_exe产生标准输出test.out """
        data = cyaron.IO(file_prefix='test', data_id=i)
        self.setData(data, i)
        data.output_gen(self.std_exe)

    def pyCompare(self, i=1, data_show=True):
        """ 使用setData()产生数据并比较cmp_exe和std_exe的输出 """
        data = cyaron.IO(file_prefix='test', data_id=i, disable_output=True)
        self.setData(data, i)
        try:
            cyaron.Compare.program(self.cmp_exe, input=data, std_program=self.std_exe)
            if data_show:
                print("\033[1;32mAC:\033[0m", f"test{i}.in")
            return True
        except:
            if data_show:
                print("\033[1;31mWA:\033[0m", f"test{i}.in")
            return False

    def lower_bound(self, l=0, r=1000000):
        while r - l > 1:
            mid = (l + r) // 2
            if self.pyCompare(mid, False):
                print(f"\033[1;32m[{l},{mid})\033[0m")
                l = mid
            else:
                print(f"\033[1;31m[{mid},{r})\033[0m")
                r = mid
        print(f"\033[1;32m[{l},{r})\033[0m")

    def run(self, n, compare=True, data_show=True):
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