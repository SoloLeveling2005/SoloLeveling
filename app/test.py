# # from PyQt5.QtCore import QUrl
# # from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView
# # from PyQt5.QtWidgets import QApplication
# #
# # app = QApplication([])
# #
# # view = QWebEngineView()
# # page = QWebEnginePage()
# # view.setPage(page)
# #
# # # def on_url_changed(url):
# # #     print('URL changed:', url.toString())
# # #
# # # page.urlChanged.connect(on_url_changed)
# #
# # view.load(QUrl('https://www.google.com'))
# # view.show()
# #
# # app.exec_()
# # #
#
# from PyQt5.QtCore import QUrl
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, QLineEdit, QPushButton, \
#     QSizePolicy
# from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
#
#
# class Browser(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.tabs = QTabWidget()
#         self.tabs.setMinimumSize(1024, 768)
#         self.tabs.setTabsClosable(True)
#         self.tabs.tabCloseRequested.connect(self.close_tab)
#
#         self.new_tab_button = QPushButton('+')
#         self.new_tab_button.clicked.connect(self.new_tab)
#
#         self.url_input = QLineEdit()
#         self.url_input.returnPressed.connect(self.load_url)
#
#         self.layout = QVBoxLayout()
#         self.hlayout = QHBoxLayout()
#         self.hlayout.addWidget(self.url_input)
#         self.hlayout.addWidget(self.new_tab_button)
#         self.layout.addLayout(self.hlayout)
#         self.layout.addWidget(self.tabs)
#
#         self.setLayout(self.layout)
#         # self.new_tab()
#         self.new_tab()
#         self.setWindowTitle("Browser")
#
#     def new_tab(self):
#         view = QWebEngineView()
#         page = QWebEnginePage()
#         view.setPage(page)
#         view.setMinimumSize(1024, 768)
#
#         view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#
#         view.load(QUrl("https://www.google.com"))
#
#         index = self.tabs.addTab(view, "New Tab")
#         self.tabs.setCurrentIndex(index)
#
#     def close_tab(self, index):
#         if self.tabs.count() == 1:
#             self.close()
#         else:
#             self.tabs.removeTab(index)
#
#     def load_url(self):
#         url = self.url_input.text()
#         if url:
#             self.tabs.currentWidget().load(QUrl(url))
#
#
# if __name__ == "__main__":
#     app = QApplication([])
#     browser = Browser()
#     browser.show()
#     app.exec_()


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
    
        grip = QSizeGrip(self)
        self.setCorner(Qt.BottomRightCorner, Qt.RightDockWidgetArea)
        grip.setVisible(True)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.setContentsMargins(0, 0, 0, 0)
        self.setMaximumHeight(QApplication.desktop().availableGeometry().height())

        # получаем размеры экрана
        desktop = app.desktop()
        self.rect = desktop.availableGeometry()
        print(self.rect)
        # Создаем режим вкладок
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setStyleSheet("background-color:grey;")
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)
        self.tabs.currentChanged.connect(self.current_tab_changed)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)

        # making tabs as central widget
        self.setCentralWidget(self.tabs)

        # creating a status bar
        self.status = QStatusBar()
        self.setStatusBar(self.status)

        # creating a tool bar for navigation
        navtb = QToolBar("Navigation")
        navtb.setStyleSheet("background-color:black; color:white; padding:5px;")

        # adding tool bar tot he main window
        self.addToolBar(navtb)

        # creating back action
        icon = QIcon("left.png")
        left_button = QToolButton()
        left_button.setStyleSheet("width:10px;margin:3px;")
        left_button.clicked.connect(lambda: self.tabs.currentWidget().back())
        left_button.setIcon(icon)
        navtb.addWidget(left_button)


        # similarly adding next button
        icon = QIcon("right.png")
        right_button = QToolButton()
        right_button.setStyleSheet("width:10px;margin:3px;")
        right_button.clicked.connect(lambda: self.tabs.currentWidget().forward())
        right_button.setIcon(icon)
        navtb.addWidget(right_button)


        # similarly adding reload button
        icon = QIcon("reload.png")
        reload_button = QToolButton()
        reload_button.setStyleSheet("width:10px;margin:1px;")
        reload_button.clicked.connect(lambda: self.tabs.currentWidget().reload())
        reload_button.setIcon(icon)
        navtb.addWidget(reload_button)

        # creating home action
        icon = QIcon("home.png")
        home_btn = QToolButton()
        home_btn.setStyleSheet("width:10px;margin:3px;")
        home_btn.triggered.connect(self.navigate_home)
        home_btn.setIcon(icon)
        navtb.addWidget(home_btn)


        # adding a separator
        navtb.addSeparator()

        # creating a line edit widget for URL
        self.urlbar = QLineEdit()
        self.urlbar.setStyleSheet("padding:4px 10px; border-radius:6px; border:1px solid white;")
        self.urlbar.returnPressed.connect(self.navigate_to_url)

        navtb.addWidget(self.urlbar)


        # скрыть, закрыть, свернуть
        icon = QIcon("roll_up_in_window.png")
        close_button = QToolButton()
        close_button.clicked.connect(self.showMinimized)
        close_button.setStyleSheet("width:10px;margin:3px;")
        close_button.setIcon(icon)
        navtb.addWidget(close_button)

        icon = QIcon("roll_up.png")
        close_button = QToolButton()
        close_button.clicked.connect(self.maximize)
        close_button.setStyleSheet("width:10px;margin:3px;")
        close_button.setIcon(icon)
        navtb.addWidget(close_button)

        icon = QIcon("close.png")
        close_button = QToolButton()
        close_button.clicked.connect(self.close)
        close_button.setStyleSheet("width:10px;margin:3px;")
        close_button.setIcon(icon)
        navtb.addWidget(close_button)


        # creating first tab
        self.add_new_tab(QUrl('http://www.google.com'), 'Homepage')
        self.setGeometry(0,0,self.rect.width(), self.rect.height())

        # showing all the components
        self.show()

        # setting window title
        self.setWindowTitle("SoloLeveling")

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
    # method for adding new tab
    def add_new_tab(self, qurl=None, label="Homepage"):

        # if url is blank
        if qurl is None:
            # creating a google url
            qurl = QUrl('http://www.google.com')

        # creating a QWebEngineView object
        browser = QWebEngineView()

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

    # when double clicked is pressed on tabs
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

    # when tab is closed
    def close_current_tab(self, i):

        # if there is only one tab
        if self.tabs.count() < 2:
            # do nothing
            return

        # else remove the tab
        self.tabs.removeTab(i)

    # method for updating the title
    def update_title(self, browser):

        # if signal is not from the current tab
        if browser != self.tabs.currentWidget():
            # do nothing
            return

        # get the page title
        title = self.tabs.currentWidget().page().title()
        self.setWindowTitle(title)

    # action to go to home
    def navigate_home(self):

        # go to google
        self.tabs.currentWidget().setUrl(QUrl("http://www.google.com"))

    # method for navigate to url
    def navigate_to_url(self):

        # get the line edit text
        # convert it to QUrl object
        q = QUrl(self.urlbar.text())

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
        self.urlbar.setText(q.toString())

        # set cursor position
        self.urlbar.setCursorPosition(0)

    def mousePressEvent(self, event):
        # Получаем начальные координаты мыши при нажатии на левую кнопку мыши
        if event.button() == Qt.LeftButton:
            # print(self.rect.width())
            # self.resize(self.rect.width()//2, self.rect.height()//2)
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
                self.setGeometry(0,0,self.rect.width(), self.rect.height())
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
window.setGeometry(0,0,rect.width(), rect.height())
window.setStyleSheet("padding:0;")
app.exec_()
