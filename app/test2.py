from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication

class Window(QWidget):
    def __init__(self):
        super().__init__()


        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)

        # Растягиваем окно на всю ширину экрана при достижении верхней границы
        self.setContentsMargins(0, 0, 0, 0)
        self.setMinimumHeight(100)
        self.setMaximumHeight(QApplication.desktop().availableGeometry().height())
        # Создаем кнопки для закрытия, сворачивания и разворачивания окна
        close_button = QPushButton("Закрыть")
        close_button.clicked.connect(self.close)

        minimize_button = QPushButton("Свернуть")
        minimize_button.clicked.connect(self.showMinimized)

        maximize_button = QPushButton("Развернуть")
        maximize_button.clicked.connect(self.maximize)

        # Создаем горизонтальный лайаут для кнопок
        button_layout = QHBoxLayout()
        button_layout.addWidget(close_button)
        button_layout.addWidget(minimize_button)
        button_layout.addWidget(maximize_button)

        # Создаем вертикальный лайаут для горизонтального лайаута с кнопками и добавляем его на виджет
        main_layout = QVBoxLayout()
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

        # Устанавливаем флаг Qt.FramelessWindowHint, чтобы сделать окно без рамки и возможности перетаскивания
        self.setWindowFlags(Qt.FramelessWindowHint)

    def mousePressEvent(self, event):
        # Получаем начальные координаты мыши при нажатии на левую кнопку мыши
        if event.button() == Qt.LeftButton:
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        # Перетаскиваем окно, если левая кнопка мыши была нажата и перемещена на новые координаты
        if event.buttons() == Qt.LeftButton:
            x = event.globalX()
            y = event.globalY()
            self.move(x - self.offset.x(), y - self.offset.y())

    def maximize(self):
        # Разворачиваем или сворачиваем окно при нажатии на кнопку "Развернуть"
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec_()
# importing libraries
