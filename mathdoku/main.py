import sys  # sys нужен для передачи argv в QApplication

from PyQt5 import QtWidgets

import CalculatorGui

class CalculatorApp(QtWidgets.QMainWindow, CalculatorGui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.calcButton.clicked.connect(self.button_pushed)  # Выполнить функцию browse_folder при нажатии кнопки

    def button_pushed(self):
        self.listWidget.addItem(str(self.checkBox_1.isChecked()))

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = CalculatorApp()  # Создаём объект класса CalculatorApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
