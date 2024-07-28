from PyQt6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
import sqlite3

server_name = ""
database = ""
username = ""
password = ""


def connection_sqlite():
    global db
    conn_string = sqlite3.connect('D:\\servi\\source\\ProfitnetDB\\profitnetdb.db')


# def conexion_sql():
#     global db
#     conn_string = \
#         f'DRIVER={{SQL Server}};'\
#         f'SERVER={server_name};'\
#         f'DATABASE={database};'\
#         f'UID={username};'\
#         f'PWD={password}'
#
#     if QSqlDatabase.contains("qt_sql_default_connection"):
#         db = QSqlDatabase.database("qt_sql_default_connection")
#     else:
#         db = QSqlDatabase.addDatabase("QODBC")
#         db.setDatabaseName(conn_string)
#         if db.open():
#             print("Conexion established")
#         else:
#             print("Error connecting to database")


connection_sqlite()
