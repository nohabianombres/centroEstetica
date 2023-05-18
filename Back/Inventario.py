from BD.Conexion import *

basedatos = Database("postgres", "00112233", "centroestetica.ccwkcz7cjsk2.us-east-2.rds.amazonaws.com")
conexion= basedatos.conectar()

class Inventario():

    def verificar_producto(self):
        producto_a_buscar = input("Ingrese el id del producto")
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM inventario WHERE id_producto=" + str(producto_a_buscar))
                producto = cursor.fetchone()
                if producto:
                    print(producto)
                else:
                    print("Producto no encontrado")
        except psycopg2.Error as e:
            print("Ocurrio un error al consultar: ", e)

    def agregar_nuevo_producto(self):
        try:
            with conexion.cursor() as cursor:
                consulta = "INSERT INTO inventario(nombre_producto, cantidad, precio) VALUES (%s, %s, %s);"
                nombre_pro = input("Ingrese el nombre del producto: ")
                cantidad_pro = int(input("Ingrese la cantidad actual del producto: "))
                precio_pro = int(input("Ingrese el precio del producto: "))
                cursor.execute(consulta, (nombre_pro, cantidad_pro, precio_pro))
            conexion.commit()
            print("Producto ingresado")
        except psycopg2.Error as e:
            print("Ocurrió un error al ingresar el producto:", e)

    def consultar_inverntario(self):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM inventario;")
                inventario = cursor.fetchall()
                for productos in inventario:
                    print(productos)
        except psycopg2.Error as e:
            print("Ocurrio un error al consultar: ", e)

    def cambiar_precio_producto(self):
        try:
            with conexion.cursor() as cursor:
                id_buscar = int(input("Ingrese el ID del producto"))
                precio_nuevo = int(input("Precio actual"))
                consulta = "UPDATE inventario SET precio = '" + str(precio_nuevo) + "' WHERE id_producto = " + str(id_buscar)

                cursor.execute(consulta)
            conexion.commit()
            print("Precio modificado")
        except psycopg2.Error as e:
            print("Ocurrió un error al editar: ", e)

    def agregar_cantidad_inventario(self):
        try:
            with conexion.cursor() as cursor:
                id_buscar = int(input("Ingrese el ID del producto"))
                cantidad_nueva = int(input("Cantidad actual"))
                consulta = "UPDATE inventario SET cantidad = '" + str(cantidad_nueva) + "' WHERE id_producto = " + str(id_buscar)

                cursor.execute(consulta)
            conexion.commit()
        except psycopg2.Error as e:
            print("Ocurrió un error al editar: ", e)

