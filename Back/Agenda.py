from BD.Conexion import *
from datetime import datetime, timedelta
from Front.administrador.ventanasAdmin import *
from Front.recepcionista.ventanasRecepcionista import *
from Front.trabajador.ventanasTrabajador import *
from Front.administrador.emeAdm.emeAdmcodigo import *
from Front.comunes.emerComunes import *
basedatos = Database("postgres", "00112233", "centroestetica.ccwkcz7cjsk2.us-east-2.rds.amazonaws.com")
conexion = basedatos.conectar()

class Agendas():
    def crear_cita(self, in_hora, in_fecha, in_documento, in_trabajador, in_servicio):
        print('entre')
        intervalos_citas = []
        '''in_hora = input("Ingrese la hora de la cita: ")'''
        hora_cita = datetime.strptime(in_hora, '%H:%M:%S')

        '''in_fecha = input("Ingrese la fecha de la cita aaaa/mm/dd: ")
        in_documento = input("Ingrese el documento : ")
        in_trabajador = int(input("Ingrese id del trabajador: "))
        in_servicio = int(input("Ingrese el servicio: "))'''
        var_control = True
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM servicios WHERE id_servicios=" + str(in_servicio))
                servicio = cursor.fetchone()
                tiempo_promedio = timedelta(minutes=servicio[3])
                hora_fin_promedio = hora_cita + tiempo_promedio
                # hora_fin_promedio_str = datetime.strptime(hora_fin_promedio,'%H:%M:%S')#

        except psycopg2.Error as e:
            print("Ocurrió un error al crear la cita: ", e)

        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM clientes WHERE documento=" + str(in_documento))
                cliente = cursor.fetchone()
                if cliente:
                    try:
                        with conexion.cursor() as cursor:
                            cursor.execute("SELECT * FROM citas WHERE fecha=%s AND documento_fk=%s",
                                           (in_fecha, in_documento))
                            citas = cursor.fetchall()

                            for cita in citas:

                                cita_con_1 = datetime.strptime(str(cita[1]), '%H:%M:%S')
                                cita_con_7 = datetime.strptime(str(cita[7]), '%H:%M:%S')
                                if hora_cita <= cita_con_1 and hora_fin_promedio <= cita_con_1:
                                    pass
                                elif hora_cita >= cita_con_7 and hora_fin_promedio >= cita_con_7:
                                    pass
                                elif hora_cita >= cita_con_1 and hora_cita <= cita_con_7:
                                    var_control = False
                                elif hora_fin_promedio >= cita_con_1 and hora_fin_promedio <= cita_con_7:
                                    var_control = False
                                else:
                                    print("ALGO FALLO")
                    except psycopg2.Error as e:
                        pass

                    try:
                        with conexion.cursor() as cursor:
                            cursor.execute("SELECT * FROM usuario WHERE usuario=" + str(in_trabajador))
                            trabajador = cursor.fetchone()
                            if trabajador:
                                if trabajador[7] != "Cajero" and trabajador[7] != "Recepcion" and trabajador[7] != "Admin":
                                    try:
                                        with conexion.cursor() as cursor:
                                            cursor.execute("SELECT * FROM citas WHERE fecha=%s AND trabajador=%s",
                                                           (in_fecha, in_trabajador))
                                            citas_t = cursor.fetchall()

                                            for cita_t in citas_t:
                                                cita_con_1_t = datetime.strptime(str(cita_t[1]), '%H:%M:%S')
                                                cita_con_7_t = datetime.strptime(str(cita_t[7]), '%H:%M:%S')
                                                if hora_cita <= cita_con_1_t and hora_fin_promedio <= cita_con_1_t:
                                                    pass
                                                elif hora_cita >= cita_con_7_t and hora_fin_promedio >= cita_con_7_t:
                                                    pass
                                                elif hora_cita >= cita_con_1_t and hora_cita <= cita_con_7_t:
                                                    var_control = False
                                                elif hora_fin_promedio >= cita_con_1_t and hora_fin_promedio <= cita_con_7_t:
                                                    var_control = False
                                                else:
                                                    print("ALGO FALLO")

                                    except psycopg2.Error as e:
                                        pass
                                else:
                                    print("No es un empleado")
                                    var_control = False
                    except psycopg2.Error as e:
                        print("Usuario no existe")
                else:
                    print('siga')
            if var_control == True:
                try:
                    with conexion.cursor() as cursor:
                        consulta = "INSERT INTO citas (hora, fecha, documento_fk, servicio_fk, trabajador, hora_aproximada_fin) VALUES (%s, %s, %s, %s, %s, %s);"
                        cursor.execute(consulta,
                                       (in_hora, in_fecha, in_documento, in_servicio, in_trabajador, hora_fin_promedio))
                        conexion.commit()
                        print("Cita creada")
                except psycopg2.Error as e:
                    print("Ocurrio un error : ", e)
            else:
                print("Algo paso")
        except psycopg2.Error as e:
            print("Ocurrio un error al consultar el cliente: ", e)
            var_control = False









    def consultar_citas(self, cliente_consultar):
        '''cita_a_buscar = input("Ingrese el id de la cita")'''
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM citas WHERE documento_cliente=" + str(cliente_consultar))
                citas = cursor.fetchall()
                for cita in citas:
                    if cita:
                        print(cita)
                    else:
                        print("Cliente no tiene citas")
        except psycopg2.Error as e:
            print("Ocurrio un error al consultar: ", e)

    def cancelar_cita(self, cliente_cancelar):
        '''cita_a_cancelar=input("Ingerese el id de la cita: ")'''
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM citas WHERE documento_cliente=" + str(cliente_cancelar))
                citas = cursor.fetchall()
                for cita in citas:
                    if cita:
                        print(cita)
                    else:
                        print("Cliente no tiene citas")
                    id_cita_cancelar = input('Ingrese el id de la cita que quiere cancelar, (el primer numero de la fila)')
                    try:
                        with conexion.cursor() as cursor:
                            consulta = "DELETE FROM citas WHERE documento_cliente=" + str(id_cita_cancelar)
                            cursor.execute(consulta)
                            print("Cita cancelada correctamente")
                        conexion.commit()
                    except psycopg2.Error as e:
                        print("Error al eliminar cita: ", e)
        except psycopg2.Error as e:
            print("Ocurrio un error al consultar: ", e)


