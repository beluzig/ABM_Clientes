import psycopg2

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


def insertar_cliente(datos):

    conexion = crear_conexion()

    if conexion is None:
        return False, "No se pudo conectar con PostgreSQL."

    try:
        cursor = conexion.cursor()

        consulta = """
            INSERT INTO customers (
                customerid,
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
            )
            VALUES (%s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s)
        """

        cursor.execute(consulta, datos)

        conexion.commit()

        cursor.close()

        return True, None

    except Exception as error:
        conexion.rollback()
        print("Error al insertar cliente:", error)
        return False, str(error)

    finally:
        conexion.close()

def actualizar_cliente(datos, customerid_original):

    conexion = crear_conexion()

    if conexion is None:
        return False, "No se pudo conectar con PostgreSQL."

    try:
        cursor = conexion.cursor()

        consulta = """
            UPDATE customers
            SET companyname = %s,
                contactname = %s,
                contacttitle = %s,
                address = %s,
                city = %s,
                region = %s,
                postalcode = %s,
                country = %s,
                phone = %s,
                fax = %s
            WHERE customerid = %s
        """

        cursor.execute(
            consulta,
            datos + (customerid_original,)
        )

        conexion.commit()
        cursor.close()

        return True, None

    except Exception as error:
        conexion.rollback()
        print("Error al actualizar cliente:", error)
        return False, str(error)

    finally:
        conexion.close()        

def eliminar_cliente(customerid):

    conexion = crear_conexion()

    if conexion is None:
        return False, "No se pudo conectar con PostgreSQL."

    try:
        cursor = conexion.cursor()

        consulta = """
            DELETE FROM customers
            WHERE customerid = %s
        """

        cursor.execute(consulta, (customerid,))

        if cursor.rowcount == 0:
            conexion.rollback()
            cursor.close()
            return False, "No se encontró el cliente."

        conexion.commit()
        cursor.close()

        return True, None

    except psycopg2.errors.ForeignKeyViolation:

        conexion.rollback()

        return False, (
            "No se puede eliminar este cliente porque "
            "tiene pedidos asociados."
        )

    except Exception as error:

        conexion.rollback()
        print("Error al eliminar cliente:", error)

        return False, "Ocurrió un error al intentar eliminar el cliente."

    finally:
        conexion.close()