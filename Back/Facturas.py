from BD.Conexion import *

basedatos = Database("postgres", "00112233", "centroestetica.ccwkcz7cjsk2.us-east-2.rds.amazonaws.com")
conexion= basedatos.conectar()

class Facturas():

    def generar_factura_servicios_productos(self):
        cliente_cobrar = input('Ingrese el documento: ')
        precios_servicio = []  # Lista para almacenar los precios de los servicios
        nombres_servicio = []  # Lista para almacenar los nombres de los servicios
        id_productos = []
        nombres_productos = []
        precio_productos =[]
        cantidad_productos = []
        acceso_menu_factura = True
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM citas WHERE documento_fk=" + str(cliente_cobrar))
                servicios = cursor.fetchall()

                if not servicios:
                    try:
                        with conexion.cursor() as cursor:
                            cursor.execute("SELECT * FROM clientes WHERE documento=" + str(cliente_cobrar))
                            cliente_facturar = cursor.fetchone()
                            if cliente_facturar:
                                while acceso_menu_factura:
                                    menu_factura = int(input("Desea agregar productos a la factura? Marque 1 para agregar, 0 para salir: "))
                                    if menu_factura == 0:
                                        print(precio_productos)
                                        print(cantidad_productos)
                                        valor_total = sum(precio * cantidad for precio, cantidad in zip(precio_productos, cantidad_productos))+sum(precios_servicio)
                                        print(valor_total)
                                        try:
                                            with conexion.cursor() as cursor:
                                                consulta = "INSERT INTO facturas(documento_cliente, nombre_servicio, precio_ser, nombre_producto, precio_producto, cantidad_producto, valor_total) VALUES (%s, %s, %s, %s, %s, %s, %s);"
                                                cursor.execute(consulta, (cliente_cobrar, nombres_servicio, precios_servicio, nombres_productos, precio_productos, cantidad_productos, valor_total))
                                            conexion.commit()
                                            acceso_menu_factura = False
                                        except psycopg2.Error as e:
                                            print("Ocurrió un error al crear la factura:", e)
                                            continue

                                    if menu_factura == 1:
                                        while True:
                                            id_producto_factura = int(
                                                input("Ingrese ID del producto (0 para crear factura): "))
                                            if id_producto_factura == 0:
                                                break
                                            cantidad_productos_comprar = int(input("Ingrese la cantidad: "))
                                            try:
                                                with conexion.cursor() as cursor:
                                                    cursor.execute("SELECT * FROM inventario WHERE id_producto = %s",(id_producto_factura,))
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
                            try:
                                with conexion.cursor() as cursor:
                                    consulta = "INSERT INTO facturas(documento_cliente, nombre_servicio, precio_ser, nombre_producto, precio_producto, cantidad_producto, valor_total) VALUES (%s, %s, %s, %s, %s, %s, %s);"
                                    cursor.execute(consulta, (cliente_cobrar, nombres_servicio, precios_servicio, nombres_productos, precio_productos, cantidad_productos, 0))
                                conexion.commit()
                                print("Factura creada")
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

    def buscar_facturas(self):
        pass

