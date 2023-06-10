from PyQt5.QtWidgets import QApplication, QMainWindow

import sys
from Front.cajero import *



from Front.comunes.emerComunes import emerRetorno, emerBuscPro, emerAgrCli, emerBusFac, emerCreFac, emerPagFacId, emerPagFacDoc, emerBuscClien, emerAdiFal

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication

class Cajero(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(Cajero, self).__init__(parent)
        uic.loadUi('Front/cajero/CajeroVenta.ui', self)

        self.botCliCaj.clicked.connect(self.open_view_caj)
        self.botFacCaj.clicked.connect(self.open_view_caj)
        self.botInvCaj.clicked.connect(self.open_view_caj)

        self.cajInventavio = None
        self.cajFactu = None

    def open_view_caj(self):
        sender_button_Caj = self.sender()
        if sender_button_Caj == self.botInvCaj:
            self.hide()
            self.cajInventavio = CajeroInventario()
            self.cajInventavio.recibir_datos(self.datos_usuario)
            self.cajInventavio.show()
        elif sender_button_Caj == self.botFacCaj:
            self.hide()
            self.cajFactu = CajeroFacturacion()
            self.cajFactu.recibir_datos(self.datos_usuario)
            self.cajFactu.show()
        elif sender_button_Caj == self.botCliCaj:
            self.hide()
            self.cajClien = CajeroClientes ()
            self.cajClien.recibir_datos(self.datos_usuario)
            self.cajClien.show()

    def recibir_datos (self, usuario_validar):
        self.datos_usuario = usuario_validar



class CajeroFacturacion(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(CajeroFacturacion, self).__init__(parent)
        uic.loadUi('Front/cajero/CajeroFacturacion.ui', self)

        self.botCliCaj.clicked.connect(self.open_view_caj_fac)
        self.botFacCaj.clicked.connect(self.open_view_caj_fac)
        self.botInvCaj.clicked.connect(self.open_view_caj_fac)

        self.botBusFacDoc.clicked.connect(self.open_view_eme_BusFac)
        self.botPagId.clicked.connect(self.open_view_eme_PagFacId)
        self.botPagDoc.clicked.connect(self.open_view_eme_PagFacDoc)
        self.botCreFac.clicked.connect(self.open_view_eme_CreFac)

        self.cajInventavio = None
        self.cajFactu = None

    def open_view_caj_fac(self):
        sender_button_Caj_fac = self.sender()

        if sender_button_Caj_fac == self.botInvCaj:
            self.hide()
            self.cajInventavio = CajeroInventario()
            self.cajInventavio.recibir_datos(self.datos_usuario)
            self.cajInventavio.show()
        elif sender_button_Caj_fac == self.botFacCaj:
            self.hide()
            self.cajFactu = CajeroFacturacion()
            self.cajFactu.recibir_datos(self.datos_usuario)
            self.cajFactu.show()
        elif sender_button_Caj_fac == self.botCliCaj:
            self.hide()
            self.cajClien = CajeroClientes ()
            self.cajClien.recibir_datos(self.datos_usuario)
            self.cajClien.show()

    def open_view_eme_CreFac(self):
        self.CreFac = emerCreFac ()
        self.CreFac.set_callback(self.crear_ventana)
        self.CreFac.show()

    def open_view_eme_PagFacId(self):
        self.PagFacId = emerPagFacId()
        self.PagFacId.set_callback(self.crear_ventana)
        self.PagFacId.show()

    def open_view_eme_PagFacDoc(self):
        self.PagFacDoc = emerPagFacDoc()
        self.PagFacDoc.set_callback(self.crear_ventana)
        self.PagFacDoc.show()

    def open_view_eme_BusFac(self):
        self.BusFac = emerBusFac ()
        self.BusFac.set_callback(self.imprimir_tablas)
        self.BusFac.show()

    def crear_ventana(self, retorno):
        self.emer_retorno = emerRetorno()
        self.emer_retorno.imprimir_retorno(retorno)
        self.emer_retorno.show()

    def imprimir_tablas (self,listas):
        pass

    def recibir_datos (self, usuario_validar):
        self.datos_usuario = usuario_validar


class CajeroInventario(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(CajeroInventario, self).__init__(parent)
        uic.loadUi('Front/cajero/CajeroInventario.ui', self)

        self.botCliCaj.clicked.connect(self.open_view_caj_inv)
        self.botFacCaj.clicked.connect(self.open_view_caj_inv)
        self.botInvCaj.clicked.connect(self.open_view_caj_inv)
        self.botBusPro.clicked.connect(self.open_view_eme_BusPro)
        self.botMosPro.clicked.connect(self.open_view_eme_MosTodPro)

        self.cajInventavio = None
        self.cajFactu = None

    def open_view_caj_inv(self):
        sender_button_Caj_inv = self.sender()

        if sender_button_Caj_inv == self.botInvCaj:
            self.hide()
            self.cajInventavio = CajeroInventario()
            self.cajInventavio.recibir_datos(self.datos_usuario)
            self.cajInventavio.show()
        elif sender_button_Caj_inv == self.botFacCaj:
            self.hide()
            self.cajFactu = CajeroFacturacion()
            self.cajFactu.recibir_datos(self.datos_usuario)
            self.cajFactu.show()

        elif sender_button_Caj_inv == self.botCliCaj:
            self.hide()
            self.cajClien = CajeroClientes()
            self.cajClien.recibir_datos(self.datos_usuario)
            self.cajClien.show()

    def open_view_eme_BusPro(self):
        self.BusPro = emerBuscPro()
        self.BusPro.set_callback(self.imprimir_tabla)
        self.BusPro.show()

    def open_view_eme_MosTodPro(self):
        pass

    def crear_ventana(self, retorno):
        self.emer_retorno = emerRetorno()
        self.emer_retorno.imprimir_retorno(retorno)
        self.emer_retorno.show()

    def imprimir_tabla(self, listas):
        pass

    def recibir_datos(self, usuario_validar):
        self.datos_usuario = usuario_validar



class CajeroClientes(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(CajeroClientes, self).__init__(parent)
        uic.loadUi('Front/cajero/CajeroClientes.ui', self)

        self.botBusCli.clicked.connect(self.open_view_eme_BusCli)
        self.botAdcFal.clicked.connect(self.open_view_eme_AdcFal)
        self.botAgrCli.clicked.connect(self.open_view_eme_AgrCli)
        self.botCliCaj.clicked.connect(self.open_view_caj_cli)
        self.botFacCaj.clicked.connect(self.open_view_caj_cli)
        self.botInvCaj.clicked.connect(self.open_view_caj_cli)

        self.cajInventavio = None
        self.cajFactu = None
        self.cajClien = None

    def open_view_caj_cli(self):
        sender_button_Caj_cli = self.sender()

        if sender_button_Caj_cli == self.botInvCaj:
            self.hide()
            self.cajInventavio = CajeroInventario()
            self.cajInventavio.recibir_datos(self.datos_usuario)
            self.cajInventavio.show()
        elif sender_button_Caj_cli == self.botFacCaj:
            self.hide()
            self.cajFactu = CajeroFacturacion()
            self.cajFactu.recibir_datos(self.datos_usuario)
            self.cajFactu.show()
        elif sender_button_Caj_cli == self.botCliCaj:
            self.hide()
            self.cajClien = CajeroClientes()
            self.cajClien.recibir_datos(self.datos_usuario)
            self.cajClien.show()


    def open_view_eme_AdcFal(self):
        self.AdcFal = emerAdiFal()
        self.AdcFal.set_callback(self.crear_ventana)
        self.AdcFal.show()

    def open_view_eme_AgrCli(self):
        self.AgrCli = emerAgrCli()
        self.AgrCli.set_callback(self.crear_ventana)
        self.AgrCli.show()

    def open_view_eme_BusCli(self):
        print('llegue')
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
