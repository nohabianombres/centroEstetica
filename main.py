from Back.Clientes import *
from Back.Facturas import *
from Back.Informes import *
from Back.Servicios import *
from Back.Usuarios import *
from Back.Inventario import *
from BD.Conexion import *
from Back.Agenda import *
import psycopg2

basedatos = Database("postgres", "00112233", "centroestetica.ccwkcz7cjsk2.us-east-2.rds.amazonaws.com")
conexion = basedatos.conectar()

### definir funciones

inicio_usuario = int(input("Ingrese el usuario"))
inicio_contrasena = input("Ingrese contraseña")

var_control = True
var_control2 = True

try:
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM usuario WHERE usuario = " + str(inicio_usuario))
        usuario = cursor.fetchone()
        if usuario:
            usuario_login = usuario[0]
            usuario_contrasena = usuario[1]
            if usuario_contrasena == inicio_contrasena:
                rol_usuario = usuario[7]
                if rol_usuario == "Admin":
                    administrador = Administracion(usuario[2], usuario[3], int(usuario[0]), usuario[1], int(usuario[4]), usuario[5], usuario[6], usuario[7])
                    print("Hola admin")
                    while var_control == True :
                        var_control2 = True
                        print('Ingrese "1" para ingresar al inventario')
                        print('Ingrese "2" para ingresar a los servicios')
                        print('Ingrese "3" para ingresar a las facturas')
                        print('Ingrese "4" para ingresar a los clientes')
                        print('Ingrese "5" para ingresar a la agenda')
                        print('Ingrese "6" para ingresar a los informes')
                        print('Ingrese "7" para ingresar a los usuarios')
                        print('Ingrese "0" para salir del programa')
                        menu = int(input("Ingrese la opcion a elegir: "))
                        if menu == 1:
                            inventario = Inventario()
                            while var_control2 == True:
                                print('Ingrese "1" para agregar producto al inventario')
                                print('Ingrese "2" para consultar el inventario')
                                print('Ingrese "3" para consultar un producto del inventario')
                                print('Ingrese "4" para cambiar precio de un producto del inventario')
                                print('Ingrese "5" para cambiar la cantidad de un producto del inventario')
                                print('Ingrese "0" para salir al menu principal')
                                menu2 = int(input("Ingrese la opcion a elegir: "))
                                if menu2 == 1:
                                    inventario.agregar_nuevo_producto()
                                elif menu2 == 2:
                                    inventario.consultar_inverntario()
                                elif menu2 == 3:
                                    inventario.verificar_producto()
                                elif menu2 == 4:
                                    inventario.cambiar_precio_producto()
                                elif menu2 == 5:
                                    inventario.agregar_cantidad_inventario()
                                elif menu2 == 0:
                                    print("Regresando al menu principal")
                                    var_control2 = False
                                    del inventario
                                else:
                                    print("valor no valido")
                        if menu == 2:
                            servicios = Servicios()
                            while var_control2 == True:
                                print('Ingrese "1" para consultar los servicios')
                                print('Ingrese "2" para agregar nuevo servicio')
                                print('Ingrese "3" para modificar el precio de un servicio')
                                print('Ingrese "0" para salir al menu principal')
                                menu2 = int(input("Ingrese la opcion a elegir: "))
                                if menu2 == 1:
                                    servicios.consultar_servicios()
                                elif menu2 == 2:
                                    servicios.agregar_servicio()
                                elif menu2 == 3:
                                    servicios.modificar_servicios()
                                elif menu2 == 0:
                                    print("Regresando al menu principal")
                                    var_control2 = False
                                    del servicios
                                else:
                                    print("valor no valido")
                        if menu == 3:
                            ### falta programas las funciones
                            facturas = Facturas()
                            while var_control2 == True:
                                print('Ingrese "1" generar factura')
                                print('Ingrese "2" generar pago de todas las facturas pendientes ')
                                print('Ingrese "3" para pagar una factura con su respectivo id:  ')
                                print('Ingrese "4" para buscar factuas de un cliente: ')
                                print('Ingrese "0" para salir al menu principal')
                                menu2 = int(input("Ingrese la opcion a elegir: "))
                                if menu2 == 1:
                                    facturas.generar_factura_servicios_productos()
                                elif menu2 == 2:
                                    facturas.pagar_facturas_documento()
                                elif menu2 == 3:
                                    facturas.pagar_facturas_idFactura()
                                elif menu2 == 4:
                                    facturas.buscar_facturas_cliente()
                                elif menu2 == 0:
                                    print("Regresando al menu principal")
                                    var_control2 = False
                                    del facturas
                                else:
                                    print("valor no valido")
                        if menu == 4:
                            clientes = Clientes()
                            while var_control2 == True:
                                print('Ingrese "1" para consultar cliente')
                                print('Ingrese "2" crear nuevo cliente')
                                print('Ingrese "3" adicionar falta al cliente')
                                print('Ingrese "4" ver todos los cliente')
                                print('Ingrese "0" para salir al menu principal')
                                menu2 = int(input("Ingrese la opcion a elegir: "))
                                if menu2 == 1:
                                    clientes.verificar_cliente()
                                elif menu2 == 2:
                                    clientes.crear_clientes()
                                elif menu2 == 3:
                                    clientes.adicionar_falta_cliente()
                                elif menu2 == 4:
                                    clientes.consultar_clientes()
                                elif menu2 == 0:
                                    print("Regresando al menu principal")
                                    var_control2 = False
                                    del clientes
                                else:
                                    print("valor no valido")
                        if menu == 5:
                            agenda = Agendas()
                            while var_control2 == True:
                                print('Ingrese "1" para crear cita')
                                print('Ingrese "2" para buscar cita')
                                print('Ingrese "3" para cancelar cita')
                                print('Ingrese "0" para salir al menu principal')
                                menu2 = int(input("Ingrese la opcion a elegir: "))
                                if menu2 == 1:
                                    agenda.crear_cita()
                                elif menu2 == 2:
                                    agenda.consultar_cita()
                                elif menu2 == 3:
                                    agenda.cancelar_cita()
                                elif menu2 == 0:
                                    print("Regresando al menu principal")
                                    var_control2 = False
                                    del agenda
                                else:
                                    print("valor no valido")

                        if menu == 6:
                            informe = Informe()
                            while var_control2 == True:
                                print('Ingrese "1" para ver informe de facturas')
                                print('Ingrese "2" para ver cartera')
                                print('Ingrese "3" para ver informe de productos')
                                print('Ingrese "4" para ver informe de servicios')
                                print('Ingrese "0" para salir al menu principal')
                                menu2 = int(input("Ingrese la opcion a elegir: "))
                                if menu2 == 1:
                                    informe.mostar_informe_facturas()
                                elif menu2 == 2:
                                    informe.mostrar_cartera()
                                elif menu2 == 3:
                                    informe.informe_productos()
                                elif menu2 == 4:
                                    informe.informe_servicios()
                                    print("Regresando al menu principal")
                                    var_control2 = False
                                elif menu2 == 0:
                                    del informe
                                else:
                                    print("valor no valido")
                        if menu == 7:
                            while var_control2 == True:
                                print('Ingrese "1" para crear un nuevo usuarios')
                                print('Ingrese "2" para mostrar listado de usuarios')
                                print('Ingrese "3" para buscar a un usuario')
                                print('Ingrese "4" para cambiar la contrasela de un usuario')
                                print('Ingrese "0" para salir al menu principal')
                                menu2 = int(input("Ingrese la opcion a elegir: "))
                                if menu2 == 1:
                                    administrador.crear_usuarios()
                                elif menu2 == 2:
                                    administrador.consultar_usuarios()
                                elif menu2 == 3:
                                    administrador.verificar_usuario()
                                elif menu2 == 4:
                                    administrador.recuperar_contrasena()
                                elif menu2 == 0:
                                    print("Regresando al menu principal")
                                    var_control2 = False
                                else:
                                    print("valor no valido")
                        if menu ==0:
                            var_control = False

                        else:
                            print("Valor ingresado no valido")

                elif rol_usuario == "Cajero":
                    cajero = Cajero(usuario[2], usuario[3], int(usuario[0]), usuario[1], int(usuario[4]), usuario[5], usuario[6], usuario[7])
                    print("Hola cajero")
                    while var_control == True :
                        var_control2 = True
                        print('Ingrese "1" para ingresar al inventario')
                        print('Ingrese "2" para ingresar a servicios')
                        print('Ingrese "3" para ingresar a facturación')
                        print('Ingrese "0" para salir del programa')
                        menu = int(input("Ingrese la opcion a elegir: "))
                        if menu == 1:
                            inventario = Inventario()
                            while var_control2 == True:
                                print('Ingrese "1" para consultar el inventario')
                                print('Ingrese "2" para consultar un producto del inventario')
                                print('Ingrese "0" para salir al menu principal')
                                menu2 = int(input("Ingrese la opcion a elegir: "))
                                if menu2 == 1:
                                    inventario.consultar_inverntario()
                                elif menu2 == 2:
                                    inventario.verificar_producto()
                                elif menu2 == 0:
                                    print("Regresando al menu principal")
                                    var_control2 = False
                                    del inventario
                                else:
                                    print("valor no valido")
                        if menu == 2:
                            servicios = Servicios()
                            while var_control2 == True:
                                print('Ingrese "1" para consultar los servicios')
                                print('Ingrese "2" para consultar un servicio')
                                print('Ingrese "0" para salir al menu principal')
                                menu2 = int(input("Ingrese la opcion a elegir: "))
                                if menu2 == 1:
                                    servicios.consultar_servicios()
                                elif menu2 == 2:
                                    servicios.verificar_servicio()
                                elif menu2 == 0:
                                    print("Regresando al menu principal")
                                    var_control2 = False
                                    del servicios
                                else:
                                    print("valor no valido")
                        if menu == 3:
                            ### falta programas las funciones
                            facturas = Facturas()
                            while var_control2 == True:
                                print('Ingrese "1" ')
                                print('Ingrese "2" ')
                                print('Ingrese "3" ')
                                print('Ingrese "0" para salir al menu principal')
                                menu2 = int(input("Ingrese la opcion a elegir: "))
                                if menu2 == 1:
                                    pass
                                elif menu2 == 2:
                                    pass
                                elif menu2 == 3:
                                    pass
                                elif menu2 == 0:
                                    print("Regresando al menu principal")
                                    var_control2 = False
                                    del facturas
                                else:
                                    print("valor no valido")
                        if menu == 0 :
                            var_control = False

                elif rol_usuario == "Recepcion":
                    recepcionista = Recepcion(usuario[2], usuario[3], int(usuario[0]), usuario[1], int(usuario[4]), usuario[5], usuario[6], usuario[7])
                    print("Hola Recepcion")
                    while var_control == True :
                        var_control2 = True
                        print('Ingrese "1" para ingresar a los clientes')
                        print('Ingrese "2" para ingresar a la agenda')
                        print('Ingrese "3" para ingresar a los usuarios')
                        print('Ingrese "0" para salir del programa')
                        menu = int(input("Ingrese la opcion a elegir: "))
                        if menu == 1:
                            cliente = Clientes()
                            while var_control2 == True:
                                print('Ingrese "1" para crear cliente')
                                print('Ingrese "2" para consultar cliente')
                                print('Ingrese "3" para adicionar falta')
                                print('Ingrese "4" para consultar todos los clientes')
                                print('Ingrese 0 para salir al menu principal')
                                menu2 = int(input("Ingrese la opcion a elegir: "))
                                if menu2 == 1:
                                    cliente.crear_clientes()
                                elif menu2 == 2:
                                    cliente.verificar_cliente()
                                elif menu2 == 3:
                                    cliente.adicionar_falta_cliente()
                                elif menu2 == 4:
                                    cliente.consultar_clientes()
                                elif menu2 == 0:
                                    print("Regresando al menu principal")
                                    var_control2 = False
                                    del cliente
                                else:
                                    print("valor no valido")

                        if menu == 2:
                            agenda = Agendas()
                            while var_control2 == True:
                                print('Ingrese "1" para crear cita')
                                print('Ingrese "2" para buscar cita')
                                print('Ingrese "3" para cancelar cita')
                                print('Ingrese "0" para salir al menu principal')
                                menu2 = int(input("Ingrese la opcion a elegir: "))
                                if menu2 == 1:
                                    agenda.crear_cita()
                                elif menu2 == 2:
                                    agenda.consultar_cita()
                                elif menu2 == 3:
                                    agenda.cancelar_cita()
                                elif menu2 == 0:
                                    print("Regresando al menu principal")
                                    var_control2 = False
                                    del agenda
                                else:
                                    print("valor no valido")
                        if menu == 3:
                            while var_control2 == True:
                                print('Ingrese "1" para consultar usuarios')
                                print('Ingrese "0" para salir al menu principal')
                                menu2 = int(input("Ingrese la opcion a elegir: "))
                                if menu2 == 1:
                                    recepcionista.consultar_usuarios()
                                elif menu2 == 0:
                                    print("Regresando al menu principal")
                                    var_control2 = False
                                else:
                                    print("valor no valido")
                        if menu ==0:
                            var_control = False

                        else:
                            print("Valor ingresado no valido")
                else:
                    empleado = Trabajadores(usuario[2], usuario[3], int(usuario[0]), usuario[1], int(usuario[4]), usuario[5], usuario[6], usuario[7])
                    print("Hola Empleado")
                    while var_control == True :
                        print('Ingrese  1 para consultar agenda personal')
                        print("Ingrese 2 para inicializar cita")
                        print('Ingrese "0" para salir del programa')
                        menu = int(input("Ingrese la opcion a elegir: "))
                        if menu == 1:
                            empleado.consultar_agenda_personal()
                        elif menu == 2:
                            empleado.inicializar_finalizar_cita_()
                        elif menu ==0:
                            var_control = False
                        else:
                            print("Valor ingresado no valido")
            else:
                print("Contraseña incorrecta")
        else:
            print("El usuario no existe")
except psycopg2.Error as e:
    print("Ocurrio un error al consultar: ", e)

