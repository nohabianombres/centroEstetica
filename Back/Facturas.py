from BD.Conexion import *
from datetime import datetime

basedatos = Database("postgres", "00112233", "centroestetica.ccwkcz7cjsk2.us-east-2.rds.amazonaws.com")
conexion= basedatos.conectar()

class Facturas():

    def generar_factura_servicios_productos(self, cliente_cobrar):
        self.precios_servicio = []
        self.nombres_servicio = []
        self.id_productos = []
        self.nombres_productos = []
        self.precio_productos = []
        self.cantidad_productos = []
        self.id_citas_cobrar = []
        self.id_servicios_cobrar = []
        self.acceso_menu_factura = True
        self.hora_actual = datetime.now().strftime('%H:%M:%S')
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM citas WHERE documento_fk = %s AND facturado = %s AND hora_fin < %s", (cliente_cobrar, False, self.hora_actual))
                self.servicios_ee = cursor.fetchall()
                for servicio_ee in self.servicios_ee:
                    self.id_citas_cobrar.append(servicio_ee[0])
                if not self.servicios_ee:
                    try:
                        with conexion.cursor() as cursor:
                            cursor.execute("SELECT * FROM clientes WHERE documento=" + str(cliente_cobrar))
                            self.cliente_facturar = cursor.fetchone()
                            if self.cliente_facturar:
                                return self.cliente_facturar, cliente_cobrar
                            else:
                                return ("Cliente no encontrado")
                    except psycopg2.Error as e:
                        return ("Ocurrio un error al consultar: ", e)
                else:
                    return (self.servicios_ee, cliente_cobrar)
        except psycopg2.Error as e:
            return ("Ocurrió un error al obtener las citas a facturar")

    def agr_fac (self, cliente_cobrar):
        with conexion.cursor() as cursor:
            for id_producto, cantidad in zip(self.id_productos, self.cantidad_productos):
                consulta = "UPDATE inventario SET cantidad = cantidad - %s WHERE id_producto = %s"
                cursor.execute(consulta, (cantidad, id_producto))
        conexion.commit()
        valor_total = sum(precio * cantidad for precio, cantidad in zip(self.precio_productos, self.cantidad_productos)) + sum(
            self.precios_servicio)
        fecha_creacion = datetime.now().date()
        try:
            with conexion.cursor() as cursor:
                consulta = "INSERT INTO facturas(documento_cliente, nombre_servicio, precio_ser, nombre_producto, precio_producto, cantidad_producto, valor_total, fecha_creacion, hora_creacion ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
                cursor.execute(consulta, (cliente_cobrar, self.nombres_servicio, self.precios_servicio, self.nombres_productos, self.precio_productos,self.cantidad_productos, valor_total, fecha_creacion, self.hora_actual))
            conexion.commit()
            try:
                with conexion.cursor() as cursor:
                    cursor.execute("""SELECT * FROM facturas WHERE id_factura = (SELECT MAX(id_factura) FROM facturas)""")
                ultimo_dato_insertado = cursor.fetchone()
                try:
                    with conexion.cursor() as cursor:
                        consulta = "INSERT INTO informe_productos(id_factura_pro, nombre_productos, precio_productos, cantidad_productos, valor_total, fecha_factura_pro, estado ) VALUES (%s, %s, %s, %s, %s, %s, %s);"
                        cursor.execute(consulta, (ultimo_dato_insertado[0], ultimo_dato_insertado[4], ultimo_dato_insertado[5],ultimo_dato_insertado[6], 0, ultimo_dato_insertado[9], ultimo_dato_insertado[8]))
                    conexion.commit()
                except psycopg2.Error as e:
                    return ("Ocurrió un error al crear el informe:", e)
            except psycopg2.Error as e:
                return ("Ocurrió un error al obtener la última fila insertada en la tabla facturas:",e)
            return ('La factura, con debidos informes creado correctamente')
        except psycopg2.Error as e:
            return ("Ocurrió un error al crear la factura:", e)


    def agr_pro_fac(self, id_producto_factura):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM inventario WHERE id_producto = %s", (id_producto_factura,))
                producto_nueva_factura_l = cursor.fetchone()
                if producto_nueva_factura_l is None:
                    return ("El producto no existe")
                else:
                    cantidad_productos_comprar = int(input("Ingrese la cantidad: "))
                    if producto_nueva_factura_l is None:
                        return ("El producto no existe")
                    else:
                        cantidad_disponible = producto_nueva_factura_l[2]
                        cantidades_correspondientes = [cantidad for cantidad, id_producto_s in zip(self.cantidad_productos, self.id_productos) if id_producto_s == id_producto_factura]
                    if cantidad_disponible >= cantidad_productos_comprar + sum(cantidades_correspondientes):
                        self.id_productos.append(id_producto_factura)
                        self.nombres_productos.append(producto_nueva_factura_l[1])
                        self.precio_productos.append(producto_nueva_factura_l[3])
                        self.cantidad_productos.append(cantidad_productos_comprar)
                        return ("Producto agregado")
                    else:
                        return ("No hay suficientes unidades disponibles en el inventario.")
        except psycopg2.Error as e:
            return ("Ocurrió un error al consultar el producto:", e)


    def agr_fac_con_ser(self, cliente_cobrar):
        for id_cita_facturar in self.id_citas_cobrar:
            print(id_cita_facturar)
            try:
                with conexion.cursor() as cursor:
                    cursor.execute("SELECT * FROM citas WHERE id_cita = %s", (id_cita_facturar,))
                    citas_facturar = cursor.fetchall()
                    for cita_facturar in citas_facturar:
                        self.id_servicios_cobrar.append(cita_facturar[4])

                        with conexion.cursor() as cursor:
                            cursor.execute("SELECT * FROM servicios WHERE id_servicios = %s", (cita_facturar[4],))
                            servicios_facturar = cursor.fetchall()
                        for servicio_facturar in servicios_facturar:
                            self.nombres_servicio.append(servicio_facturar[1])
                            self.precios_servicio.append(servicio_facturar[2])

                with conexion.cursor() as cursor:
                    for id_producto, cantidad in zip(self.id_productos, self.cantidad_productos):
                        consulta = "UPDATE inventario SET cantidad = cantidad - %s WHERE id_producto = %s"
                        cursor.execute(consulta, (cantidad, id_producto))
                conexion.commit()
                valor_total = sum(precio * cantidad for precio, cantidad in zip(self.precio_productos, self.cantidad_productos)) + sum(self.precios_servicio)
                fecha_creacion = datetime.now().date()
                try:
                    with conexion.cursor() as cursor:
                        consulta = "INSERT INTO facturas(documento_cliente, nombre_servicio, precio_ser, nombre_producto, precio_producto, cantidad_producto, valor_total, fecha_creacion, hora_creacion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
                        cursor.execute(consulta, (cliente_cobrar, self.nombres_servicio, self.precios_servicio, self.nombres_productos, self.precio_productos,self.cantidad_productos, valor_total, fecha_creacion, self.hora_actual))
                    conexion.commit()
                    try:
                        with conexion.cursor() as cursor:
                            for id_cita_facturar in self.id_citas_cobrar:
                                consulta = "UPDATE citas SET facturado = %s WHERE id_cita = %s"
                                cursor.execute(consulta, (True, id_cita_facturar))
                        conexion.commit()
                        try:
                            with conexion.cursor() as cursor:
                                cursor.execute(
                                    """SELECT * FROM facturas WHERE id_factura = (SELECT MAX(id_factura) FROM facturas)""")
                                ultimo_dato_insertado = cursor.fetchone()
                            try:
                                with conexion.cursor() as cursor:
                                    consulta = "INSERT INTO informe_servicios(id_factura_ser, nombre_servicio, precio_servicio, valor_total, fecha_factura_ser, estado ) VALUES (%s, %s, %s, %s, %s, %s);"
                                    cursor.execute(consulta, (ultimo_dato_insertado[0], ultimo_dato_insertado[2], ultimo_dato_insertado[3],sum(ultimo_dato_insertado[3]), ultimo_dato_insertado[9], ultimo_dato_insertado[8]))
                                conexion.commit()
                                try:
                                    valor_total_productos = sum(
                                        x * y for x, y in zip(ultimo_dato_insertado[5], ultimo_dato_insertado[6]))
                                    with conexion.cursor() as cursor:
                                        consulta = "INSERT INTO informe_productos(id_factura_pro, nombre_productos, precio_productos, cantidad_productos, valor_total, fecha_factura_pro, estado ) VALUES (%s, %s, %s, %s, %s, %s, %s);"
                                        cursor.execute(consulta, (ultimo_dato_insertado[0], ultimo_dato_insertado[4],ultimo_dato_insertado[5],ultimo_dato_insertado[6], valor_total_productos, ultimo_dato_insertado[9],ultimo_dato_insertado[8]))
                                    conexion.commit()
                                except psycopg2.Error as e:
                                    return ("Ocurrió un error al crear el informe:", e)
                            except psycopg2.Error as e:
                                return ("Ocurrió un error al crear el informe:", e)
                        except psycopg2.Error as e:
                            return ("Ocurrió un error al obtener la última fila insertada en la tabla facturas:", e)
                    except psycopg2.Error as e:
                        return ("Ocurrió un error al editar: ", e)
                except psycopg2.Error as e:
                    return ("Ocurrió un error al crear la factura:", e)
                return ('se creo la factura')
            except psycopg2.Error as e:
                return ("Ocurrió un error al consultar los datos de los servicios: ", e)



    def pagar_facturas_documento(self, documento_cliente_pagar):
        '''documento_cliente_pagar = input('Ingrese el documento del cliente el cual generó el pago de todas sus facturas: ')'''
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT valor_total FROM facturas WHERE documento_cliente = %s AND pagado = %s", (documento_cliente_pagar, False))
                valores_totales= cursor.fetchall()
                valores_totales_list = [valor[0] for valor in valores_totales]
                print('La lista de los valores de cada factura que debe pagar es la siguiente: ', (valores_totales_list))
                valor_total = sum(valores_totales_list)
                return valor_total, documento_cliente_pagar
        except psycopg2.Error as e:
            return ("Ocurrió un error al consultar: ", e)

    def pagar_facturas_documento_aceptar(self, documento_cliente_pagar):
        print('hpta')
        try:
            with conexion.cursor() as cursor:
                consulta = "UPDATE facturas SET pagado = %s WHERE documento_cliente = %s"
            cursor.execute(consulta, (True, documento_cliente_pagar))
            conexion.commit()
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM facturas WHERE documento_cliente = %s ", (documento_cliente_pagar))
            facturas_pendientes = cursor.fetchall()
            conexion.commit()
            if facturas_pendientes:
                facturas_pendientes_list = [factura[1] for factura in facturas_pendientes]
                for factura_pendi in facturas_pendientes_list:
                    with conexion.cursor() as cursor:
                        consulta = "UPDATE informe_productos SET estado = %s WHERE id_factura_pro = %s"
                    cursor.execute(consulta, (True, factura_pendi))
                    with conexion.cursor() as cursor:
                        consulta = "UPDATE informe_servicios SET estado = %s WHERE id_factura_ser = %s"
                    cursor.execute(consulta, (True, factura_pendi))
                return ('Se efectuo el pago de la factura correctamente')
            else:
                return ('No tienes facturas pendientes')
        except psycopg2.Error as e:
            return ("Ocurrió un error al pagar: ", e)







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