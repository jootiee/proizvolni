import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint as r


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(
            '/Users/jootiee/Google Drive/visual_studio/python/lyceum/11/2411/proizvolni/UI.ui', self)
        self.do_paint = False
        self.button.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        radius = r(10, 100)
        width = r(1, 400 - radius)
        height = r(1, 300 - radius)
        qp.drawEllipse(width, height, radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
