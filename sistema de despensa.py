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

class Detalle_compra
    def __init__(self, id_detallecompra, id_compras, cantidad_compra, id_producto, precio_compra, sub_total, fecha_caducidad ):
        self.id_detallecompra = id_detallecompra
        self.id_compras = id_compras
        self.cantidad_compra = cantidad_compra
        self.id_producto = id_producto
        self.precio_compra = precio_compra
        self.sub_total = sub_total
        self.fecha_caducidad = fecha_caducidad

