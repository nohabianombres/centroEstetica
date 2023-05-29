from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import sys
from Front.cajero import *
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication
from Front.comunes.emerComunes import *
class Cajero(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Cajero, self).__init__(parent)
        uic.loadUi('Front/cajero/CajeroVenta.ui', self)

        self.botFacCaj.clicked.connect(self.open_view_caj)
        self.botInvCaj.clicked.connect(self.open_view_caj)

        self.cajInventavio = None
        self.cajFactu = None

    def open_view_caj(self):
        sender_button_Caj = self.sender()

        if sender_button_Caj == self.botInvCaj:
            self.hide()
            self.cajInventavio = CajeroInventario()
            self.cajInventavio.show()
        elif sender_button_Caj == self.botFacCaj:
            self.hide()
            self.cajFactu = CajeroFacturacion()
            self.cajFactu.show()


class CajeroFacturacion(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(CajeroFacturacion, self).__init__(parent)
        uic.loadUi('Front/cajero/CajeroFacturacion.ui', self)

        self.botFacCaj.clicked.connect(self.open_view_caj_fac)
        self.botInvCaj.clicked.connect(self.open_view_caj_fac)
        self.cajInventavio = None
        self.cajFactu = None

    def open_view_caj_fac(self):
        sender_button_Caj_fac = self.sender()

        if sender_button_Caj_fac == self.botInvCaj:
            self.hide()
            self.cajInventavio = CajeroInventario()
            self.cajInventavio.show()
        elif sender_button_Caj_fac == self.botFacCaj:
            self.hide()
            self.cajFactu = CajeroFacturacion()
            self.cajFactu.show()


class CajeroInventario(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(CajeroInventario, self).__init__(parent)
        uic.loadUi('Front/cajero/CajeroInventario.ui', self)

        self.botFacCaj.clicked.connect(self.open_view_caj_inv)
        self.botInvCaj.clicked.connect(self.open_view_caj_inv)
        self.botBusProCaj.clicked.connect(self.open_view_eme_BusPro)
        self.botMosTodCaj.clicked.connect(self.open_view_eme_MosTod)

        self.cajInventavio = None
        self.cajFactu = None

    def open_view_caj_inv(self):
        sender_button_Caj_inv = self.sender()

        if sender_button_Caj_inv == self.botInvCaj:
            self.hide()
            self.cajInventavio = CajeroInventario()
            self.cajInventavio.show()
        elif sender_button_Caj_inv == self.botFacCaj:
            self.hide()
            self.cajFactu = CajeroFacturacion()
            self.cajFactu.show()

    def open_view_eme_BusPro(self):
        self.BusPro = emerBuscPro()
        self.BusPro.show()

    def open_view_eme_MosTod(self):
        pass
