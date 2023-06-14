from BD.Conexion import *

from datetime import datetime, timedelta


basedatos = Database("postgres", "00112233", "centroestetica.ccwkcz7cjsk2.us-east-2.rds.amazonaws.com")
conexion= basedatos.conectar()

class Usuarios():
    nombre_usuario = ""
    apellido_usuario = ""
    usuario_propio = 1
    contrasena = ""
    documento = 1
    telefono = ""
    correo = ""
    rol = ""

    def __init__(self, nombre, apellido,usuario, contrasena_var, documento_var, telefono_var, correo_var, rol_var):
        self.nombre_usuario = nombre
        self.apellido_usuario = apellido
        self.usuario_propio = usuario
        self.contrasena = contrasena_var
        self.documento = documento_var
        self.telefono = telefono_var
        self.correo = correo_var
        self.rol = rol_var

class Cajero(Usuarios):
    pass

class Recepcion(Usuarios):

    def consultar_usuarios(self):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM usuario;")
                usuarios = cursor.fetchall()
                for usuario in usuarios:
                    print(usuario)
                return usuarios
        except psycopg2.Error as e:
            return "Ocurrio un error al consultar: "

class Trabajadores(Usuarios):

    def consultar_agenda_personal(self):
        id_trabajador = self.usuario_propio
        fecha_actual = datetime.now().date()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM citas WHERE trabajador = %s AND fecha >= %s ORDER BY hora, fecha;",(id_trabajador, fecha_actual))
                citas = cursor.fetchall()
                if citas:
                    for cada_cita in citas:
                        print(cada_cita)
                    return citas
                else:
                    return print("No tienes agenda")
        except psycopg2.Error as e:
            return print("Ocurrió un error al consultar: ", e)

    def inicializar_finalizar_cita_(self, cita_ejercer, hora_inicio, hora_fin):
        try:
            with conexion.cursor() as cursor:
                consulta = "UPDATE citas SET hora_inicio = %s, hora_fin = %s WHERE id_cita = %s"
                cursor.execute(consulta, (hora_inicio, hora_fin, cita_ejercer))
            conexion.commit()

            try:
                with conexion.cursor() as cursor:
                    cursor.execute("SELECT * FROM citas WHERE id_cita=" + str(cita_ejercer))
                    cita_pendiente_d = cursor.fetchone()
                print(cita_pendiente_d)
                try:
                    with conexion.cursor() as cursor:
                        cursor.execute("SELECT * FROM servicios WHERE id_servicios = %s ", (cita_pendiente_d[4],))
                        servicio_a_puntaje = cursor.fetchone()
                    tiempo_promedio = timedelta(minutes=servicio_a_puntaje[3])
                    hora_actual_c = datetime.strptime(hora_inicio, '%H:%M:%S')
                    hora_actual_2_c = datetime.strptime(hora_fin, '%H:%M:%S')
                    puntaje_calculo_deno = hora_actual_2_c - hora_actual_c
                    puntaje_calculo = tiempo_promedio / puntaje_calculo_deno
                    print(puntaje_calculo)
                    try:
                        with conexion.cursor() as cursor:
                            cursor.execute("SELECT * FROM usuario WHERE usuario = %s ", (cita_pendiente_d[5],))
                            usuario_escogido = cursor.fetchone()
                        print(usuario_escogido)
                        try:
                            with conexion.cursor() as cursor:
                                cursor.execute("SELECT * FROM desempeno WHERE id_usuario = %s ",
                                               (cita_pendiente_d[5],))
                                usuario_buscar = cursor.fetchone()
                                print(usuario_buscar)
                                if usuario_buscar is None:
                                    try:
                                        with conexion.cursor() as cursor:
                                            consulta = "INSERT INTO desempeno (nombre, apellido, rol, puntaje, id_usuario) VALUES (%s, %s, %s, %s, %s);"
                                            cursor.execute(consulta, (
                                                usuario_escogido[2], usuario_escogido[3], usuario_escogido[7],
                                                puntaje_calculo, usuario_escogido[0]))
                                        conexion.commit()
                                        print('Nuevo puntaje de usuario creado')
                                    except psycopg2.Error as e:
                                        print("Ocurrió un error al crear la tabla de desempeño: ", e)
                                else:
                                    try:
                                        with conexion.cursor() as cursor:
                                            consulta = "UPDATE desempeno SET puntaje = %s WHERE numero_trabajadores = %s"
                                            cursor.execute(consulta, (puntaje_calculo, usuario_buscar[0]))
                                        conexion.commit()
                                        print("Puntaje agregado")
                                    except psycopg2.Error as e:
                                        return ("Ocurrió un error al editarel puntaje: ", e)
                        except psycopg2.Error as e:
                            return ("Ocurrió un error al consultar en desempeno: ", e)

                    except psycopg2.Error as e:
                        return ("Ocurrió un error al consultar en usuarios : ", e)
                except psycopg2.Error as e:
                    return ("Ocurrió un error al consultar servicios: ", e)
            except psycopg2.Error as e:
                return ("Ocurrió un error al consultar citas: ", e)
        except psycopg2.Error as e:
            return ("Ocurrió un error al editar: ", e)

        return 'Cita lista'


class Administracion(Usuarios):

    def crear_usuarios(self, in_contrasena, in_documento, in_nombre, in_apellido, in_telefono, in_correo, in_rol):
        print('entre a crear usuarios la funcion Back')
        try:
            with conexion.cursor() as cursor:
                consulta = "INSERT INTO usuario (contrasena , nombre, apellido, documento, telefono, correo, rol) VALUES (%s, %s, %s, %s, %s, %s, %s);"
                '''in_contrasena = input("ingrese la contraseña: ")
                in_documento = int(input("Ingrese el documento del usuario: "))
                in_nombre = input("Ingrese el nombre del usuario: ")
                in_apellido = input("Ingrese el apellido del usuario: ")
                in_telefono = input("Ingrese el teléfono del usuario: ")
                in_correo = input("Ingrese el correo electrónico del usuario: ")'''
                print("Cajero, Recepcion o Empleado")
                '''in_rol = input("Ingrese el rol del usuario: ")'''

                cursor.execute(consulta, (in_contrasena, in_nombre, in_apellido, in_documento, in_telefono, in_correo, in_rol))
            conexion.commit()
            return "Usuario creado"
        except psycopg2.Error as e:
            return "Ocurrió un error al crear el usuario"


    def verificar_usuario(self, usuario_a_buscar):
        '''usuario_a_buscar = input("Ingrese el usuario")'''
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM usuario WHERE docuemnto=" + str(usuario_a_buscar))
                usuario = cursor.fetchone()
                if usuario:
                    return (usuario)
                else:
                    return ("Usuario no encontrado")
        except psycopg2.Error as e:
            return ("Ocurrio un error al consultar: ", e)

    def cambiar_contrasena(self, usuario_buscar, contrasena_nueva):
        try:
            with conexion.cursor() as cursor:
                '''usuario_buscar = int(input("Ingrese el usuario"))
                contrasena_nueva = int(input("Ingrese la nueva contraseña"))'''
                consulta = "UPDATE usuario SET contrasena = '" + str(contrasena_nueva) + "' WHERE usuario = " + str(usuario_buscar)

                cursor.execute(consulta)
            conexion.commit()
            return ("Contraseña cambiada")
        except psycopg2.Error as e:
            return ("Ocurrió un error al editar: ", e)

    def consultar_usuarios(self):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM usuario;")
                usuarios = cursor.fetchall()
                for usuario in usuarios:
                    return (usuario)
        except psycopg2.Error as e:
            return ("Ocurrio un error al consultar: ", e)


