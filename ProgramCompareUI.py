import os


def setColor(strs, color):
    return f"<span style='color: {color};font-weight: bold;'>{strs}</span>"


class ProgramCompare:

    def __init__(self, setData, std: str, cmp: str, log, cppstd='c++17', optimize='O2'):
        # 数据生成器
        self.setData = setData
        self.log = log
        # 编译源代码
        self.std_exe = os.path.splitext(std)[0] + '.exe'
        self.cmp_exe = os.path.splitext(cmp)[0] + '.exe'
        if os.system(f'g++ "{std}" -o "{self.std_exe}" -std={cppstd} -{optimize} -w') != 0:
            log(setColor("std.cpp compile failed.", "red"))
        elif os.system(f'g++ "{cmp}" -o "{self.cmp_exe}" -std={cppstd} -{optimize} -w') != 0:
            log(setColor("cmp.cpp compile failed.", "red"))
        else:
            log(setColor("Compile successful.", "green"))

    def makeData(self, id=1):
        # 使用setData产生样例输入文件
        with open(f'test{id}.in', 'w') as data:
            self.setData(data, id)
        # 使用std_exe产生样例答案文件
        os.system(f'{self.std_exe} < test{id}.in > test{id}.out')

    def compare(self, id=1, display_input=False, display_output=False):
        # 获取样例答案和样例输出
        with open(f'test{id}.out', 'r') as f:
            std_out = f.read()
        cmp_out = os.popen(self.cmp_exe + ' < ' + f'test{id}.in').read()
        correct = std_out == cmp_out
        # 输出对拍结果
        if correct:
            self.log(setColor('AC:', 'green') + f'test{id}.in')
        else:
            self.log(setColor('WA:', 'red') + f'test{id}.in')
        if display_input:
            with open(f'test{id}.in', 'r', encoding='utf-8') as f:
                self.log(setColor('input:', 'Chocolate'))
                self.log(f.read())
        if display_output:
            self.log(setColor('std_out:', 'blue'))
            self.log(std_out)
            self.log(setColor('cmp_out:', 'purple'))
            self.log(cmp_out)
        return correct
