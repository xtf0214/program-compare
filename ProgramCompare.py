from io import TextIOWrapper
from random import randint
from tqdm import tqdm
import os

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
        # 数据生成器
        self.setData = setData
        # 编译源代码
        if std.endswith('.exe') and cmp.endswith('.exe'):
            self.std_exe = std
            self.cmp_exe = cmp
        else:
            self.std_exe = os.path.splitext(std)[0] + '.exe'
            self.cmp_exe = os.path.splitext(cmp)[0] + '.exe'
            print(GREEN + 'Compiling...' + CLEAR)
            os.system(
                f'g++ "{std}" -o "{self.std_exe}" -std={cppstd} -{optimize} -w -D_DEBUG -ID:\\Code\\include')
            os.system(
                f'g++ "{cmp}" -o "{self.cmp_exe}" -std={cppstd} -{optimize} -w -D_DEBUG -ID:\\Code\\include')
            print(GREEN + 'Succeed.' + CLEAR)

    def makeData(self, id: int = 1):
        # 使用setData产生样例输入文件
        with open(f'test{id}.in', 'w') as data:
            self.setData(data, id)
        # 使用std_exe产生样例答案文件
        os.system(f'{self.std_exe} < test{id}.in > test{id}.out')

    def compare(self, id: str = 1, display_data_when_correct=False, display_input=False, display_output=False):
        # 获取样例答案和样例输出
        with open(f'test{id}.out', 'r', encoding='utf-8') as f:
            std_out = f.read()
        cmp_out = os.popen(self.cmp_exe + ' < ' + f'test{id}.in').read()
        correct = std_out == cmp_out
        # 输出对拍结果
        if correct:
            print(GREEN + 'AC:' + CLEAR, f'test{id}.in')
        else:
            print(RED + 'WA:' + CLEAR, f'test{id}.in')
        # 输出对拍数据
        if display_data_when_correct or not correct:
            if display_input:
                with open(f'test{id}.in', 'r', encoding='utf-8') as f:
                    print('\033[1;43m' + 'input:' + CLEAR + '\n' + f.read())
            if display_output:
                print('\033[1;44m' + 'std_out:' + CLEAR + '\n' + std_out)
                print('\033[1;45m' + 'cmp_out:' + CLEAR + '\n' + cmp_out)
        return correct

    def lower_bound(self, l: int = 0, r: int = 1e8):
        while r - l > 1:
            mid = (l + r) // 2
            self.makeData(mid)
            if self.compare(mid):
                print(GREEN + f'[{l},{mid})' + CLEAR)
                l = mid
            else:
                print(RED + f'[{mid},{r})' + CLEAR)
                r = mid
        print(GREEN + f'[{l},{r})' + CLEAR)
