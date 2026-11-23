
from conexion import crear_conexion
from logs import registrar_log, registrar_notice, registrar_notices, obtener_logs


def obtener_ordenes(filtro_cliente="", filtro_empleado=""):

    conexion = crear_conexion()

    if conexion is None:
        return None

    try:
        cursor = conexion.cursor()

        consulta = """
            SELECT
                *
            FROM vw_ordenes
        """

        condiciones = []
        parametros = []

        # Filtro por cliente
        if filtro_cliente:

            condiciones.append("""
                (
                    customerid ILIKE %s
                    OR companyname ILIKE %s
                )
            """)

            parametro_cliente = f"%{filtro_cliente}%"

            parametros.append(parametro_cliente)
            parametros.append(parametro_cliente)

        # Filtro por empleado
        if filtro_empleado:

            condiciones.append("""
                (
                    firstname ILIKE %s
                    OR lastname ILIKE %s
                )
            """)

            parametro_empleado = f"%{filtro_empleado}%"

            parametros.append(parametro_empleado)
            parametros.append(parametro_empleado)

        # Agregar las condiciones si existen filtros
        if condiciones:
            consulta += " WHERE " + " AND ".join(condiciones)

        consulta += " ORDER BY orderid"

        cursor.execute(consulta, parametros)

        registrar_log(
            consulta=consulta,
            parametros=parametros,
            origen="Frontend",
            estado="Ejecutada"
        )

        ordenes = cursor.fetchall()

        cursor.close()

        return ordenes

    except Exception as error:

        print("Error al consultar órdenes:", error)

        registrar_log(
            consulta=consulta,
            parametros=locals().get("parametros"),
            origen="Frontend",
            estado="Error",
            error=error
        )

        return None

    finally:
        registrar_notices(conexion)
        print(obtener_logs())
        conexion.close()
