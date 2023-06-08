from BD.Conexion import *
from datetime import datetime, timedelta

from Front.administrador.ventanasAdmin import *
from Front.administrador.emeAdm.emeAdmcodigo import *


basedatos = Database("postgres", "00112233", "centroestetica.ccwkcz7cjsk2.us-east-2.rds.amazonaws.com")
conexion= basedatos.conectar()


class Informe():

    def informe_productos(self, numero_dias):
        '''numero_dias = int(input('Ingrese la cantidad de dias desde la cual quiere que traiga las facturas: '))'''
        fecha_actual = datetime.now().date()
        fecha_minima = fecha_actual - timedelta(days=numero_dias)
        try:
            consulta = "SELECT * FROM informe_productos WHERE fecha_factura_pro >= %s ORDER BY fecha_factura_pro DESC;"
            with conexion.cursor() as cursor:
                cursor.execute(consulta, (fecha_minima,))
                informes_pro = cursor.fetchall()
            for informe_pro in informes_pro:
                print(informe_pro)
            return informes_pro
        except psycopg2.Error as e:
            return "Ocurrió un error al consultar"

    def informe_servicios(self, numero_dias):
        '''numero_dias = int(input('Ingrese la cantidad de dias desde la cual quiere que traiga las facturas: '))'''
        fecha_actual = datetime.now().date()
        fecha_minima = fecha_actual - timedelta(days=numero_dias)
        try:
            consulta = "SELECT * FROM informe_servicios WHERE fecha_factura_ser >= %s ORDER BY fecha_factura_ser DESC;"
            with conexion.cursor() as cursor:
                cursor.execute(consulta, (fecha_minima,))
                informes_ser = cursor.fetchall()
            for informe_ser in informes_ser:
                print(informe_ser)
            return informes_ser
        except psycopg2.Error as e:
            return "Ocurrió un error al consultar"

    def mostar_informe_facturas(self, numero_dias):
        '''numero_dias = int(input('Ingrese la cantidad de dias desde la cual quiere que traiga las facturas: '))'''
        fecha_actual = datetime.now().date()
        fecha_minima = fecha_actual - timedelta(days=numero_dias)
        try:
            consulta = "SELECT * FROM facturas WHERE fecha_creacion >= %s ORDER BY fecha_creacion DESC;"
            with conexion.cursor() as cursor:
                cursor.execute(consulta, (fecha_minima,))
                facturas = cursor.fetchall()
            for factura in facturas:
                print(factura)
            return facturas
        except psycopg2.Error as e:
            return "Ocurrió un error al consultar"

    def mostrar_cartera(self, numero_dias):
        '''numero_dias = int(input('Ingrese la cantidad de dias desde la cual quiere que traiga las facturas: '))'''
        fecha_actual = datetime.now().date()
        fecha_minima = fecha_actual - timedelta(days=numero_dias)
        try:
            consulta = "SELECT * FROM facturas WHERE fecha_creacion >= %s AND pagado = %s ORDER BY fecha_creacion"
            with conexion.cursor() as cursor:
                cursor.execute(consulta, (fecha_minima,False))
                facturas = cursor.fetchall()
            for factura in facturas:
                print(factura)
            return facturas
        except psycopg2.Error as e:
            return "Ocurrió un error al consultar"

    def mostrar_desempeno(self):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM desempeno ORDER BY puntaje DESC;")
                usuarios_calificados = cursor.fetchall()
                for usuario_calificado in usuarios_calificados:
                    print(usuario_calificado)
                return usuarios_calificados
        except psycopg2.Error as e:
            return "Ocurrió un error al consultar"
