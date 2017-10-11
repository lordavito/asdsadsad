import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import calculator_vfx

class Calculator_class(calculator_vfx.Ui_MainWindow, QtWidgets.QMainWindow):

    def __init__(self):
        super(Calculator_class, self).__init__()
        self.setupUi(self)
        #self.display_screen('25662')

        self.btn_0.clicked.connect(lambda: self.display_screen('0'))
        self.btn_1.clicked.connect(lambda: self.display_screen('1'))
        self.btn_2.clicked.connect(lambda: self.display_screen('2'))
        self.btn_3.clicked.connect(lambda: self.display_screen('3'))
        self.btn_4.clicked.connect(lambda: self.display_screen('4'))
        self.btn_5.clicked.connect(lambda: self.display_screen('5'))
        self.btn_6.clicked.connect(lambda: self.display_screen('6'))
        self.btn_7.clicked.connect(lambda: self.display_screen('7'))
        self.btn_8.clicked.connect(lambda: self.display_screen('8'))
        self.btn_9.clicked.connect(lambda: self.display_screen('9'))

        self.btn_add.clicked.connect(lambda: self.display_screen(' + '))
        self.btn_sub.clicked.connect(lambda: self.display_screen(' - '))
        self.btn_multiply.clicked.connect(lambda: self.display_screen(' * '))
        self.btn_divide.clicked.connect(lambda: self.display_screen(' / '))
        self.btn_decimal.clicked.connect(lambda: self.display_screen('.'))

        self.btn_allclear.clicked.connect(self.screen.clear)
        self.btn_clear.clicked.connect(self.screen.backspace)
        self.btn_equals.clicked.connect(self.calculation)
        self.screen.setReadOnly(True)

    def display_screen(self, value):
        """
        this function will insert data to screen
        :param value:
        :return:
        """
        self.screen.insert(value)


    def calculation(self):

        """
        This is a calculation function that will take values from screen
        and pass the values to maths function
        :return:
        """

        screen_value = str(self.screen.text()).split(' ')
        #x = screen_value.split(' ')
        val1 = float(screen_value[0])
        operator = screen_value[1]
        val2 = float(screen_value[2])
        result = self.maths(val1, val2, operator)
        self.screen.setText(str(result))



    def maths(self, val1, val2, operator):

        """ this function will take argument and return output
        :param val1:
        :param val2:
        :param operator:
        :return:
        """
        val1 = float(val1)
        val2 = float(val2)

        if operator is '+':
            return (val1 + val2)
        elif operator is '-':
            return (val1 - val2)
        elif operator is '/':
            return (val1/val2)
        elif operator is '*':
            return (val1 * val2)


#print (calculation(50, 15, 'multiply'))

if __name__ == '__main__':
    qapp = QtWidgets.QApplication(sys.argv)
    calc = Calculator_class()
    calc.show()
    qapp.exec_()
