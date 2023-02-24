from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QToolBar, QAction, QToolButton
import sys


class MyToolBar(QToolBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()


    def initUI(self):
        # Создаем экземпляры QAction
        new_action = QAction("New", self)
        open_action = QAction("Open", self)
        save_action = QAction("Save", self)
        exit_action = QAction("Exit", self)

        # Добавляем их на тулбар
        self.addAction(new_action)
        self.addAction(open_action)
        self.addAction(save_action)
        self.addAction(exit_action)


class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.my_widgets = []
        self.setStyleSheet(""
                           "QTabWidget::pane {border: 0;}"
                           "QTabBar::tab { border: none; }"
                           "")

    def initUI(self):
        self.setDocumentMode(True)
        self.setTabsClosable(True)

        my_widgets = []
        widget1 = QWidget()
        widget2 = QWidget()
        widget3 = QWidget()
        my_widgets.append(widget3)
        my_widgets.append(widget2)
        my_widgets.append(widget1)
        self.addTab(widget1, 'Tab 1')
        self.addTab(widget2, 'Tab 2')
        self.addTab(widget3, 'Tab 3')
        self.my_widgets = my_widgets

        # Добавляем тулбары в виджеты
        for widget in self.my_widgets:
            toolbar = MyToolBar(self)
            toolbar.setFixedHeight(40)
            layout = QVBoxLayout(widget)
            layout.addWidget(toolbar)
            layout.setContentsMargins(0,0,0,0)


            qurl = QUrl('http://www.google.com')

            # creating a QWebEngineView object
            browser = QWebEngineView()
            browser.setStyleSheet("margin:0;")
            browser.setUrl(qurl)
            layout.addWidget(browser)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My Application')
        self.setGeometry(100, 100, 800, 600)
        tab_widget = TabWidget()
        self.setCentralWidget(tab_widget)

        self.show()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
