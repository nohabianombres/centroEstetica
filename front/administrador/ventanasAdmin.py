


from Front.comunes.emerComunes import emerRetorno, emerBuscPro, emerBuscUsu, emerAgrCli, emerValTot, emerBuscSer, emerConfirmar, emerAgrCita, emerCanCitaId, emerBusCitas, emerBusFac, emerCreFac, emerPagFacId, emerPagFacDoc, emerBuscClien, emerCanCita, emerAdiFal
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
            self.adServicios.recibir_datos(self.datos_usuario)
            self.adServicios.show()
        elif sender_button_A == self.botInvAdm:
            self.hide()
            self.adInventario = AdminInventario()
            self.adInventario.recibir_datos(self.datos_usuario)
            self.adInventario.show()
        elif sender_button_A == self.botInfAdm:
            self.hide()
            self.adInformes = AdminInformes()
            self.adInformes.recibir_datos(self.datos_usuario)
            self.adInformes.show()
        elif sender_button_A == self.botAgeAdm:
            self.hide()
            self.adAgenda = AdminAgenda()
            self.adAgenda.recibir_datos(self.datos_usuario)
            self.adAgenda.show()
        elif sender_button_A == self.botCliAdm:
            self.hide()
            self.adClientes = AdminClientes()
            self.adClientes.recibir_datos(self.datos_usuario)
            self.adClientes.show()
        elif sender_button_A == self.botUsuAdm:
            self.hide()
            self.adUsuarios = AdminUsuarios()
            self.adUsuarios.recibir_datos(self.datos_usuario)
            self.adUsuarios.show()
        elif sender_button_A == self.botFacAdm:
            self.hide()
            self.adFacturas = AdminFacturacion()
            self.adFacturas.recibir_datos(self.datos_usuario)
            self.adFacturas.show()

    def recibir_datos (self, usuario_validar):
        self.datos_usuario = usuario_validar

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
        self.botModPro.clicked.connect(self.open_view_eme_ModProPre)

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
            self.adServicios.recibir_datos(self.datos_usuario)
            self.adServicios.show()
        elif sender_button_Inv == self.botInvAdm:
            self.hide()
            self.adInventario = AdminInventario()
            self.adInventario.recibir_datos(self.datos_usuario)
            self.adInventario.show()
        elif sender_button_Inv == self.botInfAdm:
            self.hide()
            self.adInformes = AdminInformes()
            self.adInformes.recibir_datos(self.datos_usuario)
            self.adInformes.show()
        elif sender_button_Inv == self.botAgeAdm:
            self.hide()
            self.adAgenda = AdminAgenda()
            self.adAgenda.recibir_datos(self.datos_usuario)
            self.adAgenda.show()
        elif sender_button_Inv == self.botCliAdm:
            self.hide()
            self.adClientes = AdminClientes()
            self.adClientes.recibir_datos(self.datos_usuario)
            self.adClientes.show()
        elif sender_button_Inv == self.botUsuAdm:
            self.hide()
            self.adUsuarios = AdminUsuarios()
            self.adUsuarios.recibir_datos(self.datos_usuario)
            self.adUsuarios.show()
        elif sender_button_Inv == self.botFacAdm:
            self.hide()
            self.adFacturas = AdminFacturacion()
            self.adFacturas.recibir_datos(self.datos_usuario)
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

    def open_view_eme_ModProPre(self):
        self.ModProPre = emerModProPre()
        self.ModProPre.set_callback(self.crear_ventana)
        self.ModProPre.show()

    def open_view_eme_ModProCan(self):
        self.ModProCan = emerModProCan()
        self.ModProCan.set_callback(self.crear_ventana)
        self.ModProPre.show()

    def crear_ventana(self, retorno):
        self.emer_retorno = emerRetorno()
        self.emer_retorno.imprimir_retorno(retorno)
        self.emer_retorno.show()

    def imprimir_tabla(self):
        pass

    def recibir_datos (self, usuario_validar):
        self.datos_usuario = usuario_validar

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
            self.adServicios.recibir_datos(self.datos_usuario)
            self.adServicios.show()
        elif sender_button_S == self.botInvAdm:
            self.hide()
            self.adInventario = AdminInventario()
            self.adInventario.recibir_datos(self.datos_usuario)
            self.adInventario.show()
        elif sender_button_S == self.botInfAdm:
            self.hide()
            self.adInformes = AdminInformes()
            self.adInformes.show()
        elif sender_button_S == self.botAgeAdm:
            self.hide()
            self.adAgenda = AdminAgenda()
            self.adAgenda.recibir_datos(self.datos_usuario)
            self.adAgenda.show()
        elif sender_button_S == self.botCliAdm:
            self.hide()
            self.adClientes = AdminClientes()
            self.adClientes.recibir_datos(self.datos_usuario)
            self.adClientes.show()
        elif sender_button_S == self.botUsuAdm:
            self.hide()
            self.adUsuarios = AdminUsuarios()
            self.adUsuarios.recibir_datos(self.datos_usuario)
            self.adUsuarios.show()
        elif sender_button_S == self.botFacAdm:
            self.hide()
            self.adFacturas = AdminFacturacion()
            self.adFacturas.recibir_datos(self.datos_usuario)
            self.adFacturas.show()

    def open_view_eme_AgrSer(self):
        self.AgrSer = emerAgrSer()
        self.AgrSer.set_callback(self.crear_ventana)
        self.AgrSer.show()

    def open_view_eme_BusSer(self):
        self.BusSer = emerBuscSer()
        self.BusSer.set_callback(self.imprimir_tabla)
        self.BusSer.show()

    def open_view_eme_MosTodSer(self):
        pass

    def open_view_eme_ModSer(self):
        self.ModSer = emerModSer()
        self.ModSer.set_callback(self. crear_ventana)
        self.ModSer.show()

    def crear_ventana(self, retorno):
        self.emer_retorno = emerRetorno()
        self.emer_retorno.imprimir_retorno(retorno)
        self.emer_retorno.show()


    def imprimir_tabla(self):
        pass

    def recibir_datos (self, usuario_validar):
        self.datos_usuario = usuario_validar

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
            self.adServicios.recibir_datos(self.datos_usuario)
            self.adServicios.show()
        elif sender_button_Age == self.botInvAdm:
            self.hide()
            self.adInventario = AdminInventario()
            self.adInventario.recibir_datos(self.datos_usuario)
            self.adInventario.show()
        elif sender_button_Age == self.botInfAdm:
            self.hide()
            self.adInformes = AdminInformes()
            self.adInformes.recibir_datos(self.datos_usuario)
            self.adInformes.show()
        elif sender_button_Age == self.botAgeAdm:
            self.hide()
            self.adAgenda = AdminAgenda()
            self.adAgenda.recibir_datos(self.datos_usuario)
            self.adAgenda.show()
        elif sender_button_Age == self.botCliAdm:
            self.hide()
            self.adClientes = AdminClientes()
            self.adClientes.recibir_datos(self.datos_usuario)
            self.adClientes.show()
        elif sender_button_Age == self.botUsuAdm:
            self.hide()
            self.adUsuarios = AdminUsuarios()
            self.adUsuarios.recibir_datos(self.datos_usuario)
            self.adUsuarios.show()
        elif sender_button_Age == self.botFacAdm:
            self.hide()
            self.adFacturas = AdminFacturacion()
            self.adFacturas.show()


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
        #self.ui.TabAgenda.clearContents()  # Limpiar contenido existente en la tabla
        #self.ui.TabAgenda.setRowCount()  # Reiniciar número de filas

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

    def open_view_emerIdCitCan(self,a):
        print(a)
        self.IdCitCan = emerCanCitaId ()
        self.IdCitCan.set_callback(self.crear_ventana)
        self.IdCitCan.show()

    def recibir_datos (self, usuario_validar):
        self.datos_usuario = usuario_validar

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
            self.adServicios.recibir_datos(self.datos_usuario)
            self.adServicios.show()
        elif sender_button_Cli == self.botInvAdm:
            self.hide()
            self.adInventario = AdminInventario()
            self.adInventario.recibir_datos(self.datos_usuario)
            self.adInventario.show()
        elif sender_button_Cli == self.botInfAdm:
            self.hide()
            self.adInformes = AdminInformes()
            self.adInformes.recibir_datos(self.datos_usuario)
            self.adInformes.show()
        elif sender_button_Cli == self.botAgeAdm:
            self.hide()
            self.adAgenda = AdminAgenda()
            self.adAgenda.recibir_datos(self.datos_usuario)
            self.adAgenda.show()
        elif sender_button_Cli == self.botCliAdm:
            self.hide()
            self.adClientes = AdminClientes()
            self.adClientes.recibir_datos(self.datos_usuario)
            self.adClientes.show()
        elif sender_button_Cli == self.botUsuAdm:
            self.hide()
            self.adUsuarios = AdminUsuarios()
            self.adUsuarios.recibir_datos(self.datos_usuario)
            self.adUsuarios.show()
        elif sender_button_Cli == self.botFacAdm:
            self.hide()
            self.adFacturas = AdminFacturacion()
            self.adFacturas.recibir_datos(self.datos_usuario)
            self.adFacturas.show()

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

    def imprimir_tablas (self):
        pass

    def recibir_datos (self, usuario_validar):
        self.datos_usuario = usuario_validar

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

        self.botBusFacDoc.clicked.connect(self.open_view_eme_BusFac)
        self.botPagId.clicked.connect(self.open_view_eme_PagFacId)
        self.botPagDoc.clicked.connect(self.open_view_eme_PagFacDoc)
        self.botCreFac.clicked.connect(self.open_view_eme_CreFac)


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
            self.adServicios.recibir_datos(self.datos_usuario)
            self.adServicios.show()
        elif sender_button_Fac == self.botInvAdm:
            self.hide()
            self.adInventario = AdminInventario()
            self.adInventario.recibir_datos(self.datos_usuario)
            self.adInventario.show()
        elif sender_button_Fac == self.botInfAdm:
            self.hide()
            self.adInformes = AdminInformes()
            self.adInformes.recibir_datos(self.datos_usuario)
            self.adInformes.show()
        elif sender_button_Fac == self.botAgeAdm:
            self.hide()
            self.adAgenda = AdminAgenda()
            self.adAgenda.recibir_datos(self.datos_usuario)
            self.adAgenda.show()
        elif sender_button_Fac == self.botCliAdm:
            self.hide()
            self.adClientes = AdminClientes()
            self.adClientes.recibir_datos(self.datos_usuario)
            self.adClientes.show()
        elif sender_button_Fac == self.botUsuAdm:
            self.hide()
            self.adUsuarios = AdminUsuarios()
            self.adUsuarios.recibir_datos(self.datos_usuario)
            self.adUsuarios.show()
        elif sender_button_Fac == self.botFacAdm:
            self.hide()
            self.adFacturas = AdminFacturacion()
            self.adFacturas.show()


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

    def imprimir_tablas (self):
        pass

    def recibir_datos (self, usuario_validar):
        self.datos_usuario = usuario_validar

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
            self.adServicios.recibir_datos(self.datos_usuario)
            self.adServicios.show()
        elif sender_button_Inf == self.botInvAdm:
            self.hide()
            self.adInventario = AdminInventario()
            self.adInventario.recibir_datos(self.datos_usuario)
            self.adInventario.show()
        elif sender_button_Inf == self.botInfAdm:
            self.hide()
            self.adInformes = AdminInformes()
            self.adInventario.recibir_datos(self.datos_usuario)
            self.adInformes.show()
        elif sender_button_Inf == self.botAgeAdm:
            self.hide()
            self.adAgenda = AdminAgenda()
            self.adAgenda.recibir_datos(self.datos_usuario)
            self.adAgenda.show()
        elif sender_button_Inf == self.botCliAdm:
            self.hide()
            self.adClientes = AdminClientes()
            self.adClientes.recibir_datos(self.datos_usuario)
            self.adClientes.show()
        elif sender_button_Inf == self.botUsuAdm:
            self.hide()
            self.adUsuarios = AdminUsuarios()
            self.adUsuarios.recibir_datos(self.datos_usuario)
            self.adUsuarios.show()
        elif sender_button_Inf == self.botFacAdm:
            self.hide()
            self.adFacturas = AdminFacturacion()
            self.adFacturas.recibir_datos(self.datos_usuario)
            self.adFacturas.show()


    def open_view_IngPro(self):
        self.IngPro = emerBusInfPro()
        self.IngPro.set_callback(self.imprimir_tablas)
        self.IngPro.show()

    def open_view_IngSer(self):
        self.IngSer = emerBusInfSer()
        self.IngSer.set_callback(self.imprimir_tablas)
        self.IngSer.show()

    def open_view_Des(self):
        self.infDes = Informe()
        self.informe_desempe = self.infDes.mostrar_desempeno()
        self.imprimir_tablas(self.informe_desempe)

    def crear_ventana(self, retorno):
        self.emer_retorno = emerRetorno()
        self.emer_retorno.imprimir_retorno(retorno)
        self.emer_retorno.show()

    def imprimir_tablas(self):
        pass

    def recibir_datos (self, usuario_validar):
        self.datos_usuario = usuario_validar


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

        self.botAgrUsu.clicked.connect(self.open_view_emer_cre_usu)
        self.botBusUsu.clicked.connect(self.open_view_emer_cre_usu)
        self.botCamCon.clicked.connect(self.open_view_emer_cam_con)
        self.botMosTod.clicked.connect(self.open_view_emer_cre_usu)

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
            self.adServicios.recibir_datos(self.datos_usuario)
            self.adServicios.show()
        elif sender_button_Usu == self.botInvAdm:
            self.hide()
            self.adInventario = AdminInventario()
            self.adInventario.recibir_datos(self.datos_usuario)
            self.adInventario.show()
        elif sender_button_Usu == self.botInfAdm:
            self.hide()
            self.adInformes = AdminInformes()
            self.adInformes.recibir_datos(self.datos_usuario)
            self.adInformes.show()
        elif sender_button_Usu == self.botAgeAdm:
            self.hide()
            self.adAgenda = AdminAgenda()
            self.adAgenda.recibir_datos(self.datos_usuario)
            self.adAgenda.show()
        elif sender_button_Usu == self.botCliAdm:
            self.hide()
            self.adClientes = AdminClientes()
            self.adClientes.recibir_datos(self.datos_usuario)
            self.adClientes.show()
        elif sender_button_Usu == self.botUsuAdm:
            self.hide()
            self.adUsuarios = AdminUsuarios()
            self.adUsuarios.recibir_datos(self.datos_usuario)
            self.adUsuarios.show()
        elif sender_button_Usu == self.botFacAdm:
            self.hide()
            self.adFacturas = AdminFacturacion()
            self.adFacturas.recibir_datos(self.datos_usuario)
            self.adFacturas.show()


    def open_view_emer_cre_usu (self):
        self.creUsu = emerAgrUsu()
        self.creUsu.set_callback(self.crear_ventana)
        self.creUsu.recibir_datos(self.datos_usuario)
        self.creUsu.show()

    def open_view_emer_cam_con(self):
        self.camCon = emerCamCon()
        self.camCon.set_callback(self.crear_ventana)
        self.camCon.recibir_datos(self.datos_usuario)
        self.camCon.show()

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
'''from Front.comunes.emerComunes import *
from Front.administrador.emeAdm.emeAdmcodigo import *
from PyQt5 import QtWidgets, uic

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
            self.adServicios.recibir_datos(self.datos_usuario)
            self.adServicios.show()
        elif sender_button_A == self.botInvAdm:
            self.hide()
            self.adInventario = AdminInventario()
            self.adInventario.recibir_datos(self.datos_usuario)
            self.adInventario.show()
        elif sender_button_A == self.botInfAdm:
            self.hide()
            self.adInformes = AdminInformes()
            self.adInformes.recibir_datos(self.datos_usuario)
            self.adInformes.show()
        elif sender_button_A == self.botAgeAdm:
            self.hide()
            self.adAgenda = AdminAgenda()
            self.adAgenda.recibir_datos(self.datos_usuario)
            self.adAgenda.show()
        elif sender_button_A == self.botCliAdm:
            self.hide()
            self.adClientes = AdminClientes()
            self.adClientes.recibir_datos(self.datos_usuario)
            self.adClientes.show()
        elif sender_button_A == self.botUsuAdm:
            self.hide()
            self.adUsuarios = AdminUsuarios()
            self.adUsuarios.recibir_datos(self.datos_usuario)
            self.adUsuarios.show()
        elif sender_button_A == self.botFacAdm:
            self.hide()
            self.adFacturas = AdminFacturacion()
            self.adFacturas.recibir_datos(self.datos_usuario)
            self.adFacturas.show()

    def recibir_datos (self, usuario_validar):
        self.datos_usuario = usuario_validar

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
        self.botModPro.clicked.connect(self.open_view_eme_ModProPre)

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
            self.adServicios.recibir_datos(self.datos_usuario)
            self.adServicios.show()
        elif sender_button_Inv == self.botInvAdm:
            self.hide()
            self.adInventario = AdminInventario()
            self.adInventario.recibir_datos(self.datos_usuario)
            self.adInventario.show()
        elif sender_button_Inv == self.botInfAdm:
            self.hide()
            self.adInformes = AdminInformes()
            self.adInformes.recibir_datos(self.datos_usuario)
            self.adInformes.show()
        elif sender_button_Inv == self.botAgeAdm:
            self.hide()
            self.adAgenda = AdminAgenda()
            self.adAgenda.recibir_datos(self.datos_usuario)
            self.adAgenda.show()
        elif sender_button_Inv == self.botCliAdm:
            self.hide()
            self.adClientes = AdminClientes()
            self.adClientes.recibir_datos(self.datos_usuario)
            self.adClientes.show()
        elif sender_button_Inv == self.botUsuAdm:
            self.hide()
            self.adUsuarios = AdminUsuarios()
            self.adUsuarios.recibir_datos(self.datos_usuario)
            self.adUsuarios.show()
        elif sender_button_Inv == self.botFacAdm:
            self.hide()
            self.adFacturas = AdminFacturacion()
            self.adFacturas.recibir_datos(self.datos_usuario)
            self.adFacturas.show()

    def open_view_eme_AgrPro(self):
        self.AgrPro = emerAgrPro()
        self.AgrPro.set_callback(self.crear_ventana)
        self.AgrPro.show()

    def open_view_eme_BusPro(self):
        print('entre a buscar producto')
        self.BusPro = emerBuscPro()
        self.BusPro.set_callback(self.imprimir_tabla)
        self.BusPro.show()

    def open_view_eme_MosTodPro(self):
        pass

    def open_view_eme_ModProPre(self):
        self.ModProPre = emerModProPre()
        self.ModProPre.set_callback(self.crear_ventana)
        self.ModProPre.show()

    def open_view_eme_ModProCan(self):
        self.ModProCan = emerModProCan()
        self.ModProCan.set_callback(self.crear_ventana)
        self.ModProPre.show()

    def crear_ventana(self, retorno):
        self.emer_retorno = emerRetorno()
        self.emer_retorno.imprimir_retorno(retorno)
        self.emer_retorno.show()

    def imprimir_tabla(self, listas):
        pass


    def recibir_datos (self, usuario_validar):
        self.datos_usuario = usuario_validar

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
            self.adServicios.recibir_datos(self.datos_usuario)
            self.adServicios.show()
        elif sender_button_S == self.botInvAdm:
            self.hide()
            self.adInventario = AdminInventario()
            self.adInventario.recibir_datos(self.datos_usuario)
            self.adInventario.show()
        elif sender_button_S == self.botInfAdm:
            self.hide()
            self.adInformes = AdminInformes()
            self.adInformes.show()
        elif sender_button_S == self.botAgeAdm:
            self.hide()
            self.adAgenda = AdminAgenda()
            self.adAgenda.recibir_datos(self.datos_usuario)
            self.adAgenda.show()
        elif sender_button_S == self.botCliAdm:
            self.hide()
            self.adClientes = AdminClientes()
            self.adClientes.recibir_datos(self.datos_usuario)
            self.adClientes.show()
        elif sender_button_S == self.botUsuAdm:
            self.hide()
            self.adUsuarios = AdminUsuarios()
            self.adUsuarios.recibir_datos(self.datos_usuario)
            self.adUsuarios.show()
        elif sender_button_S == self.botFacAdm:
            self.hide()
            self.adFacturas = AdminFacturacion()
            self.adFacturas.recibir_datos(self.datos_usuario)
            self.adFacturas.show()

    def open_view_eme_AgrSer(self):
        self.AgrSer = emerAgrSer()
        self.AgrSer.set_callback(self.crear_ventana)
        self.AgrSer.show()

    def open_view_eme_BusSer(self):
        self.BusSer = emerBuscSer()
        self.BusSer.set_callback(self.imprimir_tabla)
        self.BusSer.show()

    def open_view_eme_MosTodSer(self):
        pass

    def open_view_eme_ModSer(self):
        self.ModSer = emerModSer()
        self.ModSer.set_callback(self. crear_ventana)
        self.ModSer.show()

    def crear_ventana(self, retorno):
        self.emer_retorno = emerRetorno()
        self.emer_retorno.imprimir_retorno(retorno)
        self.emer_retorno.show()


    def imprimir_tabla(self):
        pass

    def recibir_datos (self, usuario_validar):
        self.datos_usuario = usuario_validar

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
            self.adServicios.recibir_datos(self.datos_usuario)
            self.adServicios.show()
        elif sender_button_Age == self.botInvAdm:
            self.hide()
            self.adInventario = AdminInventario()
            self.adInventario.recibir_datos(self.datos_usuario)
            self.adInventario.show()
        elif sender_button_Age == self.botInfAdm:
            self.hide()
            self.adInformes = AdminInformes()
            self.adInformes.recibir_datos(self.datos_usuario)
            self.adInformes.show()
        elif sender_button_Age == self.botAgeAdm:
            self.hide()
            self.adAgenda = AdminAgenda()
            self.adAgenda.recibir_datos(self.datos_usuario)
            self.adAgenda.show()
        elif sender_button_Age == self.botCliAdm:
            self.hide()
            self.adClientes = AdminClientes()
            self.adClientes.recibir_datos(self.datos_usuario)
            self.adClientes.show()
        elif sender_button_Age == self.botUsuAdm:
            self.hide()
            self.adUsuarios = AdminUsuarios()
            self.adUsuarios.recibir_datos(self.datos_usuario)
            self.adUsuarios.show()
        elif sender_button_Age == self.botFacAdm:
            self.hide()
            self.adFacturas = AdminFacturacion()
            self.adFacturas.show()


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
        pass

    def crear_ventana(self, retorno):
        self.emer_retorno = emerRetorno()
        self.emer_retorno.imprimir_retorno(retorno)
        self.emer_retorno.show()

    def open_view_emerIdCitCan(self,a):
        print(a)
        self.IdCitCan = emerCanCitaId ()
        self.IdCitCan.set_callback(self.crear_ventana)
        self.IdCitCan.show()

    def recibir_datos (self, usuario_validar):
        self.datos_usuario = usuario_validar

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
            self.adServicios.recibir_datos(self.datos_usuario)
            self.adServicios.show()
        elif sender_button_Cli == self.botInvAdm:
            self.hide()
            self.adInventario = AdminInventario()
            self.adInventario.recibir_datos(self.datos_usuario)
            self.adInventario.show()
        elif sender_button_Cli == self.botInfAdm:
            self.hide()
            self.adInformes = AdminInformes()
            self.adInformes.recibir_datos(self.datos_usuario)
            self.adInformes.show()
        elif sender_button_Cli == self.botAgeAdm:
            self.hide()
            self.adAgenda = AdminAgenda()
            self.adAgenda.recibir_datos(self.datos_usuario)
            self.adAgenda.show()
        elif sender_button_Cli == self.botCliAdm:
            self.hide()
            self.adClientes = AdminClientes()
            self.adClientes.recibir_datos(self.datos_usuario)
            self.adClientes.show()
        elif sender_button_Cli == self.botUsuAdm:
            self.hide()
            self.adUsuarios = AdminUsuarios()
            self.adUsuarios.recibir_datos(self.datos_usuario)
            self.adUsuarios.show()
        elif sender_button_Cli == self.botFacAdm:
            self.hide()
            self.adFacturas = AdminFacturacion()
            self.adFacturas.recibir_datos(self.datos_usuario)
            self.adFacturas.show()

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
        self.BusCli.set_callback(self.crear_ventana)
        self.BusCli.show()

    def crear_ventana(self, retorno):
        self.emer_retorno = emerRetorno()
        self.emer_retorno.imprimir_retorno(retorno)
        self.emer_retorno.show()

    def imprimir_tablas (self):
        pass

    def recibir_datos (self, usuario_validar):
        self.datos_usuario = usuario_validar

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

        self.botBusFacDoc.clicked.connect(self.open_view_eme_BusFac)
        self.botPagId.clicked.connect(self.open_view_eme_PagFacId)
        self.botPagDoc.clicked.connect(self.open_view_eme_PagFacDoc)
        self.botCreFac.clicked.connect(self.open_view_eme_CreFac)


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
            self.adServicios.recibir_datos(self.datos_usuario)
            self.adServicios.show()
        elif sender_button_Fac == self.botInvAdm:
            self.hide()
            self.adInventario = AdminInventario()
            self.adInventario.recibir_datos(self.datos_usuario)
            self.adInventario.show()
        elif sender_button_Fac == self.botInfAdm:
            self.hide()
            self.adInformes = AdminInformes()
            self.adInformes.recibir_datos(self.datos_usuario)
            self.adInformes.show()
        elif sender_button_Fac == self.botAgeAdm:
            self.hide()
            self.adAgenda = AdminAgenda()
            self.adAgenda.recibir_datos(self.datos_usuario)
            self.adAgenda.show()
        elif sender_button_Fac == self.botCliAdm:
            self.hide()
            self.adClientes = AdminClientes()
            self.adClientes.recibir_datos(self.datos_usuario)
            self.adClientes.show()
        elif sender_button_Fac == self.botUsuAdm:
            self.hide()
            self.adUsuarios = AdminUsuarios()
            self.adUsuarios.recibir_datos(self.datos_usuario)
            self.adUsuarios.show()
        elif sender_button_Fac == self.botFacAdm:
            self.hide()
            self.adFacturas = AdminFacturacion()
            self.adFacturas.show()


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
            self.adServicios.recibir_datos(self.datos_usuario)
            self.adServicios.show()
        elif sender_button_Inf == self.botInvAdm:
            self.hide()
            self.adInventario = AdminInventario()
            self.adInventario.recibir_datos(self.datos_usuario)
            self.adInventario.show()
        elif sender_button_Inf == self.botInfAdm:
            self.hide()
            self.adInformes = AdminInformes()
            self.adInventario.recibir_datos(self.datos_usuario)
            self.adInformes.show()
        elif sender_button_Inf == self.botAgeAdm:
            self.hide()
            self.adAgenda = AdminAgenda()
            self.adAgenda.recibir_datos(self.datos_usuario)
            self.adAgenda.show()
        elif sender_button_Inf == self.botCliAdm:
            self.hide()
            self.adClientes = AdminClientes()
            self.adClientes.recibir_datos(self.datos_usuario)
            self.adClientes.show()
        elif sender_button_Inf == self.botUsuAdm:
            self.hide()
            self.adUsuarios = AdminUsuarios()
            self.adUsuarios.recibir_datos(self.datos_usuario)
            self.adUsuarios.show()
        elif sender_button_Inf == self.botFacAdm:
            self.hide()
            self.adFacturas = AdminFacturacion()
            self.adFacturas.recibir_datos(self.datos_usuario)
            self.adFacturas.show()


    def open_view_IngPro(self):
        self.IngPro = emerBusInfPro()
        self.IngPro.set_callback(self.imprimir_tablas)
        self.IngPro.show()

    def open_view_IngSer(self):
        self.IngSer = emerBusInfSer()
        self.IngSer.set_callback(self.imprimir_tablas)
        self.IngSer.show()

    def open_view_Des(self):
        self.IngSer = emerBusInfSer()
        self.IngSer.set_callback(self.imprimir_tablas)
        self.IngSer.show()

    def crear_ventana(self, retorno):
        self.emer_retorno = emerRetorno()
        self.emer_retorno.imprimir_retorno(retorno)
        self.emer_retorno.show()

    def imprimir_tablas(self, listas):
        pass

    def recibir_datos (self, usuario_validar):
        self.datos_usuario = usuario_validar


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

        self.botAgrUsu.clicked.connect(self.open_view_emer_cre_usu)
        self.botBusUsu.clicked.connect(self.open_view_emer_cre_usu)
        self.botCamCon.clicked.connect(self.open_view_emer_cam_con)
        self.botMosTod.clicked.connect(self.open_view_emer_cre_usu)

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
            self.adServicios.recibir_datos(self.datos_usuario)
            self.adServicios.show()
        elif sender_button_Usu == self.botInvAdm:
            self.hide()
            self.adInventario = AdminInventario()
            self.adInventario.recibir_datos(self.datos_usuario)
            self.adInventario.show()
        elif sender_button_Usu == self.botInfAdm:
            self.hide()
            self.adInformes = AdminInformes()
            self.adInformes.recibir_datos(self.datos_usuario)
            self.adInformes.show()
        elif sender_button_Usu == self.botAgeAdm:
            self.hide()
            self.adAgenda = AdminAgenda()
            self.adAgenda.recibir_datos(self.datos_usuario)
            self.adAgenda.show()
        elif sender_button_Usu == self.botCliAdm:
            self.hide()
            self.adClientes = AdminClientes()
            self.adClientes.recibir_datos(self.datos_usuario)
            self.adClientes.show()
        elif sender_button_Usu == self.botUsuAdm:
            self.hide()
            self.adUsuarios = AdminUsuarios()
            self.adUsuarios.recibir_datos(self.datos_usuario)
            self.adUsuarios.show()
        elif sender_button_Usu == self.botFacAdm:
            self.hide()
            self.adFacturas = AdminFacturacion()
            self.adFacturas.recibir_datos(self.datos_usuario)
            self.adFacturas.show()


    def open_view_emer_cre_usu (self):
        self.creUsu = emerAgrUsu()
        self.creUsu.set_callback(self.crear_ventana)
        self.creUsu.recibir_datos(self.datos_usuario)
        self.creUsu.show()

    def open_view_emer_cam_con(self):
        self.camCon = emerCamCon()
        self.camCon.set_callback(self.crear_ventana)
        self.camCon.recibir_datos(self.datos_usuario)
        self.camCon.show()

    def open_view_emer_bus_usu(self):
        self.busUsu = emerBuscUsu()
        self.busUsu.set_callback(self.imprimir_tablas)
        self.busUsu.recibir_datos(self.datos_usuario)
        self.busUsu.show()

    def crear_ventana(self, retorno):
        self.emer_retorno = emerRetorno()
        self.emer_retorno.imprimir_retorno(retorno)
        self.emer_retorno.show()

    def imprimir_tablas(self, listas):
        pass
    def recibir_datos(self, usuario_validar):
        self.datos_usuario = usuario_validar
        print(self.datos_usuario) '''