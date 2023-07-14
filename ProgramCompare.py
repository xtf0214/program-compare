# https://github.com/luogu-dev/cyaron/wiki
import math
import os
import time
from random import randint

import cyaron
from tqdm import tqdm

RED = '\033[1;31m'
GREEN = '\033[1;32m'
CLEAR = '\033[0m'


def randPair(a: int, b: int):
    """ 返回大小属于区间[a,b]的随机数对 """
    l = randint(a, b)
    r = randint(a, b)
    return (l, r) if l < r else (r, l)


class ProgramCompare:

    def __init__(self, setData, std: str, cmp: str, cppstd='c++17', optimize='O2'):
        # 设置./temp为workspace
        workspace = os.path.join(os.getcwd(), 'temp')
        if not os.path.exists(workspace):
            os.mkdir(workspace)
        os.chdir(workspace)
        # 编译源代码
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

    def compare(self, id: int = 1, show_input=True, show_output=True):
        # 产生样例输入
        data = cyaron.IO(file_prefix='test', data_id=id, disable_output=True)
        self.setData(data, id)
        data.close()
        # 获取样例答案和样例输出
        std_out = os.popen(self.std_exe + ' < ' + f'test{id}.in').read()
        cmp_out = os.popen(self.cmp_exe + ' < ' + f'test{id}.in').read()
        if std_out == cmp_out:
            print(GREEN + 'AC:' + CLEAR, f'test{id}.in')
            return True
        else:
            print(RED + 'WA:' + CLEAR, f'test{id}.in')
            if show_input:
                inputs = ''.join([line for line in open(f'test{id}.in', 'r', encoding='utf-8')])
                print('\033[1;42m' + 'input:' + CLEAR + '\n' + inputs)
            if show_output:
                print('\033[1;43m' + 'std_out:' + CLEAR + '\n' + std_out)
                print('\033[1;44m' + 'cmp_out:' + CLEAR + '\n' + cmp_out)
            return False

    def makeData(self, i: int = 1):
        # 使用setData产生样例输入并用std_exe产生样例答案
        data = cyaron.IO(file_prefix='test', data_id=i)
        self.setData(data, i)
        data.output_gen(self.std_exe)
        data.close()

    def lower_bound(self, l: int = 0, r: int = 1e6):
        while r - l > 1:
            mid = (l + r) // 2
            if self.compare(mid, False, False):
                print(GREEN + f'[{l},{mid})' + CLEAR)
                l = mid
            else:
                print(RED + f'[{mid},{r})' + CLEAR)
                r = mid
        print(GREEN + f'[{l},{r})' + CLEAR)

    def run(self, n: int, compare=True, show_input=True, show_output=True):
        if compare:
            for id in range(1, n + 1):
                self.compare(id, show_input, show_output)
        else:
            for id in tqdm(range(1, n + 1)):
                time.sleep(0.1 / n)
                self.makeData(id)

    def clear(self):
        os.system('del *.exe')
        os.system('del *.in')
        os.system('del *.out')