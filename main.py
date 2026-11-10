import tkinter as tk
from tkinter import ttk


# Crear ventana principal
ventana = tk.Tk()
ventana.title("Northwind - Gestión de Clientes")
ventana.geometry("1100x650")
ventana.minsize(900, 550)
ventana.configure(bg="#F4F6FA")


# Colores
COLOR_MENU = "#1E293B"
COLOR_FONDO = "#F4F6FA"
COLOR_BLANCO = "#FFFFFF"
COLOR_AZUL = "#2563EB"
COLOR_TEXTO = "#1E293B"


# Menu lateral
menu = tk.Frame(ventana, bg=COLOR_MENU, width=220)
menu.pack(side="left", fill="y")
menu.pack_propagate(False)


# Nombre de la aplicacion
titulo_menu = tk.Label(
    menu,
    text="NORTHWIND",
    font=("Arial", 18, "bold"),
    bg=COLOR_MENU,
    fg="white"
)
titulo_menu.pack(pady=(35, 5))

subtitulo_menu = tk.Label(
    menu,
    text="GESTION DE CLIENTES",
    font=("Arial", 9),
    bg=COLOR_MENU,
    fg="#94A3B8"
)
subtitulo_menu.pack(pady=(0, 40))


# Opciones del menu
opciones = ["Inicio", "Clientes", "Acerca de"]

for opcion in opciones:
    boton = tk.Button(
        menu,
        text="    " + opcion,
        font=("Arial", 11),
        bg=COLOR_MENU,
        fg="white",
        activebackground="#334155",
        activeforeground="white",
        relief="flat",
        anchor="w",
        padx=20,
        pady=14,
        cursor="hand2"
    )
    boton.pack(fill="x", padx=10, pady=3)


# Area principal
contenido = tk.Frame(ventana, bg=COLOR_FONDO)
contenido.pack(side="left", fill="both", expand=True)


# Encabezado
encabezado = tk.Frame(contenido, bg=COLOR_BLANCO, height=75)
encabezado.pack(fill="x")
encabezado.pack_propagate(False)

tk.Label(
    encabezado,
    text="Administracion de clientes",
    font=("Arial", 19, "bold"),
    bg=COLOR_BLANCO,
    fg=COLOR_TEXTO
).pack(side="left", padx=30, pady=20)


# Panel central
panel = tk.Frame(contenido, bg=COLOR_FONDO)
panel.pack(fill="both", expand=True, padx=30, pady=25)


tk.Label(
    panel,
    text="Listado de clientes",
    font=("Arial", 16, "bold"),
    bg=COLOR_FONDO,
    fg=COLOR_TEXTO
).pack(anchor="w")

tk.Label(
    panel,
    text="Consulta, registra y administra los clientes de Northwind.",
    font=("Arial", 10),
    bg=COLOR_FONDO,
    fg="#64748B"
).pack(anchor="w", pady=(5, 20))


# Barra de busqueda
barra = tk.Frame(panel, bg=COLOR_FONDO)
barra.pack(fill="x", pady=(0, 20))

buscador = tk.Entry(
    barra,
    font=("Arial", 11),
    width=35
)
buscador.pack(side="left", ipady=8)

boton_buscar = tk.Button(
    barra,
    text="Buscar",
    bg=COLOR_AZUL,
    fg="white",
    font=("Arial", 10, "bold"),
    relief="flat",
    padx=18,
    pady=8,
    cursor="hand2"
)
boton_buscar.pack(side="left", padx=10)


# Botones de operaciones
boton_nuevo = tk.Button(
    barra,
    text="+ Nuevo cliente",
    bg="#16A34A",
    fg="white",
    font=("Arial", 10, "bold"),
    relief="flat",
    padx=15,
    pady=8,
    cursor="hand2"
)
boton_nuevo.pack(side="right")


# Tabla de clientes
columnas = (
    "customerid",
    "companyname",
    "contactname",
    "contacttitle",
    "address",
    "city",
    "region",
    "postalcode",
    "country",
    "phone",
    "fax"
)

tabla = ttk.Treeview(
    panel,
    columns=columnas,
    show="headings"
)

tabla.heading("customerid", text="customerid")
tabla.heading("companyname", text="companyname")
tabla.heading("contactname", text="contactname")
tabla.heading("contacttitle", text="contacttitle")
tabla.heading("address", text="address")
tabla.heading("city", text="city")
tabla.heading("region", text="region")
tabla.heading("postalcode", text="postalcode")
tabla.heading("country", text="country")
tabla.heading("phone", text="phone")
tabla.heading("fax", text="fax")

tabla.column("customerid", width=100, anchor="center")
tabla.column("companyname", width=120, anchor="center")
tabla.column("contactname", width=140, anchor="center")
tabla.column("contacttitle", width=120, anchor="center")
tabla.column("address", width=120, anchor="center")
tabla.column("city", width=100, anchor="center")
tabla.column("region", width=90, anchor="center")
tabla.column("postalcode", width=90, anchor="center")
tabla.column("country", width=70, anchor="center")
tabla.column("phone", width=100, anchor="center")
tabla.column("fax", width=100, anchor="center")

tabla.pack(fill="both", expand=True)


# Estilo de la tabla
estilo = ttk.Style()
estilo.theme_use("clam")

estilo.configure(
    "Treeview",
    background="white",
    foreground=COLOR_TEXTO,
    rowheight=35,
    fieldbackground="white",
    font=("Arial", 10)
)

estilo.configure(
    "Treeview.Heading",
    background="#E2E8F0",
    foreground=COLOR_TEXTO,
    font=("Arial", 10, "bold")
)


# Iniciar aplicacion
ventana.mainloop()