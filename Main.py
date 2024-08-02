import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget, QPushButton
from PySide6.QtWidgets import QDialog
from view.menu_toolbar import menu_ppal
from view.Catalogo_frm import Catalogo


class App(QMainWindow):
    def __init__(self, parent=None):
        super(App, self).__init__(parent=parent)
        self.msg = None
        self.areah1 = None
        self.button1 = None
        self.dialog = None
        self.setWindowTitle("Mi app de toda la vida")
        self.setFixedSize(1080, 624)
        self.setMenuBar(menu_ppal(self))
        self.configurar()

    def configurar(self):
        container = QWidget(self)
        self.areah1 = QHBoxLayout()
        container.setLayout(self.areah1)
        self.setCentralWidget(container)

        self.button1 = QPushButton(text="Click here")
        self.button1.clicked.connect(self.button_clicked)
        self.areah1.addWidget(self.button1)
        # self.setCentralWidget(self.button1)

        container.setStyleSheet("QHBoxLayout{\n"
                                "    background: red;\n"
                                "    color: black\n"
                                "}")

    def button_clicked(self):
        # self.dialog = QDialog()
        # self.dialog.setWindowTitle("New dialog here")
        # self.dialog.resize(200, 200)
        # self.dialog.setFixedSize(200, 200)
        # self.dialog.exec()

        # self.msg = "Button clicked"
        # print(self.msg)
        # return self.msg

        self.dialog = Catalogo()
        self.dialog.setWindowTitle("Catalogo Dialogo")
        self.dialog.exec()


def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
