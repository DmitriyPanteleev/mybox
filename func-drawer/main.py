import sys  # sys нужен для передачи argv в QApplication
import math

from PIL import Image, ImageColor
from PIL import ImageDraw

from PyQt5 import QtWidgets

import interface  # Это наш конвертированный файл дизайна

class MainApp(QtWidgets.QMainWindow, interface.Ui_MainWindow):
    def __init__(self):
        super().__init__() # Это здесь нужно для доступа к переменным, методам и т.д. в файле interface.py
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.buttonDrawGraph.clicked.connect(self.draw_graph)  # Выполнить функцию browse_folder

    def draw_graph(self):
        sizewidth = 1000 # size of pictures in pixels
        sizeheight = 1000 # size of pictures in pixels
        formule = "x**2 + y**2 - 2500" # formula of function

        # real area of drawing
        xmin = -100
        xmax = 100
        xlen = abs((xmax-xmin) / sizewidth)
        ymin = -100
        ymax = 100
        ylen = abs((ymax-ymin) / sizeheight)

        def mfunc(x,y,exec_formule):
            return eval(exec_formule)

        image = Image.new("RGB", (sizewidth, sizeheight))
        draw = ImageDraw.Draw(image)

        xr = xmin
        yr = ymin
        f1 = mfunc(xr,yr,formule)
        f2 = mfunc(xr,yr + ylen,formule)
        f3 = mfunc(xr + xlen,yr,formule)
        f4 = mfunc(xr + xlen,yr + ylen,formule)

        for x in range(sizewidth):
            xr = xmin + x * xlen
            for y in range(sizeheight):
                yr = ymin + y * ylen

                f2 = mfunc(xr,yr + ylen,formule)
                f4 = mfunc(xr + xlen,yr + ylen,formule)

                if (f1 > 0 and f2 > 0 and f3 > 0 and f3 > 0) or (f1 < 0 and f2 < 0 and f3 < 0 and f3 < 0) :
                    continue
                draw.point((x, y), fill=ImageColor.getrgb("red"))

                f1 = f2
                f3 = f4

        image.save("/home/dpanteleev/SomeStuff/mybox/func-drawer/empty.png", "PNG")

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainApp()  # Создаём объект класса MainApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()