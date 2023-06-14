from BD.Conexion import *


basedatos = Database("postgres", "00112233", "centroestetica.ccwkcz7cjsk2.us-east-2.rds.amazonaws.com")
conexion= basedatos.conectar()

class Servicios():

    def modificar_servicios(self, id_buscar, precio_nuevo):
        try:
            with conexion.cursor() as cursor:
                '''id_buscar = int(input("Ingrese el ID del servicio"))
                precio_nuevo = int(input("Precio actual"))'''
                consulta = "UPDATE servicios SET precio = '" + str(precio_nuevo) + "' WHERE id_servicios = " + str(id_buscar)
                cursor.execute(consulta)
            conexion.commit()
            return "Precio modificado"
        except psycopg2.Error as e:
            return "Ocurrió un error al editar"

    def agregar_servicio(self, nombre_ser, tiempo_promedio, precio_ser):
        try:
            with conexion.cursor() as cursor:
                consulta = "INSERT INTO servicios(nombre_servicio, precio, tiempo_promedio) VALUES (%s, %s, %s);"
                '''nombre_ser = input("Ingrese el nombre del servicio: ")
                tiempo_promedio = int(input("Ingrese el tiempo promedio de este servicio: "))
                precio_ser = int(input("Ingrese el precio del servicio: "))'''
                cursor.execute(consulta, (nombre_ser, precio_ser, tiempo_promedio))
            conexion.commit()
            return "Servicio ingresado"
        except psycopg2.Error as e:
            return "Ocurrió un error al ingresar el servicio"


    def consultar_servicios(self):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM servicios;")
                servicios = cursor.fetchall()
                for servicio in servicios:
                    print(servicio)
                return servicios
        except psycopg2.Error as e:
            return "Ocurrio un error al consultar"

    def verificar_servicio(self, servicio_a_buscar):
        '''servicio_a_buscar = input("Ingrese el id del servicio")'''
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM servicios WHERE id_servicios=" + str(servicio_a_buscar))
                servicio = cursor.fetchone()
                if servicio:
                    print(servicio)
                    return servicio
                else:
                    return "El servicio no existe"
        except psycopg2.Error as e:
            return "Ocurrio un error al consultar"
