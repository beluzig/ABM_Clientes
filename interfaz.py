import tkinter as tk
from tkinter import ttk, messagebox

from clientes import (
    obtener_clientes,
    insertar_cliente,
    actualizar_cliente,
    eliminar_cliente
)


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
        self.mostrar_inicio()

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
        tk.Button(
            menu,
            text="    Inicio",
            font=("Arial", 11),
            bg=self.COLOR_MENU,
            fg="white",
            activebackground="#334155",
            activeforeground="white",
            relief="flat",
            anchor="w",
            padx=20,
            pady=14,
            cursor="hand2",
            command=self.mostrar_inicio
        ).pack(fill="x", padx=10, pady=3)

        tk.Button(
            menu,
            text="    Clientes",
            font=("Arial", 11),
            bg=self.COLOR_MENU,
            fg="white",
            activebackground="#334155",
            activeforeground="white",
            relief="flat",
            anchor="w",
            padx=20,
            pady=14,
            cursor="hand2",
            command=self.mostrar_clientes
        ).pack(fill="x", padx=10, pady=3)

        tk.Button(
            menu,
            text="    Acerca de",
            font=("Arial", 11),
            bg=self.COLOR_MENU,
            fg="white",
            activebackground="#334155",
            activeforeground="white",
            relief="flat",
            anchor="w",
            padx=20,
            pady=14,
            cursor="hand2",
            command=self.mostrar_acerca_de
        ).pack(fill="x", padx=10, pady=3)

        # Area principal
        self.contenido = tk.Frame(
            self.ventana,
            bg=self.COLOR_FONDO
        )

        self.contenido.pack(
            side="left",
            fill="both",
            expand=True
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

    # Elimina el contenido de la pantalla actual
    def limpiar_contenido(self):

        for elemento in self.contenido.winfo_children():
            elemento.destroy()

    # Crea el encabezado de cada pantalla
    def crear_encabezado(self, titulo):

        encabezado = tk.Frame(
            self.contenido,
            bg=self.COLOR_BLANCO,
            height=75
        )

        encabezado.pack(fill="x")
        encabezado.pack_propagate(False)

        tk.Label(
            encabezado,
            text=titulo,
            font=("Arial", 19, "bold"),
            bg=self.COLOR_BLANCO,
            fg=self.COLOR_TEXTO
        ).pack(side="left", padx=30, pady=20)

    # Pantalla de inicio
    def mostrar_inicio(self):

        self.limpiar_contenido()
        self.crear_encabezado("Inicio")

        panel = tk.Frame(
            self.contenido,
            bg=self.COLOR_FONDO
        )

        panel.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=40
        )

        tk.Label(
            panel,
            text="¡Bienvenido a Northwind!",
            font=("Arial", 23, "bold"),
            bg=self.COLOR_FONDO,
            fg=self.COLOR_TEXTO
        ).pack(anchor="w", pady=(20, 10))

        tk.Label(
            panel,
            text="Sistema de gestión de clientes",
            font=("Arial", 13),
            bg=self.COLOR_FONDO,
            fg="#64748B"
        ).pack(anchor="w")

        tk.Label(
            panel,
            text="Desde el menú lateral podés acceder al módulo de clientes "
                 "y administrar su información.",
            font=("Arial", 11),
            bg=self.COLOR_FONDO,
            fg=self.COLOR_TEXTO,
            wraplength=650,
            justify="left"
        ).pack(anchor="w", pady=(25, 0))

    # Pantalla de clientes
    def mostrar_clientes(self):

        self.limpiar_contenido()
        self.crear_encabezado("Administración de clientes")

        panel = tk.Frame(
            self.contenido,
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

        boton_editar = tk.Button(
            barra,
            text="Editar seleccionado",
            bg="#D97706",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            padx=15,
            pady=8,
            cursor="hand2",
            command=self.editar_cliente
        )

        boton_editar.pack(side="right", padx=10)   

        boton_eliminar = tk.Button(
            barra,
            text="Eliminar seleccionado",
            bg="#DC2626",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            padx=15,
            pady=8,
            cursor="hand2",
            command=self.eliminar_cliente
        )

        boton_eliminar.pack(side="right", padx=10)

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

        # Cargar clientes desde PostgreSQL
        self.cargar_clientes()

    # Pantalla acerca de
    def mostrar_acerca_de(self):

        self.limpiar_contenido()
        self.crear_encabezado("Acerca de")

        panel = tk.Frame(
            self.contenido,
            bg=self.COLOR_FONDO
        )

        panel.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=40
        )

        tk.Label(
            panel,
            text="Northwind - Gestión de Clientes",
            font=("Arial", 19, "bold"),
            bg=self.COLOR_FONDO,
            fg=self.COLOR_TEXTO
        ).pack(anchor="w", pady=(10, 20))

        tk.Label(
            panel,
            text="Sistema de administración de clientes desarrollado "
                 "como trabajo práctico integrador.",
            font=("Arial", 11),
            bg=self.COLOR_FONDO,
            fg="#64748B",
            wraplength=650,
            justify="left"
        ).pack(anchor="w", pady=5)

        
        tk.Label(
                    panel,
                    text="Tecnologías utilizadas:",
                    font=("Arial", 12, "bold"),
                    bg=self.COLOR_FONDO,
                    fg=self.COLOR_TEXTO
                ).pack(anchor="w", pady=(25, 10))
        
        tk.Label(
                    panel,
                    text="• Python\n• Tkinter\n• PostgreSQL",
                    font=("Arial", 11),
                    bg=self.COLOR_FONDO,
                    fg=self.COLOR_TEXTO,
                    justify="left"
                ).pack(anchor="w")

        tk.Label(
                    panel,
                    text="Desarrollado por:",
                    font=("Arial", 12, "bold"),
                    bg=self.COLOR_FONDO,
                    fg=self.COLOR_TEXTO
                ).pack(anchor="w", pady=(25, 10))
        
        tk.Label(
                    panel,
                    text="• Samuel\n• Daniela\n• Joaquín\n• Belén",
                    font=("Arial", 11),
                    bg=self.COLOR_FONDO,
                    fg=self.COLOR_TEXTO,
                    justify="left"
                ).pack(anchor="w")


    # Cargar clientes
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

    # Buscar clientes
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

    # Nuevo cliente
    
    def nuevo_cliente(self):

        # Crear ventana del formulario
        formulario = tk.Toplevel(self.ventana)
        formulario.title("Nuevo cliente")
        formulario.geometry("500x650")
        formulario.resizable(False, False)
        formulario.configure(bg=self.COLOR_FONDO)

        # Mantener el formulario delante de la ventana principal
        formulario.transient(self.ventana)
        formulario.grab_set()

        tk.Label(
            formulario,
            text="Registrar nuevo cliente",
            font=("Arial", 18, "bold"),
            bg=self.COLOR_FONDO,
            fg=self.COLOR_TEXTO
        ).pack(pady=(20, 5))

        tk.Label(
            formulario,
            text="Completá los datos del cliente",
            font=("Arial", 10),
            bg=self.COLOR_FONDO,
            fg="#64748B"
        ).pack(pady=(0, 15))

        # Campos del formulario
        campos = [
            ("ID del cliente", "customerid"),
            ("Empresa", "companyname"),
            ("Nombre del contacto", "contactname"),
            ("Cargo", "contacttitle"),
            ("Dirección", "address"),
            ("Ciudad", "city"),
            ("Región", "region"),
            ("Código postal", "postalcode"),
            ("País", "country"),
            ("Teléfono", "phone"),
            ("Fax", "fax")
        ]

        entradas = {}

        contenedor = tk.Frame(
            formulario,
            bg=self.COLOR_FONDO
        )

        contenedor.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=5
        )

        for etiqueta, nombre in campos:

            fila = tk.Frame(
                contenedor,
                bg=self.COLOR_FONDO
            )

            fila.pack(fill="x", pady=4)

            tk.Label(
                fila,
                text=etiqueta,
                font=("Arial", 10),
                bg=self.COLOR_FONDO,
                fg=self.COLOR_TEXTO,
                width=20,
                anchor="w"
            ).pack(side="left")

            entrada = tk.Entry(
                fila,
                font=("Arial", 10),
                width=28
            )

            entrada.pack(
                side="right",
                ipady=4
            )

            entradas[nombre] = entrada

        # Guardar cliente
        def guardar():

            datos = []

            for etiqueta, nombre in campos:
                valor = entradas[nombre].get().strip()
                datos.append(valor)

            # Validar campos obligatorios
            if datos[0] == "":
                messagebox.showwarning(
                    "Validación",
                    "El ID del cliente es obligatorio.",
                    parent=formulario
                )
                entradas["customerid"].focus()
                return

            if datos[1] == "":
                messagebox.showwarning(
                    "Validación",
                    "El nombre de la empresa es obligatorio.",
                    parent=formulario
                )
                entradas["companyname"].focus()
                return

            # Validar longitud del ID
            if len(datos[0]) > 5:
                messagebox.showwarning(
                    "Validación",
                    "El ID no puede superar los 5 caracteres.",
                    parent=formulario
                )
                entradas["customerid"].focus()
                return

            datos[0] = datos[0].upper()

            # Insertar en PostgreSQL
            resultado, error = insertar_cliente(tuple(datos))

            if resultado:

                messagebox.showinfo(
                    "Alta exitosa",
                    "El cliente se registró correctamente.",
                    parent=formulario
                )

                formulario.destroy()

                # Actualizar la tabla
                self.buscador.delete(0, tk.END)
                self.cargar_clientes()

            else:

                messagebox.showerror(
                    "Error al registrar",
                    "No se pudo guardar el cliente.\n\n" + error,
                    parent=formulario
                )

        # Botones
        botones = tk.Frame(
            formulario,
            bg=self.COLOR_FONDO
        )

        botones.pack(pady=15)

        tk.Button(
            botones,
            text="Guardar",
            bg="#16A34A",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            padx=25,
            pady=9,
            cursor="hand2",
            command=guardar
        ).pack(side="left", padx=10)

        tk.Button(
            botones,
            text="Cancelar",
            bg="#64748B",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            padx=25,
            pady=9,
            cursor="hand2",
            command=formulario.destroy
        ).pack(side="left", padx=10)

        entradas["customerid"].focus()

        # Modificar cliente
    def editar_cliente(self):

        seleccionado = self.tabla.selection()

        if not seleccionado:
            messagebox.showwarning(
                "Seleccionar cliente",
                "Primero seleccioná un cliente de la tabla."
            )
            return

        # Obtener los datos de la fila seleccionada
        elemento = self.tabla.item(seleccionado[0])
        valores = elemento["values"]

        customerid = valores[0]

        formulario = tk.Toplevel(self.ventana)
        formulario.title("Modificar cliente")
        formulario.geometry("500x620")
        formulario.resizable(False, False)
        formulario.configure(bg=self.COLOR_FONDO)

        formulario.transient(self.ventana)
        formulario.grab_set()

        tk.Label(
            formulario,
            text="Modificar cliente",
            font=("Arial", 18, "bold"),
            bg=self.COLOR_FONDO,
            fg=self.COLOR_TEXTO
        ).pack(pady=(20, 5))

        tk.Label(
            formulario,
            text="ID del cliente: " + str(customerid),
            font=("Arial", 10, "bold"),
            bg=self.COLOR_FONDO,
            fg=self.COLOR_TEXTO
        ).pack(pady=(0, 15))

        campos = [
            ("Empresa", "companyname"),
            ("Nombre del contacto", "contactname"),
            ("Cargo", "contacttitle"),
            ("Dirección", "address"),
            ("Ciudad", "city"),
            ("Región", "region"),
            ("Código postal", "postalcode"),
            ("País", "country"),
            ("Teléfono", "phone"),
            ("Fax", "fax")
        ]

        entradas = {}

        contenedor = tk.Frame(
            formulario,
            bg=self.COLOR_FONDO
        )

        contenedor.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=5
        )

        # Crear los campos y completar con los datos actuales
        for i in range(len(campos)):

            etiqueta, nombre = campos[i]

            fila = tk.Frame(
                contenedor,
                bg=self.COLOR_FONDO
            )

            fila.pack(fill="x", pady=4)

            tk.Label(
                fila,
                text=etiqueta,
                font=("Arial", 10),
                bg=self.COLOR_FONDO,
                fg=self.COLOR_TEXTO,
                width=20,
                anchor="w"
            ).pack(side="left")

            entrada = tk.Entry(
                fila,
                font=("Arial", 10),
                width=28
            )

            entrada.pack(side="right", ipady=4)

            entrada.insert(0, valores[i + 1])

            entradas[nombre] = entrada

        # Guardar modificaciones
        def guardar():

            datos = []

            for etiqueta, nombre in campos:
                valor = entradas[nombre].get().strip()
                datos.append(valor)

            if datos[0] == "":
                messagebox.showwarning(
                    "Validación",
                    "El nombre de la empresa es obligatorio.",
                    parent=formulario
                )
                entradas["companyname"].focus()
                return

            resultado, error = actualizar_cliente(
                tuple(datos),
                customerid
            )

            if resultado:

                messagebox.showinfo(
                    "Modificación exitosa",
                    "Los datos del cliente se actualizaron correctamente.",
                    parent=formulario
                )

                formulario.destroy()

                self.buscador.delete(0, tk.END)
                self.cargar_clientes()

            else:

                messagebox.showerror(
                    "Error al modificar",
                    "No se pudo actualizar el cliente.\n\n" + error,
                    parent=formulario
                )

        # Botones
        botones = tk.Frame(
            formulario,
            bg=self.COLOR_FONDO
        )

        botones.pack(pady=15)

        tk.Button(
            botones,
            text="Guardar cambios",
            bg="#16A34A",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            padx=20,
            pady=9,
            cursor="hand2",
            command=guardar
        ).pack(side="left", padx=10)

        tk.Button(
            botones,
            text="Cancelar",
            bg="#64748B",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            padx=25,
            pady=9,
            cursor="hand2",
            command=formulario.destroy
        ).pack(side="left", padx=10)

        entradas["companyname"].focus()

        # Eliminar cliente
    def eliminar_cliente(self):

        seleccionado = self.tabla.selection()

        if not seleccionado:
            messagebox.showwarning(
                "Seleccionar cliente",
                "Primero seleccioná un cliente de la tabla."
            )
            return

        elemento = self.tabla.item(seleccionado[0])
        valores = elemento["values"]

        customerid = valores[0]
        empresa = valores[1]

        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            "¿Estás seguro de que querés eliminar este cliente?\n\n"
            "ID: " + str(customerid) + "\n"
            "Empresa: " + str(empresa),
            icon="warning"
        )

        if not confirmar:
            return

        resultado, error = eliminar_cliente(customerid)

        if resultado:

            messagebox.showinfo(
                "Eliminación exitosa",
                "El cliente fue eliminado correctamente."
            )

            self.cargar_clientes()

        else:

            messagebox.showerror(
                "No se pudo eliminar",
                error
            ) 