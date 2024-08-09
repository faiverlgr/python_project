from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
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


def viewdata(self):
    connection = sqlite3.connect('D:\\servi\\source\\ProfitnetDB\\profitnetdb.db')
    cursor = connection.cursor()
    sql = "SELECT CAT_CodigoPUC, CAT_NombrePUC FROM Catalogo_PAR"
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()

    header_data = [field[0] for field in cursor.description]
    # Aqui van los controles en la interfaz para mostrar los datos
    # self.model = MyTableModel(data, header_data)
    # self.tableViewCata.setModel(self.model)
