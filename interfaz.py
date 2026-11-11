
import tkinter as tk
from tkinter import ttk, messagebox

from clientes import obtener_clientes


class AplicacionClientes:

    def __init__(self, ventana):

        self.ventana = ventana

        self.ventana.title("Northwind - Gestión de Clientes")
        self.ventana.geometry("1100x650")
        self.ventana.minsize(900, 550)
        self.ventana.configure(bg="#F4F6FA")

        # Colores
        self.COLOR_MENU = "#1E293B"
        self.COLOR_FONDO = "#F4F6FA"
        self.COLOR_BLANCO = "#FFFFFF"
        self.COLOR_AZUL = "#2563EB"
        self.COLOR_TEXTO = "#1E293B"

        self.crear_interfaz()
        self.cargar_clientes()

    def crear_interfaz(self):

        # Menu lateral
        menu = tk.Frame(
            self.ventana,
            bg=self.COLOR_MENU,
            width=220
        )

        menu.pack(side="left", fill="y")
        menu.pack_propagate(False)

        # Nombre de la aplicacion
        tk.Label(
            menu,
            text="NORTHWIND",
            font=("Arial", 18, "bold"),
            bg=self.COLOR_MENU,
            fg="white"
        ).pack(pady=(35, 5))

        tk.Label(
            menu,
            text="GESTION DE CLIENTES",
            font=("Arial", 9),
            bg=self.COLOR_MENU,
            fg="#94A3B8"
        ).pack(pady=(0, 40))

        # Opciones del menu
        opciones = ["Inicio", "Clientes", "Acerca de"]

        for opcion in opciones:

            boton = tk.Button(
                menu,
                text="    " + opcion,
                font=("Arial", 11),
                bg=self.COLOR_MENU,
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
        contenido = tk.Frame(
            self.ventana,
            bg=self.COLOR_FONDO
        )

        contenido.pack(side="left", fill="both", expand=True)

        # Encabezado
        encabezado = tk.Frame(
            contenido,
            bg=self.COLOR_BLANCO,
            height=75
        )

        encabezado.pack(fill="x")
        encabezado.pack_propagate(False)

        tk.Label(
            encabezado,
            text="Administración de clientes",
            font=("Arial", 19, "bold"),
            bg=self.COLOR_BLANCO,
            fg=self.COLOR_TEXTO
        ).pack(side="left", padx=30, pady=20)

        # Panel central
        panel = tk.Frame(
            contenido,
            bg=self.COLOR_FONDO
        )

        panel.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=25
        )

        tk.Label(
            panel,
            text="Listado de clientes",
            font=("Arial", 16, "bold"),
            bg=self.COLOR_FONDO,
            fg=self.COLOR_TEXTO
        ).pack(anchor="w")

        tk.Label(
            panel,
            text="Consulta, registra y administra los clientes de Northwind.",
            font=("Arial", 10),
            bg=self.COLOR_FONDO,
            fg="#64748B"
        ).pack(anchor="w", pady=(5, 20))

        # Barra de busqueda
        barra = tk.Frame(
            panel,
            bg=self.COLOR_FONDO
        )

        barra.pack(fill="x", pady=(0, 20))

        self.buscador = tk.Entry(
            barra,
            font=("Arial", 11),
            width=35
        )

        self.buscador.pack(side="left", ipady=8)

        boton_buscar = tk.Button(
            barra,
            text="Buscar",
            bg=self.COLOR_AZUL,
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            padx=18,
            pady=8,
            cursor="hand2",
            command=self.buscar_clientes
        )

        boton_buscar.pack(side="left", padx=10)

        boton_nuevo = tk.Button(
            barra,
            text="+ Nuevo cliente",
            bg="#16A34A",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            padx=15,
            pady=8,
            cursor="hand2",
            command=self.nuevo_cliente
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

        self.tabla = ttk.Treeview(
            panel,
            columns=columnas,
            show="headings"
        )

        nombres = {
            "customerid": "ID",
            "companyname": "Empresa",
            "contactname": "Contacto",
            "contacttitle": "Cargo",
            "address": "Dirección",
            "city": "Ciudad",
            "region": "Región",
            "postalcode": "Código postal",
            "country": "País",
            "phone": "Teléfono",
            "fax": "Fax"
        }

        anchos = {
            "customerid": 90,
            "companyname": 180,
            "contactname": 150,
            "contacttitle": 140,
            "address": 180,
            "city": 120,
            "region": 100,
            "postalcode": 110,
            "country": 110,
            "phone": 130,
            "fax": 130
        }

        for columna in columnas:

            self.tabla.heading(
                columna,
                text=nombres[columna]
            )

            self.tabla.column(
                columna,
                width=anchos[columna],
                minwidth=70,
                anchor="center"
            )

        # Barras de desplazamiento
        scroll_vertical = ttk.Scrollbar(
            panel,
            orient="vertical",
            command=self.tabla.yview
        )

        scroll_horizontal = ttk.Scrollbar(
            panel,
            orient="horizontal",
            command=self.tabla.xview
        )

        self.tabla.configure(
            yscrollcommand=scroll_vertical.set,
            xscrollcommand=scroll_horizontal.set
        )

        self.tabla.pack(
            side="top",
            fill="both",
            expand=True
        )

        scroll_vertical.pack(
            side="right",
            fill="y"
        )

        scroll_horizontal.pack(
            side="bottom",
            fill="x"
        )

        # Estilo de la tabla
        estilo = ttk.Style()

        estilo.theme_use("clam")

        estilo.configure(
            "Treeview",
            background="white",
            foreground=self.COLOR_TEXTO,
            rowheight=35,
            fieldbackground="white",
            font=("Arial", 10)
        )

        estilo.configure(
            "Treeview.Heading",
            background="#E2E8F0",
            foreground=self.COLOR_TEXTO,
            font=("Arial", 10, "bold")
        )

        estilo.map(
            "Treeview",
            background=[("selected", self.COLOR_AZUL)],
            foreground=[("selected", "white")]
        )

    def cargar_clientes(self):

        self.tabla.delete(*self.tabla.get_children())

        clientes = obtener_clientes()

        if clientes is None:
            messagebox.showerror(
                "Error",
                "No se pudieron cargar los clientes.\n"
                "Verificá la conexión con PostgreSQL."
            )
            return

        for cliente in clientes:
            self.tabla.insert(
                "",
                "end",
                values=cliente
            )

    def buscar_clientes(self):

        filtro = self.buscador.get().strip()

        self.tabla.delete(*self.tabla.get_children())

        clientes = obtener_clientes(filtro)

        if clientes is None:
            messagebox.showerror(
                "Error",
                "No se pudo realizar la búsqueda."
            )
            return

        for cliente in clientes:
            self.tabla.insert(
                "",
                "end",
                values=cliente
            )

    def nuevo_cliente(self):

        messagebox.showinfo(
            "Nuevo cliente",
            "Esto falta implementar."
        )
