class Categoria:
    def __init__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self.nombre = nombre

    def mostrar_info(self):
        print(f"ID de la categoria: {self.id_categoria} | Categoria: {self.nombre}")

class Producto:
    _codigo_auto = 1
    def __init__(self, nombre, precio_venta, categoria, stock=0, fecha_caducidad=None):
        self.id_producto = Producto._codigo_auto
        Producto._codigo_auto += 1
        self.nombre = nombre
        self.precio_venta = precio_venta
        self.categoria = categoria
        self.Id_categoria = categoria.id_categoria
        self.total_compras = 0
        self.total_ventas = 0
        self.stock = stock

    def registrar_compra(self, cantidad):
        self.total_compras += cantidad
        self.stock += cantidad

    def registrar_venta(self, cantidad):
        if cantidad > self.stock:
            print(f"No hay suficiente stock de {self.nombre}. Disponible: {self.stock}")
            return False
        self.total_ventas += cantidad
        self.stock = self.total_compras - self.total_ventas
        return True

    def mostrar_info(self):
        return f"ID del producto: {self.id_producto} | Producto: {self.nombre} | Precio: {self.precio_venta} | Stock: {self.stock} | Caducidad: {self.fecha_caducidad}"

class Persona:
    def __init__(self, nombre, telefono, direccion, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo

class Cliente(Persona):
    def __init__(self, nit, nombre, telefono, direccion, correo):
        super().__init__(nombre,telefono,direccion,correo)
        self.nit = nit

    def mostrar_info(self):
        return f"NIT: {self.nit} | Cliente: {self.nombre} | Teléfono: {self.telefono} | Dirección:{self.direccion} | Correo: {self.correo}"

class Empleado(Persona):
    def __init__(self, id_empleado, nombre, telefono, direccion, correo):
        super().__init__(nombre, telefono, direccion, correo)
        self.id_empleado = id_empleado

    def cargar_empleados(self):
        try:
            with open("empleados.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    id_emp, nombre, telefono, direccion, correo = linea.strip().split(":")
                    self.empleados.append(Empleado(int(id_emp), nombre, telefono, direccion, correo))
        except FileNotFoundError:
            pass

    def guardar_empleados(self):
        with open("empleados.txt", "w", encoding="utf-8") as archivo:
            for e in self.empleados:
                archivo.write(f"{e.id_empleado}:{e.nombre}:{e.telefono}:{e.direccion}:{e.correo}\n")

    def agregar_empleado(self, nombre, telefono, direccion, correo):
        id_emp = len(self.empleados) + 1
        self.empleados.append(Empleado(id_emp, nombre, telefono, direccion, correo))
        self.guardar_empleados()

class Cajero(Empleado):
    def realizar_venta(self, productos_seleccionados):
        total = 0
        print("\n--- Resumen de venta----")
        for producto, cantidad in productos_seleccionados.items():
            if producto.registrar_venta(cantidad):
                subtotal = producto.precio * cantidad
                total += subtotal
                print(f"{producto.nombre}: {cantidad} x {producto.precio} = {subtotal}")
                print(f"Total a pagar: {total}")
                return total

class Administrador(Persona):
    def registrar_producto(self, gestion_productos, nombre, precio, categoria, stock=0, fecha_caducidad=None):
        gestion_productos.agregar(nombre, precio, categoria, stock, fecha_caducidad)

class Proveedor(Persona):
    def cargar_proveedores(self):
        try:
            with open("proveedores.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    id_proveedor, nombre, empresa = linea.strip().split(":")
                    self.proveedores.append(Proveedor(int(id_proveedor), nombre, empresa))
        except FileNotFoundError:
            pass

    def guardar_proveedores(self):
        with open("proveedores.txt", "w", encoding="utf-8") as archivo:
            for pr in self.proveedores:
                archivo.write(f"{pr.id_proveedor}:{pr.nombre}:{pr.empresa}\n")

    def agregar_proveedor(self, nombre, empresa):
        id_proveedor = len(self.proveedores) + 1
        self.proveedores.append(Proveedor(id_proveedor, nombre, empresa))
        self.guardar_proveedores()


class GestionCategorias:
    def __init__(self):
        self,categorias = {}

    def agregar(self, id_categoria, nombre):
        self.categorias[id_categoria] = Categoria(id_categoria, nombre)

    def listar(self):
        if not self.categorias:
            print("No hay categorias")
        else:
            for c in self.categorias. values():
                print(c.mostrar_info())

class GestionProducto:
    def __init__(self):
        self.id_producto = {}

    def Agregar(self, nombre, precio, categoria, stock=0, fecha_caducidad=None):
        producto = Producto(nombre, precio, categoria, stock, fecha_caducidad)
        self.producto[producto.id_producto] = producto
        print(f"Producto '{nombre}' agregado correctamente. ")

    def listar(self):
        if not self.productos:
            print("No hay productos.")
        else:
            for p in self.productos.values():
                print(p.mostrar_info())

class GestionClientes:
        def __init__(self):
            self.clientes = {}
            self.cargar_clientes()

        def cargar_clientes(self):
            try:
                with open('clientes.txt', 'r', encoding="utf-8") as archivo:
                    for linea in archivo:
                        linea = linea.strip()
                        if linea:
                            nit, nombre, direccion, telefono, correo = linea.split(':')
                            self.cliente[nit] = {
                                "Nombre": nombre,
                                "Direccion": direccion,
                                "Telefono": telefono,
                                "Correo": correo
                            }
                print("Clientes importados desde clientes.txt")
            except FileNotFoundError:
                print("No existe el archivo clientes.txt, se creara uno nuevo al guardar. ")

        def guardar_clientes(self):
            with open('clientes.txt', 'w', encoding="utf-8") as archivo:
                for nit, datos in self.clientes.items():
                    archivo.write(f"{nit}: {datos['Nombre']}: {datos['Direccion']}:{datos["Telefono"]}:{datos['Correo']}")

        def agregar_cliente(self, nit, nombre, direccion, telefono, correo):
            self.clientes[nit] = {
                "Nombre": nombre,
                "Direccion": direccion,
                "Telefono": telefono,
                "Correo": correo
            }
            self.guargar_clientes()
            print(f"Cliente con NIT {nit} agregado y guardado correctamente.")

        def mostrar_todo(self):
            if self.clientes:
                print("\nLista de clientes:")
                for nit, datos in self.clientes.items():
                    print(f"\nNIT: {nit}")
                    for clave,valor in datos.items():
                        print(f"\t{clave}: {valor}")
            else:
                print("No hay clientes registrados.")

gestion_categorias = GestionCategorias()
gestion_producto = GestionProducto()
gestion_clientes = GestionClientes()

while True:
    print("\n---MENU ADMINISTRADOR---")
    print("1. Agregar proveedor")
    print("2. Agregar empleado")
    print("3. Listar proveedores")
    print("4. Listar empleados")
    print("5. Listar productos")
    print("6. Agregar productos")
    print("7. Volver")
    opcion= input("Seleccione una opcion:")

    if opcion == "1":
        nombre = input("Nombre del proveedor: ")
        empresa = input("Empresa: ")
        gestion.agregar_proveedor(nombre, empresa)
        print("Proveedor agregado.")
    elif opcion == "2":
        nombre = input("Nombre: ")
        telefeno = input("Telefono: ")
        direccion = input("Direccion: ")
        correo = input("Correo: ")
        gestion.agregar_empleado(nombre, telefeno, direccion, correo)
        print("Empleado agregado.")
    elif opcion == "3":
        for p in gestion.proveedores:
            print(f"{p.id_proveedor} - {p.nombre} -  Empresa: {p.empresa}")
    elif opcion == "4":
        for e in gestion.empleados:
            print(f"{e.id_empleado} - {e.nombre} -  {e.telefono}")
    elif opcion == "5":
        for p in gestion.productos:
            print(f"{p.id_producto} - {p.nombre} - Stock:{p.stock} - Precio: Q{p.precio}")
    elif opcion == "6":
        nombre = input("Nombre del producto: ")
        precio =float(input("Precio: "))
        stock = int(input("Stock: "))
        categoria = input("Categoria: ")
        gestion.agregar_producto(nombre, precio, stock, categoria, stock)
        print("Producto agregado.")
    elif opcion == "7":
        nombre = input("Nombre del producto: ")