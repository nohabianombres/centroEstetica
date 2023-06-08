from BD.Conexion import *
from datetime import datetime
from Front.administrador.ventanasAdmin import *
from Front.cajero.ventanasCajero import *
from Front.administrador.emeAdm.emeAdmcodigo import *
from Front.comunes.emerComunes import *

basedatos = Database("postgres", "00112233", "centroestetica.ccwkcz7cjsk2.us-east-2.rds.amazonaws.com")
conexion= basedatos.conectar()

class Facturas():

    def generar_factura_servicios_productos(self, cliente_cobrar):
        '''cliente_cobrar = int(input('Ingrese el documento: '))'''
        precios_servicio = []
        nombres_servicio = []
        id_productos = []
        nombres_productos = []
        precio_productos = []
        cantidad_productos = []
        id_citas_cobrar = []
        id_servicios_cobrar = []
        acceso_menu_factura = True
        hora_actual = datetime.now().strftime('%H:%M:%S')
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM citas WHERE documento_fk = %s AND facturado = %s AND hora_fin < %s", (cliente_cobrar, False, hora_actual))
                servicios_ee = cursor.fetchall()
                for servicio_ee in servicios_ee:
                    id_citas_cobrar.append(servicio_ee[0])
                if not servicios_ee:
                    try:
                        with conexion.cursor() as cursor:
                            cursor.execute("SELECT * FROM clientes WHERE documento=" + str(cliente_cobrar))
                            cliente_facturar = cursor.fetchone()
                            if cliente_facturar:
                                while acceso_menu_factura == True:
                                    menu_factura = int(input("Desea agregar productos a la factura? Marque 1 para agregar, 0 para salir: "))
                                    if menu_factura == 0:
                                        with conexion.cursor() as cursor:
                                            for id_producto, cantidad in zip(id_productos, cantidad_productos):
                                             consulta = "UPDATE inventario SET cantidad = cantidad - %s WHERE id_producto = %s"
                                             cursor.execute(consulta, (cantidad, id_producto))
                                        conexion.commit()
                                        valor_total = sum(precio * cantidad for precio, cantidad in zip(precio_productos, cantidad_productos)) + sum(precios_servicio)
                                        fecha_creacion = datetime.now().date()
                                        print(fecha_creacion)
                                        try:
                                            with conexion.cursor() as cursor:
                                                consulta = "INSERT INTO facturas(documento_cliente, nombre_servicio, precio_ser, nombre_producto, precio_producto, cantidad_producto, valor_total, fecha_creacion, hora_creacion ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
                                                cursor.execute(consulta, (cliente_cobrar, nombres_servicio, precios_servicio, nombres_productos,precio_productos, cantidad_productos, valor_total, fecha_creacion, hora_actual))
                                            conexion.commit()

                                            try:
                                                with conexion.cursor() as cursor:
                                                    cursor.execute("""
                                                        SELECT * FROM facturas
                                                        WHERE id_factura = (
                                                            SELECT MAX(id_factura) FROM facturas
                                                        )
                                                    """)
                                                    ultimo_dato_insertado = cursor.fetchone()
                                                    print("Última fila insertada: ", ultimo_dato_insertado)
                                            except psycopg2.Error as e:
                                                print(
                                                    "Ocurrió un error al obtener la última fila insertada en la tabla facturas:",
                                                    e)
                                            try:
                                                with conexion.cursor() as cursor:
                                                    consulta = "INSERT INTO informe_productos(id_factura_pro, nombre_productos, precio_productos, cantidad_productos, valor_total, fecha_factura_pro, estado ) VALUES (%s, %s, %s, %s, %s, %s, %s);"
                                                    cursor.execute(consulta, (ultimo_dato_insertado[0], ultimo_dato_insertado[4], ultimo_dato_insertado[5], ultimo_dato_insertado[6],0, ultimo_dato_insertado[9],ultimo_dato_insertado[8]))
                                                conexion.commit()
                                                acceso_menu_factura=False
                                            except psycopg2.Error as e:
                                                print("Ocurrió un error al crear el informe:", e)

                                        except psycopg2.Error as e:
                                            print("Ocurrió un error al crear la factura:", e)
                                            continue
                                    if menu_factura == 1:
                                            id_producto_factura = int(input("Ingrese ID del producto (0 para crear factura): "))
                                            if id_producto_factura == 0:
                                                acceso_menu_factura = False
                                            try:
                                                with conexion.cursor() as cursor:
                                                    cursor.execute("SELECT * FROM inventario WHERE id_producto = %s", (id_producto_factura,))
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
                            for id_cita_facturar in id_citas_cobrar:
                                print(id_cita_facturar)
                                try:
                                    with conexion.cursor() as cursor:
                                        cursor.execute("SELECT * FROM citas WHERE id_cita = %s", (id_cita_facturar,))
                                        citas_facturar = cursor.fetchall()
                                        for cita_facturar in citas_facturar:
                                            id_servicios_cobrar.append(cita_facturar[4])

                                            with conexion.cursor() as cursor:
                                                cursor.execute("SELECT * FROM servicios WHERE id_servicios = %s",(cita_facturar[4],))
                                                servicios_facturar = cursor.fetchall()
                                            for servicio_facturar in servicios_facturar:
                                                nombres_servicio.append(servicio_facturar[1])
                                                precios_servicio.append(servicio_facturar[2])
                                except psycopg2.Error as e:
                                    print("Ocurrió un error al consultar los datos de los servicios: ", e)
                                with conexion.cursor() as cursor:
                                    for id_producto, cantidad in zip(id_productos, cantidad_productos):
                                        consulta = "UPDATE inventario SET cantidad = cantidad - %s WHERE id_producto = %s"
                                        cursor.execute(consulta, (cantidad, id_producto))
                                conexion.commit()
                                valor_total = sum(precio * cantidad for precio, cantidad in zip(precio_productos, cantidad_productos)) + sum(precios_servicio)
                                fecha_creacion = datetime.now().date()
                                try:
                                    with conexion.cursor() as cursor:
                                        consulta = "INSERT INTO facturas(documento_cliente, nombre_servicio, precio_ser, nombre_producto, precio_producto, cantidad_producto, valor_total, fecha_creacion, hora_creacion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
                                        cursor.execute(consulta, (cliente_cobrar, nombres_servicio, precios_servicio, nombres_productos, precio_productos, cantidad_productos, valor_total, fecha_creacion, hora_actual))
                                    conexion.commit()
                                    try:
                                        with conexion.cursor() as cursor:
                                            for id_cita_facturar in id_citas_cobrar:
                                                consulta = "UPDATE citas SET facturado = %s WHERE id_cita = %s"
                                                cursor.execute(consulta, (True, id_cita_facturar))
                                        conexion.commit()
                                    except psycopg2.Error as e:
                                        print("Ocurrió un error al editar: ", e)
                                    try:
                                        with conexion.cursor() as cursor:
                                            cursor.execute("""SELECT * FROM facturas WHERE id_factura = (SELECT MAX(id_factura) FROM facturas)""")
                                            ultimo_dato_insertado = cursor.fetchone()
                                            print("Última fila insertada: ", ultimo_dato_insertado)
                                    except psycopg2.Error as e:
                                        print("Ocurrió un error al obtener la última fila insertada en la tabla facturas:",e)
                                    try:
                                        with conexion.cursor() as cursor:
                                            consulta = "INSERT INTO informe_servicios(id_factura_ser, nombre_servicio, precio_servicio, valor_total, fecha_factura_ser, estado ) VALUES (%s, %s, %s, %s, %s, %s);"
                                            cursor.execute(consulta, (ultimo_dato_insertado[0], ultimo_dato_insertado[2],ultimo_dato_insertado[3], sum(ultimo_dato_insertado[3]),ultimo_dato_insertado[9], ultimo_dato_insertado[8]))
                                        conexion.commit()
                                    except psycopg2.Error as e:
                                        print("Ocurrió un error al crear el informe:", e)
                                    try:
                                        valor_total_productos = sum(x * y for x, y in zip(ultimo_dato_insertado[5], ultimo_dato_insertado[6]))
                                        with conexion.cursor() as cursor:
                                            consulta = "INSERT INTO informe_productos(id_factura_pro, nombre_productos, precio_productos, cantidad_productos, valor_total, fecha_factura_pro, estado ) VALUES (%s, %s, %s, %s, %s, %s, %s);"
                                            cursor.execute(consulta, (ultimo_dato_insertado[0], ultimo_dato_insertado[4],ultimo_dato_insertado[5], ultimo_dato_insertado[6], valor_total_productos,ultimo_dato_insertado[9], ultimo_dato_insertado[8]))
                                        conexion.commit()
                                        acceso_menu_factura = False
                                    except psycopg2.Error as e:
                                        print("Ocurrió un error al crear el informe:", e)

                                except psycopg2.Error as e:
                                    print("Ocurrió un error al crear la factura:", e)
                                    continue
                        if menu_factura == 1:
                            id_producto_factura = int(input("Ingrese ID del producto (0 para crear factura): "))
                            if id_producto_factura == 0:
                                acceso_menu_factura = False
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
                                            cantidades_correspondientes = [cantidad for cantidad, id_producto_s in zip(cantidad_productos, id_productos) if id_producto_s == id_producto_factura]
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

    def pagar_facturas_documento(self, documento_cliente_pagar):
        '''documento_cliente_pagar = input('Ingrese el documento del cliente el cual generó el pago de todas sus facturas: ')'''
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
                    cursor.execute("SELECT * FROM facturas WHERE documento_cliente = %s ",(documento_cliente_pagar))
                    facturas_pendientes=cursor.fetchall()
                    conexion.commit()
                    facturas_pendientes_list = [factura[1] for factura in facturas_pendientes]
                    for factura_pendi in facturas_pendientes_list:
                        consulta = "UPDATE informe_productos SET estado %s WHERE id_factura_pro = %s"
                        cursor.execute(consulta, (True, factura_pendi))
                        consulta = "UPDATE informe_servicios SET estado = %s WHERE id_factura_ser = %s"
                        cursor.execute(consulta, (True, factura_pendi))
                print('Se efectuo el pago de la factura correctamente')
            except psycopg2.Error as e:
                print("Ocurrió un error al pagar: ", e)
        if menu_pago == 0:
            pass
    def buscar_facturas_cliente(self, cliente_buscar):
        '''cliente_buscar = input("Ingrese el documento del cliente: ")'''
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM facturas WHERE documento_cliente = %s AND pagado = %s", (cliente_buscar, False))
                facturas_credito = cursor.fetchall()
                print('Las facturas que debe en este momento son las siguientes: ')
            for factura_credito in facturas_credito:
                print(factura_credito)
            return facturas_credito

        except psycopg2.Error as e:
            return "Ocurrio un error al consultar"

    def pagar_facturas_idFactura(self, id_factura):
        '''id_factura = int(input('Ingrese el numero de la factura: '))'''
        try:
            with conexion.cursor() as cursor:
                    consulta = "UPDATE facturas SET pagado = %s WHERE id_factura = %s"
                    cursor.execute(consulta, (True, id_factura))
                    consulta = "UPDATE informe_productos SET estado = %s WHERE id_factura_pro = %s"
                    cursor.execute(consulta, (True, id_factura))
                    consulta = "UPDATE informe_servicios SET estado = %s WHERE id_factura_ser = %s"
                    cursor.execute(consulta, (True, id_factura))
            conexion.commit()
            print('Se efectuo el pago de las facturas')
        except psycopg2.Error as e:
            print("Ocurrió un error al pagar: ", e)
        pass