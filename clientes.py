
from conexion import crear_conexion


def obtener_clientes(filtro=""):

    conexion = crear_conexion()

    if conexion is None:
        return None

    try:
        cursor = conexion.cursor()

        consulta = """
            SELECT customerid,
                   companyname,
                   contactname,
                   contacttitle,
                   address,
                   city,
                   region,
                   postalcode,
                   country,
                   phone,
                   fax
            FROM customers
        """

        if filtro:
            consulta += """
                WHERE customerid ILIKE %s
                   OR companyname ILIKE %s
                   OR contactname ILIKE %s
                   OR city ILIKE %s
                   OR country ILIKE %s
            """

            parametro = "%" + filtro + "%"

            cursor.execute(
                consulta,
                (parametro, parametro, parametro,
                 parametro, parametro)
            )

        else:
            cursor.execute(consulta)

        clientes = cursor.fetchall()

        cursor.close()

        return clientes

    except Exception as error:
        print("Error al consultar clientes:", error)
        return None

    finally:
        conexion.close()
