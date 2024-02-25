import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re  # Importa el módulo re para trabajar con expresiones regulares

class Aplicacion:
    def __init__(self, root):
        # Inicialización de variables de usuarios, inventario, proveedores y mensajes
        self.usuarios = {"admin": {"contraseña": "0000"}}  # Diccionario de usuarios con el formato {correo: {contraseña: contraseña}}
        self.inventario = {}  # Diccionario de inventario de productos
        self.proveedores = {}  # Diccionario de proveedores con el formato {nombre_proveedor: telefono}
        self.mensajes = {}  # Diccionario de mensajes
        # Configuración de la ventana principal
        self.root = root
        self.root.title("ACCUNTI")
        self.root.geometry("600x400")  # Tamaño personalizado
        self.root.configure(bg="#90EE90")  # Establecer color de fondo verde
        # Creación de los paneles de inicio de sesión y aplicación
        self.login_panel = self.create_login_panel()
        self.app_panel = self.create_app_panel()
        self.current_panel = None  # Inicialmente no hay ningún panel mostrado
        self.mostrar_panel(self.login_panel)

    # Función para crear el panel de inicio de sesión
    def create_login_panel(self):
        login_panel = tk.Frame(self.root, bg="#90EE90", padx=20, pady=20)  # Crear un marco con fondo verde claro
        tk.Label(login_panel, text="Correo electrónico:", bg="#90EE90").grid(row=0, column=0)  # Etiqueta para correo electrónico
        tk.Label(login_panel, text="Contraseña:", bg="#90EE90").grid(row=1, column=0)  # Etiqueta para contraseña
        self.correo_entry = tk.Entry(login_panel)  # Campo de entrada para correo electrónico
        self.contraseña_entry = tk.Entry(login_panel, show="*")  # Campo de entrada para contraseña con modo de visualización oculto
        self.correo_entry.grid(row=0, column=1)
        self.contraseña_entry.grid(row=1, column=1)
        # Botón para iniciar sesión
        login_button = tk.Button(login_panel, text="Ingresar", command=self.login, bg="#2E8B57", width=10)
        login_button.grid(row=2, columnspan=2)
        # Botón para registro de usuario
        registrar_button = tk.Button(login_panel, text="Registrarse", command=self.registrar_usuario, bg="#2E8B57", width=10)
        registrar_button.grid(row=3, columnspan=2)
        return login_panel

    # Función para crear el panel de la aplicación
    def create_app_panel(self):
        app_panel = tk.Frame(self.root, bg="#90EE90")  # Crear un marco con fondo verde claro
        # Botones para las diferentes funciones de la aplicación
        inventario_button = tk.Button(app_panel, text="Inventario", command=self.mostrar_inventario, bg="#2E8B57", width=15)
        inventario_button.grid(row=0, column=0, padx=10, pady=10)
        enviar_mensaje_button = tk.Button(app_panel, text="Enviar mensaje", command=self.mostrar_dialogo_enviar_mensaje, bg="#2E8B57", width=15)
        enviar_mensaje_button.grid(row=0, column=1, padx=10, pady=10)
        añadir_usuario_button = tk.Button(app_panel, text="Añadir Usuario", command=self.mostrar_dialogo_añadir_usuario, bg="#2E8B57", width=15)
        añadir_usuario_button.grid(row=0, column=2, padx=10, pady=10)
        crear_producto_button = tk.Button(app_panel, text="Crear Producto", command=self.mostrar_dialogo_crear_producto, bg="#2E8B57", width=15)
        crear_producto_button.grid(row=1, column=0, padx=10, pady=10)
        borrar_producto_button = tk.Button(app_panel, text="Borrar Producto", command=self.borrar_producto, bg="#2E8B57", width=15)
        borrar_producto_button.grid(row=1, column=1, padx=10, pady=10)
        añadir_proveedor_button = tk.Button(app_panel, text="Añadir Proveedor", command=self.mostrar_dialogo_añadir_proveedor, bg="#2E8B57", width=15)
        añadir_proveedor_button.grid(row=1, column=2, padx=10, pady=10)
        ver_proveedores_button = tk.Button(app_panel, text="Ver Proveedores", command=self.mostrar_proveedores, bg="#2E8B57", width=15)
        ver_proveedores_button.grid(row=2, column=0, padx=10, pady=10)
        cerrar_sesion_button = tk.Button(app_panel, text="Cerrar Sesión", command=self.cerrar_sesion, bg="#2E8B57", width=10)
        cerrar_sesion_button.grid(row=3, column=0, padx=10, pady=10, sticky="sw")
        return app_panel

    # Función para mostrar un panel específico
    def mostrar_panel(self, panel):
        if self.current_panel is not None:
            self.current_panel.pack_forget()
        self.current_panel = panel
        self.current_panel.pack()

    # Función para iniciar sesión
    def login(self):
        correo = self.correo_entry.get()
        contraseña = self.contraseña_entry.get()
        if correo in self.usuarios and self.usuarios[correo]["contraseña"] == contraseña:
            messagebox.showinfo("Acceso concedido", "Acceso concedido.")
            self.mostrar_panel(self.app_panel)
        else:
            messagebox.showerror("Acceso denegado", "Acceso denegado.")

    # Función para registrar un nuevo usuario
    def registrar_usuario(self):
        correo = self.correo_entry.get()
        contraseña = self.contraseña_entry.get()
        if correo in self.usuarios:
            messagebox.showerror("Error", "El usuario ya existe.")
        else:
            self.usuarios[correo] = {"contraseña": contraseña}
            messagebox.showinfo("Registro exitoso", "Usuario registrado correctamente.")

    # Función para mostrar el inventario
    def mostrar_inventario(self):
        inventario_dialog = tk.Toplevel(self.root)
        inventario_dialog.title("Inventario")
        table = ttk.Treeview(inventario_dialog, columns=("Nombre", "Cantidad"), show="headings")
        table.heading("Nombre", text="Nombre")
        table.heading("Cantidad", text="Cantidad")
        table.pack()
        for nombre, cantidad in self.inventario.items():
            table.insert("", "end", values=(nombre, cantidad))

    # Función para mostrar el diálogo de enviar mensaje
    def mostrar_dialogo_enviar_mensaje(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Enviar Mensaje")
        tk.Label(dialog, text="Destinatario:", bg="#90EE90").grid(row=0, column=0)
        self.destinatario_combobox = ttk.Combobox(dialog, values=list(self.usuarios.keys()))
        self.destinatario_combobox.grid(row=0, column=1)
        tk.Label(dialog, text="Mensaje:", bg="#90EE90").grid(row=1, column=0)
        self.mensaje_entry = tk.Entry(dialog)
        self.mensaje_entry.grid(row=1, column=1)
        enviar_button = tk.Button(dialog, text="Enviar", command=self.enviar_mensaje, bg="#2E8B57", width=10)
        enviar_button.grid(row=2, columnspan=2)

    # Función para enviar mensaje
    def enviar_mensaje(self):
        destinatario = self.destinatario_combobox.get()
        mensaje = self.mensaje_entry.get()
        if destinatario and mensaje:
            if destinatario not in self.mensajes:
                self.mensajes[destinatario] = []
            self.mensajes[destinatario].append(mensaje)
            messagebox.showinfo("Mensaje enviado", f"Mensaje enviado a {destinatario}: {mensaje}")
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos.")

    # Función para mostrar el diálogo de añadir usuario
    def mostrar_dialogo_añadir_usuario(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Añadir Usuario")
        tk.Label(dialog, text="Nuevo Correo electrónico:", bg="#90EE90").grid(row=0, column=0)
        self.nuevo_correo_entry = tk.Entry(dialog)
        self.nuevo_correo_entry.grid(row=0, column=1)
        tk.Label(dialog, text="Contraseña:", bg="#90EE90").grid(row=1, column=0)
        self.nueva_contraseña_entry = tk.Entry(dialog, show="*")
        self.nueva_contraseña_entry.grid(row=1, column=1)
        añadir_button = tk.Button(dialog, text="Añadir", command=self.añadir_usuario, bg="#2E8B57", width=10)
        añadir_button.grid(row=2, columnspan=2)

    # Función para añadir un nuevo usuario
    def añadir_usuario(self):
        correo = self.nuevo_correo_entry.get()
        contraseña = self.nueva_contraseña_entry.get()
        if correo and contraseña:
            if correo in self.usuarios:
                messagebox.showerror("Error", "El correo electrónico ya está registrado.")
            else:
                self.usuarios[correo] = {"contraseña": contraseña}
                messagebox.showinfo("Usuario añadido", "Usuario añadido exitosamente.")
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos.")

    # Función para mostrar el diálogo de crear producto
    def mostrar_dialogo_crear_producto(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Crear Producto")
        tk.Label(dialog, text="Nombre del Producto:", bg="#90EE90").grid(row=0, column=0)
        tk.Label(dialog, text="Cantidad:", bg="#90EE90").grid(row=1, column=0)
        self.nombre_producto_entry = tk.Entry(dialog)
        self.cantidad_entry = tk.Entry(dialog)
        self.nombre_producto_entry.grid(row=0, column=1)
        self.cantidad_entry.grid(row=1, column=1)
        crear_button = tk.Button(dialog, text="Crear", command=self.crear_producto, bg="#2E8B57", width=10)
        crear_button.grid(row=2, columnspan=2)

    # Función para crear un nuevo producto
    def crear_producto(self):
        nombre_producto = self.nombre_producto_entry.get()
        cantidad = self.cantidad_entry.get()
        if nombre_producto and cantidad:
            self.inventario[nombre_producto] = int(cantidad)
            messagebox.showinfo("Producto creado", "Producto creado exitosamente.")
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos.")

    # Función para mostrar el diálogo de añadir proveedor
    def mostrar_dialogo_añadir_proveedor(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Añadir Proveedor")
        tk.Label(dialog, text="Nombre del Proveedor:", bg="#90EE90").grid(row=0, column=0)
        self.nombre_proveedor_entry = tk.Entry(dialog)
        self.nombre_proveedor_entry.grid(row=0, column=1)
        tk.Label(dialog, text="Teléfono:", bg="#90EE90").grid(row=1, column=0)
        self.telefono_entry = tk.Entry(dialog)
        self.telefono_entry.grid(row=1, column=1)
        añadir_button = tk.Button(dialog, text="Añadir", command=self.añadir_proveedor, bg="#2E8B57", width=10)
        añadir_button.grid(row=2, columnspan=2)

    # Función para añadir un nuevo proveedor
    def añadir_proveedor(self):
        nombre_proveedor = self.nombre_proveedor_entry.get()
        telefono = self.telefono_entry.get()
        if nombre_proveedor and telefono:
            self.proveedores[nombre_proveedor] = telefono
            messagebox.showinfo("Proveedor añadido", "Proveedor añadido exitosamente.")
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos.")

    # Función para mostrar el diálogo de ver proveedores
    def mostrar_proveedores(self):
        proveedores_dialog = tk.Toplevel(self.root)
        proveedores_dialog.title("Proveedores")
        for proveedor, telefono in self.proveedores.items():
            tk.Label(proveedores_dialog, text=f"Nombre: {proveedor}, Teléfono: {telefono}").pack()

    # Función para borrar un producto
    def borrar_producto(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Borrar Producto")
        tk.Label(dialog, text="Seleccione un producto para borrar:", bg="#90EE90").pack()
        productos_listbox = tk.Listbox(dialog)
        for nombre in self.inventario.keys():
            productos_listbox.insert("end", nombre)
        productos_listbox.pack()
        borrar_button = tk.Button(dialog, text="Borrar", command=lambda: self.borrar_producto_seleccionado(productos_listbox), bg="#2E8B57", width=10)
        borrar_button.pack()

    # Función para borrar un producto seleccionado
    def borrar_producto_seleccionado(self, listbox):
        nombre_producto = listbox.get(listbox.curselection())
        del self.inventario[nombre_producto]
        messagebox.showinfo("Producto borrado", "Producto borrado exitosamente.")
        listbox.delete(listbox.curselection())

    # Función para cerrar sesión
    def cerrar_sesion(self):
        self.mostrar_panel(self.login_panel)

# Crear la ventana principal de la aplicación
root = tk.Tk()
# Iniciar la aplicación
app = Aplicacion(root)
# Ejecutar el bucle principal de la aplicación
root.mainloop()
