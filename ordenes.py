
from conexion import crear_conexion


def obtener_ordenes(filtro_cliente="", filtro_empleado=""):

    conexion = crear_conexion()

    if conexion is None:
        return None

    try:
        cursor = conexion.cursor()

        consulta = """
            SELECT
                o.orderid,
                o.customerid,
                c.companyname,
                o.employeeid,
                e.firstname,
                e.lastname,
                o.orderdate,
                o.requireddate,
                o.shippeddate,
                o.shipvia,
                o.freight,
                o.shipname,
                o.shipaddress,
                o.shipcity,
                o.shipregion,
                o.shippostalcode,
                o.shipcountry
            FROM orders o
            INNER JOIN customers c
                ON o.customerid = c.customerid
            INNER JOIN employees e
                ON o.employeeid = e.employeeid
        """

        condiciones = []
        parametros = []

        # Filtro por cliente
        if filtro_cliente:

            condiciones.append("""
                (
                    c.customerid ILIKE %s
                    OR c.companyname ILIKE %s
                )
            """)

            parametro_cliente = "%" + filtro_cliente + "%"

            parametros.append(parametro_cliente)
            parametros.append(parametro_cliente)

        # Filtro por empleado
        if filtro_empleado:

            condiciones.append("""
                (
                    e.lastname ILIKE %s
                    OR e.firstname ILIKE %s
                )
            """)

            parametro_empleado = "%" + filtro_empleado + "%"

            parametros.append(parametro_empleado)
            parametros.append(parametro_empleado)

        if condiciones:
            consulta += " WHERE " + " AND ".join(condiciones)

        consulta += " ORDER BY o.orderid"

        cursor.execute(consulta, parametros)

        ordenes = cursor.fetchall()

        cursor.close()

        return ordenes

    except Exception as error:

        print("Error al consultar órdenes:", error)
        return None

    finally:
        conexion.close()
