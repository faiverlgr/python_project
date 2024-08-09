from model.connect import conn


def query_catalogo():
    sql = "SELECT CAT_CodigoPUC, CAT_NombrePUC FROM Catalogo_PAR WHERE CAT_Clase IS NULL"
    conect = conn()
    cursor = conect.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conect.close()
    return result


def query_account(
        name_col: str,
        par_code: str,
        par_null: str):
    sql = (f"SELECT "
           f"CAT_CodigoPUC, "
           f"CAT_NombrePUC, "
           f"CAT_Detalle "
           f"FROM Catalogo_PAR "
           f"WHERE {name_col} {par_code} AND {par_null}")
    conect = conn()
    cursor = conect.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conect.close()
    return result

# print(query_catalogo())
