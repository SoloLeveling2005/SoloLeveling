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

        desktop = app.desktop()
        self.rect = desktop.availableGeometry()
        print(self.rect)
        # todo Создаем режим вкладок
        self.tabs = QTabWidget()

        # Метод setDocumentMode(True) устанавливает режим документа для QTabWidget, что означает, что каждая вкладка
        # будет иметь свой набор инструментов, относящихся к содержимому этой вкладки. В этом режиме, каждая вкладка
        # будет иметь свой набор кнопок управления, включая кнопки "Назад", "Вперед", "Обновить", а также адресную
        # строку для ввода URL. Это позволяет удобнее управлять содержимым каждой вкладки независимо друг от друга.
        self.tabs.setDocumentMode(True)

        # кликнув по свободному пространству на виджете tabs мы создадим новую вкладку
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)

        # adding action when tab is changed
        self.tabs.currentChanged.connect(self.current_tab_changed)

        # making tabs closeable
        self.tabs.setTabsClosable(True)

        # adding action when tab close is requested
        self.tabs.tabCloseRequested.connect(self.close_current_tab)

        # making tabs as central widget
        self.setCentralWidget(self.tabs)

        # # creating a status bar
        # self.status = QStatusBar()
        #
        # # setting status bar to the main window
        # self.setStatusBar(self.status)

        # creating a tool bar for navigation
        navtb = QToolBar("Navigation")

        # adding tool bar tot he main window
        self.addToolBar(navtb)

        # creating back action
        back_btn = QAction("◄", self)

        # setting status tip
        back_btn.setStatusTip("Back to previous page")

        # adding action to back button
        # making current tab to go back
        back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())

        # adding this to the navigation tool bar
        navtb.addAction(back_btn)

        # similarly adding next button
        next_btn = QAction("►", self)
        next_btn.setStatusTip("Forward to next page")
        next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
        navtb.addAction(next_btn)

        # similarly adding reload button
        reload_btn = QAction("Reload", self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
        navtb.addAction(reload_btn)

        # creating home action
        home_btn = QAction("Home", self)
        home_btn.setStatusTip("Go home")

        # adding action to home button
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        # adding a separator
        navtb.addSeparator()

        # creating a line edit widget for URL
        self.urlbar = QLineEdit()

        # adding action to line edit when return key is pressed
        self.urlbar.returnPressed.connect(self.navigate_to_url)

        # adding line edit to
        navtb.addWidget(self.urlbar)

        # similarly adding stop action
        stop_btn = QAction("Stop", self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
        navtb.addAction(stop_btn)

        # creating first tab
        self.add_new_tab(QUrl('http://www.google.com'), 'Homepage')
        self.resize(self.rect.width(), self.rect.height())
        # showing all the components
        self.show()

        # setting window title
        self.setWindowTitle("SoloLeveling")


    # method for adding new tab
    def add_new_tab(self, qurl=None, label="Blank"):

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
                                     self.tabs.setTabText(i, browser.page().title()[:10] + "...") if len(browser.page().title())>10 else browser.page().title())

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


# todo Program running
app = QApplication(sys.argv)
app.setApplicationName("SoloLeveling")
window = MainWindow()
app.exec_()
