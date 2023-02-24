
# def on_url_changed(url):
#     print('URL changed:', url.toString())
#
# page.urlChanged.connect(on_url_changed)


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
        self.browser = None
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
        grip.setStyleSheet("padding:0; margin:0;")

        # Создаем виджет вкладок
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setStyleSheet("background-color:grey; margin:0; padding:0;")
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)
        self.tabs.currentChanged.connect(self.current_tab_changed)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)

        # размещаем виджет вкладок tabs по центру страницы
        self.setCentralWidget(self.tabs)

        # добавляем toolbar
        self.tool_bar = self.new_toolbar()

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

                                    }
                                    QTabBar::tab:selected {
                                        background-color: black;
                                        border-color: white;
                                    }
                                """)

    # создаем панель инструментов
    def new_toolbar(self):
        self.tool_bar = QToolBar("Navigation")
        self.tool_bar.setMovable(False)
        self.tool_bar.setStyleSheet("background-color:black; color:white; padding:5px;")
        # adding tool bar tot he main window
        # self.addToolBar(self.tool_bar)

        # переключиться на вкладку назад
        self.create_icon_button(icon_url="left.png",
                                action=lambda: self.browser.back(),
                                styles="width:10px;margin:3px;")

        # переключиться на вкладку вперед
        self.create_icon_button(icon_url="right.png",
                                action=lambda: self.browser.forward(),
                                styles="width:10px;margin:3px;")

        # перезагрузка страницы
        self.create_icon_button(icon_url="reload.png",
                                action=lambda: self.browser.reload(),
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
        return self.tool_bar
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
        if qurl is None:
            qurl = QUrl('http://www.google.com')

        # создаем новый toolbar для каждой вкладки
        tool_bar = self.new_toolbar()

        browser = QWebEngineView()
        layout = QVBoxLayout()
        layout.addWidget(tool_bar)
        layout.addWidget(browser)
        layout.setContentsMargins(0,0,0,0)
        browser.load(QUrl(qurl))

        widget = QWidget()
        widget.setLayout(layout)

        i = self.tabs.addTab(widget, label)

        # сохраняем ссылку на toolbar в user data для вкладки
        self.tabs.setCurrentIndex(i)

        browser.urlChanged.connect(lambda qurl, browser=browser:
                                   self.update_urlbar(qurl, browser))

        browser.loadFinished.connect(lambda _, i=i, browser=browser:
                                     self.tabs.setTabText(i, browser.page().title()[:10] + "...") if len(
                                         browser.page().title()) > 10 else browser.page().title())

        # сохраняем ссылку на текущий QWebEngineView
        self.browser = browser

    # открытие новой вкладки при двойном клике
    def tab_open_doubleclick(self, i):

        # checking index i.e
        # No tab under the click
        if i == -1:
            # creating a new tab
            self.add_new_tab()

    def current_tab_changed(self, i):
        # print(self.tabs.currentWidget().url())
        print(i)
        widget = self.tabs.widget(i)
        try:
            qurl = widget.url()
            self.update_urlbar(qurl, self.tabs.currentWidget())
            self.update_title(self.tabs.currentWidget())
        except:
            pass
    # закрытие вкладки
    def close_current_tab(self, i):

        # если вкладка одна, закрываем браузер
        if self.tabs.count() < 2:
            self.close()
            return

        # удаляем вкладкуу
        self.tabs.removeTab(i)

    # обновление заголовка страницы
    def update_title(self, browser):

        # if signal is not from the current tab
        if browser != self.tabs.currentWidget():
            # do nothing
            print("Noo")
            return

        # get the page title
        title = self.tabs.currentWidget().page().title()
        self.setWindowTitle(title)

    # переходим в домашнюю страницу браузера
    def navigate_home(self):
        print("Go home")
        # go to google
        self.browser.setUrl(QUrl("http://www.google.com"))

    # method for navigate to url
    def navigate_to_url(self):

        # convert it to QUrl object
        q = QUrl(self.url.text())

        # if scheme is blank
        if q.scheme() == "":
            # set scheme
            q.setScheme("http")

        # set the url
        self.browser.setUrl(q)

    # method to update the url
    def update_urlbar(self, q, browser=None):
        print("update_urlbar")
        # If this signal is not from the current tab, ignore
        # if browser != self.tabs.currentWidget():
        #     return

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
app.exec_()
