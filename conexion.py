
import psycopg2


def crear_conexion():

    try:
        conexion = psycopg2.connect(
            host="localhost",
            database="northwind",
            user="postgres",
            password="abelu89sql",
            port="5432"
        )

        return conexion

    except Exception as error:
        print("Error al conectar con PostgreSQL:", error)
        return None
