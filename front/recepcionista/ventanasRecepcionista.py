from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication
from Front.comunes.emerComunes import *




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
            self.recServicios.show()
        elif sender_button_rec == self.botUsuRec:
            self.hide()
            self.recUsuarios = RecepcionistaUsuarios()
            self.recUsuarios.show()
        elif sender_button_rec == self.botAgeRec:
            self.hide()
            self.recAgenda = RecepcionistaAgenda()
            self.recAgenda.show()
        elif sender_button_rec == self.botCliRec:
            self.hide()
            self.recClientes = RecepcionistaClientes()
            self.recClientes.show()

class RecepcionistaClientes(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(RecepcionistaClientes, self).__init__(parent)
        uic.loadUi('Front/recepcionista/RecepcionistaClientes.ui', self)

        self.botAgeRec.clicked.connect(self.open_view_rec_cli)
        self.botCliRec.clicked.connect(self.open_view_rec_cli)
        self.botSerRec.clicked.connect(self.open_view_rec_cli)
        self.botUsuRec.clicked.connect(self.open_view_rec_cli)
        self.botAdiFalRec.clicked.connect(self.open_view_eme_AdiFal)
        self.botAgrCliRec.clicked.connect(self.open_view_eme_AgrCli)
        self.botBusCliRec.clicked.connect(self.open_view_eme_BusCli)
        self.botModCliRec.clicked.connect(self.open_view_eme_ModCli)

        self.recServicios = None
        self.recAgenda = None
        self.recUsuarios = None
        self.recClientes = None

    def open_view_rec_cli(self):
        sender_button_rec_cli = self.sender()
        if sender_button_rec_cli == self.botSerRec:
            self.hide()
            self.recServicios = RecepcionistaServicios()
            self.recServicios.show()
        elif sender_button_rec_cli == self.botUsuRec:
            self.hide()
            self.recUsuarios = RecepcionistaUsuarios()
            self.recUsuarios.show()
        elif sender_button_rec_cli == self.botAgeRec:
            self.hide()
            self.recAgenda = RecepcionistaAgenda()
            self.recAgenda.show()
        elif sender_button_rec_cli == self.botCliRec:
            self.hide()
            self.recClientes = RecepcionistaClientes()
            self.recClientes.show()

    def open_view_eme_AdiFal(self):
        self.AdiFal = emerAdiFal()
        self.AdiFal.show()

    def open_view_eme_AgrCli(self):
        self.AgrCli = emerAgrCli()
        self.AgrCli.show()

    def open_view_eme_BusCli(self):
        pass

    def open_view_eme_ModCli(self):
        self.ModCli = emerModClien()
        self.ModCli.show()

class RecepcionistaAgenda(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(RecepcionistaAgenda, self).__init__(parent)
        uic.loadUi('Front/recepcionista/RecepcionistaAgendaventa.ui', self)

        self.botAgeRec.clicked.connect(self.open_view_rec_Age)
        self.botCliRec.clicked.connect(self.open_view_rec_Age)
        self.botSerRec.clicked.connect(self.open_view_rec_Age)
        self.botUsuRec.clicked.connect(self.open_view_rec_Age)
        self.botBusCitRec.clicked.connect(self.open_view_eme_BusCit)
        self.botCanCitRec.clicked.connect(self.open_view_eme_CanCit)
        self.botCreCitRec.clicked.connect(self.open_view_eme_CreCit)
        self.botModCitRec.clicked.connect(self.open_view_eme_ModCit)


        self.recServicios = None
        self.recAgenda = None
        self.recUsuarios = None
        self.recClientes = None

    def open_view_rec_Age(self):

        sender_button_rec_age = self.sender()
        if sender_button_rec_age == self.botSerRec:
            self.hide()
            self.recServicios = RecepcionistaServicios()
            self.recServicios.show()
        elif sender_button_rec_age == self.botUsuRec:
            self.hide()
            self.recUsuarios = RecepcionistaUsuarios()
            self.recUsuarios.show()
        elif sender_button_rec_age == self.botAgeRec:
            self.hide()
            self.recAgenda = RecepcionistaAgenda()
            self.recAgenda.show()
        elif sender_button_rec_age == self.botCliRec:
            self.hide()
            self.recClientes = RecepcionistaClientes()
            self.recClientes.show()

    def open_view_eme_BusCit(self):
        self.BusCit = emerBusCita()
        self.BusCit.show()

    def open_view_eme_CanCit(self):
        self.CanCit = emerCamCita()
        self.CanCit.show()

    def open_view_eme_ModCit(self):
        pass

    def open_view_eme_CreCit(self):
        self.CreCit = emerAgrCita()
        self.CreCit.show()

class RecepcionistaServicios(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(RecepcionistaServicios, self).__init__(parent)
        uic.loadUi('Front/recepcionista/RecepcionistaServicios.ui', self)

        self.botAgeRec.clicked.connect(self.open_view_rec_Ser)
        self.botCliRec.clicked.connect(self.open_view_rec_Ser)
        self.botSerRec.clicked.connect(self.open_view_rec_Ser)
        self.botUsuRec.clicked.connect(self.open_view_rec_Ser)
        self.botBusSerRec.clicked.connect(self.open_view_eme_BusSer)
        self.botMosTodRec.clicked.connect(self.open_view_eme_MosTod)

        self.recServicios = None
        self.recAgenda = None
        self.recUsuarios = None
        self.recClientes = None

    def open_view_eme_BusSer(self):
        self.BusSer = emerBuscSer()
        self.BusSer.show()

    def open_view_eme_MosTod(self):
        pass

    def open_view_rec_Ser(self):
        sender_button_rec_ser = self.sender()
        if sender_button_rec_ser == self.botSerRec:
            self.hide()
            self.recServicios = RecepcionistaServicios()
            self.recServicios.show()
        elif sender_button_rec_ser == self.botUsuRec:
            self.hide()
            self.recUsuarios = RecepcionistaUsuarios()
            self.recUsuarios.show()
        elif sender_button_rec_ser == self.botAgeRec:
            self.hide()
            self.recAgenda = RecepcionistaAgenda()
            self.recAgenda.show()
        elif sender_button_rec_ser == self.botCliRec:
            self.hide()
            self.recClientes = RecepcionistaClientes()
            self.recClientes.show()



class RecepcionistaUsuarios(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(RecepcionistaUsuarios, self).__init__(parent)
        uic.loadUi('Front/recepcionista/RecepcionistaUsuarios.ui', self)

        self.botAgeRec.clicked.connect(self.open_view_rec_usu)
        self.botCliRec.clicked.connect(self.open_view_rec_usu)
        self.botSerRec.clicked.connect(self.open_view_rec_usu)
        self.botUsuRec.clicked.connect(self.open_view_rec_usu)

        self.recServicios = None
        self.recAgenda = None
        self.recUsuarios = None
        self.recClientes = None

    def open_view_rec_usu(self):

        sender_button_rec_usu = self.sender()
        if sender_button_rec_usu == self.botSerRec:
            self.hide()
            self.recServicios = RecepcionistaServicios()
            self.recServicios.show()
        elif sender_button_rec_usu == self.botUsuRec:
            self.hide()
            self.recUsuarios = RecepcionistaUsuarios()
            self.recUsuarios.show()
        elif sender_button_rec_usu == self.botAgeRec:
            self.hide()
            self.recAgenda = RecepcionistaAgenda()
            self.recAgenda.show()
        elif sender_button_rec_usu == self.botCliRec:
            self.hide()
            self.recClientes = RecepcionistaClientes()
            self.recClientes.show()