from PyQt5.QtWidgets import QApplication, QMainWindow

import sys
from Front.cajero import *
from Front.comunes.emerComunes import emerRetorno, emerBuscPro, emerAgrCli, emerBusFac, emerCreFac, emerPagFacId, emerPagFacDoc, emerBuscClien, emerAdiFal
from Back.Inventario import Inventario
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication

class Cajero(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(Cajero, self).__init__(parent)
        uic.loadUi('Front/cajero/CajeroVenta.ui', self)

        self.botCliCaj.clicked.connect(self.open_view_caj)
        self.botFacCaj.clicked.connect(self.open_view_caj)
        self.botInvCaj.clicked.connect(self.open_view_caj)
        self.botCerCaj.clicked.connect(self.cerrar_sesion)

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

    def cerrar_sesion(self):
        quit()

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
        self.botCerCaj.clicked.connect(self.cerrar_sesion)

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

    def cerrar_sesion(self):
        quit()

class CajeroInventario(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(CajeroInventario, self).__init__(parent)
        uic.loadUi('Front/cajero/CajeroInventario.ui', self)

        self.botCliCaj.clicked.connect(self.open_view_caj_inv)
        self.botFacCaj.clicked.connect(self.open_view_caj_inv)
        self.botInvCaj.clicked.connect(self.open_view_caj_inv)
        self.botBusPro.clicked.connect(self.open_view_eme_BusPro)
        self.botMosPro.clicked.connect(self.open_view_eme_MosTodPro)
        self.botCerCaj.clicked.connect(self.cerrar_sesion)

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
        self.BusPro.set_callback(self.imprimir_tabla_filas)
        self.BusPro.show()

    def open_view_eme_MosTodPro(self):
        self.inventario = Inventario()
        self.ret_inv = self.inventario.consultar_inverntario()
        self.imprimir_tabla(self.ret_inv)

    def crear_ventana(self, retorno):
        self.emer_retorno = emerRetorno()
        self.emer_retorno.imprimir_retorno(retorno)
        self.emer_retorno.show()

    def imprimir_tabla_filas(self, listas):
        self.TabInventario.clearContents()
        print(listas)
        self.TabInventario.show()
        if listas != None:
            fila = 0
            self.TabInventario.setRowCount(len(listas))
            for elementos in listas:
                print(elementos)
                self.TabInventario.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(elementos[0])))
                self.TabInventario.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(elementos[1])))
                self.TabInventario.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(elementos[2])))
                self.TabInventario.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(elementos[3])))
                fila = fila + 1
        else:
            print('no encontre')

    def imprimir_tabla(self, lista):
        self.TabInventario.clearContents()
        self.TabInventario.show()
        if lista != None:
            fila = 0
            self.TabInventario.setRowCount(len(lista))
            self.TabInventario.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(lista[0])))
            self.TabInventario.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(lista[1])))
            self.TabInventario.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(lista[2])))
            self.TabInventario.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(lista[3])))
        else:
            print('no encontre')


    def recibir_datos(self, usuario_validar):
        self.datos_usuario = usuario_validar

    def cerrar_sesion(self):
        quit()

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
        self.botCerCaj.clicked.connect(self.cerrar_sesion)

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
