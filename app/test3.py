import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QStyle
# from PyQt5.QtGui import QWindowOpacityChangeEvent
from PyQt5.QtCore import Qt, QRect, QPropertyAnimation, QSize


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Задаем размеры окна и центрируем его на экране
        self.width = 300
        self.height = 200
        self.setGeometry(
            QStyle.alignedRect(
                Qt.LeftToRight,
                Qt.AlignCenter,
                QSize(self.width, self.height),
                QApplication.desktop().availableGeometry()
            )
        )

        # Задаем фоновый цвет окна
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

        # Создаем кнопку
        self.button = QPushButton('Скрыть окно', self)
        self.button.setGeometry(QRect(100, 100, 100, 30))
        self.button.clicked.connect(self.hide_animation)

        # Задаем начальное значение прозрачности окна
        self.setWindowOpacity(1.0)

    def hide_animation(self):
        # Создаем анимацию изменения прозрачности окна
        animation = QPropertyAnimation(self, b'windowOpacity')
        animation.setDuration(1000)
        animation.setStartValue(1.0)
        animation.setEndValue(0.0)

        # Задаем, что после окончания анимации окно будет скрыто
        animation.finished.connect(self.hide)

        # Запускаем анимацию
        animation.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
