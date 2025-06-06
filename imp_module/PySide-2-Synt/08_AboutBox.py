import sys
from PySide2.QtWidgets import \
    QApplication, QWidget, QPushButton, QMessageBox,\
    QDesktopWidget, QLabel, QToolBar

from PySide2.QtGui import QIcon, QPixmap, QFont

# Квласс Наследует от QWidget.
# Получаем доступ ко всем возможностям класса QWidget.
class Window(QWidget):
    def __init__(self): # Консеруктор
        super().__init__()
        self.setWindowTitle("About Box Creat") # Title.
        self.setGeometry(300, 300, 300, 300) # Положения окна.

        self.setIcon()
        self.setButton()
        self.center()

        self.pushButton()
    def setIcon(self):
        appicon =QIcon("feather/anchor.svg")
        self.setWindowIcon(appicon)


    # -----------------------------------------------
    # Кнопка отправки Сообщения
    def pushButton(self):
        self.aboutButton = QPushButton("Open About Box", self)
        self.aboutButton.move(20, 50)
        self.aboutButton.clicked.connect(self.aboutBox)

    # Окно сообшения.
    def aboutBox(self):
        QMessageBox.about(self.aboutButton, "About Pysibe_2", "Crodss pay")

    # -----------------------------------------------
    # Центрирования Окна на мониторе.
    def center(self):
        qReact = self.frameGeometry() # Очередь
        centerPoint = QDesktopWidget().availableGeometry().center()
        qReact.moveCenter(centerPoint)
        self.move(qReact.topLeft())

    # -----------------------------------------------
    # Отрисовка кнопки.
    def setButton(self):
        btn_1 = QPushButton("Quit", self) # Названия.
        btn_1.move(50, 100)
        # Действие по Слушателю.
        btn_1.clicked.connect(self.quiteApp)

    # Слушатель сигнала
    def quiteApp(self):
        userInfo = QMessageBox.question(self, "Имя приложения !", "Do you want Quit ?",
                                        QMessageBox.Yes | QMessageBox.No)
        if userInfo == QMessageBox.Yes:
            myApp.quit()
        elif userInfo == QMessageBox.No:
            pass
    # -----------------------------------------------

myApp = QApplication(sys.argv) #
window = Window()
window.show() # Показать окно.

myApp.exec_() # Выполнить.
sys.exit(0) # Выдим из цикла.
