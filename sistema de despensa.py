class Categoria:
    def __init__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self.nombre = nombre

class Producto:
    def __init__(self, id_producto, nombre, precio, categoria, total_compras=0, total_ventas=0, stock=0):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.total_compras = total_compras
        self.total_ventas = total_ventas
        self.stock = stock

class Cliente:
    def __init__(self, nit,  nombre_cliente, telefono, direccion, correo):
        self.nit = nit
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo

    def mostrar_info(self):
        print(f"NIT: {self.nit} | Nombre: {self.nombre} | Teléfono: {self.telefono} | Dirección:{self.direccion} | Correo: {self.correo}")


class Empleado:
    def __init__(self, id_empleado, nombre, telefono, direccion, correo):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo

    def mostrar_info(self):
        return f"ID: {self.id_empleado}, Nombre: {self.nombre}, Teléfono: {self.telefono}, Dirección:{self.direccion}, Correo: {self.correo}"
class Provedor:
    def __init__(self, id_provedor, nombre_provedor, empresa, telefono, direccion, correo, id_categoria):
        self.id_provedor = id_provedor
        self.nombre = nombre
        self.empresa = empresa
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo
        self.id_categoria = id_categoria

class Venta:
    def __init__(self, id_venta, fecha, nit, id_empleado, total):
        self.id_venta = id_venta
        self.fecha = fecha
        self.nit = nit
        self.id_empleado = id_empleado
        self.total = total

class Detalle_venta:
    def __init__(self, id_detalleventa, id_venta, cantidad, id_producto, precio, subtotal):
        self.id_venta = id_venta
        self.cantidad = cantidad
        self.id_producto = id_producto
        self.precio = precio
        self.subtotal = subtotal
        self.id_detalleventa = id_detalleventa

class Compra:
    def __init__(self, id_compras, fecha_compra, id_provedor, id_empleado, total):
        self.id_compras = id_compras
        self.fecha_compra = fecha_compra
        self.id_provedor = id_provedor
        self.id_empleado = id_empleado
        self.total = total

class Detalle_compra:
    def __init__(self, id_detallecompra, id_compras, cantidad_compra, id_producto, precio_compra, sub_total, fecha_caducidad ):
        self.id_detallecompra = id_detallecompra
        self.id_compras = id_compras
        self.cantidad_compra = cantidad_compra
        self.id_producto = id_producto
        self.precio_compra = precio_compra
        self.sub_total = sub_total
        self.fecha_caducidad = fecha_caducidad


clientes =  {}
empleados = {}
provedor = {}
ventas = {}
detalle_ventas = {}
compras = {}
detalle_compras = {}

class GestionCategorias:
    def __init__(self):
        self.categorias = {}

    def agregar(self, id_categoria, nombre):
        self.categorias[id_categoria] = Categoria(id_categoria,nombre)

    def listar(self):
        for c in self.categorias.values():
            print(f"[{c.id_categoria}] {c.nombre}")

class GestionProductos:
    def __init__(self):
        self.productos = {}

    def agregar(self, id_producto, nombre, id_categoria, precio, stock):
        self.productos[id_producto] = Producto(id_producto, nombre, id_categoria, precio, 0,0, stock)

    def listar(self):
        for p in self.productos.values():
            print(p.mostrar_info())

class GestinClientes:
    def __init__(self):
        self.clientes = {}

    def agregar_cliente(self, cliente):
        if cliente.nit in self.clientes:
            print("El cliente con este NIT ya existe.")
        else:
            self.clientes[cliente.nit] = cliente
            print("El cliente ha sido agregado correctamente.")

    def listar_clientes(self):
        if not self.clientes:
            print("No hay clientes registrados.")
        else:
            print("\n Lista de clientes:")
            for clientes in self.clientes.values():
                print(clientes.mostrar_info())

    def buscar_cliente(self, nit):
        if nit in self.clientes:
            return self.clientes[nit]
        else:
            print("No hay cliente registrado.")
            return None

usuario = {
    "admin": "123",
    "empleado": "abcd"
}
print("\n ---SISTEMA DE GESTIÓN--- ")
print("1. Adminstrador")
print("2. Empleado")
rol = input("Selecciona tu rol en la empresa: ")

if rol =="1":
    usuario = "admin"
elif rol =="2":
    usuario = "empleado"
else:
    print("Rol inválido. Saliendo...")
    exit()

password = input(f" Ingrese contraseña para {usuario}: ")
if usuario[usuario] !=password:
    print("Contraseña incorrecta. Acceso denegado.")
    exit()
    print(f"Bienvenido, {usuario}")

while True:
    print("\n--- MENÚ PRINCIPAL---")
    if rol == "admin":

        print("1. Cantegorias")
        print("2. Productos")
        print("3. Clientes")
        print("4. Empleados")
        print("5. Proveedores")
        print("6. Ventas")
        print("7. Detalles de ventas")
        print("8. Compras")
        print("9. Detalle de compras")
        print("10. Salir")
    else:
        print("1. Categorías")
        print("2. Productos")
        print("3. Clientes")
        print("4. Ventas")
        print("5. Compras")
        print("6. Salir")

    opcion = input("Elige una opción:")
    if (usuario == "admin" and opcion == "10") or (usuario == "empleado" and opcion == "6"):
        print("Saliendo del sistema...")
        break
def muenu_principal():
    if opcion == "1":
        print("\n---CATEGORIAS---")
        print("1. Agregar categorías")
        print("2. Lista de categorias")
        sub = input("Opción: ")
        if sub == "1":
            idc = input("ID Categoria: ")
            nombre = input("Nombre: ")
            categorias[idc] = Categoria(idc, nombre )
            print("Categoría agregada.")
        elif sub == "2":
            for c in categorias.values():
                print(f"[{c.id_categoria}]")

    elif opcion == "2":
        print("\n--- PRODUCTOS---")
        print("1. Agregar producto")
        print("2. Listas de productos")
        sub = input("Opcion: ")
        if sub == "1":
            idp = input("ID Producto: ")
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            idc = input("ID Categoría: ")
            if idc not in categorias:
                print("Error: la categoria no existe dentro del sistema.")
            else:
                stock = int(input("Stock: "))
                productos[idp] = Producto(idp, nombre, precio, idc, stock)
                print("Producto agregada.")
        elif sub == "2":
            for p in productos.values():
                cant = categorias[p.id_categoria]
                print(f"[{p.id_producto}] {p.nombre} | Precio: {p.precio} | Cantidad: {cant.nombre}| Stock: {p.stock}")

    elif opcion == "3":
        print("\n ---CLIENTES---")
        print("1. Agregar cliente")
        print("2. Lista de clientes")
        sub = input("Opcion: ")
        if sub == "1":
            idc = input("Nit: ")
            nombre = input("Nombre: ")
            clientes[idc] = Cliente(idc, nombre)
            print("Cliente agregado.")
        elif sub == "2":
            for e in empleados.values():
                print(f"[{c.id_cliente}] {c.nombre}")

    elif opcion == "4":
        print("\n ---EMPLEADOS---")
        print("1. Agregar empleado")
        print("2. Listas de empleados")
        sub = input("Opcion: ")
        if sub == "1":
            ide = input("ID Empleado: ")
            nombre = input("Nombre: ")
            empleados[ide] = Empleado(ide, nombre)
            print("Nuevo empleado agregado.")
        elif sub == "2":
            for e in empleados.values():
                print(f"[{e.id_empleado}] {e.nombre}")

    elif opcion == "5":
        print("\n --- PROVEEDORES ---")