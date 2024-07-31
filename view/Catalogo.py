import sys
from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from PySide6.QtWidgets import QApplication, QTableWidgetItem, QDialog
from ui.CatalogoDialog_ui import Ui_Dialog
import sqlite3


class MyTableModel(QAbstractTableModel):
    def __init__(self, data, header_data, parent=None):
        super(MyTableModel, self).__init__(parent)
        self._data = data
        self._header_data = header_data

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)
        # return self.data.shape[0]

    def columnCount(self, parent=QModelIndex()):
        if self.rowCount() > 0:
            return len(self._data[0])
        return 0

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            # column_key = self._header_data[index.column()]
            return str(self._data[index.row()][index.column()])
        return None

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return str(self._header_data[section])
        return None


class Catalogo(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(Catalogo, self).__init__(parent)

        # VARIABLES
        self.model = None
        self.msg = None
        self.item = None
        self.setupUi(self)
        self.setWindowTitle('Catalogo')
        self.configurar()
        self.loaddata()
        self.viewdata()

        # EVENTOS
        self.tbl_detalle.itemSelectionChanged.connect(self.show_items)

    def muestra_clases(self, row):
        self.btn_clase.setText(self.tbl_detalle.item(row, 0).text())
        self.txt_clase.setText(self.tbl_detalle.item(row, 1).text())

    def show_items(self):
        self.muestra_clases(self.tbl_detalle.currentRow())

    def configurar(self):
        self.tbl_detalle.setColumnWidth(0, 120)
        self.tbl_detalle.setColumnWidth(1, 348)

    def loaddata(self):
        connection = sqlite3.connect('D:\\servi\\source\\ProfitnetDB\\profitnetdb.db')
        cursor = connection.cursor()
        sql = "SELECT CAT_CodigoPUC, CAT_NombrePUC FROM Catalogo_PAR WHERE CAT_Clase IS NULL"
        cursor.execute(sql)
        # almacena el resultado de la consulta en una lista
        resultado = cursor.fetchall()
        cursor.close()

        # almacena la cantidad de filas en una variable
        registros = len(resultado)
        # especifica la cantidad de filas a la tabla
        if registros > 0:
            self.tbl_detalle.setRowCount(registros)
            fila = 0
            for item_resultado in resultado:
                self.tbl_detalle.setItem(fila, 0, QTableWidgetItem(item_resultado[0]))
                self.tbl_detalle.setItem(fila, 1, QTableWidgetItem(item_resultado[1]))
                fila += 1

            # la tabla recibe el foco y selecciona la primera fila
            self.tbl_detalle.setFocus()
            self.tbl_detalle.selectRow(0)
            # Llena botones y textos con valores de la primera fila de la tabla
            self.muestra_clases(0)

    def viewdata(self):
        connection = sqlite3.connect('D:\\servi\\source\\ProfitnetDB\\profitnetdb.db')
        cursor = connection.cursor()
        sql = "SELECT CAT_CodigoPUC, CAT_NombrePUC FROM Catalogo_PAR"
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()

        header_data = [field[0] for field in cursor.description]
        self.model = MyTableModel(data, header_data)
        self.tableViewCata.setModel(self.model)


def main():
    app = QApplication(sys.argv)
    window = Catalogo()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
