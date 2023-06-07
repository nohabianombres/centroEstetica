from Front.comunes.emerComunes import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidget
from PyQt5 import QtWidgets, uic

from Front.administrador.emeAdm.emeAdmcodigo import *



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

        self.botAgrPro.clicked.connect(self.open_view_eme_AgrPro)
        self.botBusPro.clicked.connect(self.open_view_eme_BusPro)
        self.botMosPro.clicked.connect(self.open_view_eme_MosTodPro)
        self.botModPro.clicked.connect(self.open_view_eme_ModPro)


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

    def open_view_eme_AgrPro(self):
        self.AgrPro = emerAgrPro()
        self.AgrPro.set_callback(self.crear_ventana)
        self.AgrPro.show()

    def open_view_eme_BusPro(self):
        self.BusPro = emerBuscPro()
        self.BusPro.set_callback(self.imprimir_tabla)
        self.BusPro.show()

    def open_view_eme_MosTodPro(self):
        pass

    def open_view_eme_ModPro(self):
        self.ModPro = emerModProPre()
        self.ModPro.set_callback(self.crear_ventana)
        self.ModPro.show()

    def crear_ventana(self):
        pass

    def imprimir_tabla(self):
        pass

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

        self.botAgrSer.clicked.connect(self.open_view_eme_AgrSer)
        self.botBusSer.clicked.connect(self.open_view_eme_BusSer)
        self.botMosSer.clicked.connect(self.open_view_eme_MosTodSer)
        self.botModSer.clicked.connect(self.open_view_eme_ModSer)

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



    def open_view_eme_AgrSer(self):
        self.AgrSer = emerAgrSer()
        self.AgrSer.show()

    def open_view_eme_BusSer(self):
        self.BusSer = emerBuscSer()
        self.BusSer.show()

    def open_view_eme_MosTodSer(self):
        pass

    def open_view_eme_ModSer(self):
        self.ModSer = emerModSer()
        self.ModSer.show()

    def crear_ventana(self):
        pass

    def imprimir_tabla(self):
        pass



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

        self.botAgrCit.clicked.connect(self.open_view_eme_AgrCit)
        self.botBusCit.clicked.connect(self.open_view_eme_BusCita)
        self.botCanCit.clicked.connect(self.open_view_eme_CanCita)
        self.botModCit.clicked.connect(self.open_view_eme_ModCita)



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


    def open_view_eme_AgrCit(self):
        self.AgrCit = emerAgrCita()
        self.AgrCit.show()



    def open_view_eme_BusCita(self):
        self.BusCit = emerBusCitas()
        self.BusCit.set_callback(self.imprimir_tablas)
        self.BusCit.show()


    def open_view_eme_ModCita(self):
        pass

    def open_view_eme_CanCita(self):
        self.CanCita = emerCanCita()
        self.CanCita.show()

    def imprimir_tablas(self, listas):
        self.ui.TabAgenda.clearContents()  # Limpiar contenido existente en la tabla
        self.ui.TabAgenda.setRowCount(0)  # Reiniciar número de filas

        for lista in listas:
            fila = self.ui.TabAgenda.rowCount()
            self.ui.TabAgenda.insertRow(fila)

            for columna, elemento in enumerate(lista):
                celda = QtWidgets.QTableWidgetItem(elemento)
                self.ui.TabAgenda.setItem(fila, columna, celda)


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

        self.botAdcFal.clicked.connect(self.open_view_eme_AdcFal)
        self.botAgrCli.clicked.connect(self.open_view_eme_AgrCli)
        self.botBusCli.clicked.connect(self.open_view_eme_BusCli)



        self.cliente_ins = None
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


    def open_view_eme_AdcFal(self):
        self.AdcFal = emerAdiFal()
        self.AdcFal.show()

    def open_view_eme_AgrCli(self):
        self.AgrCli = emerAgrCli()
        self.AgrCli.show()

    def open_view_eme_BusCli(self):
        self.BusCli = emerBuscClien()
        self.BusCli.show()

    def crear_ventana(self):
        pass

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

    def crear_ventana(self):
        pass

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

        self.botDes.clicked.connect(self.open_view_Des)
        self.botIngPro.clicked.connect(self.open_view_IngPro)
        self.botIngSer.clicked.connect(self.open_view_IngSer)


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

    def crear_ventana(self):
        pass


    def open_view_IngPro(self):
        self.IngPro = AdminInformesProductos()
        self.IngPro.show()

    def open_view_IngSer(self):
        self.IngSer = AdminInformesServicios()
        self.IngSer.show()

    def open_view_Des(self):
        self.InfDes = AdminInformesDesempeno()
        self.InfDes.show()



class AdminInformesDesempeno(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(AdminInformesDesempeno, self).__init__(parent)
        uic.loadUi('Front/administrador/adminDesempeño.ui', self)

class AdminInformesProductos(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(AdminInformesProductos, self).__init__(parent)
        uic.loadUi('Front/administrador/adminIngresoProductos.ui', self)

class AdminInformesServicios(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(AdminInformesServicios, self).__init__(parent)
        uic.loadUi('Front/administrador/adminIngresoServicios.ui', self)


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

        self.botAgrUsu.clicked.connect(self.open_view_5)
        self.botBusUsu.clicked.connect(self.open_view_5)
        self.botCamCon.clicked.connect(self.open_view_5)
        self.botMosTod.clicked.connect(self.open_view_5)

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

    def crear_ventana(self):
        pass