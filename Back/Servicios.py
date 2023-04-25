from BD.Conexion import *

basedatos = Database("postgres", "87b3d9baf", "localhost")
conexion= basedatos.conectar()

class Servicios():

    def modificar_servicios(self):
        try:
            with conexion.cursor() as cursor:
                id_buscar = int(input("Ingrese el ID del servicio"))
                precio_nuevo = int(input("Precio actual"))
                consulta = "UPDATE servicios SET precio = '" + str(precio_nuevo) + "' WHERE id_servicios = " + str(
                    id_buscar)

                cursor.execute(consulta)
            conexion.commit()
            print("Precio modificado")
        except psycopg2.Error as e:
            print("Ocurrió un error al editar: ", e)

    def agregar_servicio(self):
        try:
            with conexion.cursor() as cursor:
                consulta = "INSERT INTO servicios(nombre_servicio, precio, tiempo_promedio) VALUES (%s, %s, %s);"
                nombre_pro = input("Ingrese el nombre del servicio: ")
                tiempo_promedio = int(input("Ingrese el tiempo promedio de este servicio: "))
                precio_pro = int(input("Ingrese el precio del servicio: "))
                cursor.execute(consulta, (nombre_pro, precio_pro, tiempo_promedio))
            conexion.commit()
            print("Servicio ingresado")
        except psycopg2.Error as e:
            print("Ocurrió un error al ingresar el servicio:", e)

    def consultar_servicios(self):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM servicios;")
                servicios = cursor.fetchall()
                for servicio in servicios:
                    print(servicio)
        except psycopg2.Error as e:
            print("Ocurrio un error al consultar: ", e)

    def verificar_servicio(self):
        servicio_a_buscar = input("Ingrese el id del servicio")
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM servicios WHERE id_servicios=" + str(servicio_a_buscar))
                servicio = cursor.fetchone()
                if servicio:
                    print(servicio)
                else:
                    print("El servicio no existe")
        except psycopg2.Error as e:
            print("Ocurrio un error al consultar: ", e)
