from BD.Conexion import *

basedatos = Database("postgres", "00112233", "centroestetica.ccwkcz7cjsk2.us-east-2.rds.amazonaws.com")
conexion= basedatos.conectar()

class Facturas():

    def generar_factura_servicios_productos(self):
        cliente_cobrar = int(input('Ingrese el documento: '))
        precios_servicio = []
        nombres_servicio = []
        id_productos = []
        nombres_productos = []
        precio_productos = []
        cantidad_productos = []
        id_servicios_cobrar = []
        acceso_menu_factura = True
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM citas WHERE documento_fk = %s AND facturado = %s", (cliente_cobrar, False))
                servicios = cursor.fetchall()
                for servicio in servicios:
                    id_servicios_cobrar.append(servicio[0])
                if not servicios:
                    try:
                        with conexion.cursor() as cursor:
                            cursor.execute("SELECT * FROM clientes WHERE documento=" + str(cliente_cobrar))
                            cliente_facturar = cursor.fetchone()
                            if cliente_facturar:
                                while acceso_menu_factura:
                                    menu_factura = int(input(
                                        "Desea agregar productos a la factura? Marque 1 para agregar, 0 para salir: "))
                                    if menu_factura == 0:
                                        with conexion.cursor() as cursor:
                                            for id_producto, cantidad in zip(id_productos, cantidad_productos):
                                                consulta = "UPDATE inventario SET cantidad = cantidad - %s WHERE id_producto = %s"
                                                cursor.execute(consulta, (cantidad, id_producto))
                                            conexion.commit()
                                        valor_total = sum(precio * cantidad for precio, cantidad in
                                                          zip(precio_productos, cantidad_productos)) + sum(
                                            precios_servicio)
                                        try:
                                            with conexion.cursor() as cursor:
                                                consulta = "INSERT INTO facturas(documento_cliente, nombre_servicio, precio_ser, nombre_producto, precio_producto, cantidad_producto, valor_total) VALUES (%s, %s, %s, %s, %s, %s, %s);"
                                                cursor.execute(consulta, (cliente_cobrar, nombres_servicio, precios_servicio, nombres_productos,precio_productos, cantidad_productos, valor_total))
                                            conexion.commit()
                                            acceso_menu_factura = False
                                        except psycopg2.Error as e:
                                            print("Ocurrió un error al crear la factura:", e)
                                            continue
                                    if menu_factura == 1:
                                        while True:
                                            id_producto_factura = int(input("Ingrese ID del producto (0 para crear factura): "))
                                            if id_producto_factura == 0:
                                                break
                                            try:
                                                with conexion.cursor() as cursor:
                                                    cursor.execute("SELECT * FROM inventario WHERE id_producto = %s", (id_producto_factura,))
                                                    producto_nueva_factura = cursor.fetchone()
                                                    if producto_nueva_factura is None:
                                                        print("El producto no existe")
                                                    else:
                                                        cantidad_productos_comprar = int(input("Ingrese la cantidad: "))

                                                        cantidad_disponible = producto_nueva_factura[2]
                                                        if cantidad_disponible >= cantidad_productos_comprar + sum(cantidad_productos):
                                                            id_productos.append(id_producto_factura)
                                                            nombres_productos.append(producto_nueva_factura[1])
                                                            precio_productos.append(producto_nueva_factura[3])
                                                            cantidad_productos.append(cantidad_productos_comprar)
                                                            print("Producto agregado")
                                                        else:
                                                            print("No hay suficientes unidades disponibles en el inventario.")
                                                            break
                                            except psycopg2.Error as e:
                                                print("Ocurrió un error al consultar el producto:", e)

                                print("La factura se creó correctamente")
                            else:
                                print("Cliente no encontrado")
                    except psycopg2.Error as e:
                        print("Ocurrio un error al consultar: ", e)
                else:
                    for servicio in servicios:
                        cursor.execute("SELECT * FROM servicios WHERE id_servicios=" + str(servicio[4]))
                        servicios_cobrar = cursor.fetchall()
                        for servicioen_cobrar in servicios_cobrar:
                            nombres_servicio.append(servicioen_cobrar[1])
                            precios_servicio.append(servicioen_cobrar[2])

                    while acceso_menu_factura:
                        menu_factura = int(input("Desea agregar productos a la factura? Marque 1 para agregar, 0 para salir: "))
                        if menu_factura == 0:
                            valor_total = sum(precio * cantidad for precio, cantidad in zip(precio_productos, cantidad_productos)) + sum(precios_servicio)
                            try:
                                with conexion.cursor() as cursor:
                                    consulta = "INSERT INTO facturas(documento_cliente, nombre_servicio, precio_ser, nombre_producto, precio_producto, cantidad_producto, valor_total) VALUES (%s, %s, %s, %s, %s, %s, %s);"
                                    cursor.execute(consulta, (cliente_cobrar, nombres_servicio, precios_servicio, nombres_productos, precio_productos, cantidad_productos, valor_total))
                                conexion.commit()
                                try:
                                    with conexion.cursor() as cursor:
                                        for id_cita_facturar in id_servicios_cobrar:
                                            consulta = "UPDATE citas SET facturado = %s WHERE id_cita = %s"
                                            cursor.execute(consulta, (True, id_cita_facturar))
                                    conexion.commit()
                                except psycopg2.Error as e:
                                    print("Ocurrió un error al editar: ", e)
                                acceso_menu_factura = False
                            except psycopg2.Error as e:
                                print("Ocurrió un error al crear la factura:", e)
                                continue
                        if menu_factura == 1:
                            while True:
                                id_producto_factura = int(input("Ingrese ID del producto (0 para crear factura): "))
                                if id_producto_factura == 0:
                                    break
                                cantidad_productos_comprar = int(input("Ingrese la cantidad: "))
                                try:
                                    with conexion.cursor() as cursor:
                                        cursor.execute("SELECT * FROM inventario WHERE id_producto = %s", (id_producto_factura,))
                                        producto_nueva_factura = cursor.fetchone()

                                        if producto_nueva_factura is None:
                                            print("El producto no existe")
                                        else:
                                            nombres_productos.append(producto_nueva_factura[1])
                                            precio_productos.append(producto_nueva_factura[3])
                                            cantidad_productos.append(cantidad_productos_comprar)
                                            print("Producto agregado")
                                except psycopg2.Error as e:
                                    print("Ocurrió un error al consultar el producto:", e)

                    print("La factura se creó correctamente")

        except psycopg2.Error as e:
            print("No encontro el cliente en ninguna tabla: ", e)


    def pagar_facturas_documento(self):
        documento_cliente_pagar = int(
            input('Ingrese el documento del cliente el cual generó el pago de todas sus facturas: '))
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT valor_total FROM facturas WHERE documento_cliente = %s AND pagado = %s", (documento_cliente_pagar, True))
                valores_totales= cursor.fetchall()
                valores_totales_list = [valor[0] for valor in valores_totales]
                print(valores_totales_list)
                valor_total = sum(valores_totales_list)
                print("Valor total a pagar:", valor_total)
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)
        menu_pago = int(input('Ingrese 1 si desea pagar, de lo contrario ingrese 0: '))
        if menu_pago == 1:
            try:
                with conexion.cursor() as cursor:
                    consulta = "UPDATE facturas SET pagado = %s WHERE documento_cliente = %s"
                    cursor.execute(consulta, (False, documento_cliente_pagar))
                conexion.commit()
                print('Se efectuo el pago de la factura correctamente')
            except psycopg2.Error as e:
                print("Ocurrió un error al pagar: ", e)
        if menu_pago == 0:
            pass






    def pagar_facturas_idFactura(self):
        id_factura = int(input('Ingrese el numero de la factura: '))
        try:
            with conexion.cursor() as cursor:
                    consulta = "UPDATE facturas SET pagado = %s WHERE documento_cliente = %s"
                    cursor.execute(consulta, (True, id_factura))
            conexion.commit()
            print('Se efectuo el pago de las facturas')
        except psycopg2.Error as e:
            print("Ocurrió un error al pagar: ", e)
        pass

