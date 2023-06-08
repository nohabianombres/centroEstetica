from BD.Conexion import *
from Front.administrador.ventanasAdmin import *
from Front.recepcionista.ventanasRecepcionista import *
from Front.cajero.ventanasCajero import *
from Front.trabajador.ventanasTrabajador import *
from Front.administrador.emeAdm.emeAdmcodigo import *
from Front.comunes.emerComunes import *


basedatos = Database("postgres", "00112233", "centroestetica.ccwkcz7cjsk2.us-east-2.rds.amazonaws.com")
conexion= basedatos.conectar()

class Clientes():

    def crear_clientes(self, in_documento, in_nombre, in_apellido, in_telefono, in_correo):
        try:
            with conexion.cursor() as cursor:
                consulta = "INSERT INTO clientes(documento, nombre, apellido, telefono, correo, numero_faltas, estado) VALUES (%s, %s, %s, %s, %s, %s, %s);"
                '''in_documento = input("Ingrese el documento del cliente: ")
                in_nombre = input("Ingrese el nombre del cliente: ")
                in_apellido = input("Ingrese el apellido del cliente: ")
                in_telefono = input("Ingrese el teléfono del cliente: ")
                in_correo = input("Ingrese el correo electrónico del cliente: ")'''
                cursor.execute(consulta, (in_documento, in_nombre, in_apellido, in_telefono, in_correo, 0, True))
            conexion.commit()
            print("Cliente creado")
            return 'Cliente creado'
        except psycopg2.Error as e:
            return "Ocurrió un error al crear el cliente:"


    def adicionar_falta_cliente(self, documento):
        '''documento = input("Ingrese el documento")'''
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM clientes WHERE documento=" + str(documento))
                cliente = cursor.fetchone()
                if cliente:
                    faltas = cliente[5]
                    valor_total = faltas + 1
                    if valor_total < 3:
                        try:
                            with conexion.cursor() as cursor:
                                consulta = "UPDATE clientes SET numero_faltas = '" + str(
                                    valor_total) + "' WHERE documento = " + str(documento)

                                cursor.execute(consulta)
                            conexion.commit()
                            print("falta agregada")
                            return 'Falta agregada'
                        except psycopg2.Error as e:
                            print("Ocurrió un error al editar: ", e)
                    elif valor_total >= 3:
                        try:
                            with conexion.cursor() as cursor:
                                consulta = "UPDATE clientes SET numero_faltas = '" + str(
                                    valor_total) + "' WHERE documento = " + str(documento)
                                cursor.execute(consulta)
                            conexion.commit()
                            print("falta agregada")
                        except psycopg2.Error as e:
                            print("Ocurrió un error al editar: ", e)
                        try:
                            with conexion.cursor() as cursor:
                                consulta = "UPDATE clientes SET estado = '" + str(False) + "' WHERE documento = " + str(
                                    documento)

                                cursor.execute(consulta)
                            conexion.commit()
                            return "Usuario betado por cantidad de faltas"

                        except psycopg2.Error as e:
                            return "Ocurrió un error al editar: "
                else:
                    return "El cliente no existe"
        except psycopg2.Error as e:
            return "Ocurrio un error al consultar: "



    def verificar_cliente(self, cliente_a_buscar):
        '''cliente_a_buscar = input("Ingrese el documento")'''
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM clientes WHERE documento=" + str(cliente_a_buscar))
                cliente = cursor.fetchone()
                if cliente:
                    print(cliente)
                    return cliente
                else:
                    print("El cliente no existe")
                    return 'No se encontro ningun cliente'
        except psycopg2.Error as e:
            return "Ocurrio un error al consultar: "

    def consultar_clientes(self):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM clientes;")
                clientes_con = cursor.fetchall()
                for cliente in clientes_con:
                    print(cliente)
                return clientes_con
        except psycopg2.Error as e:
            return "Ocurrio un error al consultar: "



