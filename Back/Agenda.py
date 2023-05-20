from BD.Conexion import *
from datetime import datetime, timedelta
basedatos = Database("postgres", "00112233", "centroestetica.ccwkcz7cjsk2.us-east-2.rds.amazonaws.com")
conexion = basedatos.conectar()

class Agendas():

    def crear_cita(self):

                in_hora = input("Ingrese la hora de la cita: ")
                hora_cita = datetime.strptime(in_hora, '%H:%M:%S')
                in_fecha = input("Ingrese la fecha de la cita aaaa/mm/dd: ")
                in_documento = input("Ingrese el documento : ")
                in_trabajador = int(input("Ingrese id del trabajador: "))
                in_servicio = int(input("Ingrese el servicio: "))
                try:
                    with conexion.cursor() as cursor:
                        cursor.execute("SELECT * FROM servicios WHERE id_servicios=" + str(in_servicio))
                        servicio = cursor.fetchone()

                        tiempo_promedio = timedelta(minutes=servicio[3])
                        hora_fin_promedio = hora_cita + tiempo_promedio
                        hora_fin_promedio_str = hora_fin_promedio.strftime('%H:%M:%S')
                        print("Nuevo tiempo:", hora_fin_promedio_str)

                    try:
                        with conexion.cursor() as cursor:
                            consulta = "INSERT INTO citas (hora, fecha, documento_fk, servicio_fk, trabajador) VALUES (%s, %s, %s, %s, %s);"
                            cursor.execute(consulta, (in_hora, in_fecha, in_documento, in_servicio, in_trabajador))
                        conexion.commit()
                        print("Cita creada")
                    except psycopg2.Error as e:
                        print("Ocurrio un error al dar el tiempo fin promedio: ", e)

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
