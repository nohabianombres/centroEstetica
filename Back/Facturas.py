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
                                    menu_factura = int(input("Desea agregar productos a la factura? Marque 1 para agregar, 0 para salir: "))
                                    if menu_factura == 0:
                                        with conexion.cursor() as cursor:
                                            for id_producto, cantidad in zip(id_productos, cantidad_productos):
                                             consulta = "UPDATE inventario SET cantidad = cantidad - %s WHERE id_producto = %s"
                                             cursor.execute(consulta, (cantidad, id_producto))
                                        conexion.commit()
                                        valor_total = sum(precio * cantidad for precio, cantidad in zip(precio_productos, cantidad_productos)) + sum(precios_servicio)
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
                                            id_producto_factura = int(input("Ingrese ID del producto (0 para crear factura): "))
                                            if id_producto_factura == 0:
                                                break
                                            try:
                                                with conexion.cursor() as cursor:
                                                    cursor.execute("SELECT * FROM inventario WHERE id_producto = %s", (id_producto_factura,))
                                                    producto_nueva_factura_l = cursor.fetchone()
                                                    if producto_nueva_factura_l is None:
                                                        print("El producto no existe")
                                                    else:
                                                        cantidad_productos_comprar = int(input("Ingrese la cantidad: "))


                                                        print('aca estuve sjajajajaja')
                                                        if producto_nueva_factura_l is None:
                                                            print("El producto no existe")
                                                        else:
                                                            cantidad_disponible = producto_nueva_factura_l[2]

                                                                    # Obtener las cantidades correspondientes al último valor de id_producto_factura_s
                                                            cantidades_correspondientes = [cantidad for cantidad, id_producto_s in zip(cantidad_productos,id_productos) if id_producto_s == id_producto_factura]
                                                            print(cantidades_correspondientes)
                                                                    # Verificar si la cantidad disponible es suficiente
                                                        if cantidad_disponible >= cantidad_productos_comprar + sum(cantidades_correspondientes):
                                                            id_productos.append(id_producto_factura)
                                                            nombres_productos.append(producto_nueva_factura_l[1])
                                                            precio_productos.append(producto_nueva_factura_l[3])
                                                            cantidad_productos.append(cantidad_productos_comprar)
                                                            print("Producto agregado")
                                                        else:
                                                            print("No hay suficientes unidades disponibles en el inventario.")
                                            except psycopg2.Error as e:
                                                print("Ocurrió un error al consultar el producto:", e)
                            else:
                                print("Cliente no encontrado")
                    except psycopg2.Error as e:
                        print("Ocurrio un error al consultar: ", e)
                else:
                    while acceso_menu_factura:
                        menu_factura = int(input("Desea agregar productos a la factura? Marque 1 para agregar, 0 para salir: "))
                        if menu_factura == 0:
                            with conexion.cursor() as cursor:
                                for id_producto, cantidad in zip(id_productos, cantidad_productos):
                                    consulta = "UPDATE inventario SET cantidad = cantidad - %s WHERE id_producto = %s"
                                    cursor.execute(consulta, (cantidad, id_producto))
                            conexion.commit()
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
                            id_producto_factura = int(input("Ingrese ID del producto (0 para crear factura): "))
                            if id_producto_factura == 0:
                                break
                            try:
                                with conexion.cursor() as cursor:
                                    cursor.execute("SELECT * FROM inventario WHERE id_producto = %s",
                                                   (id_producto_factura,))
                                    producto_nueva_factura_l = cursor.fetchone()
                                    if producto_nueva_factura_l is None:
                                        print("El producto no existe")
                                    else:
                                        cantidad_productos_comprar = int(input("Ingrese la cantidad: "))
                                        if producto_nueva_factura_l is None:
                                            print("El producto no existe")
                                        else:
                                            cantidad_disponible = producto_nueva_factura_l[2]
                                            # Obtener las cantidades correspondientes al último valor de id_producto_factura_s
                                            cantidades_correspondientes = [cantidad for cantidad, id_producto_s in zip(cantidad_productos, id_productos) if id_producto_s == id_producto_factura]
                                            # Verificar si la cantidad disponible es suficiente
                                        if cantidad_disponible >= cantidad_productos_comprar + sum(cantidades_correspondientes):
                                            id_productos.append(id_producto_factura)
                                            nombres_productos.append(producto_nueva_factura_l[1])
                                            precio_productos.append(producto_nueva_factura_l[3])
                                            cantidad_productos.append(cantidad_productos_comprar)
                                            print("Producto agregado")
                                        else:
                                            print("No hay suficientes unidades disponibles en el inventario.")
                            except psycopg2.Error as e:
                                print("Ocurrió un error al consultar el producto:", e)

            print("La factura se creó correctamente")
        except psycopg2.Error as e:
            print("No encontro el cliente en ninguna tabla: ", e)

    def pagar_facturas_documento(self):
        documento_cliente_pagar = int(input('Ingrese el documento del cliente el cual generó el pago de todas sus facturas: '))
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT valor_total FROM facturas WHERE documento_cliente = %s AND pagado = %s", (documento_cliente_pagar, False))
                valores_totales= cursor.fetchall()
                valores_totales_list = [valor[0] for valor in valores_totales]
                print('La lista de los valores de cada factura que debe pagar es la siguiente: ', (valores_totales_list))
                valor_total = sum(valores_totales_list)
                print("Valor total a pagar:", valor_total)
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)
        menu_pago = int(input('Ingrese 1 si desea pagar, de lo contrario ingrese 0: '))
        if menu_pago == 1:
            try:
                with conexion.cursor() as cursor:
                    consulta = "UPDATE facturas SET pagado = %s WHERE documento_cliente = %s"
                    cursor.execute(consulta, (True, documento_cliente_pagar))
                conexion.commit()
                print('Se efectuo el pago de la factura correctamente')
            except psycopg2.Error as e:
                print("Ocurrió un error al pagar: ", e)
        if menu_pago == 0:
            pass
    def buscar_facturas_cliente(self):
        cliente_buscar = input("Ingrese el documento del cliente: ")
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM facturas WHERE documento_cliente=" + str(cliente_buscar))
                facturas_credito = cursor.fetchall()
                print('Las facturas que debe en este momento son las siguientes: ')
            for factura_credito in facturas_credito:
                print(factura_credito)

        except psycopg2.Error as e:
            print("Ocurrio un error al consultar: ", e)
    pass






    def pagar_facturas_idFactura(self):
        id_factura = int(input('Ingrese el numero de la factura: '))
        try:
            with conexion.cursor() as cursor:
                    consulta = "UPDATE facturas SET pagado = %s WHERE id_factura = %s"
                    cursor.execute(consulta, (True, id_factura))
            conexion.commit()
            print('Se efectuo el pago de las facturas')
        except psycopg2.Error as e:
            print("Ocurrió un error al pagar: ", e)
        pass

