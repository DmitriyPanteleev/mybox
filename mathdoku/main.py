import sys  # sys нужен для передачи argv в QApplication

from PyQt5 import QtWidgets

import CalculatorGui

class CalculatorApp(QtWidgets.QMainWindow, CalculatorGui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.calcButton.clicked.connect(self.button_pushed)

    def button_pushed(self):
        self.incl_list = []
        self.excl_list = []
        if self.checkBox_1.isChecked():
            if self.checkBox_15.isChecked():
                self.incl_list = ['conflict']
            else:
                self.incl_list.append('1')
        if self.checkBox_4.isChecked():
            if self.checkBox_12.isChecked():
                self.incl_list = ['conflict']
            else:
                self.incl_list.append('2')
        if self.checkBox_6.isChecked():
            if self.checkBox_14.isChecked():
                self.incl_list = ['conflict']
            else:
                self.incl_list.append('3')
        if self.checkBox_2.isChecked():
            self.incl_list.append('4')
        if self.checkBox_3.isChecked():
            self.incl_list.append('5')
        if self.checkBox_5.isChecked():
            self.incl_list.append('6')
        if self.checkBox_8.isChecked():
            self.incl_list.append('7')
        if self.checkBox_7.isChecked():
            self.incl_list.append('8')
        if self.checkBox_9.isChecked():
            self.incl_list.append('9')

        if self.checkBox_15.isChecked():
            self.excl_list.append('1')
        if self.checkBox_12.isChecked():
            self.excl_list.append('2')
        if self.checkBox_14.isChecked():
            self.excl_list.append('3')
        if self.checkBox_11.isChecked():
            self.excl_list.append('4')
        if self.checkBox_18.isChecked():
            self.excl_list.append('5')
        if self.checkBox_16.isChecked():
            self.excl_list.append('6')
        if self.checkBox_17.isChecked():
            self.excl_list.append('7')
        if self.checkBox_13.isChecked():
            self.excl_list.append('8')
        if self.checkBox_10.isChecked():
            self.excl_list.append('9')        

        self.listWidget.clear()
        self.listWidget.addItem(str(self.incl_list))
        self.listWidget.addItem(str(self.excl_list))

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = CalculatorApp()  # Создаём объект класса CalculatorApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':
    main()
