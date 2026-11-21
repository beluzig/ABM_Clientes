#Registro en memoria de las sentencias SQL ejecutadas por la aplicación.

from datetime import datetime
from threading import Lock

_registros = []
_bloqueo = Lock()

def registrar_log(consulta, parametros=None, origen="Frontend", estado="Ejecutada", error=None):
    ##Agrega una sentencia al historial.
    #Args:
    #    consulta: SQL enviado a PostgreSQL.
    #    parametros: parámetros enviados a cursor.execute(), si existen.
    #    origen: "Frontend" o "Backend".
    #    estado: estado de la ejecución, por ejemplo "Ejecutada" o "Error".
    #    error: descripción del error, si la ejecución falló.
    if not consulta:
        return

    if parametros is None:
        parametros = ()
    elif not isinstance(parametros, (tuple, list)):
        parametros = (parametros,)
    else:
        parametros = tuple(parametros)

    registro = {
        "fecha_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "consulta": str(consulta).strip(),
        "parametros": parametros,
        "origen": origen,
        "estado": estado,
        "error": str(error) if error else None,
    }

    with _bloqueo:
        _registros.append(registro)


def registrar_notice(mensaje):
    #Registra un NOTICE de PostgreSQL marcado con el prefijo SQL_LOG:.
    if not mensaje:
        return

    mensaje = str(mensaje).strip()
    prefijo = "SQL_LOG:"

    if not mensaje.startswith(prefijo):
        return

    consulta = mensaje[len(prefijo):].strip()
    if consulta:
        registrar_log(
            consulta=consulta,
            origen="Backend",
            estado="Ejecutada",
        )

def registrar_notices(conexion):
    """Recupera los NOTICE SQL_LOG enviados por PostgreSQL."""
    if conexion is None:
        return

    try:
        # psycopg2 agrega los NOTICE recibidos a esta lista.
        for notice in conexion.notices:
            # El mensaje suele incluir "NOTICE:" antes del texto enviado
            # mediante RAISE NOTICE. Extraemos el marcador que nos interesa.
            marcador = "SQL_LOG:"
            posicion = notice.find(marcador)

            if posicion != -1:
                registrar_notice(notice[posicion:])

        # Evita volver a procesar los mismos mensajes.
        conexion.notices.clear()

    except Exception as error:
        print("No se pudieron recuperar los NOTICE de PostgreSQL:", error)

def obtener_logs():
    #Devuelve una copia del historial, del registro más nuevo al más antiguo.
    with _bloqueo:
        return [registro.copy() for registro in reversed(_registros)]


def limpiar_logs():
    #Vacía el historial de consultas.
    with _bloqueo:
        _registros.clear()
