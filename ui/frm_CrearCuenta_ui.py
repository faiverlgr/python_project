# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_CrearCuenta.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(545, 283)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(104, 240, 121, 24))
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(320, 240, 121, 24))
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(128, 88, 369, 56))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.txt_nombre = QLineEdit(self.widget)
        self.txt_nombre.setObjectName(u"txt_nombre")

        self.verticalLayout_2.addWidget(self.txt_nombre)

        self.txt_detalle = QLineEdit(self.widget)
        self.txt_detalle.setObjectName(u"txt_detalle")

        self.verticalLayout_2.addWidget(self.txt_detalle)

        self.widget1 = QWidget(Dialog)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(48, 56, 65, 89))
        self.verticalLayout = QVBoxLayout(self.widget1)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_codigo = QLabel(self.widget1)
        self.lbl_codigo.setObjectName(u"lbl_codigo")

        self.verticalLayout.addWidget(self.lbl_codigo)

        self.lbl_nombre = QLabel(self.widget1)
        self.lbl_nombre.setObjectName(u"lbl_nombre")

        self.verticalLayout.addWidget(self.lbl_nombre)

        self.lbl_nombre_2 = QLabel(self.widget1)
        self.lbl_nombre_2.setObjectName(u"lbl_nombre_2")

        self.verticalLayout.addWidget(self.lbl_nombre_2)

        self.txt_codnew = QLineEdit(Dialog)
        self.txt_codnew.setObjectName(u"txt_codnew")
        self.txt_codnew.setGeometry(QRect(280, 56, 41, 24))
        self.txt_codigo = QLineEdit(Dialog)
        self.txt_codigo.setObjectName(u"txt_codigo")
        self.txt_codigo.setGeometry(QRect(128, 56, 142, 24))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Guardar", None))
        self.lbl_codigo.setText(QCoreApplication.translate("Dialog", u"Codigo", None))
        self.lbl_nombre.setText(QCoreApplication.translate("Dialog", u"Nombre", None))
        self.lbl_nombre_2.setText(QCoreApplication.translate("Dialog", u"Detalle", None))
    # retranslateUi

