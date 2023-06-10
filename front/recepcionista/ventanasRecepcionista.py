from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication
from Front.comunes.emerComunes import emerRetorno, emerBuscUsu, emerAgrCli, emerBuscSer, emerAgrCita, emerCanCitaId, emerBusCitas,  emerBuscClien, emerCanCita, emerAdiFal
from Back.Usuarios import Recepcion

class Recepcionista(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Recepcionista, self).__init__(parent)
        uic.loadUi('Front/recepcionista/Recepcionista.ui', self)

        self.botAgeRec.clicked.connect(self.open_view_rec)
        self.botCliRec.clicked.connect(self.open_view_rec)
        self.botSerRec.clicked.connect(self.open_view_rec)
        self.botUsuRec.clicked.connect(self.open_view_rec)

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

class RecepcionistaClientes(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(RecepcionistaClientes, self).__init__(parent)
        uic.loadUi('Front/recepcionista/RecepcionistaClientes.ui', self)

        self.botAgeRec.clicked.connect(self.open_view_rec_cli)
        self.botCliRec.clicked.connect(self.open_view_rec_cli)
        self.botSerRec.clicked.connect(self.open_view_rec_cli)
        self.botUsuRec.clicked.connect(self.open_view_rec_cli)

        self.botAdiFalRec.clicked.connect(self.open_view_eme_AdcFal)
        self.botAgrCliRec.clicked.connect(self.open_view_eme_AgrCli)
        self.botBusCliRec.clicked.connect(self.open_view_eme_BusCli)


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
        self.BusCli.set_callback(self.imprimir_tablas)
        self.BusCli.show()

    def crear_ventana(self, retorno):
        self.emer_retorno = emerRetorno()
        self.emer_retorno.imprimir_retorno(retorno)
        self.emer_retorno.show()

    def imprimir_tablas(self):
        pass

    def recibir_datos(self, usuario_validar):
        self.datos_usuario = usuario_validar

class RecepcionistaAgenda(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(RecepcionistaAgenda, self).__init__(parent)
        uic.loadUi('Front/recepcionista/RecepcionistaAgendaventa.ui', self)

        self.botAgeRec.clicked.connect(self.open_view_rec_Age)
        self.botCliRec.clicked.connect(self.open_view_rec_Age)
        self.botSerRec.clicked.connect(self.open_view_rec_Age)
        self.botUsuRec.clicked.connect(self.open_view_rec_Age)

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
        self.BusCit.set_callback(self.imprimir_tablas)
        self.BusCit.show()

    def open_view_eme_ModCita(self):
        pass

    def open_view_eme_CanCita(self):
        self.CanCita = emerCanCita()
        self.CanCita.set_callback(self.open_view_emerIdCitCan)
        self.CanCita.show()

    def imprimir_tablas(self, listas):
        print('entre:')
        # self.ui.TabAgenda.clearContents()  # Limpiar contenido existente en la tabla
        # self.ui.TabAgenda.setRowCount()  # Reiniciar número de filas

        for lista in listas:
            print(lista)
            fila = self.ui.TabAgenda.rowCount()
            self.ui.TabAgenda.insertRow(fila)

            for columna, elemento in enumerate(lista):
                celda = QtWidgets.QTableWidgetItem(elemento)
                self.ui.TabAgenda.setItem(fila, columna, celda)

    def crear_ventana(self, retorno):
        self.emer_retorno = emerRetorno()
        self.emer_retorno.imprimir_retorno(retorno)
        self.emer_retorno.show()

    def open_view_emerIdCitCan(self, a):
        self.IdCitCan = emerCanCitaId()
        self.IdCitCan.set_callback(self.crear_ventana)
        self.IdCitCan.show()

    def recibir_datos(self, usuario_validar):
        self.datos_usuario = usuario_validar

class RecepcionistaServicios(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(RecepcionistaServicios, self).__init__(parent)
        uic.loadUi('Front/recepcionista/RecepcionistaServicios.ui', self)

        self.botAgeRec.clicked.connect(self.open_view_rec_Ser)
        self.botCliRec.clicked.connect(self.open_view_rec_Ser)
        self.botSerRec.clicked.connect(self.open_view_rec_Ser)
        self.botUsuRec.clicked.connect(self.open_view_rec_Ser)

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
        pass

    def crear_ventana(self, retorno):
        self.emer_retorno = emerRetorno()
        self.emer_retorno.imprimir_retorno(retorno)
        self.emer_retorno.show()

    def imprimir_tabla(self):
        pass

    def recibir_datos (self, usuario_validar):
        self.datos_usuario = usuario_validar

class RecepcionistaUsuarios(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(RecepcionistaUsuarios, self).__init__(parent)
        uic.loadUi('Front/recepcionista/RecepcionistaUsuarios.ui', self)

        self.botAgeRec.clicked.connect(self.open_view_rec_usu)
        self.botCliRec.clicked.connect(self.open_view_rec_usu)
        self.botSerRec.clicked.connect(self.open_view_rec_usu)
        self.botUsuRec.clicked.connect(self.open_view_rec_usu)
        self.botBusUsu.clicked.connect(self.open_view_emer_bus_usu)

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

    def imprimir_tablas(self):
        pass

    def recibir_datos(self, usuario_validar):
        self.datos_usuario = usuario_validar
        print(self.datos_usuario)
        self.ins_recepcionista = Recepcion(usuario_validar[0], usuario_validar[1], usuario_validar[2], usuario_validar[3], usuario_validar[4], usuario_validar[5], usuario_validar[6], usuario_validar[7])
