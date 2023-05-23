from BD.Conexion import *
from datetime import datetime, timedelta
basedatos = Database("postgres", "00112233", "centroestetica.ccwkcz7cjsk2.us-east-2.rds.amazonaws.com")
conexion= basedatos.conectar()


class Informe():

    def informe_productos(self):
        numero_dias = int(input('Ingrese la cantidad de dias desde la cual quiere que traiga las facturas: '))
        fecha_actual = datetime.now().date()
        fecha_minima = fecha_actual - timedelta(days=numero_dias)
        consulta = "SELECT * FROM informe_productos WHERE fecha_factura_pro >= %s"
        with conexion.cursor() as cursor:
            cursor.execute(consulta, (fecha_minima,))
            informes_pro = cursor.fetchall()
        for informe_pro in informes_pro:
            print(informe_pro)

    def informe_servicios(self):
        numero_dias = int(input('Ingrese la cantidad de dias desde la cual quiere que traiga las facturas: '))
        fecha_actual = datetime.now().date()
        fecha_minima = fecha_actual - timedelta(days=numero_dias)
        consulta = "SELECT * FROM informe_servicios WHERE fecha_factura_ser >= %s"
        with conexion.cursor() as cursor:
            cursor.execute(consulta, (fecha_minima,))
            informes_ser = cursor.fetchall()
        for informe_ser in informes_ser:
            print(informe_ser)

    def mostar_informe_facturas(self):
        numero_dias = int(input('Ingrese la cantidad de dias desde la cual quiere que traiga las facturas: '))
        fecha_actual = datetime.now().date()

        fecha_minima = fecha_actual - timedelta(days=numero_dias)
        consulta = "SELECT * FROM facturas WHERE fecha_creacion >= %s"
        with conexion.cursor() as cursor:
            cursor.execute(consulta, (fecha_minima,))
            facturas = cursor.fetchall()
        for factura in facturas:
            print(factura)

    def mostrar_cartera(self):
        numero_dias = int(input('Ingrese la cantidad de dias desde la cual quiere que traiga las facturas: '))
        fecha_actual = datetime.now().date()

        fecha_minima = fecha_actual - timedelta(days=numero_dias)
        consulta = "SELECT * FROM facturas WHERE fecha_creacion >= %s AND pagado = %s"
        with conexion.cursor() as cursor:
            cursor.execute(consulta, (fecha_minima,False))
            facturas = cursor.fetchall()
        for factura in facturas:
            print(factura)

class Productividad():

    def mostar_informe_semanal(self):
        pass

    def mostrar_informe_mensual(self):
        pass