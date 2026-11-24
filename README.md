# ABM de Clientes – Northwind

**Proyecto Integrador – Programación Avanzada en Base de Datos**

## Integrantes

- Daniela Susana Acosta
- Angel Samuel Rodriguez Parodi
- Jorge Joaquin Rojas
- María Belén Soria Zigarán

## Descripción

Aplicación de escritorio para la gestión de clientes, desarrollada en Python con Tkinter y PostgreSQL, utilizando la base de datos Northwind.

## Tecnologías utilizadas

- Python
- Tkinter
- PostgreSQL
- Psycopg2

## Requisitos

- Python 3 instalado.
- PostgreSQL instalado y configurado.
- Base de datos Northwind creada.
- Dependencia `psycopg2-binary`.

Para instalar la dependencia, ejecutar:

```bash
pip install psycopg2-binary
```

## Configuración de la conexión

La aplicación utiliza la variable de entorno `DB_PASSWORD` para obtener la contraseña de acceso a PostgreSQL, evitando almacenarla directamente en el código fuente.

Cada integrante debe configurar esta variable una sola vez en su equipo, utilizando las instrucciones correspondientes a su sistema operativo.

**Windows (PowerShell):**

Ejecutar el siguiente comando, reemplazando `TU_CONTRASEÑA` por la contraseña de PostgreSQL:

```powershell
[Environment]::SetEnvironmentVariable("DB_PASSWORD", "TU_CONTRASEÑA", "User")
```

Una vez configurada, cerrar y volver a abrir VS Code o la terminal para que los cambios tengan efecto.

**Linux (Bash):**

Abrir el archivo de configuración de Bash:

```bash
nano ~/.bashrc
```

Agregar al final del archivo, reemplazando `TU_CONTRASEÑA` por la contraseña de PostgreSQL:

```bash
export DB_PASSWORD="TU_CONTRASEÑA"
```

Guardar los cambios y ejecutar:

```bash
source ~/.bashrc
```

## Ejecución

**Windows:**

```powershell
py main.py
```

**Linux:**

```bash
python3 main.py
```

## Estructura del proyecto

| Archivo | Descripción |
|---|---|
| `main.py` | Punto de entrada de la aplicación. |
| `interfaz.py` | Interfaz gráfica. |
| `conexion.py` | Conexión con PostgreSQL. |
| `clientes.py` | Operaciones ABM de clientes. |
| `ordenes.py` | Consulta de órdenes. |
| `logs.py` | Registro de logs. |
| `funciones y triggers.sql` | Funciones, triggers y vista de la base de datos. |