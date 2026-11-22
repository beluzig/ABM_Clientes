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

def registrar_notice(notice):
    marcador = "SQL_LOG:"
    if not notice or marcador not in notice:
        return
    consulta = notice.split(marcador, 1)[1].strip()
    if consulta:
        print("NOTICE registrado:", consulta)
        registrar_log(
            consulta=consulta,
            origen="Backend",
            estado="Ejecutada"
        )

def registrar_notices(conexion):
    if conexion is None:
        return
    try:
        # Copiar los mensajes antes de limpiar la lista.
        notices = list(conexion.notices)
        for notice in notices:
            if "SQL_LOG:" in notice:
                registrar_notice(notice)
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
