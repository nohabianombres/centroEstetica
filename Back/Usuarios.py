from BD.Conexion import *

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
        except psycopg2.Error as e:
            print("Ocurrio un error al consultar: ", e)

class Trabajadores(Usuarios):

    def consultar_agenda_personal(self):
        id_trabajador = self.usuario_propio
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM citas WHERE trabajador=" + str(id_trabajador))
                citas = cursor.fetchall()
                if citas:
                    for cada_cita in citas:
                        print(cada_cita)
                else:
                    print("No tienes agenda")
        except psycopg2.Error as e:
            print("Ocurrio un error al consultar: ", e)


    def inicializar_servicio(self):
        pass

    def finalizar_servicio(self):
        pass


class Administracion(Usuarios):

    def crear_usuarios(self):
        try:
            with conexion.cursor() as cursor:
                consulta = "INSERT INTO usuario (contrasena , nombre, apellido, documento, telefono, correo, rol) VALUES (%s, %s, %s, %s, %s, %s, %s);"
                in_contrasena = input("ingrese la contraseña: ")
                in_documento = int(input("Ingrese el documento del usuario: "))
                in_nombre = input("Ingrese el nombre del usuario: ")
                in_apellido = input("Ingrese el apellido del usuario: ")
                in_telefono = input("Ingrese el teléfono del usuario: ")
                in_correo = input("Ingrese el correo electrónico del usuario: ")
                print("Cajero, Recepcion o Empleado")
                in_rol = input("Ingrese el rol del usuario: ")

                cursor.execute(consulta, (in_contrasena, in_nombre, in_apellido, in_documento, in_telefono, in_correo, in_rol))
            conexion.commit()
            print("Usuario creado")
        except psycopg2.Error as e:
            print("Ocurrió un error al crear el usuario:", e)

    def ver_informe_productos(self):
        pass

    def ver_informe_servicios(self):
        pass

    def ver_informe_desempeno(self):
        pass

    def verificar_usuario(self):
        usuario_a_buscar = input("Ingrese el usuario")
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM usuario WHERE usuario=" + str(usuario_a_buscar))
                usuario = cursor.fetchone()
                if usuario:
                    print(usuario)
                else:
                    print("Usuario no encontrado")
        except psycopg2.Error as e:
            print("Ocurrio un error al consultar: ", e)

    def recuperar_contrasena(self):
        try:
            with conexion.cursor() as cursor:
                usuario_buscar = int(input("Ingrese el usuario"))
                contrasena_nueva = int(input("Ingrese la nueva contraseña"))
                consulta = "UPDATE usuario SET contrasena = '" + str(contrasena_nueva) + "' WHERE usuario = " + str(usuario_buscar)

                cursor.execute(consulta)
            conexion.commit()
            print("Contraseña cambiada")
        except psycopg2.Error as e:
            print("Ocurrió un error al editar: ", e)

    def consultar_usuarios(self):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM usuario;")
                usuarios = cursor.fetchall()
                for usuario in usuarios:
                    print(usuario)
        except psycopg2.Error as e:
            print("Ocurrio un error al consultar: ", e)


