import sys
from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from PySide6.QtWidgets import QApplication, QTableWidgetItem, QDialog
from ui.CatalogoDialog_ui import Ui_Dialog
from model.Catalogo_model import query_catalogo, query_account
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
        self.mode: str = "mode_class"
        self.new_code: str = ""
        self.setupUi(self)
        self.setWindowTitle('Catalogo')
        self.configurar()
        self.loaddata()
        self.viewdata()

        # EVENTOS
        self.tbl_detalle.itemSelectionChanged.connect(self.show_items)
        self.btn_clase.clicked.connect(lambda: self.navega_cuentas(par_mode="click_class"))
        self.btn_grupo.clicked.connect(lambda: self.navega_cuentas(par_mode="click_group"))
        self.btn_cuenta.clicked.connect(lambda: self.navega_cuentas(par_mode="click_account"))
        self.btn_subcta.clicked.connect(lambda: self.navega_cuentas(par_mode="click_subaccount"))
        self.btn_iniciar.clicked.connect(lambda: self.navega_cuentas(par_mode="click_init"))

    def show_items(self):
        row = self.tbl_detalle.currentRow()
        if self.mode == "mode_class":
            self.btn_clase.setText(self.tbl_detalle.item(row, 0).text())
            self.txt_clase.setText(self.tbl_detalle.item(row, 1).text())
            self.btn_grupo.setText("")
            self.txt_grupo.setText("")
            self.btn_cuenta.setText("")
            self.txt_cuenta.setText("")
            self.btn_subcta.setText("")
            self.txt_subcta.setText("")
        elif self.mode == "mode_group":
            self.btn_grupo.setText(self.tbl_detalle.item(row, 0).text())
            self.txt_grupo.setText(self.tbl_detalle.item(row, 1).text())
            self.btn_cuenta.setText("")
            self.txt_cuenta.setText("")
            self.btn_subcta.setText("")
            self.txt_subcta.setText("")
        elif self.mode == "mode_account":
            self.btn_cuenta.setText(self.tbl_detalle.item(row, 0).text())
            self.txt_cuenta.setText(self.tbl_detalle.item(row, 1).text())
            self.btn_subcta.setText("")
            self.txt_subcta.setText("")
        elif self.mode == "mode_subaccount":
            self.btn_subcta.setText(self.tbl_detalle.item(row, 0).text())
            self.txt_subcta.setText(self.tbl_detalle.item(row, 1).text())
        else:
            print("self.mode")

    def configurar(self):
        self.tbl_detalle.setColumnWidth(0, 120)
        self.tbl_detalle.setColumnWidth(1, 348)

    def navega_cuentas(self, par_mode: str):
        par_column: str = ""
        par_value: str = ""
        par_codenull: str = ""
        if par_mode == "click_init":
            # Almacena en variable codigo si se crea un grupo
            self.new_code = self.btn_clase.text()
            # resetea textos
            self.btn_grupo.setText("")
            self.txt_grupo.setText("")
            self.btn_cuenta.setText("")
            self.txt_cuenta.setText("")
            self.btn_subcta.setText("")
            self.txt_subcta.setText("")
            # prepara el sql
            par_column = "CAT_Clase"
            par_value = "IS NULL"
            par_codenull = "CAT_Grupo IS NULL"
            self.mode = "mode_class"
        elif par_mode == "click_class":
            # Almacena en variable codigo si se crea una cuenta
            self.new_code = self.btn_grupo.text()
            # resetea textos
            self.btn_cuenta.setText("")
            self.txt_cuenta.setText("")
            self.btn_subcta.setText("")
            self.txt_subcta.setText("")
            # prepara el sql
            par_column = "CAT_Clase ="
            par_value = self.btn_clase.text()
            par_codenull = "CAT_Grupo IS NULL"
            self.mode = "mode_group"
        elif par_mode == "click_group":
            # Almacena en variable codigo si se crea una subcuenta
            self.new_code = self.btn_cuenta.text()
            # resetea textos
            self.btn_subcta.setText("")
            self.txt_subcta.setText("")
            # prepara el sql
            par_column = "CAT_Grupo ="
            par_value = self.btn_grupo.text()
            par_codenull = "CAT_Cuenta IS NULL"
            self.mode = "mode_account"
        elif par_mode == "click_account":
            # Almacena en variable codigo si se crea un item
            self.new_code = self.btn_subcta.text()
            # prepara el sql
            par_column = "CAT_Cuenta ="
            par_value = self.btn_cuenta.text()
            par_codenull = "CAT_Subcuenta IS NULL"
            self.mode = "mode_subaccount"
        elif par_mode == "click_subaccount":
            # prepara el sql
            par_column = "CAT_Subcuenta ="
            par_value = self.btn_subcta.text()
            par_codenull = "CAT_Clase IS NOT NULL"
            # TODO: Este modo self.mode se debe dar solo si la consulta tiene resultados
            self.mode = "mode_item"
        else:
            print("El par_column no esta definido")

        if par_value:
            # consulta datos y si encuentra llena la tabla
            data = query_account(name_col=par_column, par_code=par_value, par_null=par_codenull)
            count = len(data)
            if count > 0:
                self.tbl_detalle.setRowCount(count)
                fila = 0
                for item_resultado in data:
                    self.tbl_detalle.setItem(fila, 0, QTableWidgetItem(item_resultado[0]))
                    self.tbl_detalle.setItem(fila, 1, QTableWidgetItem(item_resultado[1]))
                    self.tbl_detalle.setRowHeight(fila, 22)
                    fila += 1

                # la tabla recibe el foco y selecciona la primera fila
                self.tbl_detalle.setFocus()
                self.tbl_detalle.selectRow(0)
                # Llena botones y textos con valores de la primera fila de la tabla
                self.show_items()

    def loaddata(self):
        # almacena el resultado de la consulta en una lista
        resultado = query_catalogo()
        # almacena la cantidad de filas en una variable
        registros = len(resultado)
        # especifica la cantidad de filas a la tabla
        if registros > 0:
            self.tbl_detalle.setRowCount(registros)
            fila = 0
            for item_resultado in resultado:
                self.tbl_detalle.setItem(fila, 0, QTableWidgetItem(item_resultado[0]))
                self.tbl_detalle.setItem(fila, 1, QTableWidgetItem(item_resultado[1]))
                self.tbl_detalle.setRowHeight(fila, 22)
                fila += 1

            # la tabla recibe el foco y selecciona la primera fila
            self.tbl_detalle.setFocus()
            self.tbl_detalle.selectRow(0)
            # Llena botones y textos con valores de la primera fila de la tabla
            self.show_items()

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
