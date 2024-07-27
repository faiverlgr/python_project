import sys
from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem
from ui.Catalogo_ui import Ui_frm_catalogo
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


class Catalogo(QWidget, Ui_frm_catalogo):
    def __init__(self, parent=None):
        super(Catalogo, self).__init__(parent)
        # self.model = None
        self.model = None
        self.setupUi(self)
        self.setWindowTitle('Catalogo')
        self.configurar()
        self.loaddata()
        self.viewdata()

    def configurar(self):
        self.tableCuentas.setColumnWidth(0, 120)
        self.tableCuentas.setColumnWidth(1, 348)

    def loaddata(self):
        connection = sqlite3.connect('D:\\servi\\source\\ProfitnetDB\\profitnetdb.db')
        cursor = connection.cursor()
        sql = "SELECT CAT_CodigoPUC, CAT_NombrePUC FROM Catalogo_PAR"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        cursor.close()

        registros = len(resultado)
        self.tableCuentas.setRowCount(registros)
        if registros > 0:
            count = 0
            for row in resultado:
                self.tableCuentas.setItem(count, 0, QTableWidgetItem(row[0]))
                self.tableCuentas.setItem(count, 1, QTableWidgetItem(row[1]))
                count += 1

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
