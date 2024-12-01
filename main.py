import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QPoint


class CircleWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Random Circles")
        self.setGeometry(100, 100, 500, 500)

        self.button = QPushButton("Нарисовать кружочки", self)
        self.button.setGeometry(180, 20, 140, 40)
        self.button.clicked.connect(self.add_circle)

        self.circles = []

    def add_circle(self):
        x = random.randint(50, self.width() - 50)
        y = random.randint(100, self.height() - 50)
        radius = random.randint(10, 80)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.circles.append((x, y, radius, color))
        self.update()

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.begin(self)
        for circle in self.circles:
            x, y, radius, color = circle
            qp.setBrush(color)
            qp.drawEllipse(QPoint(x, y), radius, radius)
        qp.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CircleWindow()
    window.show()
    sys.exit(app.exec())
