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
    def __init__(self, nit,  nombre, telefono, direccion, correo):
        self.nit = nit
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo

class Empleado:
    def __init__(self, id_empleado, nombre, telefono, direccion, correo):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo

class Provedor:
    def __init__(self, id_provedor, nombre, empresa, telefono, direccion, correo, id_categoria):
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

