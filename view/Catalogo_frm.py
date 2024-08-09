import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QTableWidgetItem, QDialog
from model.Catalogo_model import query_account
from ui.CatalogoDialog_ui import Ui_Dialog as Frm1
from ui.frm_CrearCuenta_ui import Ui_Dialog as Frm2


class Catalogo(QDialog, Frm1):
    def __init__(self, parent=None):
        super(Catalogo, self).__init__(parent)

        # Variables locales
        self.model = None
        self.msg = None
        self.item = None
        self.dialog = None
        self.mode: str = "mode_init"
        self.new_code: str = ""
        self.setupUi(self)
        self.setWindowTitle('Catalogo')
        self.configurar()
        self.navega_cuentas(par_event="click_init")

        # Eventos
        self.tbl_detalle.itemActivated.connect(self.explora_cuentas)
        self.btn_clase.clicked.connect(lambda: self.navega_cuentas(par_event="click_class"))
        self.btn_grupo.clicked.connect(lambda: self.navega_cuentas(par_event="click_group"))
        self.btn_cuenta.clicked.connect(lambda: self.navega_cuentas(par_event="click_account"))
        self.btn_subcta.clicked.connect(lambda: self.navega_cuentas(par_event="click_subaccount"))
        self.btn_iniciar.clicked.connect(lambda: self.navega_cuentas(par_event="click_init"))
        self.btn_agregar.clicked.connect(self.show_dialog)
        self.btn_editar.clicked.connect(self.editar)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            pass
            # print("Tecla Esc presionada, pero la ventana no se cerrará.")

    def editar(self):
        print("editando")
        self.btn_agregar.clearFocus()
        # self.tbl_detalle.setFocus()

    def show_dialog(self):
        codigo_temp = self.new_code
        # print("impreso desde el llamado:" + codigo_temp)
        self.dialog = FrmCrearCuenta(codigo_temp)
        self.dialog.rejected.connect(self.cierra_dialogo)

    def cierra_dialogo(self):
        pass
        # self.tbl_detalle.setFocus()

    def navega_cuentas(self, par_event: str):
        """Navega en cuentas desde botones"""
        # Limpia controles | crea query para el boton clickeado | almacena cuenta del boton
        if par_event == "click_init":
            par_value = "IS NULL"
            self.prepara_data('init', par_value)
        elif par_event == "click_class":
            # Llena variable y lanza para consulta
            par_value = self.btn_clase.text()
            self.prepara_data('clase', par_value)
        elif par_event == "click_group":
            # Llena variable y lanza para consulta
            par_value = self.btn_grupo.text()
            self.prepara_data('grupo', par_value)
        elif par_event == "click_account":
            # Llena variable y lanza para consulta
            par_value = self.btn_cuenta.text()
            self.prepara_data('cuenta', par_value)
        elif par_event == "click_subaccount":
            # Llena variable y lanza para consulta
            par_value = self.btn_subcta.text()
            self.prepara_data('subcuenta', par_value)
        else:
            pass
        # print(self.new_code)

    def explora_cuentas(self):
        """Modo explorar cuentas desde la tabla"""
        # Toma el numero de la fila seleccionada
        row = self.tbl_detalle.currentRow()
        par_value = self.tbl_detalle.item(row, 0).text()
        # Detecta el tipo de cuenta activado
        if len(par_value) == 1:
            # llena controles con item activado
            self.btn_clase.setText(self.tbl_detalle.item(row, 0).text())
            self.txt_clase.setText(self.tbl_detalle.item(row, 1).text())
            self.prepara_data('clase', par_value)
        elif len(par_value) == 2:
            # llena controles con item activado
            self.btn_grupo.setText(self.tbl_detalle.item(row, 0).text())
            self.txt_grupo.setText(self.tbl_detalle.item(row, 1).text())
            self.prepara_data('grupo', par_value)
        elif len(par_value) == 4:
            # llena controles con item activado
            self.btn_cuenta.setText(self.tbl_detalle.item(row, 0).text())
            self.txt_cuenta.setText(self.tbl_detalle.item(row, 1).text())
            self.prepara_data('cuenta', par_value)
        elif len(par_value) == 6:
            # llena controles con item activado
            self.btn_subcta.setText(self.tbl_detalle.item(row, 0).text())
            self.txt_subcta.setText(self.tbl_detalle.item(row, 1).text())
            self.prepara_data('subcuenta', par_value)
        else:
            pass

    def prepara_data(self, par_nivel: str, par_value: str):
        par_column: str = ""
        par_codenull: str = ""
        consulta: bool = True
        # prepara sql y cambia a modos segun el nivel
        if par_nivel == "init":
            par_column = "CAT_Clase"
            par_codenull = "CAT_Grupo IS NULL"
            # cambia el modo a init
            self.mode = "mode_init"
        elif par_nivel == "clase":
            par_column = "CAT_Clase ="
            par_codenull = "CAT_Grupo IS NULL"
            # cambia el modo a grupo
            self.mode = "mode_group"
        elif par_nivel == "grupo":
            par_column = "CAT_Grupo ="
            par_codenull = "CAT_Cuenta IS NULL"
            # cambia el modo a cuenta
            self.mode = "mode_account"
        elif par_nivel == "cuenta":
            par_column = "CAT_Cuenta ="
            par_codenull = "CAT_Subcuenta IS NULL"
            # cambia el modo a subcuenta
            self.mode = "mode_subaccount"
        elif par_nivel == "subcuenta":
            par_column = "CAT_Subcuenta ="
            par_codenull = "CAT_Clase IS NOT NULL"
            # cambia el modo a subcuenta
            self.mode = "mode_item"
        elif par_nivel == "item":
            pass
        else:
            consulta = False
        # consulta datos y si encuentra llena la tabla y cambia el modo
        if consulta:
            data = query_account(name_col=par_column, par_code=par_value, par_null=par_codenull)
            count = len(data)
            if count > 0:
                self.tbl_detalle.setRowCount(count)
                fila = 0
                for item_resultado in data:
                    # ajusta propiedades para que las celdas no sean editables
                    cell1 = QTableWidgetItem(item_resultado[0])
                    # cell1.setFlags(~Qt.ItemIsSelectable)
                    cell1.setFlags(~Qt.ItemIsEditable)
                    cell2 = QTableWidgetItem(item_resultado[1])
                    # cell2.setFlags(~Qt.ItemIsSelectable)
                    cell2.setFlags(~Qt.ItemIsEditable)
                    # asigna valores a las celdas
                    self.tbl_detalle.setItem(fila, 0, cell1)
                    self.tbl_detalle.setItem(fila, 1, cell2)
                    self.tbl_detalle.setRowHeight(fila, 22)
                    fila += 1
                # la tabla recibe el foco y selecciona la primera fila
                # self.tbl_detalle.setFocus()
                self.tbl_detalle.selectRow(0)
                # Llena botones y textos con valores de la primera fila de la tabla
                self.groupBox.setTitle(f"")
                self.show_items(self.mode)
            else:
                self.groupBox.setTitle(f"No encontro datos para la cuenta: {par_value}")
                # print(f"no encontro datos para 'par_value': {par_value}")
        else:
            print(f"no es posible hacer la consulta")

    def show_items(self, par_mode: str = None):
        """Muestra los items en la tabla"""
        # Toma el numero de la fila seleccionada
        row = self.tbl_detalle.currentRow()
        # Llena y limpia controles segun el modo
        if par_mode == "mode_init":
            self.btn_clase.setText(self.tbl_detalle.item(row, 0).text())
            self.txt_clase.setText(self.tbl_detalle.item(row, 1).text())
            self.btn_grupo.setText("")
            self.txt_grupo.setText("")
            self.btn_cuenta.setText("")
            self.txt_cuenta.setText("")
            self.btn_subcta.setText("")
            self.txt_subcta.setText("")
        elif par_mode == "mode_group":
            self.btn_grupo.setText(self.tbl_detalle.item(row, 0).text())
            self.txt_grupo.setText(self.tbl_detalle.item(row, 1).text())
            self.btn_cuenta.setText("")
            self.txt_cuenta.setText("")
            self.btn_subcta.setText("")
            self.txt_subcta.setText("")
            # Almacena clase para crear grupo
            self.new_code = self.btn_clase.text()
        elif par_mode == "mode_account":
            self.btn_cuenta.setText(self.tbl_detalle.item(row, 0).text())
            self.txt_cuenta.setText(self.tbl_detalle.item(row, 1).text())
            self.btn_subcta.setText("")
            self.txt_subcta.setText("")
            # Almacena grupo para crear cuenta
            self.new_code = self.btn_grupo.text()
        elif par_mode == "mode_subaccount":
            self.btn_subcta.setText(self.tbl_detalle.item(row, 0).text())
            self.txt_subcta.setText(self.tbl_detalle.item(row, 1).text())
            # Almacena cuenta para crear subcuenta
            self.new_code = self.btn_cuenta.text()
        elif par_mode == "mode_item":
            # Almacena subcuenta para crear item
            self.new_code = self.btn_subcta.text()
            pass
        else:
            print("self.mode no esta definido. No hay mas niveles para mostrar")

    def configurar(self):
        self.tbl_detalle.setColumnWidth(0, 120)
        self.tbl_detalle.setColumnWidth(1, 348)


class FrmCrearCuenta(QDialog, Frm2):
    def __init__(self, par1):
        super(FrmCrearCuenta, self).__init__()
        # VARIABLES
        self.setupUi(self)
        self.setWindowTitle('Administrar Catalogo')
        self.setModal(True)
        self.setSizeGripEnabled(False)
        self.show()

        # Llena informacion del formulario
        # print("impreso desde la clase: " + par1)
        self.txt_codigo.setText(par1)


def main():
    app = QApplication(sys.argv)
    window = Catalogo()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
