from Back.Clientes import *
from Back.Facturas import *
from Back.Informes import *
from Back.Servicios import *
from Back.Usuarios import *
from Back.Inventario import *
from BD.Conexion import *
from Back.Agenda import *
import psycopg2
from Front.administrador.ventanasAdmin import *
from Front.recepcionista.ventanasRecepcionista import *
from Front.administrador.emeAdm.emeAdmcodigo import *
from Front.comunes.emerComunes import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import sys
from PyQt5 import QtWidgets, uic
from Front.cajero.ventanasCajero import *
from Front.trabajador.ventanasTrabajador import *
basedatos = Database("postgres", "00112233", "centroestetica.ccwkcz7cjsk2.us-east-2.rds.amazonaws.com")
conexion = basedatos.conectar()


def validacion(user_log, contrasena_log, instancia_log):
    print('hpta que chimba')
    print(user_log)
    var_control = True
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM usuario WHERE usuario = " + str(user_log))
            usuario = cursor.fetchone()
            if usuario:
                usuario_contrasena = usuario[1]
                if usuario_contrasena == contrasena_log:
                    rol_usuario = usuario[7]
                else:
                    print('hpta')
            else:
                print('gonorrea')
    except psycopg2.Error as e:
        print("Ocurrio un error al consultar: ", e)

    return rol_usuario

class Login(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        uic.loadUi('Front/login.ui', self)
        self.BorraPrograma.clicked.connect(self.borrar)
        self.BotEntrar.clicked.connect(self.obtener_datos)

    def obtener_datos (self):
        print('entre')
        self.user = self.VarUsu.text()
        self.contrasena = self.VarPass.text()
        usuario_validacion = validacion(self.user, self.contrasena, login)


        if usuario_validacion == 'Admin':
            self.open_view_adm()
        elif usuario_validacion == 'Recepcion':
            self.open_view_rec()
        elif usuario_validacion == 'Cajero':
            self.open_view_caj()
        else:
            print('voy en el if')
            self.open_view_tra()

    def borrar(self):
        for line_edit in self.findChildren(QtWidgets.QLineEdit):
            line_edit.clear()

    def open_view_rec(self):
        print('entre rec')
        self.close()
        self.hide()
        self.recepcionista = Recepcionista()
        self.recepcionista.show()

    def open_view_adm(self):
        self.close()
        self.hide()
        self.admin = Admin()
        self.admin.show()

    def open_view_caj(self):
        self.close()
        self.hide()
        self.cajero = Cajero()
        self.cajero.show()

    def open_view_tra(self):
        print('llegue a la funcion')
        self.close()
        self.hide()
        self.trabajador_ins = TrabajadorVentana()
        self.trabajador_ins.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec_())

'''
def escoger ventana():
                    if rol_usuario == "Admin":
                        instancia_log.open_view_adm()
                        administrador = Administracion(usuario[2], usuario[3], int(usuario[0]), usuario[1],
                                                       int(usuario[4]), usuario[5], usuario[6], usuario[7])

                        while var_control == True:
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
                            if menu == 0:
                                var_control = False

                            else:
                                print("Valor ingresado no valido")

                    elif rol_usuario == "Cajero":
                        cajero = Cajero(usuario[2], usuario[3], int(usuario[0]), usuario[1], int(usuario[4]),
                                        usuario[5], usuario[6], usuario[7])
                        print("Hola cajero")
                        while var_control == True:
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
                            if menu == 0:
                                var_control = False

                    elif rol_usuario == "Recepcion":
                        recepcionista = Recepcion(usuario[2], usuario[3], int(usuario[0]), usuario[1], int(usuario[4]),
                                                  usuario[5], usuario[6], usuario[7])
                        print("Hola Recepcion")
                        while var_control == True:
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
                            if menu == 0:
                                var_control = False

                            else:
                                print("Valor ingresado no valido")
                    else:
                        empleado = Trabajadores(usuario[2], usuario[3], int(usuario[0]), usuario[1], int(usuario[4]),
                                                usuario[5], usuario[6], usuario[7])
                        print("Hola Empleado")
                        while var_control == True:
                            print('Ingrese  1 para consultar agenda personal')
                            print("Ingrese 2 para inicializar cita")
                            print('Ingrese "0" para salir del programa')
                            menu = int(input("Ingrese la opcion a elegir: "))
                            if menu == 1:
                                empleado.consultar_agenda_personal()
                            elif menu == 2:
                                empleado.inicializar_finalizar_cita_()
                            elif menu == 0:
                                var_control = False
                            else:
                                print("Valor ingresado no valido")
                else:
                    print("Contraseña incorrecta")
            else:
                print("El usuario no existe")
    except psycopg2.Error as e:
        print("Ocurrio un error al consultar: ", e)'''



















'''class Login(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Login, self).__init__(*args, **kwargs)
        uic.loadUi('Front/login.ui', self)
        self.BorraPrograma.clicked.connect(self.borrar)
        self.BotEntrar.clicked.connect(self.open_view)

    def borrar(self):
        for line_edit in self.findChildren(QtWidgets.QLineEdit):
            line_edit.clear()

    def open_view(self):
        self.close()
        self.admin = Admin()
        self.admin.show()
        del login


class Admin(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Admin, self).__init__(*args, **kwargs)
        uic.loadUi('Front/administrador/Admin.ui', self)
        self.botInvAdm.clicked.connect(self.open_view)
        self.botSerAdm.clicked.connect(self.open_view)
        self.botFacAdm.clicked.connect(self.open_view)
        self.botCliAdm.clicked.connect(self.open_view)
        self.botAgenAdm.clicked.connect(self.open_view)
        self.botAgenAdm.clicked.connect(self.open_view)

    def open_view(self):
        self.close()
        self.adInventario = AdminInventario()
        self.adInventario.show()

    def open_view_sevicios(self):
        self.close()
        self.adServicios = AdminServicio()
        self.adServicios.show()


class AdminAgenda(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(AdminAgenda, self).__init__(parent)
        uic.loadUi('Front/administrador/adminAgenda', self)


class AdminFacturacion(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(AdminFacturacion, self).__init__(parent)
        uic.loadUi('Front/administrador/adminFacturacion.ui', self)


class AdminInforme(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(AdminInforme, self).__init__(parent)
        uic.loadUi('Front/administrador/adminInformes.ui', self)


class AdminInventario(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(AdminInventario, self).__init__(parent)
        uic.loadUi('Front/administrador/adminInventario.ui', self)


class AdminServicio(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(AdminServicio, self).__init__(parent)
        uic.loadUi('Front/administrador/adminSevicios.ui', self)


class AdminUsuario(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(AdminUsuario, self).__init__(parent)
        uic.loadUi('Front/administrador/adminUsuarios.ui', self)


class EmergenteModificarProducto(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(EmergenteModificarProducto, self).__init__(parent)
        uic.loadUi('Front/emerModPro.ui', self)


login = Login()
login.show()
app.exec_()'''
