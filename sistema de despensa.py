class Categoria:
    def __init__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self.nombre = nombre

    def mostrar_info(self):
        print(f"ID de la categoria: {self.id_categoria} | Nombre: {self.nombre}")
class Producto:
    def __init__(self, id_producto, nombre, precio, categoria, total_compras=0, total_ventas=0, stock=0):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.total_compras = total_compras
        self.total_ventas = total_ventas
        self.stock = stock

    def mostrar_info(self):
        print(f"ID del producto: {self.id_producto} | Nombre del producto: {self.nombre} | Precio: {self.precio} | Categoría: {self.categoria} | Total de compra: {self.total_compras} | Total de Ventas: {self.total_ventas} | Stock: {self.stock}")
class Cliente:
    def __init__(self, nit,  nombre_cliente, telefono, direccion, correo):
        self.nit = nit
        self.nombre = nombre_cliente
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
        self.nombre = nombre_provedor
        self.empresa = empresa
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo
        self.id_categoria = id_categoria

    def mostrar_info(self):
        return(f"ID:{self.id_provedor} | Nombre: {self.nombre} | Empresa:{self.empresa} | Teléfono:{self.telefono} | Dirección: {self.direccion} | Correo: {self.correo} | ID de Categoría {self.id_categoria}")

class Venta:
    def __init__(self, id_venta, fecha, nit, id_empleado, total):
        self.id_venta = id_venta
        self.fecha = fecha
        self.nit = nit
        self.id_empleado = id_empleado
        self.total = total

    def mostrar_info(self):
        return(f"ID Venta: {self.id_venta} | Fecha: {self.fecha} | NIT: {self.nit} | ID del empleado: {self.id_empleado} | Total: {self.total}")

class Detalle_venta:
    def __init__(self, id_detalleventa, id_venta, cantidad, id_producto, precio, subtotal):
        self.id_venta = id_venta
        self.cantidad = cantidad
        self.id_producto = id_producto
        self.precio = precio
        self.subtotal = subtotal
        self.id_detalleventa = id_detalleventa

    def  mostrar_info(self):
        return (f"ID Detalle de la venta: {self.id_detalleventa} |  ID de la venta: {self.id_venta} | Cantidad: {self.cantidad} | ID del producto: {self.id_producto} | Precio: {self.precio} | Subtotal: {self.subtotal}")

class Compra:
    def __init__(self, id_compras, fecha_compra, id_provedor, id_empleado, total):
        self.id_compras = id_compras
        self.fecha_compra = fecha_compra
        self.id_provedor = id_provedor
        self.id_empleado = id_empleado
        self.total = total

    def mostrar_info(self):
        return (f"ID de compras: {self.id_compras} | Fecha de compra: {self.fecha_compra} | ID del proveedor: {self.id_provedor} | ID del empleado:{self.id_empleado} | Total: {self.total}")
class Detalle_compra:
    def __init__(self, id_detallecompra, id_compras, cantidad_compra, id_producto, precio_compra, sub_total, fecha_caducidad ):
        self.id_detallecompra = id_detallecompra
        self.id_compras = id_compras
        self.cantidad_compra = cantidad_compra
        self.id_producto = id_producto
        self.precio_compra = precio_compra
        self.sub_total = sub_total
        self.fecha_caducidad = fecha_caducidad

    def mostrar_info(self):
        return (f"ID del detalle de compra: {self.id_detallecompra} | ID de compras: {self.id_compras} | Cantidad de compra: {self.cantidad_compra} | ID del producto: {self.id_producto} Fecha de caducidad: {self.fecha_caducidad} | Precio de compra: {self.precio_compra} | Sub total: {self.sub_total}")

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

class GestionClientes:
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

class GestionEmpleados:
    def __init__(self):
        self.empleados = {}

    def agrear_empleado(self, empleado):
        if empleado.id_empleado not in self.empleados:
            self.empleados[empleado.id_empleado] = empleado
            print(f"Empleado '{empleado.nombre}' agregado correctamente ")
        else:
            print(f"El empleado con ID {empleado.id_empleado} ya existe.")

    def listar_empleados(self):
        if self.empleados:
            print("\n---LISTA DE EMPLEADOS---")
            for empleado in self.empleados.values():
                print(empleado.mostrar_info())
        else:
            print("No hay empleados registrados.")

    def buscar_empleado(self, id_empleado):
        if id_empleado in self.empleados:
            return self.empleados[id_empleado]
        else:
            print("Empleado no encontrado.")
            return None

class GestionProvedores:
    def __init__(self):
        self.provedores = {}

    def agregar_provedor(self, provedor):
        if provedor.id_provedor not in self.provedores:
            print(f"El proveedor con ID {provedor.id_provedor} ya existe.")
        else:
            self.provedores[provedor.id_provedor] = provedor
            print(f"Proveedor '{provedor.nombre}' agregado correctamente. ")

    def listar_provedors(self):
        if not self.provedores:
            print("No hay proveedores registrados.")
        else:
            print("\n--- LISTA DE PROOVEDORES---")
            for prov in self.provedores.values():
                print(prov.mostrar_info())

    def buscar_provedor(self, id_provedor):
        if id_provedor in self.provedores:
            return self.provedores[id_provedor]
        else:
            print("El proveedor no ha sido encontrado.")
            return None

class GestionVenta:
    def __init__(self):
        self.venta = {}

    def agregar_venta(self, venta):
        if venta.id_venta in self.venta:
            print(f"La venta con ID {venta.id_venta} ya existe.")
        else:
            self.ventas[venta.id_venta] = venta
            print(f"Venta '{venta.nombre}' agregada correctamente.")

    def listar_ventas(self):
        if not self.ventas:
            print("No hay ventas registrados.")
        else:
            print("\n--- LISTA DE VENTAS---")
            for v in self.ventas.values():
                print(v.mostrar_info())

    def buscar_venta(self, id_venta):
        if id_venta in self.venta:
            return self.venta[id_venta]
        else:
            print("Venta no encontrada.")
            return None

class GestionDetalleVenta:
    def __init__(self):
        self.detalles_venta = {}

    def buscar_detalle(self, id_detalleventa):
        if id_detalleventa in self.detalles_venta:
            return self.detalles_venta[id_detalleventa]
        else:
            print("No hay registro de ventas realizadas.")
            return None

class GestionCompras:
    def __init__(self):
        self.compras = {}

    def agregar_compra(self, compra):
        if compra.id_compra in self.compras:
            print(f"La compra con ID {compra.id_compra} ya existe.")
        else:
            self.compras[compra.id_compra] = compra
            print(f"La compra '{compra.nombre}' agregada correctamente.")

    def buscar_compra(self, id_compra):
        if id_compra in self.compras:
            return self.compras[id_compra]
        else:
            print("No hay registro de compras realizadas.")
            return None

class GestionDetalleCompra:
    def __init__(self):
        self.detalles_compra = {}

    def buscar_detalle(self, id_detallecompra):
        if id_detallecompra in self.detalles_compra:
            return self.detalles_compra[id_detallecompra]
        else:
            print("No hay registro de compras realizadas.")
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
