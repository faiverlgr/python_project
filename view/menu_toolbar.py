from PyQt6.QtCore import QSize
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QToolBar, QPushButton, QStatusBar


def menu_ppal(master):
    # menu_bar = QMenuBar()
    menu_bar = master.menuBar()
    file_menu = menu_bar.addMenu("Files")
    quit_action = file_menu.addAction("Exit")
    quit_action.triggered.connect(lambda x: quit_app(master))

    edit_menu = menu_bar.addMenu("Edit")
    edit_menu.addAction("Copy")
    edit_menu.addAction("Cut")
    edit_menu.addAction("Paste")
    edit_menu.addAction("Undo")
    edit_menu.addAction("Redo")

    menu_bar.addMenu("Window")
    menu_bar.addMenu("Setting")
    menu_bar.addMenu("Help")

    # Working with toolbars
    toolbar = QToolBar("My main toolbar")
    toolbar.setMovable(True)
    toolbar.setIconSize(QSize(16, 16))
    master.addToolBar(toolbar)

    # Add the quit action to the toolbar
    toolbar.addAction(quit_action)

    action = QAction("Some action", master)
    action.setShortcut("Ctrl+Q")
    action.triggered.connect(toolbar_button_clicked1)
    action.setStatusTip("Status message for some action")
    toolbar.addAction(action)

    action1 = QAction(QIcon("src/start.png"), "Some action", master)
    action1.setStatusTip("Status message for some other action")
    action1.triggered.connect(lambda: toolbar_button_clicked(master))
    # action1.setCheckable(True)
    toolbar.addAction(action1)

    toolbar.addSeparator()
    toolbar.addWidget(QPushButton("Click here"))

    # Working with status bars
    master.setStatusBar(QStatusBar(master))


def quit_app(par1):
    par1.app.quit()


def toolbar_button_clicked1():
    print("Ready")


def toolbar_button_clicked(par2):
    par2.statusBar().showMessage("Toolbar clicked", 3000)
