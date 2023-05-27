from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication


class Admin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Admin, self).__init__(parent)
        uic.loadUi('Front/administrador/Admin.ui', self)
        self.botInvAdm.clicked.connect(self.open_view_2)
        self.botSerAdm.clicked.connect(self.open_view_2)
        self.botInfAdm.clicked.connect(self.open_view_2)
        self.botAgeAdm.clicked.connect(self.open_view_2)
        self.botCliAdm.clicked.connect(self.open_view_2)
        self.botUsuAdm.clicked.connect(self.open_view_2)
        self.botFacAdm.clicked.connect(self.open_view_2)
        self.adInventario = None
        self.adServicios = None
        self.adInformes = None
        self.adAgenda = None
        self.adFacturas = None
        self.adUsuarios = None
        self.adClientes = None

    def open_view_2(self):
        sender_button_A = self.sender()
        if sender_button_A == self.botSerAdm:
            self.hide()
            self.adServicios = AdminServicios()
            self.adServicios.show()
        elif sender_button_A == self.botInvAdm:
            self.hide()
            self.adInventario = AdminInventario()
            self.adInventario.show()
        elif sender_button_A == self.botInfAdm:
            self.hide()
            self.adInformes = AdminServicios()
            self.adInformes.show()
        elif sender_button_A == self.botAgeAdm:
            self.hide()
            self.adAgenda = AdminAgenda()
            self.adAgenda.show()
        elif sender_button_A == self.botCliAdm:
            self.hide()
            self.adClientes = AdminClientes()
            self.adClientes.show()
        elif sender_button_A == self.botUsuAdm:
            self.hide()
            self.adUsuarios = AdminUsuarios()
            self.adUsuarios.show()
        elif sender_button_A == self.botFacAdm:
            self.hide()
            self.adFacturas = AdminFacturacion()
            self.adFacturas.show()

class AdminInventario(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(AdminInventario, self).__init__(parent)
        uic.loadUi('Front/administrador/adminInventario.ui', self)
        self.botInvAdm.clicked.connect(self.open_view_3)
        self.botSerAdm.clicked.connect(self.open_view_3)
        self.botInfAdm.clicked.connect(self.open_view_3)
        self.botAgeAdm.clicked.connect(self.open_view_3)
        self.botCliAdm.clicked.connect(self.open_view_3)
        self.botUsuAdm.clicked.connect(self.open_view_3)
        self.botFacAdm.clicked.connect(self.open_view_3)
        self.adInventario = None
        self.adServicios = None
        self.adInformes = None
        self.adAgenda = None
        self.adFacturas = None
        self.adUsuarios = None
        self.adClientes = None

    def open_view_3(self):
        sender_button_Inv = self.sender()
        if sender_button_Inv == self.botSerAdm:
            self.hide()
            self.adServicios = AdminServicios()
            self.adServicios.show()
        elif sender_button_Inv == self.botInvAdm:
            self.hide()
            self.adInventario = AdminInventario()
            self.adInventario.show()
        elif sender_button_Inv == self.botInfAdm:
            self.hide()
            self.adInformes = AdminInformes()
            self.adInformes.show()
        elif sender_button_Inv == self.botAgeAdm:
            self.hide()
            self.adAgenda = AdminAgenda()
            self.adAgenda.show()
        elif sender_button_Inv == self.botCliAdm:
            self.hide()
            self.adClientes = AdminClientes()
            self.adClientes.show()
        elif sender_button_Inv == self.botUsuAdm:
            self.hide()
            self.adUsuarios = AdminUsuarios()
            self.adUsuarios.show()
        elif sender_button_Inv == self.botFacAdm:
            self.hide()
            self.adFacturas = AdminFacturacion()
            self.adFacturas.show()

class AdminServicios(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(AdminServicios, self).__init__(parent)
        uic.loadUi('Front/administrador/adminServicios.ui', self)
        self.botInvAdm.clicked.connect(self.open_view_4)
        self.botSerAdm.clicked.connect(self.open_view_4)
        self.botInfAdm.clicked.connect(self.open_view_4)
        self.botAgeAdm.clicked.connect(self.open_view_4)
        self.botCliAdm.clicked.connect(self.open_view_4)
        self.botUsuAdm.clicked.connect(self.open_view_4)
        self.botFacAdm.clicked.connect(self.open_view_4)
        self.adInventario = None
        self.adServicios = None
        self.adInformes = None
        self.adAgenda = None
        self.adFacturas = None
        self.adUsuarios = None
        self.adClientes = None

    def open_view_4(self):
        sender_button_S = self.sender()
        if sender_button_S == self.botSerAdm:
            self.hide()
            self.adServicios = AdminServicios()
            self.adServicios.show()
        elif sender_button_S == self.botInvAdm:
            self.hide()
            self.adInventario = AdminInventario()
            self.adInventario.show()
        elif sender_button_S == self.botInfAdm:
            self.hide()
            self.adInformes = AdminInformes()
            self.adInformes.show()
        elif sender_button_S == self.botAgeAdm:
            self.hide()
            self.adAgenda = AdminAgenda()
            self.adAgenda.show()
        elif sender_button_S == self.botCliAdm:
            self.hide()
            self.adClientes = AdminClientes()
            self.adClientes.show()
        elif sender_button_S == self.botUsuAdm:
            self.hide()
            self.adUsuarios = AdminUsuarios()
            self.adUsuarios.show()
        elif sender_button_S == self.botFacAdm:
            self.hide()
            self.adFacturas = AdminFacturacion()
            self.adFacturas.show()

class AdminAgenda(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(AdminAgenda, self).__init__(parent)
        uic.loadUi('Front/administrador/adminAgenda.ui', self)
        self.botInvAdm.clicked.connect(self.open_view_5)
        self.botSerAdm.clicked.connect(self.open_view_5)
        self.botInfAdm.clicked.connect(self.open_view_5)
        self.botAgeAdm.clicked.connect(self.open_view_5)
        self.botCliAdm.clicked.connect(self.open_view_5)
        self.botUsuAdm.clicked.connect(self.open_view_5)
        self.botFacAdm.clicked.connect(self.open_view_5)
        self.adInventario = None
        self.adServicios = None
        self.adInformes = None
        self.adAgenda = None
        self.adFacturas = None
        self.adUsuarios = None
        self.adClientes = None

    def open_view_5(self):
        sender_button_Age = self.sender()
        if sender_button_Age == self.botSerAdm:
            self.hide()
            self.adServicios = AdminServicios()
            self.adServicios.show()
        elif sender_button_Age == self.botInvAdm:
            self.hide()
            self.adInventario = AdminInventario()
            self.adInventario.show()
        elif sender_button_Age == self.botInfAdm:
            self.hide()
            self.adInformes = AdminInformes()
            self.adInformes.show()
        elif sender_button_Age == self.botAgeAdm:
            self.hide()
            self.adAgenda = AdminAgenda()
            self.adAgenda.show()
        elif sender_button_Age == self.botCliAdm:
            self.hide()
            self.adClientes = AdminClientes()
            self.adClientes.show()
        elif sender_button_Age == self.botUsuAdm:
            self.hide()
            self.adUsuarios = AdminUsuarios()
            self.adUsuarios.show()
        elif sender_button_Age == self.botFacAdm:
            self.hide()
            self.adFacturas = AdminFacturacion()
            self.adFacturas.show()

class AdminClientes(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(AdminClientes, self).__init__(parent)
        uic.loadUi('Front/administrador/adminClientes.ui', self)
        self.botInvAdm.clicked.connect(self.open_view_6)
        self.botSerAdm.clicked.connect(self.open_view_6)
        self.botInfAdm.clicked.connect(self.open_view_6)
        self.botAgeAdm.clicked.connect(self.open_view_6)
        self.botCliAdm.clicked.connect(self.open_view_6)
        self.botUsuAdm.clicked.connect(self.open_view_6)
        self.botFacAdm.clicked.connect(self.open_view_6)
        self.adInventario = None
        self.adServicios = None
        self.adInformes = None
        self.adAgenda = None
        self.adFacturas = None
        self.adUsuarios = None
        self.adClientes = None

    def open_view_6(self):
        sender_button_Cli = self.sender()
        if sender_button_Cli == self.botSerAdm:
            self.hide()
            self.adServicios = AdminServicios()
            self.adServicios.show()
        elif sender_button_Cli == self.botInvAdm:
            self.hide()
            self.adInventario = AdminInventario()
            self.adInventario.show()
        elif sender_button_Cli == self.botInfAdm:
            self.hide()
            self.adInformes = AdminInformes()
            self.adInformes.show()
        elif sender_button_Cli == self.botAgeAdm:
            self.hide()
            self.adAgenda = AdminAgenda()
            self.adAgenda.show()
        elif sender_button_Cli == self.botCliAdm:
            self.hide()
            self.adClientes = AdminClientes()
            self.adClientes.show()
        elif sender_button_Cli == self.botUsuAdm:
            self.hide()
            self.adUsuarios = AdminUsuarios()
            self.adUsuarios.show()
        elif sender_button_Cli == self.botFacAdm:
            self.hide()
            self.adFacturas = AdminFacturacion()
            self.adFacturas.show()

class AdminFacturacion(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(AdminFacturacion, self).__init__(parent)
        uic.loadUi('Front/administrador/adminFacturacion.ui', self)
        self.botInvAdm.clicked.connect(self.open_view_7)
        self.botSerAdm.clicked.connect(self.open_view_7)
        self.botInfAdm.clicked.connect(self.open_view_7)
        self.botAgeAdm.clicked.connect(self.open_view_7)
        self.botCliAdm.clicked.connect(self.open_view_7)
        self.botUsuAdm.clicked.connect(self.open_view_7)
        self.botFacAdm.clicked.connect(self.open_view_7)
        self.adInventario = None
        self.adServicios = None
        self.adInformes = None
        self.adAgenda = None
        self.adFacturas = None
        self.adUsuarios = None
        self.adClientes = None

    def open_view_7(self):
        sender_button_Fac = self.sender()
        if sender_button_Fac == self.botSerAdm:
            self.hide()
            self.adServicios = AdminServicios()
            self.adServicios.show()
        elif sender_button_Fac == self.botInvAdm:
            self.hide()
            self.adInventario = AdminInventario()
            self.adInventario.show()
        elif sender_button_Fac == self.botInfAdm:
            self.hide()
            self.adInformes = AdminInformes()
            self.adInformes.show()
        elif sender_button_Fac == self.botAgeAdm:
            self.hide()
            self.adAgenda = AdminAgenda()
            self.adAgenda.show()
        elif sender_button_Fac == self.botCliAdm:
            self.hide()
            self.adClientes = AdminClientes()
            self.adClientes.show()
        elif sender_button_Fac == self.botUsuAdm:
            self.hide()
            self.adUsuarios = AdminUsuarios()
            self.adUsuarios.show()
        elif sender_button_Fac == self.botFacAdm:
            self.hide()
            self.adFacturas = AdminFacturacion()
            self.adFacturas.show()

class AdminInformes(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(AdminInformes, self).__init__(parent)
        uic.loadUi('Front/administrador/adminInformes.ui', self)
        self.botInvAdm.clicked.connect(self.open_view_8)
        self.botSerAdm.clicked.connect(self.open_view_8)
        self.botInfAdm.clicked.connect(self.open_view_8)
        self.botAgeAdm.clicked.connect(self.open_view_8)
        self.botCliAdm.clicked.connect(self.open_view_8)
        self.botUsuAdm.clicked.connect(self.open_view_8)
        self.botFacAdm.clicked.connect(self.open_view_8)
        self.adInventario = None
        self.adServicios = None
        self.adInformes = None
        self.adAgenda = None
        self.adFacturas = None
        self.adUsuarios = None
        self.adClientes = None

    def open_view_8(self):
        sender_button_Inf = self.sender()
        if sender_button_Inf == self.botSerAdm:
            self.hide()
            self.adServicios = AdminServicios()
            self.adServicios.show()
        elif sender_button_Inf == self.botInvAdm:
            self.hide()
            self.adInventario = AdminInventario()
            self.adInventario.show()
        elif sender_button_Inf == self.botInfAdm:
            self.hide()
            self.adInformes = AdminInformes()
            self.adInformes.show()
        elif sender_button_Inf == self.botAgeAdm:
            self.hide()
            self.adAgenda = AdminAgenda()
            self.adAgenda.show()
        elif sender_button_Inf == self.botCliAdm:
            self.hide()
            self.adClientes = AdminClientes()
            self.adClientes.show()
        elif sender_button_Inf == self.botUsuAdm:
            self.hide()
            self.adUsuarios = AdminUsuarios()
            self.adUsuarios.show()
        elif sender_button_Inf == self.botFacAdm:
            self.hide()
            self.adFacturas = AdminFacturacion()
            self.adFacturas.show()

class AdminUsuarios(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(AdminUsuarios, self).__init__(parent)
        uic.loadUi('Front/administrador/adminUsuarios.ui', self)
        self.botInvAdm.clicked.connect(self.open_view_9)
        self.botSerAdm.clicked.connect(self.open_view_9)
        self.botInfAdm.clicked.connect(self.open_view_9)
        self.botAgeAdm.clicked.connect(self.open_view_9)
        self.botCliAdm.clicked.connect(self.open_view_9)
        self.botUsuAdm.clicked.connect(self.open_view_9)
        self.botFacAdm.clicked.connect(self.open_view_9)
        self.adInventario = None
        self.adServicios = None
        self.adInformes = None
        self.adAgenda = None
        self.adFacturas = None
        self.adUsuarios = None
        self.adClientes = None

    def open_view_9(self):
        sender_button_Usu = self.sender()
        if sender_button_Usu == self.botSerAdm:
            self.hide()
            self.adServicios = AdminServicios()
            self.adServicios.show()
        elif sender_button_Usu == self.botInvAdm:
            self.hide()
            self.adInventario = AdminInventario()
            self.adInventario.show()
        elif sender_button_Usu == self.botInfAdm:
            self.hide()
            self.adInformes = AdminInformes()
            self.adInformes.show()
        elif sender_button_Usu == self.botAgeAdm:
            self.hide()
            self.adAgenda = AdminAgenda()
            self.adAgenda.show()
        elif sender_button_Usu == self.botCliAdm:
            self.hide()
            self.adClientes = AdminClientes()
            self.adClientes.show()
        elif sender_button_Usu == self.botUsuAdm:
            self.hide()
            self.adUsuarios = AdminUsuarios()
            self.adUsuarios.show()
        elif sender_button_Usu == self.botFacAdm:
            self.hide()
            self.adFacturas = AdminFacturacion()
            self.adFacturas.show()