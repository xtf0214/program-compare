# https://github.com/luogu-dev/cyaron/wiki
import os


def setColor(s, color):
    return f"<span style='color: {color};font-weight: bold;'>{s}</span>"


class ProgramCompare:

    def __init__(self, setData, std: str, cmp: str, writeln, cppstd='c++17', optimize='O2'):
        # 编译源代码
        self.setData = setData
        self.writeln = writeln
        self.std_exe = os.path.splitext(std)[0] + '.exe'
        self.cmp_exe = os.path.splitext(cmp)[0] + '.exe'
        if os.system(f'g++ "{std}" -o "{self.std_exe}" -std={cppstd} -{optimize} -fexec-charset=GBK -w') != 0:
            writeln(setColor("std.cpp compile failed.", "red"))
        elif os.system(f'g++ "{cmp}" -o "{self.cmp_exe}" -std={cppstd} -{optimize} -fexec-charset=GBK -w') != 0:
            writeln(setColor("cmp.cpp compile failed.", "red"))
        else:
            writeln(setColor("Compile successful.", "green"))

    def __del__(self):
        os.system('del *.exe')

    def compare(self, id: int = 1, show_input=True, show_output=True):
        # 产生样例输入
        with open(f'test{id}.in', 'w') as file:
            self.setData(file, id)
        # 获取样例答案和样例输出
        std_out = os.popen(self.std_exe + ' < ' + f'test{id}.in').read()
        cmp_out = os.popen(self.cmp_exe + ' < ' + f'test{id}.in').read()
        if std_out == cmp_out:
            self.writeln(setColor('AC:', 'green') + f'test{id}.in')
            return True
        else:
            self.writeln(setColor('WA:', 'red') + f'test{id}.in')
            if show_input:
                with open(f'test{id}.in', 'r', encoding='utf-8') as file:
                    self.writeln(setColor('input:', 'Chocolate'))
                    self.writeln(file.read())
            if show_output:
                self.writeln(setColor('std_out:', 'blue'))
                self.writeln(std_out)
                self.writeln(setColor('cmp_out:', 'purple'))
                self.writeln(cmp_out)
            return False

    def makeData(self, id: int = 1):
        # 使用setData产生样例输入并用std_exe产生样例答案
        with open(f'test{id}.in', 'w') as file:
            self.setData(file, id)
        os.system(f'{self.std_exe} < test{id}.in > test{id}.out')