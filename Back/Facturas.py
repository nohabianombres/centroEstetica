from BD.Conexion import *

basedatos = Database("postgres", "00112233", "centroestetica.ccwkcz7cjsk2.us-east-2.rds.amazonaws.com")
conexion= basedatos.conectar()

class Facturas():

    def generar_factura(self):
        cliente_cobrar = input('Ingrese el documento: ')
        precios_servicio = []  # Lista para almacenar los precios de los servicios
        nombres_servicio = []  # Lista para almacenar los nombres de los servicios

        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM citas WHERE documento_fk=" + str(cliente_cobrar))
                servicios = cursor.fetchall()

                for servicio in servicios:
                    cursor.execute("SELECT * FROM servicios WHERE id_servicios=" + str(servicio[4]))
                    servicios_cobrar = cursor.fetchall()
                    for servicioen_cobrar in servicios_cobrar:
                        nombres_servicio.append(servicioen_cobrar[1])
                        precios_servicio.append(servicioen_cobrar[2])
            # Imprime las listas de nobres y precios de los servicios
            print("Nombres de servicios:", nombres_servicio)
            print("Precios de servicios:", precios_servicio)
            try:
                with conexion.cursor() as cursor:
                    consulta = "INSERT INTO facturas(documento_cliente, nombre_servicio, precio_ser, id_pro, cantidad_pro, valor_total) VALUES (%s, %s, %s, %s, %s, %s);"
                    cursor.execute(consulta, (cliente_cobrar, nombres_servicio, precios_servicio, [], [], 0))
                conexion.commit()
                print("Factura creada")
            except psycopg2.Error as e:
                print("Ocurrió un error al crear la factura:", e)

        except psycopg2.Error as e:
            print("Ocurrio un error al consultar: ", e)
    def buscar_facturas(self):
        pass

