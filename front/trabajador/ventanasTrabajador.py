from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication
from Front.comunes.emerComunes import *

class TrabajadorVentana(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(TrabajadorVentana, self).__init__(parent)
        uic.loadUi('Front/trabajador/Trabajador.ui', self)

        self.botAgenPers.clicked.connect(self.open_view_tra_2)
        self.borSerProc.clicked.connect(self.open_view_tra_2)

        self.traAgenda = None
        self.traSerPro = None

    def open_view_tra_2(self):
        sender_button_tra_2 = self.sender()
        if sender_button_tra_2 == self.botAgenPers:
            self.hide()
            self.traAgenda = TrabajadorAgenda()
            self.traAgenda.show()
        elif sender_button_tra_2 == self.botSerProc:
            self.hide()
            self.traSerPro = TrabajadorProceso()
            self.traSerPro.show()

class TrabajadorAgenda(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(TrabajadorAgenda, self).__init__(parent)
        uic.loadUi('Front/trabajador/TrabajadorAgenda.ui', self)

        self.botAgenPers.clicked.connect(self.open_view_tra_age)
        self.borSerProc.clicked.connect(self.open_view_tra_age)

        self.traAgenda = None
        self.traSerPro = None

    def open_view_tra_age(self):
        sender_button_tra_age = self.sender()
        if sender_button_tra_age == self.botAgenPers:
            self.hide()
            self.traAgenda = TrabajadorAgenda()
            self.traAgenda.show()
        elif sender_button_tra_age == self.botSerProc:
            self.hide()
            self.traSerPro = TrabajadorProceso()
            self.traSerPro.show()

class TrabajadorProceso(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(TrabajadorProceso, self).__init__(parent)
        uic.loadUi('Front/trabajador/TrabajadorProceso.ui', self)

        self.botAgenPers.clicked.connect(self.open_view_tra_pro)
        self.borSerProc.clicked.connect(self.open_view_tra_pro)
        self.botSerProc_2.clicked.connect(self.open_view_eme_SerPro)

        self.traAgenda = None
        self.traSerPro = None

    def open_view_tra_pro(self):
        sender_button_tra_pro = self.sender()

        if sender_button_tra_pro == self.botAgenPers:
            self.hide()
            self.traAgenda = TrabajadorAgenda()
            self.traAgenda.show()
        elif sender_button_tra_pro == self.botSerProc:
            self.hide()
            self.traSerPro = TrabajadorProceso()
            self.traSerPro.show()

    def open_view_eme_BusPro(self):
        self.IniFin = emerIniFin()
        self.IniFin.show()

class emerIniFin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerIniFin, self).__init__(parent)
        uic.loadUi('Front/trabajador/emerIniFin.ui', self)

