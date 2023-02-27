# from PyQt5.QtCore import QUrl
# from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView
# from PyQt5.QtWidgets import QApplication
#
# app = QApplication([])
#
# view = QWebEngineView()
# page = QWebEnginePage()
# view.setPage(page)
#
# def on_url_changed(url):
#     print('URL changed:', url.toString())
#
# page.urlChanged.connect(on_url_changed)
#
# view.load(QUrl('https://www.google.com'))
# view.show()
#
# app.exec_()
#


# importing required libraries
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import os
import sys


# main window
class MainWindow(QMainWindow):

    # constructor
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # получаем размеры экрана
        desktop_info = app.desktop()
        self.rect = desktop_info.availableGeometry()
        # начальные настройки
        self.setWindowTitle("SoloLeveling")
        self.setCorner(Qt.BottomRightCorner, Qt.RightDockWidgetArea)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.setContentsMargins(0, 0, 0, 0)
        self.setMaximumHeight(QApplication.desktop().availableGeometry().height())
        self.setGeometry(0, 0, self.rect.width(), self.rect.height())

        grip = QSizeGrip(self)
        grip.setVisible(True)

        # Создаем виджет вкладок
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setStyleSheet("background-color:grey;")
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)
        self.tabs.currentChanged.connect(self.current_tab_changed)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)

        # размещаем виджет вкладок tabs по центру страницы
        self.setCentralWidget(self.tabs)

        # создаем панель инструментов
        self.tool_bar = QToolBar("Navigation")
        self.tool_bar.setMovable(False)
        self.tool_bar.setStyleSheet("background-color:black; color:white; padding:5px;")

        # adding tool bar tot he main window
        self.addToolBar(self.tool_bar)

        # переключиться на вкладку назад
        self.create_icon_button(icon_url="left.png",
                                action=lambda: self.tabs.currentWidget().back(),
                                styles="width:10px;margin:3px;")

        # переключиться на вкладку вперед
        self.create_icon_button(icon_url="right.png",
                                action=lambda: self.tabs.currentWidget().forward(),
                                styles="width:10px;margin:3px;")

        # перезагрузка страницы
        self.create_icon_button(icon_url="reload.png",
                                action=lambda: self.tabs.currentWidget().reload(),
                                styles="width:10px;margin:3px;")

        # кнопки перехода на домашнюю страницу
        self.create_icon_button(icon_url="home.png",
                                action=self.navigate_home,
                                styles="width:10px;margin:3px;")

        # adding a separator
        self.tool_bar.addSeparator()

        # создаем поле в котором отображается url и где делают запросы
        self.url_bar = QLineEdit()
        self.url_bar.setStyleSheet("padding:4px 10px; border-radius:6px; border:1px solid white;")
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        self.tool_bar.addWidget(self.url_bar)

        # скрыть, закрыть, свернуть
        self.create_icon_button(icon_url="roll_up_in_window.png",
                                action=self.showMinimized,
                                styles="width:10px;margin:3px;")

        self.create_icon_button(icon_url="roll_up.png",
                                action=self.maximize,
                                styles="width:10px;margin:3px;")

        self.create_icon_button(icon_url="close.png",
                                action=self.close,
                                styles="width:10px;margin:3px;")

        # создаем первую вкладку домашней страницы
        self.add_new_tab(QUrl('http://www.google.com'), 'Homepage')

        # отображение страницы
        self.show()

        # стилизируем
        self.tabs.setStyleSheet("""
                                    QTabBar::tab {
                                        background-color: #161a1d;
                                        color: white;
                                        border-left: 1px solid gray;
                                        border-bottom: 1px solid gray;
                                        border-right: 1px solid gray;
                                        border-bottom-left-radius: 4px;
                                        border-bottom-right-radius: 4px;
                                        padding: 4px;
                                        margin: 0 3px;
                                    }
                                    QTabBar::tab:selected {
                                        background-color: black;
                                        border-color: white;
                                    }
                                """)

    # создание кнопки с иконой
    def create_icon_button(self, icon_url: str, action, styles: str):
        icon = QIcon(icon_url)
        button = QToolButton()
        button.clicked.connect(action)
        button.setStyleSheet(styles)
        button.setIcon(icon)
        self.tool_bar.addWidget(button)

    # добавление новой вкладки
    def add_new_tab(self, qurl=None, label="Homepage"):

        # if url is blank
        if qurl is None:
            # creating a google url
            qurl = QUrl('http://www.google.com')

        # creating a QWebEngineView object
        browser = QWebEngineView()
        browser.setStyleSheet("border:0;")

        # setting url to browser
        browser.setUrl(qurl)
        # setting tab index
        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)

        # Эта строка кода устанавливает соединение между сигналом urlChanged от объекта QWebEngineView и слотом,
        # который обновляет строку адреса URL.
        #
        # Когда пользователь перемещается по страницам, загруженным в QWebEngineView, объект QWebEngineView
        # генерирует сигнал urlChanged, который содержит новый URL.
        #
        # С помощью этой строки кода устанавливается обработчик для сигнала urlChanged, который вызывает слот
        # update_urlbar(), который обновляет строку адреса URL в соответствии с новым URL.
        #
        # В лямбда-функции также передается объект browser, чтобы получить доступ к объекту Browser внутри слота
        # update_urlbar().

        browser.urlChanged.connect(lambda qurl, browser=browser:
                                   self.update_urlbar(qurl, browser))

        # Эта строка кода устанавливает соединение между сигналом loadFinished объекта QWebEngineView и
        # лямбда-функцией, которая обновляет заголовок текущей вкладки в QTabWidget после загрузки страницы.
        #
        # Когда страница загружена в QWebEngineView, объект QWebEngineView генерирует сигнал loadFinished,
        # который сообщает об окончании загрузки страницы.

        browser.loadFinished.connect(lambda _, i=i, browser=browser:
                                     self.tabs.setTabText(i, browser.page().title()[:10] + "...") if len(
                                         browser.page().title()) > 10 else browser.page().title())

    # открытие новой вкладки при двойном клике
    def tab_open_doubleclick(self, i):

        # checking index i.e
        # No tab under the click
        if i == -1:
            # creating a new tab
            self.add_new_tab()

    # when tab is changed
    def current_tab_changed(self, i):

        # get the curl
        qurl = self.tabs.currentWidget().url()

        # update the url
        self.update_urlbar(qurl, self.tabs.currentWidget())

        # update the title
        self.update_title(self.tabs.currentWidget())

    # закрытие вкладки
    def close_current_tab(self, i):

        # если вкладка одна, закрываем браузер
        if self.tabs.count() < 2:
            self.close()

        # удаляем вкладкуу
        self.tabs.removeTab(i)

    # обновление заголовка страницы
    def update_title(self, browser):

        # if signal is not from the current tab
        if browser != self.tabs.currentWidget():
            # do nothing
            return

        # get the page title
        title = self.tabs.currentWidget().page().title()
        self.setWindowTitle(title)

    # переходим в домашнюю страницу браузера
    def navigate_home(self):
        print("Go home")
        # go to google
        self.tabs.currentWidget().setUrl(QUrl("http://www.google.com"))

    # method for navigate to url
    def navigate_to_url(self):

        # get the line edit text
        # convert it to QUrl object
        q = QUrl(self.url_bar.text())

        # if scheme is blank
        if q.scheme() == "":
            # set scheme
            q.setScheme("http")

        # set the url
        self.tabs.currentWidget().setUrl(q)

    # method to update the url
    def update_urlbar(self, q, browser=None):

        # If this signal is not from the current tab, ignore
        if browser != self.tabs.currentWidget():
            return
        # print(q.toString())
        # set text to the url bar
        self.url_bar.setText(q.toString())

        # set cursor position
        self.url_bar.setCursorPosition(0)

    # функции управления окном браузера
    def mousePressEvent(self, event):
        # Получаем начальные координаты мыши при нажатии на левую кнопку мыши
        if event.button() == Qt.LeftButton:
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        # Перетаскиваем окно, если левая кнопка мыши была нажата и перемещена на новые координаты
        if event.buttons() == Qt.LeftButton:
            x = event.globalX()
            y = event.globalY()
            print(x - self.offset.x(), y - self.offset.y())
            self.move(x - self.offset.x(), y - self.offset.y())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mousePressed = False
            event.accept()
            print(event.globalY())
            if event.globalY() < 20 or event.globalY() == 0:
                self.setGeometry(0, 0, self.rect.width(), self.rect.height())
                print("self.showMaximized()")

    def maximize(self):
        # Разворачиваем или сворачиваем окно при нажатии на кнопку "Развернуть"
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()


# todo Program running
app = QApplication(sys.argv)
app.setApplicationName("SoloLeveling")
desktop = app.desktop()
rect = desktop.availableGeometry()
window = MainWindow()
window.setGeometry(0, 0, rect.width(), rect.height())
window.setStyleSheet("padding:0;")
app.exec_()


