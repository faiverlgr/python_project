from PyQt6.QtWidgets import QMainWindow
from view.menu_toolbar import menu_ppal


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        # self.app = app  # Declare an app member
        self.setWindowTitle("FinPy")
        # self.setGeometry(60, 60, 1088, 624)
        # self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setFixedSize(1088, 624)

        menu_ppal(self)
        # self.statusBar().showMessage("Ready")

        # layout_a = QVBoxLayout()
        # self.setLayout(layout_a)

        # layout_b = QVBoxLayout()
        # self.setLayout(layout_b)

        # frame2 = QWidget(self)
        # frame = QWidget(self)
        # self.setCentralWidget(frame2)

        # frame2.setLayout(layout_a)
        # frame.setLayout(layout_b)
        # self.setCentralWidget(frame)

        # button1 = QPushButton("Button 1")
        # button2 = QPushButton("Button 2")
        # button3 = QPushButton("Button 3")
        # button4 = QPushButton("Button 4")
        # button5 = QPushButton("Button 5")
        # button6 = QPushButton("Button 6")

        # label1 = QLabel("texto label")
        # layout_a.addWidget(label1)

        # frame.setStyleSheet("""
        #     background-color: #a7c6d7;
        # """)
        #
        # frame2.setStyleSheet("""
        #     background-color: #1f1f1f;
        # """)

        # label1.setStyleSheet("""
        #     background-color: "yellow";
        # """)
