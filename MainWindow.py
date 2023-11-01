import os
import sys
import time

from PyQt5.QtGui import QColor, QFont, QPalette
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QFileDialog, QHBoxLayout, QLabel, QLineEdit, QMainWindow,
                             QPushButton, QTextEdit, QVBoxLayout, QWidget)

from ProgramCompareUI import ProgramCompare


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.std = None
        self.cmp = None
        self.setData = None
        self.programCompare = None

    def initUI(self):
        self.setWindowTitle("ProgramCompare")

        # 创建主窗口的中心部件
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # 创建主布局
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        ########## 创建文件选择部件
        file_layout = QHBoxLayout()
        main_layout.addLayout(file_layout)

        # 创建按钮上传std.cpp
        self.std_button = QPushButton("std.cpp")
        self.std_button.clicked.connect(self.upload_std)
        file_layout.addWidget(self.std_button)

        # 创建按钮上传cmp.cpp
        self.cmp_button = QPushButton("cmp.cpp")
        self.cmp_button.clicked.connect(self.upload_cmp)
        file_layout.addWidget(self.cmp_button)

        # 创建按钮上传setData.py
        self.setData_button = QPushButton("setData.py")
        self.setData_button.clicked.connect(self.upload_setData)
        file_layout.addWidget(self.setData_button)

        # 创建选择菜单设置cppstd
        self.cppstd_comboBox = QComboBox()
        self.cppstd_comboBox.addItem("c++17")
        self.cppstd_comboBox.addItem("c++14")
        self.cppstd_comboBox.addItem("c++11")
        file_layout.addWidget(self.cppstd_comboBox)

        self.compile_button = QPushButton("compile")
        self.compile_button.clicked.connect(self.compile)
        file_layout.addWidget(self.compile_button)

        ########## 创建中心文本框
        self.textbox = QTextEdit()
        self.textbox.setReadOnly(True)  # 设置为只读
        main_layout.addWidget(self.textbox)

        ########## 创建执行部件
        run_layout = QHBoxLayout()
        main_layout.addLayout(run_layout)

        # 创建输入框输入样例数
        self.test_label = QLabel("test number")
        self.testNum_LineEdit = QLineEdit()
        self.testNum_LineEdit.setText("10")
        run_layout.addWidget(self.test_label)
        run_layout.addWidget(self.testNum_LineEdit)

        # 创建选择框选择是否显示输入内容和输出内容
        self.display_input_checkBox = QCheckBox("display_input")
        run_layout.addWidget(self.display_input_checkBox)
        self.display_output_checkBox = QCheckBox("display_output")
        run_layout.addWidget(self.display_output_checkBox)

        # 创建按钮执行makeData
        self.makeData_button = QPushButton("makeData")
        self.makeData_button.clicked.connect(self.makeData)
        run_layout.addWidget(self.makeData_button)

        # 创建按钮执行bruteJudge
        self.bruteJudge_button = QPushButton("bruteJudge")
        self.bruteJudge_button.clicked.connect(self.bruteJudge)
        run_layout.addWidget(self.bruteJudge_button)

    def log(self, message: str):
        self.textbox.append(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}] " + message)

    def upload_std(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "std.cpp", "", "CPP Files (*.cpp)")
        if file_path:
            self.std = file_path
            self.log(f"Upload std.cpp: {file_path}")

    def upload_cmp(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "cmp.cpp", "", "CPP Files (*.cpp)")
        if file_path:
            self.cmp = file_path
            self.log(f"Upload cmp.cpp: {file_path}")

    def upload_setData(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "setData.py", "", "Python Files (*.py)")
        if file_path:
            # 加载生成器
            with open(file_path, "r") as file:
                setData_code = file.read()
            namespace = {}
            exec(setData_code, namespace)
            self.setData = namespace.get("setData")
            self.log(f"Upload setData.py: {file_path}")

    def compile(self):
        if self.std == None or self.cmp == None or self.setData == None:
            self.log("Please upload file first.")
            return
        cppstd = self.cppstd_comboBox.currentText()
        self.log("Compiling...")
        self.programCompare = ProgramCompare(self.setData, self.std, self.cmp, self.textbox.append, cppstd)

    def makeData(self):
        if self.programCompare == None:
            self.log("Please complie first.")
            return
        testNum = int(self.testNum_LineEdit.text())
        for id in range(1, testNum + 1):
            self.programCompare.makeData(id)
        self.log(f"Make {testNum} test data finish.")

    def bruteJudge(self):
        if self.programCompare == None:
            self.log("Please complie first.")
            return
        testNum = int(self.testNum_LineEdit.text())
        display_input = self.display_input_checkBox.isChecked()
        display_output = self.display_output_checkBox.isChecked()
        correct, wrong = 0, 0
        for id in range(1, testNum + 1):
            if self.programCompare.compare(id, display_input, display_output):
                correct += 1
            else:
                wrong += 1
        self.log(f"Brute judge {testNum} test data finish. {correct} correct, {wrong} wrong.")


if __name__ == "__main__":
    # 设置./temp为workspace
    workspace = os.path.join(os.getcwd(), 'temp')
    if not os.path.exists(workspace):
        os.mkdir(workspace)
    os.chdir(workspace)

    font = QFont()
    font.setFamily("Consolas")
    font.setPointSize(14)
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setFont(font)
    window.show()
    window.resize(1024, 640)
    sys.exit(app.exec_())
