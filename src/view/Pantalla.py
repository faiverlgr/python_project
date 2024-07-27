import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QApplication, QWidget, QDialog, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QLabel


class Pantalla(QMainWindow):
    def __init__(self, parent=None):
        super(Pantalla, self).__init__(parent)
        loadUi("FormPrincipal.ui", self)


def main():
    app = QApplication(sys.argv)
    window = Pantalla()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
