import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget, QPushButton
from view.menu_toolbar import menu_ppal


class App(QMainWindow):
    def __init__(self, parent=None):
        super(App, self).__init__(parent=parent)
        self.areah1 = None
        self.button1 = None
        self.setWindowTitle("Mi app de toda la vida")
        self.setFixedSize(1080, 624)
        self.setMenuBar(menu_ppal(self))
        self.configurar()

    def configurar(self):
        container = QWidget()
        self.areah1 = QHBoxLayout()
        container.setLayout(self.areah1)
        self.setCentralWidget(container)

        self.button1 = QPushButton(text="Click here")
        self.button1.clicked.connect(button_clicked)
        self.areah1.addWidget(self.button1)

        container.setStyleSheet("QHBoxLayout{\n"
                                "    background: red;\n"
                                "    color: black\n"
                                "}")


def button_clicked():
    print("Button clicked")


def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
