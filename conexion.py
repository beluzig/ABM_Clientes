import psycopg2


import psycopg2
import os


def crear_conexion():
    try:
        conexion = psycopg2.connect(
            host="localhost",
            database="northwind",
            user="postgres",
            password=os.getenv("DB_PASSWORD", "TU_CONTRASEÑA"),
            port="5432"
        )

        return conexion

    except Exception as error:
        print("Error al conectar con la base de datos:", error)
        return None