from BD.Conexion import *

basedatos = Database("postgres", "87b3d9baf", "localhost")
conexion = basedatos.conectar()

class Agendas():

    def crear_cita(self):
        try:
            with conexion.cursor() as cursor:
                consulta = "INSERT INTO citas (hora, fecha, documento_fk, servicio_fk, trabajador) VALUES (%s, %s, %s, %s, %s);"
                in_hora = input("Ingrese la hora de la cita: ")
                in_fecha = input("Ingrese la fecha de la cita: ")
                in_documento = input("Ingrese el documento : ")
                in_servicio = input("Ingrese el servicio: ")
                in_trabajador = input("Ingrese id del trabajador: ")

                cursor.execute(consulta, (in_hora, in_fecha, in_documento, in_servicio, in_trabajador))
            conexion.commit()
            print("Cita creada")
        except psycopg2.Error as e:
            print("Ocurrió un error al crear la cita: ", e)

    def consultar_cita(self):
        cita_a_buscar = input("Ingrese el id de la cita")
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM citas WHERE id_cita=" + str(cita_a_buscar))
                cita = cursor.fetchone()
                if cita:
                    print(cita)
                else:
                    print("Cita no encontrada")
        except psycopg2.Error as e:
            print("Ocurrio un error al consultar: ", e)

    def cancelar_cita(self):
        cita_a_cancelar=input("Ingerese el id de la cita: ")
        try:
            with conexion.cursor() as cursor:
                consulta = "DELETE FROM citas WHERE id_cita=" + str(cita_a_cancelar)
                cursor.execute(consulta)
                print("Cita cancelada correctamente")
            conexion.commit()
        except psycopg2.Error as e:
            print("Error al eliminar cita: ", e)
