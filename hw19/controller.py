import math

from calculator_interface import Ui_MainWindow


class Control:
    def __init__(self, window):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(window)
        self.ui.pushButton.clicked.connect(self.press_button("1"))
        self.ui.pushButton_2.clicked.connect(self.press_button("2"))
        self.ui.pushButton_3.clicked.connect(self.press_button("3"))
        self.ui.pushButton_4.clicked.connect(self.press_button("4"))
        self.ui.pushButton_5.clicked.connect(self.press_button("5"))
        self.ui.pushButton_6.clicked.connect(self.press_button("6"))
        self.ui.pushButton_7.clicked.connect(self.press_button("7"))
        self.ui.pushButton_8.clicked.connect(self.press_button("8"))
        self.ui.pushButton_9.clicked.connect(self.press_button("9"))
        self.ui.pushButton_10.clicked.connect(self.press_button("0"))
        self.ui.pushButton_11.clicked.connect(self.press_button("+"))
        self.ui.pushButton_12.clicked.connect(self.press_button("-"))
        self.ui.pushButton_13.clicked.connect(self.equal)
        self.ui.pushButton_14.clicked.connect(self.press_button("*"))
        self.ui.pushButton_15.clicked.connect(self.press_button("/"))
        self.ui.pushButton_16.clicked.connect(self.reset)
        self.ui.pushButton_17.clicked.connect(self.press_button("**"))
        self.ui.pushButton_18.clicked.connect(self.sin_num)
        self.ui.pushButton_19.clicked.connect(self.cos_num)
        window.show()

    def press_button(self, symbol):
        def click(*args, **kwargs):
            txt = self.ui.lineEdit.text() + symbol
            self.ui.lineEdit.setText(txt)

        return click

    def equal(self):
        txt = self.ui.lineEdit.text()
        try:
            result = str(eval(txt))
        except SyntaxError:
            result = "error"
        self.ui.lineEdit.setText(result)

    def reset(self):
        txt = self.ui.lineEdit.text()
        result = ""
        self.ui.lineEdit.setText(result)

    def sin_num(self):
        txt = self.ui.lineEdit.text()
        result = math.ceil(math.sin(int(txt)))
        print(result)
        self.ui.lineEdit.setText(str(result))
    def cos_num(self):
        txt = self.ui.lineEdit.text()
        result = math.ceil(math.cos(int(txt)))
        print(result)
        self.ui.lineEdit.setText(str(result))
