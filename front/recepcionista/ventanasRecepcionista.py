
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication
from Front.comunes.emerComunes import emerRetorno, emerBuscUsu, emerAgrCli, emerBuscSer, emerAgrCita, emerCanCitaId, emerBusCitas,  emerBuscClien, emerCanCita, emerAdiFal
from Back.Usuarios import Recepcion
from Back.Servicios import Servicios

class Recepcionista(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Recepcionista, self).__init__(parent)
        uic.loadUi('Front/recepcionista/Recepcionista.ui', self)

        self.botAgeRec.clicked.connect(self.open_view_rec)
        self.botCliRec.clicked.connect(self.open_view_rec)
        self.botSerRec.clicked.connect(self.open_view_rec)
        self.botUsuRec.clicked.connect(self.open_view_rec)
        self.botCerRec.clicked.connect(self.cerrar_sesion)

        self.recServicios = None
        self.recAgenda = None
        self.recUsuarios = None
        self.recClientes = None

    def open_view_rec(self):

        sender_button_rec = self.sender()
        if sender_button_rec == self.botSerRec:
            self.hide()
            self.recServicios = RecepcionistaServicios()
            self.recServicios.recibir_datos(self.datos_usuario)
            self.recServicios.show()
        elif sender_button_rec == self.botUsuRec:
            self.hide()
            self.recUsuarios = RecepcionistaUsuarios()
            self.recUsuarios.recibir_datos(self.datos_usuario)
            self.recUsuarios.show()
        elif sender_button_rec == self.botAgeRec:
            self.hide()
            self.recAgenda = RecepcionistaAgenda()
            self.recAgenda.recibir_datos(self.datos_usuario)
            self.recAgenda.show()
        elif sender_button_rec == self.botCliRec:
            self.hide()
            self.recClientes = RecepcionistaClientes()
            self.recClientes.recibir_datos(self.datos_usuario)
            self.recClientes.show()

    def recibir_datos (self, usuario_validar):
        self.datos_usuario = usuario_validar

    def cerrar_sesion(self):
        quit()


class RecepcionistaClientes(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(RecepcionistaClientes, self).__init__(parent)
        uic.loadUi('Front/recepcionista/RecepcionistaClientes.ui', self)

        self.botAgeRec.clicked.connect(self.open_view_rec_cli)
        self.botCliRec.clicked.connect(self.open_view_rec_cli)
        self.botSerRec.clicked.connect(self.open_view_rec_cli)
        self.botUsuRec.clicked.connect(self.open_view_rec_cli)

        self.botAdcFalRec.clicked.connect(self.open_view_eme_AdcFal)
        self.botAgrCliRec.clicked.connect(self.open_view_eme_AgrCli)
        self.botBusCliRec.clicked.connect(self.open_view_eme_BusCli)
        self.botCerRec.clicked.connect(self.cerrar_sesion)


        self.recServicios = None
        self.recAgenda = None
        self.recUsuarios = None
        self.recClientes = None

    def open_view_rec_cli(self):
        sender_button_rec_cli = self.sender()
        if sender_button_rec_cli == self.botSerRec:
            self.hide()
            self.recServicios = RecepcionistaServicios()
            self.recServicios.recibir_datos(self.datos_usuario)
            self.recServicios.show()
        elif sender_button_rec_cli == self.botUsuRec:
            self.hide()
            self.recUsuarios = RecepcionistaUsuarios()
            self.recUsuarios.recibir_datos(self.datos_usuario)
            self.recUsuarios.show()
        elif sender_button_rec_cli == self.botAgeRec:
            self.hide()
            self.recAgenda = RecepcionistaAgenda()
            self.recAgenda.recibir_datos(self.datos_usuario)
            self.recAgenda.show()
        elif sender_button_rec_cli == self.botCliRec:
            self.hide()
            self.recClientes = RecepcionistaClientes()
            self.recClientes.recibir_datos(self.datos_usuario)
            self.recClientes.show()

    def open_view_eme_AdcFal(self):
        self.AdcFal = emerAdiFal()
        self.AdcFal.set_callback(self.crear_ventana)
        self.AdcFal.show()

    def open_view_eme_AgrCli(self):
        self.AgrCli = emerAgrCli()
        self.AgrCli.set_callback(self.crear_ventana)
        self.AgrCli.show()

    def open_view_eme_BusCli(self):
        self.BusCli = emerBuscClien()
        self.BusCli.set_callback(self.imprimir_tabla)
        self.BusCli.show()

    def crear_ventana(self, retorno):
        self.emer_retorno = emerRetorno()
        self.emer_retorno.imprimir_retorno(retorno)
        self.emer_retorno.show()

    def imprimir_tabla(self, listas):
        self.TabClientes.clearContents()
        self.TabClientes.show()
        if listas != None:
            fila = 0
            self.TabClientes.setRowCount(len(listas))
            self.TabClientes.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(listas[0])))
            self.TabClientes.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(listas[1])))
            self.TabClientes.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(listas[2])))
            self.TabClientes.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(listas[3])))
            self.TabClientes.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(listas[4])))
            self.TabClientes.setItem(fila, 5, QtWidgets.QTableWidgetItem(str(listas[5])))
            self.TabClientes.setItem(fila, 6, QtWidgets.QTableWidgetItem(str(listas[6])))
        else:
            print('no encontre')

    def recibir_datos(self, usuario_validar):
        self.datos_usuario = usuario_validar

    def cerrar_sesion(self):
        quit()

class RecepcionistaAgenda(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(RecepcionistaAgenda, self).__init__(parent)
        uic.loadUi('Front/recepcionista/RecepcionistaAgendaventa.ui', self)

        self.botAgeRec.clicked.connect(self.open_view_rec_Age)
        self.botCliRec.clicked.connect(self.open_view_rec_Age)
        self.botSerRec.clicked.connect(self.open_view_rec_Age)
        self.botUsuRec.clicked.connect(self.open_view_rec_Age)
        self.botCerRec.clicked.connect(self.cerrar_sesion)

        self.botBusCitRec.clicked.connect(self.open_view_eme_BusCita)
        self.botCanCitRec.clicked.connect(self.open_view_eme_CanCita)
        self.botCreCitRec.clicked.connect(self.open_view_eme_AgrCit)



        self.recServicios = None
        self.recAgenda = None
        self.recUsuarios = None
        self.recClientes = None

    def open_view_rec_Age(self):

        sender_button_rec_age = self.sender()
        if sender_button_rec_age == self.botSerRec:
            self.hide()
            self.recServicios = RecepcionistaServicios()
            self.recServicios.recibir_datos(self.datos_usuario)
            self.recServicios.show()
        elif sender_button_rec_age == self.botUsuRec:
            self.hide()
            self.recUsuarios = RecepcionistaUsuarios()
            self.recUsuarios.recibir_datos(self.datos_usuario)
            self.recUsuarios.show()
        elif sender_button_rec_age == self.botAgeRec:
            self.hide()
            self.recAgenda = RecepcionistaAgenda()
            self.recAgenda.recibir_datos(self.datos_usuario)
            self.recAgenda.show()
        elif sender_button_rec_age == self.botCliRec:
            self.hide()
            self.recClientes = RecepcionistaClientes()
            self.recClientes.recibir_datos(self.datos_usuario)
            self.recClientes.show()



    def open_view_eme_AgrCit(self):
        self.AgrCit = emerAgrCita()
        self.AgrCit.set_callback(self.crear_ventana)
        self.AgrCit.show()

    def open_view_eme_BusCita(self):
        self.BusCit = emerBusCitas()
        self.BusCit.set_callback(self.imprimir_tabla_filas)
        self.BusCit.show()

    def open_view_eme_CanCita(self):
        self.CanCita = emerCanCitaId()
        self.CanCita.set_callback(self.crear_ventana)
        self.CanCita.show()

    def imprimir_tabla_filas(self, listas):
        self.TabAgenda.clearContents()
        print(listas)
        self.TabAgenda.show()
        if listas != None:
            fila = 0
            self.TabAgenda.setRowCount(len(listas))
            for elementos in listas:
                print(elementos)
                self.TabAgenda.setItem(fila, 0, QtWidgets.QTableWidgetItem((str(elementos[0]))))
                self.TabAgenda.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(elementos[1].strftime("%H:%M"))))
                self.TabAgenda.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(elementos[2].strftime("%Y-%m-%d"))))
                self.TabAgenda.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(elementos[3])))
                self.TabAgenda.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(elementos[4])))
                self.TabAgenda.setItem(fila, 5, QtWidgets.QTableWidgetItem(str(elementos[5])))
                self.TabAgenda.setItem(fila, 6, QtWidgets.QTableWidgetItem(str(elementos[6])))
                self.TabAgenda.setItem(fila, 7, QtWidgets.QTableWidgetItem(str(elementos[7])))
                self.TabAgenda.setItem(fila, 8, QtWidgets.QTableWidgetItem(str(elementos[8])))
                self.TabAgenda.setItem(fila, 9, QtWidgets.QTableWidgetItem(str(elementos[9])))
                fila = fila + 1
            return listas
        else:
            print('no encontre')



    def crear_ventana(self, retorno):
        self.emer_retorno = emerRetorno()
        self.emer_retorno.imprimir_retorno(retorno)
        self.emer_retorno.show()

    def open_view_emerIdCitCan(self,a):
        self.CanCita.hide()
        self.IdCitCan = emerCanCitaId ()
        self.IdCitCan.set_callback(self.crear_ventana)
        self.IdCitCan.show()

    def recibir_datos (self, usuario_validar):
        self.datos_usuario = usuario_validar

    def cerrar_sesion (self):
        quit()


class RecepcionistaServicios(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(RecepcionistaServicios, self).__init__(parent)
        uic.loadUi('Front/recepcionista/RecepcionistaServicios.ui', self)

        self.botAgeRec.clicked.connect(self.open_view_rec_Ser)
        self.botCliRec.clicked.connect(self.open_view_rec_Ser)
        self.botSerRec.clicked.connect(self.open_view_rec_Ser)
        self.botUsuRec.clicked.connect(self.open_view_rec_Ser)
        self.botCerRec.clicked.connect(self.cerrar_sesion)

        self.botBusSerRec.clicked.connect(self.open_view_eme_BusSer)
        self.botMosTodRec.clicked.connect(self.open_view_eme_MosTodSer)

        self.recServicios = None
        self.recAgenda = None
        self.recUsuarios = None
        self.recClientes = None

    def open_view_rec_Ser(self):

        sender_button_rec_age = self.sender()
        if sender_button_rec_age == self.botSerRec:
            self.hide()
            self.recServicios = RecepcionistaServicios()
            self.recServicios.recibir_datos(self.datos_usuario)
            self.recServicios.show()
        elif sender_button_rec_age == self.botUsuRec:
            self.hide()
            self.recUsuarios = RecepcionistaUsuarios()
            self.recUsuarios.recibir_datos(self.datos_usuario)
            self.recUsuarios.show()
        elif sender_button_rec_age == self.botAgeRec:
            self.hide()
            self.recAgenda = RecepcionistaAgenda()
            self.recAgenda.recibir_datos(self.datos_usuario)
            self.recAgenda.show()
        elif sender_button_rec_age == self.botCliRec:
            self.hide()
            self.recClientes = RecepcionistaClientes()
            self.recClientes.recibir_datos(self.datos_usuario)
            self.recClientes.show()

    def open_view_eme_BusSer(self):
        self.BusSer = emerBuscSer()
        self.BusSer.set_callback(self.imprimir_tabla)
        self.BusSer.show()

    def open_view_eme_MosTodSer(self):
        self.servicio = Servicios()
        ser_com = self.servicio.consultar_servicios()
        self.imprimir_tabla_filas(ser_com)

    def crear_ventana(self, retorno):
        self.emer_retorno = emerRetorno()
        self.emer_retorno.imprimir_retorno(retorno)
        self.emer_retorno.show()

    def imprimir_tabla_filas(self, listas):
        self.TabServicios.clearContents()
        print(listas)
        self.TabServicios.show()
        if listas != None:
            fila = 0
            self.TabServicios.setRowCount(len(listas))
            for elementos in listas:
                print(elementos)
                self.TabServicios.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(elementos[0])))
                self.TabServicios.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(elementos[1])))
                self.TabServicios.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(elementos[2])))
                self.TabServicios.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(elementos[3])))
                fila = fila + 1
        else:
            print('no encontre')

    def imprimir_tabla(self, lista):
        self.TabServicios.clearContents()
        self.TabServicios.show()
        if lista != None:
            fila = 0
            self.TabServicios.setRowCount(len(lista))
            self.TabServicios.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(lista[0])))
            self.TabServicios.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(lista[1])))
            self.TabServicios.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(lista[2])))
            self.TabServicios.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(lista[3])))

        else:
            print('no encontre')

    def recibir_datos (self, usuario_validar):
        self.datos_usuario = usuario_validar

    def cerrar_sesion(self):
        quit()


class RecepcionistaUsuarios(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(RecepcionistaUsuarios, self).__init__(parent)
        uic.loadUi('Front/recepcionista/RecepcionistaUsuarios.ui', self)

        self.botAgeRec.clicked.connect(self.open_view_rec_usu)
        self.botCliRec.clicked.connect(self.open_view_rec_usu)
        self.botSerRec.clicked.connect(self.open_view_rec_usu)
        self.botUsuRec.clicked.connect(self.open_view_rec_usu)
        self.botBusUsu.clicked.connect(self.open_view_emer_bus_usu)
        self.botCerRec.clicked.connect(self.cerrar_sesion)
        self.botMosTod.clicked.connect(self.open_view_MosTod)

        self.recServicios = None
        self.recAgenda = None
        self.recUsuarios = None
        self.recClientes = None

    def open_view_rec_usu(self):
        sender_button_rec_usu = self.sender()
        if sender_button_rec_usu == self.botSerRec:
            self.hide()
            self.recServicios = RecepcionistaServicios()
            self.recServicios.recibir_datos(self.datos_usuario)
            self.recServicios.show()
        elif sender_button_rec_usu == self.botUsuRec:
            self.hide()
            self.recUsuarios = RecepcionistaUsuarios()
            self.recUsuarios.recibir_datos(self.datos_usuario)
            self.recUsuarios.show()
        elif sender_button_rec_usu == self.botAgeRec:
            self.hide()
            self.recAgenda = RecepcionistaAgenda()
            self.recAgenda.recibir_datos(self.datos_usuario)
            self.recAgenda.show()
        elif sender_button_rec_usu == self.botCliRec:
            self.hide()
            self.recClientes = RecepcionistaClientes()
            self.recClientes.recibir_datos(self.datos_usuario)
            self.recClientes.show()


    def open_view_emer_bus_usu(self):
        self.busUsu = emerBuscUsu()
        self.busUsu.set_callback(self.imprimir_tablas)
        self.busUsu.recibir_datos(self.datos_usuario)
        self.busUsu.show()

    def crear_ventana(self, retorno):
        self.emer_retorno = emerRetorno()
        self.emer_retorno.imprimir_retorno(retorno)
        self.emer_retorno.show()

    def open_view_MosTod(self):
        self.tod_usu = self.ins_recepcionista.consultar_usuarios()
        self.imprimir_tabla_filas(self.tod_usu)

    def imprimir_tabla_filas(self, listas):
        self.TabUsuarios.clearContents()
        self.TabUsuarios.show()
        if listas != None:
            fila = 0
            self.TabUsuarios.setRowCount(len(listas))
            for elementos in listas:
                print(elementos)
                self.TabUsuarios.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(elementos[0])))
                self.TabUsuarios.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(elementos[1])))
                self.TabUsuarios.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(elementos[2])))
                self.TabUsuarios.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(elementos[3])))
                self.TabUsuarios.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(elementos[4])))
                self.TabUsuarios.setItem(fila, 5, QtWidgets.QTableWidgetItem(str(elementos[5])))
                self.TabUsuarios.setItem(fila, 6, QtWidgets.QTableWidgetItem(str(elementos[6])))
                self.TabUsuarios.setItem(fila, 7, QtWidgets.QTableWidgetItem(str(elementos[7])))
                fila = fila + 1
        else:
            print('no encontre')

    def imprimir_tablas(self, listas):
        self.TabUsuarios.clearContents()
        self.TabUsuarios.show()
        if listas != None:
            fila = 0
            self.TabUsuarios.setRowCount(1)

            self.TabUsuarios.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(listas[0])))
            self.TabUsuarios.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(listas[1])))
            self.TabUsuarios.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(listas[2])))
            self.TabUsuarios.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(listas[3])))
            self.TabUsuarios.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(listas[4])))
            self.TabUsuarios.setItem(fila, 5, QtWidgets.QTableWidgetItem(str(listas[5])))
            self.TabUsuarios.setItem(fila, 6, QtWidgets.QTableWidgetItem(str(listas[6])))
            self.TabUsuarios.setItem(fila, 7, QtWidgets.QTableWidgetItem(str(listas[7])))

        else:
            print('no encontre')

    def recibir_datos(self, usuario_validar):
        self.datos_usuario = usuario_validar
        print(self.datos_usuario)
        self.ins_recepcionista = Recepcion(usuario_validar[0], usuario_validar[1], usuario_validar[2], usuario_validar[3], usuario_validar[4], usuario_validar[5], usuario_validar[6], usuario_validar[7])

    def cerrar_sesion(self):
        quit()
