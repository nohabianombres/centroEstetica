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
            return print("Ocurrio un error al consultar: ", e)

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

    def inicializar_finalizar_cita_(self, documento_cliente):
        id_citas = []
        var_control=False
        '''documento_cliente = int(input('Ingrese el documento del cliente: '))'''
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM citas WHERE documento_fk = %s AND facturado = %s", (documento_cliente, False))
                citas_pendientes = cursor.fetchall()

                for cita_pendiente in citas_pendientes:
                    print(cita_pendiente)
                    id_citas.append(str(cita_pendiente[0]))
                cita_ejercer = input('Ingrese el id de la cita (1 columna): ')
                if len(id_citas)!= 0:
                    for i in range (len(id_citas)):
                        if id_citas[i]==cita_ejercer:
                            var_control=True
                            print("encontrado")
                        else:
                            print("paila, siga buscando")
                if var_control== True:
                        hora_actual = datetime.now().strftime('%H:%M:%S')
                        try:
                            with conexion.cursor() as cursor:
                                consulta = "UPDATE citas SET hora_inicio = %s WHERE id_cita = %s"
                                cursor.execute(consulta, (hora_actual, cita_ejercer))
                            conexion.commit()
                            print("Hora de inicio agregada")
                        except psycopg2.Error as e:
                            print("Ocurrió un error al editar: ", e)
                else:
                    print('Pero porque eres asi')

                acceso_hora_fin = int(input('Ingrese el uno 1 si quiere finalizar cita '))
                if acceso_hora_fin == 1:
                        hora_actual_2 = datetime.now().strftime('%H:%M:%S')
                        try:
                            with conexion.cursor() as cursor:
                                consulta = "UPDATE citas SET hora_fin = %s WHERE id_cita = %s"
                                cursor.execute(consulta, (hora_actual_2, cita_ejercer))
                            conexion.commit()
                            print("Hora de fin agregada")
                            try:
                                with conexion.cursor() as cursor:
                                    cursor.execute("SELECT * FROM citas WHERE id_cita=" + str(cita_ejercer))
                                    cita_pendiente_d = cursor.fetchone()
                                print(cita_pendiente_d)
                                try:
                                    with conexion.cursor() as cursor:
                                        cursor.execute("SELECT * FROM servicios WHERE id_servicios = %s ",(cita_pendiente_d[4],))
                                        servicio_a_puntaje = cursor.fetchone()
                                    tiempo_promedio = timedelta(minutes=servicio_a_puntaje[3])
                                    hora_actual_c = datetime.strptime(hora_actual, '%H:%M:%S')
                                    hora_actual_2_c = datetime.strptime(hora_actual_2, '%H:%M:%S')
                                    puntaje_calculo_deno = hora_actual_2_c - hora_actual_c
                                    puntaje_calculo = tiempo_promedio / puntaje_calculo_deno
                                    print(puntaje_calculo)
                                    try:
                                        with conexion.cursor() as cursor:
                                            cursor.execute("SELECT * FROM usuario WHERE usuario = %s ",(cita_pendiente_d[5],))
                                            usuario_escogido = cursor.fetchone()
                                        print(usuario_escogido)
                                        try:
                                            with conexion.cursor() as cursor:
                                                cursor.execute("SELECT * FROM desempeno WHERE id_usuario = %s ",(cita_pendiente_d[5],))
                                                usuario_buscar = cursor.fetchone()
                                                print(usuario_buscar)
                                                if usuario_buscar is None:
                                                    try:
                                                        with conexion.cursor() as cursor:
                                                            consulta = "INSERT INTO desempeno (nombre, apellido, rol, puntaje, id_usuario) VALUES (%s, %s, %s, %s, %s);"
                                                            cursor.execute(consulta, (usuario_escogido[2], usuario_escogido[3],usuario_escogido[7],puntaje_calculo, usuario_escogido[0]))
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
                                                        print("Ocurrió un error al editarel puntaje: ", e)
                                        except psycopg2.Error as e:
                                            print("Ocurrió un error al consultar en desempeno: ", e)

                                    except psycopg2.Error as e:
                                        print("Ocurrió un error al consultar en usuarios : ", e)
                                except psycopg2.Error as e:
                                    print("Ocurrió un error al consultar servicios: ", e)
                            except psycopg2.Error as e:
                                print("Ocurrió un error al consultar citas: ", e)
                        except psycopg2.Error as e:
                            print("Ocurrió un error al editar: ", e)
                else:
                    print("Lo que ingreso no es valido")
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)








class Administracion(Usuarios):
    def lologre (self):
        print ('asi fueque')

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


