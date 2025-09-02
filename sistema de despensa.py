class Categoria:
    def __init__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self.nombre = nombre

    def mostrar_info(self):
        print(f"ID de la categoria: {self.id_categoria} | Categoria: {self.nombre}")

class Producto:
    _id_auto = 1

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
        self.fecha_caducidad= fecha_caducidad

    def registrar_compra(self, cantidad):
        self.total_compras += cantidad
        self.stock += cantidad

    def registrar_venta(self, cantidad):
        if cantidad > self.stock:
            print(f"No hay suficiente stock de {self.nombre}. Disponible: {self.stock}")
            return False
        self.total_ventas += cantidad
        self.stock -= cantidad
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
        self.empleados = []

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
    def __init__(self, id_proveedor, nombre, telefono, direccion, correo, empresa):
        super().__init__(nombre, telefono, direccion, correo)
        self.id_proveedor = id_proveedor
        self.empresa = empresa
        self.proveedors = []

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

class GestionCategoria:
    def __init__(self):
        self.categorias = {}

    def agregar(self, id_categoria, nombre):
        self.categorias[id_categoria] = Categoria(id_categoria, nombre)

    def listar(self):
        if not self.categorias:
            print("No hay categorías. ")
        else:
            for c in self.categorias.values():
                c.mostrar_info()

class GestionProducto:
    def __init__(self):
        self.productos = {}

    def agregar(self,nombre,precio, categoria, stock=0, fecha_caducidad=None):
        producto = Producto(nombre, precio, categoria, stock, fecha_caducidad)
        self.productos[producto.id_producto] = producto
        print(f"Producto '{nombre}' agregado correctamente.")

    def listar(self):
        if not self.productos:
            print("No hay productos. ")
        else:
            for p in self.productos.values():
                print(p.mostrar_info())

class GestionClientes:
    def __init__(self):
        self.clientes = {}
        self.carga_clientes()

    def cargar_clientes(self):
        try:
            with open("clientes.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        nit, nombre, direccion, telefono, correo = linea.split(":")
                        self.clientes[nit] = {
                            "Nombre": nombre,
                            "Direccion": direccion,
                            "Telefono": telefono,
                            "Correo": correo
                        }
            print("Clientes importados desde clientes.txt")
        except FileNotFoundError:
            print("No existe el archivo clientes.txt, se creará uno nuevo al guardar. ")

    def guardar_clientes(self):
        with open("clientes.txt", "w", encoding="utf-8") as archivo:
            for nit, datos in self.clientes.items():
                archivo.write(f"{nit}:{datos['Nombre']}:{datos['Direccion']}:{datos['Telefono']}:{datos['Correo']}")

    def agregar_cliente(self, nit, nombre, direccion,telefono, correo):
        self.clientes[nit] = {
            "Nombre": nombre,
            "Direccion": direccion,
            "Telefono": telefono,
            "Correo": correo
        }
        self.guardar_clientes()
        print(f"Cliente con NIT {nit} agregado y guardado correctamente.")

    def mostrar_todo(self):
        if self.clientes:
            print("\nLISTA DE CLIENTES")
            for nit, datos in self.clientes.items():
                print(f"NIT: {nit}")
                for clave, valor in datos.items():
                    print(f"\t{clave}: {valor}")
        else:
            print("No hay clientes registrados.")

class Venta:
    _codigo_auto=1

    def __init__(self, fecha, NIT, id_empleado, total=0.0):
        self.id_venta = Venta._codigo_auto
        Venta._codigo_auto+=1
        self.fecha = fecha
        self.NIT = NIT
        self.id_empleado = id_empleado
        self.total = total

    def mostrar_info(self):
        return f"ID Venta: {self.id_venta}| Fecha:{self.fecha} | NIT: {self.NIT} | ID del empleado: {self.id_empleado} | Total: {self.total}"

class DetalleVenta:
    def __init__(self, id_detalleventa, id_venta, nombre_producto, cantidad, id_producto, precio):
        self.id_detalleventa = id_detalleventa
        self.id_venta = id_venta
        self.cantidad = cantidad
        self.id_producto = id_producto
        self.precio = precio
        self.subtotal = precio * cantidad
        self.nombre_producto = nombre_producto

    def  mostrar_info(self):
        return f"ID Detalle de la venta: {self.id_detalleventa} |  ID de la venta: {self.id_venta} | Cantidad: {self.cantidad}  | Precio: {self.precio} | Subtotal: {self.subtotal}"

class Compra:
    def __init__(self, id_compras, fecha_compra, id_proveedor, id_empleado):
        self.id_compras = id_compras
        self.fecha_compra = fecha_compra
        self.id_proveedor = id_proveedor
        self.id_empleado = id_empleado
        self.detalles = []
        self.total = 0.0

    def mostrar_info(self):
        return f"ID de compras: {self.id_compras} | Fecha de compra: {self.fecha_compra} | ID del proveedor: {self.id_proveedor} | ID del empleado:{self.id_empleado} | Total gastado: {self.total}"

class Detalle_compra:
    def __init__(self, nombre_producto, id_detallecompra, id_compras, cantidad, id_producto, precio_compra, sub_total, fecha_caducidad ):
        self.id_detallecompra = id_detallecompra
        self.id_compras = id_compras
        self.cantidad = cantidad
        self.id_producto = id_producto
        self.precio_compra = precio_compra
        self.sub_total = cantidad * precio_compra
        self.fecha_caducidad = fecha_caducidad
        self.nombre_producto = nombre_producto

    def mostrar_info(self):
        return f"ID del detalle de compra: {self.id_detallecompra} | ID de compras: {self.id_compras} | Cantidad de compra: {self.cantidad} | ID del producto: {self.id_producto} Fecha de caducidad: {self.fecha_caducidad} | Precio de compra: {self.precio_compra} | Sub total: {self.sub_total}"

def menu_administrador():
    while True:
        print("\n=== MENÚ ADMINISTRADOR ===")
        print("1. Agregar categoría")
        print("2. Agregar producto")
        print("3. Agregar proveedor")
        print("4. Agregar empleado")
        print("5. Listar todo")
        print("6. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre de la categoría: ")
            id_categoria = len(gestion.categorias) + 1
            gestion.categorias.append(Categoria(id_categoria, nombre))
            gestion.guardar_datos()
            print("Categoría agregada.")
        elif opcion == "2":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio: "))
            stock = int(input("Stock inicial: "))
            for cat in gestion.categorias:
                print(f"{cat.id_categoria} - {cat.nombre}")
            id_categoria = int(input("ID de la categoría: "))
            categoria = next((c for c in gestion.categorias if c.id_categoria == id_categoria), None)
            if categoria:
                id_producto = len(gestion.productos) + 1
                gestion.productos.append(Producto(id_producto, nombre, precio, categoria, stock))
                gestion.guardar_datos()
                print("Producto agregado.")
            else:
                print("Categoría no encontrada.")
        elif opcion == "3":
            nombre = input("Nombre del proveedor: ")
            empresa = input("Empresa: ")
            telefono = input("Teléfono: ")
            direccion = input("Dirección: ")
            correo = input("Correo: ")
            for cat in gestion.categorias:
                print(f"{cat.id_categoria} - {cat.nombre}")
            id_categoria = int(input("ID de la categoría principal del proveedor: "))
            id_proveedor = len(gestion.proveedores) + 1
            gestion.proveedores.append(Proveedor(id_proveedor, nombre, empresa, telefono, direccion, correo, id_categoria))
            gestion.guardar_datos()
            print("Proveedor agregado.")
        elif opcion == "4":
            nombre = input("Nombre del empleado: ")
            telefono = input("Teléfono: ")
            direccion = input("Dirección: ")
            correo = input("Correo: ")
            id_empleado = len(gestion.empleados) + 1
            gestion.empleados.append(Empleado(id_empleado, nombre, telefono, direccion, correo))
            gestion.guardar_datos()
            print("Empleado agregado.")
        elif opcion == "5":
            print("\n=== CATEGORÍAS ===")
            for c in gestion.categorias:
                print(f"{c.id_categoria} - {c.nombre}")
            print("\n=== PRODUCTOS ===")
            for p in gestion.productos:
                print(f"{p.id_producto} - {p.nombre} - Precio: Q{p.precio} - Stock: {p.stock} - Categoría: {p.categoria.nombre}")
            print("\n=== PROVEEDORES ===")
            for pr in gestion.proveedores:
                print(f"{pr.id_proveedor} - {pr.nombre} - Empresa: {pr.empresa}")
            print("\n=== EMPLEADOS ===")
            for e in gestion.empleados:
                print(f"{e.id_empleado} - {e.nombre}")
        elif opcion == "6":
            break
        else:
            print("Opción inválida.")

def menu_empleado():
    while True:
        print("\n=== MENÚ EMPLEADO ===")
        print("1. Pagar compras a proveedores")
        print("2. Listar productos")
        print("3. Listar proveedores")
        print("4. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Esta opción procesaría pagos a proveedores (simulación).")
        elif opcion == "2":
            for p in gestion.productos:
                print(f"{p.id_producto} - {p.nombre} - Stock: {p.stock}")
        elif opcion == "3":
            for pr in gestion.proveedores:
                print(f"{pr.id_proveedor} - {pr.nombre} - Empresa: {pr.empresa}")
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

def menu_cajero():
    while True:
        print("\n=== MENÚ CAJERO ===")
        print("1. Agregar cliente")
        print("2. Vender productos")
        print("3. Listar productos")
        print("4. Listar clientes")
        print("5. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nit = input("NIT del cliente: ")
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            direccion = input("Dirección: ")
            correo = input("Correo: ")
            gestion.clientes.append(Cliente(nit, nombre, telefono, direccion, correo))
            gestion.guardar_datos()
            print("Cliente agregado.")
        elif opcion == "2":
            menu_cliente()
        elif opcion == "3":
            for p in gestion.productos:
                print(f"{p.id_producto} - {p.nombre} - Precio: Q{p.precio} - Stock: {p.stock}")
        elif opcion == "4":
            for c in gestion.clientes:
                print(f"{c.nit} - {c.nombre}")
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")

def menu_cliente():
    carrito = Carrito()
    while True:
        print("\n=== MENÚ CLIENTE ===")
        print("1. Ver productos y agregar al carrito")
        print("2. Finalizar selección y pasar a caja")
        print("3. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            for prod in gestion.productos:
                print(f"{prod.id_producto} - {prod.nombre} - Precio: Q{prod.precio} - Stock: {prod.stock}")
            try:
                prod_id = int(input("Ingrese el ID del producto a agregar: "))
                producto = next((p for p in gestion.productos if p.id_producto == prod_id), None)
                if producto:
                    cantidad = int(input(f"Ingrese la cantidad de '{producto.nombre}': "))
                    carrito.agregar_item(producto, cantidad)
                else:
                    print("Producto no encontrado.")
            except ValueError:
                print("Debe ingresar números válidos.")
        elif opcion == "2":
            total = carrito.mostrar_carrito()
            if total > 0:
                print("\nAhora un cajero procesará la venta...")
                menu_cajero_venta(carrito)
            break
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")

def menu_cajero_venta(carrito):
    contraseña = input("Ingrese contraseña del cajero: ")
    if contraseña != "dinero":
        print("Contraseña incorrecta.")
        return
    total = carrito.mostrar_carrito()
    confirm = input(f"El total a pagar es Q{total}. Confirmar venta? (s/n): ").lower()
    if confirm == "s":
        for item in carrito.items:
            item["producto"].stock -= item["cantidad"]
            id_detalle = len(gestion.detalle_ventas) + 1
            venta = Venta("Cliente", 1, total)
            gestion.ventas.append(venta)
            gestion.detalle_ventas.append(DetalleVenta(id_detalle, venta, item["producto"], item["cantidad"]))
        gestion.guardar_datos()
        print("Venta realizada exitosamente.")
    else:
        print("Venta cancelada.")

def menu_principal():
    while True:
        print("\n=== SISTEMA DE DESPENSA ===")
        print("1. Administrador")
        print("2. Empleado")
        print("3. Cajero")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_administrador()
        elif opcion == "2":
            menu_empleado()
        elif opcion == "3":
            menu_cajero()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")