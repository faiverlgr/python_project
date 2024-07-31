# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CatalogoDialog.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableView, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1166, 594)
        self.verticalLayoutWidget_4 = QWidget(Dialog)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(576, 248, 121, 116))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_agregar = QPushButton(self.verticalLayoutWidget_4)
        self.btn_agregar.setObjectName(u"btn_agregar")

        self.verticalLayout_4.addWidget(self.btn_agregar)

        self.btn_editar = QPushButton(self.verticalLayoutWidget_4)
        self.btn_editar.setObjectName(u"btn_editar")

        self.verticalLayout_4.addWidget(self.btn_editar)

        self.btn_salir = QPushButton(self.verticalLayoutWidget_4)
        self.btn_salir.setObjectName(u"btn_salir")

        self.verticalLayout_4.addWidget(self.btn_salir)

        self.btn_iniciar = QPushButton(self.verticalLayoutWidget_4)
        self.btn_iniciar.setObjectName(u"btn_iniciar")

        self.verticalLayout_4.addWidget(self.btn_iniciar)

        self.horizontalLayoutWidget = QWidget(Dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(40, 200, 657, 33))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_buscar = QLabel(self.horizontalLayoutWidget)
        self.lbl_buscar.setObjectName(u"lbl_buscar")

        self.horizontalLayout.addWidget(self.lbl_buscar)

        self.txt_buscar = QLineEdit(self.horizontalLayoutWidget)
        self.txt_buscar.setObjectName(u"txt_buscar")

        self.horizontalLayout.addWidget(self.txt_buscar)

        self.verticalLayoutWidget_3 = QWidget(Dialog)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(280, 40, 417, 146))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.txt_clase = QLineEdit(self.verticalLayoutWidget_3)
        self.txt_clase.setObjectName(u"txt_clase")

        self.verticalLayout_3.addWidget(self.txt_clase)

        self.txt_grupo = QLineEdit(self.verticalLayoutWidget_3)
        self.txt_grupo.setObjectName(u"txt_grupo")

        self.verticalLayout_3.addWidget(self.txt_grupo)

        self.txt_cuenta = QLineEdit(self.verticalLayoutWidget_3)
        self.txt_cuenta.setObjectName(u"txt_cuenta")

        self.verticalLayout_3.addWidget(self.txt_cuenta)

        self.txt_subcta = QLineEdit(self.verticalLayoutWidget_3)
        self.txt_subcta.setObjectName(u"txt_subcta")

        self.verticalLayout_3.addWidget(self.txt_subcta)

        self.verticalLayoutWidget_2 = QWidget(Dialog)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(136, 40, 129, 146))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_clase = QPushButton(self.verticalLayoutWidget_2)
        self.btn_clase.setObjectName(u"btn_clase")

        self.verticalLayout_2.addWidget(self.btn_clase)

        self.btn_grupo = QPushButton(self.verticalLayoutWidget_2)
        self.btn_grupo.setObjectName(u"btn_grupo")

        self.verticalLayout_2.addWidget(self.btn_grupo)

        self.btn_cuenta = QPushButton(self.verticalLayoutWidget_2)
        self.btn_cuenta.setObjectName(u"btn_cuenta")

        self.verticalLayout_2.addWidget(self.btn_cuenta)

        self.btn_subcta = QPushButton(self.verticalLayoutWidget_2)
        self.btn_subcta.setObjectName(u"btn_subcta")

        self.verticalLayout_2.addWidget(self.btn_subcta)

        self.tableViewCata = QTableView(Dialog)
        self.tableViewCata.setObjectName(u"tableViewCata")
        self.tableViewCata.setGeometry(QRect(712, 40, 393, 513))
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(40, 248, 513, 305))
        self.tbl_detalle = QTableWidget(self.groupBox)
        if (self.tbl_detalle.columnCount() < 2):
            self.tbl_detalle.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_detalle.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_detalle.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tbl_detalle.setObjectName(u"tbl_detalle")
        self.tbl_detalle.setGeometry(QRect(8, 8, 497, 289))
        self.tbl_detalle.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tbl_detalle.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tbl_detalle.verticalHeader().setVisible(False)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(40, 40, 81, 145))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_clase = QLabel(self.verticalLayoutWidget)
        self.lbl_clase.setObjectName(u"lbl_clase")

        self.verticalLayout.addWidget(self.lbl_clase)

        self.lbl_grupo = QLabel(self.verticalLayoutWidget)
        self.lbl_grupo.setObjectName(u"lbl_grupo")

        self.verticalLayout.addWidget(self.lbl_grupo)

        self.lbl_cuenta = QLabel(self.verticalLayoutWidget)
        self.lbl_cuenta.setObjectName(u"lbl_cuenta")

        self.verticalLayout.addWidget(self.lbl_cuenta)

        self.lbl_subcta = QLabel(self.verticalLayoutWidget)
        self.lbl_subcta.setObjectName(u"lbl_subcta")

        self.verticalLayout.addWidget(self.lbl_subcta)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btn_agregar.setText(QCoreApplication.translate("Dialog", u"Agregar", None))
        self.btn_editar.setText(QCoreApplication.translate("Dialog", u"Editar", None))
        self.btn_salir.setText(QCoreApplication.translate("Dialog", u"Salir", None))
        self.btn_iniciar.setText(QCoreApplication.translate("Dialog", u"Volver al inicio", None))
        self.lbl_buscar.setText(QCoreApplication.translate("Dialog", u"Buscar", None))
        self.btn_clase.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.btn_grupo.setText(QCoreApplication.translate("Dialog", u"00", None))
        self.btn_cuenta.setText(QCoreApplication.translate("Dialog", u"0000", None))
        self.btn_subcta.setText(QCoreApplication.translate("Dialog", u"000000", None))
        self.groupBox.setTitle("")
        ___qtablewidgetitem = self.tbl_detalle.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Codigo de cuenta", None));
        ___qtablewidgetitem1 = self.tbl_detalle.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Descripcion de la cuenta", None));
        self.lbl_clase.setText(QCoreApplication.translate("Dialog", u"Clase", None))
        self.lbl_grupo.setText(QCoreApplication.translate("Dialog", u"Grupo", None))
        self.lbl_cuenta.setText(QCoreApplication.translate("Dialog", u"Cuenta", None))
        self.lbl_subcta.setText(QCoreApplication.translate("Dialog", u"Subcuenta", None))
    # retranslateUi

