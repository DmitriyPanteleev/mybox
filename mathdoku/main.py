import sys  # sys нужен для передачи argv в QApplication

from PyQt5 import QtWidgets

import CalculatorGui
import mdcalc

class CalculatorApp(QtWidgets.QMainWindow, CalculatorGui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Chekboxes
        self.checkBox_1.toggled.connect(self.checkBox_15.setDisabled)
        self.checkBox_1.toggled.connect(
            lambda checked: checked and self.checkBox_15.setChecked(False)
        )

        self.checkBox_15.toggled.connect(self.checkBox_1.setDisabled)
        self.checkBox_15.toggled.connect(
            lambda checked: checked and self.checkBox_1.setChecked(False)
        )

        self.checkBox_4.toggled.connect(self.checkBox_12.setDisabled)
        self.checkBox_4.toggled.connect(
            lambda checked: checked and self.checkBox_12.setChecked(False)
        )

        self.checkBox_12.toggled.connect(self.checkBox_4.setDisabled)
        self.checkBox_12.toggled.connect(
            lambda checked: checked and self.checkBox_4.setChecked(False)
        )

        self.checkBox_6.toggled.connect(self.checkBox_14.setDisabled)
        self.checkBox_6.toggled.connect(
            lambda checked: checked and self.checkBox_14.setChecked(False)
        )

        self.checkBox_14.toggled.connect(self.checkBox_6.setDisabled)
        self.checkBox_14.toggled.connect(
            lambda checked: checked and self.checkBox_6.setChecked(False)
        )

        self.checkBox_2.toggled.connect(self.checkBox_11.setDisabled)
        self.checkBox_2.toggled.connect(
            lambda checked: checked and self.checkBox_11.setChecked(False)
        )

        self.checkBox_11.toggled.connect(self.checkBox_2.setDisabled)
        self.checkBox_11.toggled.connect(
            lambda checked: checked and self.checkBox_2.setChecked(False)
        )

        self.checkBox_3.toggled.connect(self.checkBox_18.setDisabled)
        self.checkBox_3.toggled.connect(
            lambda checked: checked and self.checkBox_18.setChecked(False)
        )

        self.checkBox_18.toggled.connect(self.checkBox_3.setDisabled)
        self.checkBox_18.toggled.connect(
            lambda checked: checked and self.checkBox_3.setChecked(False)
        )

        self.checkBox_5.toggled.connect(self.checkBox_16.setDisabled)
        self.checkBox_5.toggled.connect(
            lambda checked: checked and self.checkBox_16.setChecked(False)
        )

        self.checkBox_16.toggled.connect(self.checkBox_5.setDisabled)
        self.checkBox_16.toggled.connect(
            lambda checked: checked and self.checkBox_5.setChecked(False)
        )

        self.checkBox_8.toggled.connect(self.checkBox_17.setDisabled)
        self.checkBox_8.toggled.connect(
            lambda checked: checked and self.checkBox_17.setChecked(False)
        )

        self.checkBox_17.toggled.connect(self.checkBox_8.setDisabled)
        self.checkBox_17.toggled.connect(
            lambda checked: checked and self.checkBox_8.setChecked(False)
        )

        self.checkBox_7.toggled.connect(self.checkBox_13.setDisabled)
        self.checkBox_7.toggled.connect(
            lambda checked: checked and self.checkBox_13.setChecked(False)
        )

        self.checkBox_13.toggled.connect(self.checkBox_7.setDisabled)
        self.checkBox_13.toggled.connect(
            lambda checked: checked and self.checkBox_7.setChecked(False)
        )

        self.checkBox_9.toggled.connect(self.checkBox_10.setDisabled)
        self.checkBox_9.toggled.connect(
            lambda checked: checked and self.checkBox_10.setChecked(False)
        )

        self.checkBox_10.toggled.connect(self.checkBox_9.setDisabled)
        self.checkBox_10.toggled.connect(
            lambda checked: checked and self.checkBox_9.setChecked(False)
        )

        # Push the button
        self.calcButton.clicked.connect(self.button_pushed)

    def button_pushed(self):
        self.demenition = int(self.comboBox.currentText())
        self.finalvol = int(self.lineEdit_2.text())
        self.quantity = int(self.lineEdit.text())
        self.operand = self.comboBox_2.currentText()
        self.intersection = int(self.comboBox_3.currentText())
        self.incl_list = []
        self.excl_list = []
        if self.checkBox_1.isChecked():
            self.incl_list.append('1')
        if self.checkBox_4.isChecked():
            self.incl_list.append('2')
        if self.checkBox_6.isChecked():
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

        sorted_result = mdcalc.mdcalc(self.demenition,self.finalvol,self.quantity,self.operand)
        real_result = mdcalc.cleaning(sorted_result,self.incl_list,self.excl_list,self.demenition,self.intersection)
        
        self.listWidget.clear()
        for item in real_result:
            self.listWidget.addItem(str(item))

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = CalculatorApp()  # Создаём объект класса CalculatorApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':
    main()
