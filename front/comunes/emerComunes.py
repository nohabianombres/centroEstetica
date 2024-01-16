import sys
import path

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidget


from Back.Clientes import Clientes
from Back.Agenda import Agendas
from Back.Servicios import Servicios
from Back.Facturas import Facturas
from Back.Inventario import Inventario

from PyQt5 import QtWidgets, uic
from Back.Usuarios import Cajero,Administracion, Recepcion, Trabajadores

class emerAdiFal(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerAdiFal, self).__init__(parent)
        uic.loadUi('Front/comunes/emerAdiFalta.ui', self)

        self.EmerAdiFalta.clicked.connect(self.adicionar_falta)
        self.CanAdiFal.clicked.connect(self.cancelar_agregar_falta)
        self.documento_falta = None

    def adicionar_falta (self):
        self.documento_falta = self.lineEdit.text()
        self.hide()
        self.cliente = Clientes()
        self.retorno_adi_fal = self.cliente.adicionar_falta_cliente(self.documento_falta)
        if self.callback:
            self.callback(self.retorno_adi_fal)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_agregar_falta(self):
        self.hide()
        self.close()

class emerAgrCita(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerAgrCita, self).__init__(parent)
        uic.loadUi('Front/comunes/emerAgrCita.ui', self)

        self.AgrCit.clicked.connect(self.agregar_cita_funcion)
        self.CanAgrCit.clicked.connect(self.cancelar_agregar_cita)

    def agregar_cita_funcion (self):
        self.doc_cli = self.LDocCli.text()
        self.id_ser = self.LIdSer.text()
        self.id_tra = self.LIdTra.text()
        self.fec_cit = self.fechaCita.text()
        self.hor_cit = self.horaCita.text()
        self.hide()
        self.agenda = Agendas()
        hora = '11:00:00'
        self.retorno_agr_cit = self.agenda.crear_cita(self.hor_cit, self.fec_cit, self.doc_cli, self.id_tra, self.id_ser)
        if self.callback:
            self.callback(self.retorno_agr_cit)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_agregar_cita(self):
        self.hide()
        self.close()

class emerAgrCli(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerAgrCli, self).__init__(parent)
        uic.loadUi('Front/comunes/emerAgrClien.ui', self)

        self.AgrCli.clicked.connect(self.agregar_cliente_funcion)
        self.CanAgrCli.clicked.connect(self.cancelar_agregar_cliente)

    def agregar_cliente_funcion(self):
        self.doc_cli_agr = self.LDocCliAgr.text()
        self.nom_cli = self.LNomCliAgr.text()
        self.ape_cli = self.LApeCliAgr.text()
        self.tel_cli = self.LTelCliAgr.text()
        self.cor_cli = self.LCorCliAgr.text()
        self.hide()
        self.cliente = Clientes()
        self.retorno_agr_cli = self.cliente.crear_clientes(self.doc_cli_agr,self.nom_cli, self.ape_cli, self.tel_cli, self.cor_cli)
        if self.callback:
            self.callback(self.retorno_agr_cli)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_agregar_cliente(self):
        self.hide()
        self.close()

class emerConfirmar(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerConfirmar, self).__init__(parent)
        uic.loadUi('Front/comunes/emerConfirmar.ui', self)

class emerBuscClien(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerBuscClien, self).__init__(parent)
        uic.loadUi('Front/comunes/emerBuscClien.ui', self)

        self.BusCli.clicked.connect(self.buscar_cliente_funcion)
        self.CanBusCli.clicked.connect(self.cancelar_buscar_cliente)

    def buscar_cliente_funcion(self):
        self.doc_cli_bus = self.LDocCliBus.text()
        self.hide()
        self.cliente = Clientes()
        self.retorno_bus_cli = self.cliente.verificar_cliente(self.doc_cli_bus)
        if self.callback:
            self.callback(self.retorno_bus_cli)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_buscar_cliente(self):
        self.hide()
        self.close()

class emerBusCitas(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(emerBusCitas, self).__init__(parent)
        uic.loadUi('Front/comunes/emerBusCitas.ui', self)

        self.BusCit.clicked.connect(self.buscar_cita_funcion)
        self.CanBusCit.clicked.connect(self.cancelar_buscar_cita)
        self.callback = None

    def buscar_cita_funcion(self):
        self.doc_cit_bus = self.LDocBusCit.text()
        self.hide()
        self.agenda = Agendas()
        self.citas_encontradas = self.agenda.consultar_citas(self.doc_cit_bus)
        print(self.citas_encontradas)
        if self.callback:
            self.callback(self.citas_encontradas)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_buscar_cita(self):
        self.hide()
        self.close()

class emerBuscPro(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerBuscPro, self).__init__(parent)
        uic.loadUi('Front/comunes/emerBuscPro.ui', self)

        self.botBusPro.clicked.connect(self.buscar_producto_funcion)
        self.botCanBusPro.clicked.connect(self.cancelar_buscar_producto)

    def buscar_producto_funcion(self):
        self.id_pro_bus = self.LIdProBus.text()
        self.hide()
        print('entre a la instancia de emerBuscPro')
        self.inventario = Inventario()
        self.retorno_bus_pro = self.inventario.verificar_producto(self.id_pro_bus)

        if self.callback:
            self.callback(self.retorno_bus_pro)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_buscar_producto(self):
        self.hide()
        self.close()

class emerBuscSer(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerBuscSer, self).__init__(parent)
        uic.loadUi('Front/comunes/emerBuscSer.ui', self)

        self.botBusSer.clicked.connect(self.buscar_servicio_funcion)
        self.botCanBusSer.clicked.connect(self.cancelar_buscar_servicio)

    def buscar_servicio_funcion(self):
        self.id_ser_bus = self.LIdBusSer.text()
        self.hide()
        self.servicio = Servicios ()
        self.retorno_bus_ser = self.servicio.verificar_servicio(self.id_ser_bus)
        if self.callback:
            self.callback(self.retorno_bus_ser)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_buscar_servicio(self):
        self.hide()
        self.close()

class emerBuscUsu(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerBuscUsu, self).__init__(parent)
        uic.loadUi('Front/comunes/emerBuscUsu.ui', self)

        self.botBusUsu.clicked.connect(self.buscar_usuario_funcion)
        self.botCanBusUsu.clicked.connect(self.cancelar_buscar_usuario)

    def buscar_usuario_funcion(self):
        self.id_usu = self.LUsuBus.text()
        self.hide()
        self.retorno_bus_usu = self.instancia.verificar_usuario(self.id_usu)
        print(self.retorno_bus_usu)
        if self.callback:
            self.callback(self.retorno_bus_usu)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_buscar_usuario(self):
        self.hide()
        self.close()

    def recibir_datos(self, usuario_validar):
        self.datos_usuario = usuario_validar
        self.instancia = Administracion(self.datos_usuario[0], self.datos_usuario[1], self.datos_usuario[2], self.datos_usuario[3], self.datos_usuario[4], self.datos_usuario[5], self.datos_usuario[6], self.datos_usuario[7])

class emerCanCita(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerCanCita, self).__init__(parent)
        uic.loadUi('Front/comunes/emerCanCita.ui', self)

        self.botConCanCit.clicked.connect(self.cancelar_cita_funcion)
        self.botCanCanCit.clicked.connect(self.cancelar_cancelar_cita)

    def cancelar_cita_funcion(self):
        self.doc_cit_can = self.LDocCanCit.text()
        self.agenda = Agendas()
        self.retorno_doc_can_cit = self.agenda.cancelar_cita(self.doc_cit_can)
        if self.callback:
            self.callback(self.retorno_doc_can_cit)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_cancelar_cita(self):
        self.hide()
        self.close()

class emerCanCitaId(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerCanCitaId, self).__init__(parent)
        uic.loadUi('Front/comunes/emerCanCitaId.ui', self)

        self.botConCanCit.clicked.connect(self.cancelar_cita_funcion)
        self.botCanCanCit.clicked.connect(self.cancelar_cancelar_cita)

    def cancelar_cita_funcion(self):
        self.id_cit_can = self.LIdCanCit.text()
        self.agenda = Agendas()
        self.hide()
        self.retorno_can_cit = self.agenda.cancelar_cita_exacta(self.id_cit_can)
        if self.callback:
            self.callback(self.retorno_can_cit)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_cancelar_cita(self):
        self.hide()
        self.close()

class emerRetorno(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerRetorno, self).__init__(parent)
        uic.loadUi('Front/comunes/EmerRetorno.ui', self)

        self.botOk.clicked.connect(self.funcion_ok)

    def imprimir_retorno (self, retorno_emer):
        self.LRet.setText(retorno_emer)

    def funcion_ok (self):
        self.close()

class emerPagFacId(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(emerPagFacId, self).__init__(parent)
        uic.loadUi('Front/comunes/emerGenPag.ui', self)

        self.botGenPag.clicked.connect(self.generar_pago_funcion)
        self.botCanGenPag.clicked.connect(self.cancelar_generar_pago)
        self.callback = None

    def generar_pago_funcion(self):
        self.idFactura = self.LIdFacPag.text()
        self.hide()
        self.factura = Facturas()
        self.retorno_fac_cre = self.factura.pagar_facturas_idFactura(self.idFactura)
        if self.callback:
            self.callback(self.retorno_fac_cre)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_generar_pago(self):
        self.hide()
        self.close()

class emerBusFac(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(emerBusFac, self).__init__(parent)
        uic.loadUi('Front/comunes/emerBusFac.ui', self)

        self.botBusFac.clicked.connect(self.buscar_facturas_funcion)
        self.botCanBusFac.clicked.connect(self.cancelar_buscar_facturas)
        self.callback = None

    def buscar_facturas_funcion(self):
        self.doc_fac_bus = self.LDocBusFac.text()
        self.hide()
        self.factura = Facturas()
        self.retorno_bus_fac = self.factura.buscar_facturas_cliente(self.doc_fac_bus)
        if self.callback:
            self.callback(self.retorno_fac_cre)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_buscar_facturas(self):
        self.hide()
        self.close()

class emerValTot(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(emerValTot, self).__init__(parent)
        uic.loadUi('Front/comunes/emerValTot.ui', self)

        self.botPagar.clicked.connect(self.funcion_ok)

    def imprimir_retorno_2 (self, retorno_emer, variable_ok):
        print('llegue a imprimir_retorno_2')
        print(retorno_emer)
        print(variable_ok)
        self.LValTot.setText(str(retorno_emer))
        self.documento = variable_ok

    def funcion_ok (self):
        self.def_pag_facturas = Facturas()
        self.def_pag_facturas.pagar_facturas_documento_aceptar(self.documento)
        self.hide()

class emerPagFacDoc(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(emerPagFacDoc, self).__init__(parent)
        uic.loadUi('Front/comunes/emerGenPagDoc.ui', self)

        self.botGenPag.clicked.connect(self.generar_pago_funcion)
        self.botCanGenPag.clicked.connect(self.cancelar_generar_pago)
        self.callback = None

    def generar_pago_funcion(self):
        self.doc_fac_pag = self.LDocFacPag.text()
        self.hide()
        self.factura = Facturas()
        self.retorno_fac_pag = self.factura.pagar_facturas_documento(self.doc_fac_pag)
        self.crear_ventana_valor_total(self.retorno_fac_pag[0])

        #if self.callback:
            #self.callback(self.retorno_fac_cre)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_generar_pago(self):
        self.hide()
        self.close()

    def crear_ventana_valor_total(self, retorno):
        print('llegue crear_ventana_total')
        print(self.retorno_fac_pag[0])
        print(self.retorno_fac_pag[1])
        self.hide()
        self.emer_val_tol = emerValTot()
        self.emer_val_tol.imprimir_retorno_2(retorno, self.retorno_fac_pag[1])
        self.emer_val_tol.show()

class emerAgrProFac(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(emerAgrProFac, self).__init__(parent)
        uic.loadUi('Front/comunes/emerAgrProFac.ui', self)

        self.botAgrProFac.clicked.connect(self.agregar_producto_funcion)
        self.botCanAgrProFac.clicked.connect(self.cancelar_agregar_producto)

    def agregar_producto_funcion(self):
        self.id_pro_agr_fac = self.LIdProFac.text()
        self.can_pro_fac = self.LCanProFac.text()
        self.hide()
        self.facturas = Facturas()
        self.retorno_agr_pro = self.facturas.agr_pro_fac(self.id_pro_agr_fac, self.can_pro_fac)
        if self.callback:
            self.callback(self.retorno_agr_pro)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_agregar_producto(self):
        self.hide()
        self.close()

class emerCreFac(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(emerCreFac, self).__init__(parent)
        uic.loadUi('Front/comunes/emerCreFac.ui', self)

        self.botCreFac.clicked.connect(self.crear_factura_funcion)
        self.botCanCreFac.clicked.connect(self.cancelar_crear_factura)
        self.callback = None

    def crear_factura_funcion(self):
        self.doc_fac_cre = self.LDocCreFac.text()
        self.hide()
        self.factura = Facturas()
        self.retorno_fac_cre = self.factura.generar_factura_servicios_productos(self.doc_fac_cre)
        print(self.retorno_fac_cre)
        if self.callback:
            self.callback(self.retorno_fac_cre)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_crear_factura(self):
        self.hide()
        self.close()


'''
class emerModClien(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerModClien, self).__init__(parent)
        uic.loadUi('Front/comunes/emerModClien.ui', self)'''

'''from Back.Clientes import Clientes
from Back.Agenda import Agendas
from Back.Servicios import Servicios
from Back.Facturas import Facturas
from Back.Usuarios import *
from PyQt5 import QtWidgets, uic
from Back.Inventario import Inventario

class emerAdiFal(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerAdiFal, self).__init__(parent)
        uic.loadUi('Front/comunes/emerAdiFalta.ui', self)

        self.EmerAdiFalta.clicked.connect(self.adicionar_falta)
        self.CanAdiFal.clicked.connect(self.cancelar_agregar_falta)
        self.documento_falta = None

    def adicionar_falta (self):
        self.documento_falta = self.lineEdit.text()
        self.hide()
        self.cliente = Clientes()
        self.retorno_adi_fal = self.cliente.adicionar_falta_cliente(self.documento_falta)
        if self.callback:
            self.callback(self.retorno_adi_fal)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_agregar_falta(self):
        self.hide()
        self.close()

class emerAgrCita(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerAgrCita, self).__init__(parent)
        uic.loadUi('Front/comunes/emerAgrCita.ui', self)

        self.AgrCit.clicked.connect(self.agregar_cita_funcion)
        self.CanAgrCit.clicked.connect(self.cancelar_agregar_cita)

    def agregar_cita_funcion (self):
        self.doc_cli = self.LDocCli.text()
        self.id_ser = self.LIdSer.text()
        self.id_tra = self.LIdTra.text()
        self.fec_cit = self.fechaCita.text()
        self.hor_cit = self.horaCita.text()
        self.hide()
        self.agenda = Agendas()
        hora = '11:00:00'
        self.retorno_agr_cit = self.agenda.crear_cita(self.hor_cit, self.fec_cit, self.doc_cli, self.id_tra, self.id_ser)
        if self.callback:
            self.callback(self.retorno_agr_cit)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_agregar_cita(self):
        self.hide()
        self.close()

class emerAgrCli(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerAgrCli, self).__init__(parent)
        uic.loadUi('Front/comunes/emerAgrClien.ui', self)

        self.AgrCli.clicked.connect(self.agregar_cliente_funcion)
        self.CanAgrCli.clicked.connect(self.cancelar_agregar_cliente)

    def agregar_cliente_funcion(self):
        self.doc_cli_agr = self.LDocCliAgr.text()
        self.nom_cli = self.LNomCliAgr.text()
        self.ape_cli = self.LApeCliAgr.text()
        self.tel_cli = self.LTelCliAgr.text()
        self.cor_cli = self.LCorCliAgr.text()
        self.hide()
        self.cliente = Clientes()
        self.retorno_agr_cli = self.cliente.crear_clientes(self.doc_cli_agr,self.nom_cli, self.ape_cli, self.tel_cli, self.cor_cli)
        if self.callback:
            self.callback(self.retorno_agr_cli)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_agregar_cliente(self):
        self.hide()
        self.close()

class emerConfirmar(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerConfirmar, self).__init__(parent)
        uic.loadUi('Front/comunes/emerConfirmar.ui', self)

class emerBuscClien(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(emerBuscClien, self).__init__(parent)
        uic.loadUi('Front/comunes/emerBuscClien.ui', self)

        self.BusCli.clicked.connect(self.buscar_cliente_funcion)
        self.CanBusCli.clicked.connect(self.cancelar_buscar_cliente)

    def buscar_cliente_funcion(self):
        self.doc_cli_bus = self.LDocCliBus.text()
        self.hide()
        self.cliente = Clientes()
        self.retorno_bus_cli = self.cliente.verificar_cliente(self.doc_cli_bus)
        if self.callback:
            self.callback(self.retorno_bus_cli)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_buscar_cliente(self):
        self.hide()
        self.close()

class emerBusCitas(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(emerBusCitas, self).__init__(parent)
        uic.loadUi('Front/comunes/emerBusCitas.ui', self)

        self.BusCit.clicked.connect(self.buscar_cita_funcion)
        self.CanBusCit.clicked.connect(self.cancelar_buscar_cita)
        self.callback = None

    def buscar_cita_funcion(self):
        self.doc_cit_bus = self.LDocBusCit.text()
        self.hide()
        self.agenda = Agendas()
        self.citas_encontradas = self.agenda.consultar_citas(self.doc_cit_bus)
        print(self.citas_encontradas)
        if self.callback:
            self.callback(self.citas_encontradas)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_buscar_cita(self):
        self.hide()
        self.close()

class emerBuscPro(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerBuscPro, self).__init__(parent)
        uic.loadUi('Front/comunes/emerBuscPro.ui', self)

        self.botBusPro.clicked.connect(self.buscar_producto_funcion)
        self.botCanBusPro.clicked.connect(self.cancelar_buscar_producto)

    def buscar_producto_funcion(self):
        self.id_pro_bus = self.LIdProBus.text()
        self.hide()
        self.inventario = Inventario()
        self.retorno_bus_pro = self.inventario.verificar_producto(self.id_pro_bus)

        if self.callback:
            self.callback(self.retorno_bus_pro)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_buscar_producto(self):
        self.hide()
        self.close()

class emerBuscSer(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerBuscSer, self).__init__(parent)
        uic.loadUi('Front/comunes/emerBuscSer.ui', self)

        self.botBusSer.clicked.connect(self.buscar_servicio_funcion)
        self.botCanBusSer.clicked.connect(self.cancelar_buscar_servicio)

    def buscar_servicio_funcion(self):
        self.id_ser_bus = self.LIdBusSer.text()
        self.hide()
        self.servicio = Servicios ()
        self.retorno_bus_ser = self.servicio.verificar_servicio(self.id_ser_bus)
        if self.callback:
            self.callback(self.retorno_bus_ser)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_buscar_servicio(self):
        self.hide()
        self.close()

class emerBuscUsu(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerBuscUsu, self).__init__(parent)
        uic.loadUi('Front/comunes/emerBuscUsu.ui', self)

        self.botBusUsu.clicked.connect(self.buscar_usuario_funcion)
        self.botCanBusUsu.clicked.connect(self.cancelar_buscar_usuario)

    def buscar_usuario_funcion(self):
        self.id_usu = self.LUsuBus.text()
        self.hide()
        self.retorno_cam_con = self.instancia.verificar_usuario(self.id_usu)
        if self.callback:
            self.callback(self.retorno_cam_con)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_buscar_usuario(self):
        self.hide()
        self.close()

    def recibir_datos(self, usuario_validar):
        self.datos_usuario = usuario_validar
        self.instancia = Administracion(self.datos_usuario[0], self.datos_usuario[1], self.datos_usuario[2],self.datos_usuario[3], self.datos_usuario[4], self.datos_usuario[5],self.datos_usuario[6], self.datos_usuario[7])

class emerCanCita(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerCanCita, self).__init__(parent)
        uic.loadUi('Front/comunes/emerCanCita.ui', self)

        self.botConCanCit.clicked.connect(self.cancelar_cita_funcion)
        self.botCanCanCit.clicked.connect(self.cancelar_cancelar_cita)

    def cancelar_cita_funcion(self):
        self.doc_cit_can = self.LDocCanCit.text()
        self.agenda = Agendas()
        self.retorno_doc_can_cit = self.agenda.cancelar_cita(self.doc_cit_can)
        if self.callback:
            self.callback(self.retorno_doc_can_cit)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_cancelar_cita(self):
        self.hide()
        self.close()

class emerCanCitaId(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerCanCitaId, self).__init__(parent)
        uic.loadUi('Front/comunes/emerCanCitaId.ui', self)

        self.botConCanCit.clicked.connect(self.cancelar_cita_funcion)
        self.botCanCanCit.clicked.connect(self.cancelar_cancelar_cita)

    def cancelar_cita_funcion(self):
        self.id_cit_can = self.LIdCanCit.text()
        self.agenda = Agendas()
        self.retorno_can_cit = self.agenda.cancelar_cita_exacta(self.id_cit_can)
        if self.callback:
            self.callback(self.retorno_can_cit)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_cancelar_cita(self):
        self.hide()
        self.close()

class emerRetorno(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerRetorno, self).__init__(parent)
        uic.loadUi('Front/comunes/EmerRetorno.ui', self)

        self.botOk.clicked.connect(self.funcion_ok)

    def imprimir_retorno (self, retorno_emer):
        self.LRet.setText(retorno_emer)

    def funcion_ok (self):
        self.close()

class emerCreFac(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(emerCreFac, self).__init__(parent)
        uic.loadUi('Front/comunes/emerCreFac.ui', self)

        self.botCreFac.clicked.connect(self.crear_factura_funcion)
        self.botCanCreFac.clicked.connect(self.cancelar_crear_factura)
        self.callback = None

    def crear_factura_funcion(self):
        self.doc_fac_cre = self.LDocCreFac.text()
        self.hide()
        self.factura = Facturas()
        self.retorno_fac_cre = self.factura.generar_factura_servicios_productos(self.doc_fac_cre)
        if self.callback:
            self.callback(self.retorno_fac_cre)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_crear_factura(self):
        self.hide()
        self.close()

class emerPagFacId(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(emerPagFacId, self).__init__(parent)
        uic.loadUi('Front/comunes/emerGenPag.ui', self)

        self.botGenPag.clicked.connect(self.generar_pago_funcion)
        self.botCanGenPag.clicked.connect(self.cancelar_generar_pago)
        self.callback = None

    def generar_pago_funcion(self):
        self.idFactura = self.LIdFacPag.text()
        self.hide()
        self.factura = Facturas()
        self.retorno_fac_cre = self.factura.pagar_facturas_idFactura(self.idFactura)
        if self.callback:
            self.callback(self.retorno_fac_cre)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_generar_pago(self):
        self.hide()
        self.close()

class emerBusFac(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(emerBusFac, self).__init__(parent)
        uic.loadUi('Front/comunes/emerBusFac.ui', self)

        self.botBusFac.clicked.connect(self.buscar_facturas_funcion)
        self.botCanBusFac.clicked.connect(self.cancelar_buscar_facturas)
        self.callback = None

    def buscar_facturas_funcion(self):
        self.doc_fac_bus = self.LDocBusFac.text()
        self.hide()
        self.factura = Facturas()
        self.retorno_bus_fac = self.factura.buscar_facturas_cliente(self.doc_fac_bus)
        if self.callback:
            self.callback(self.retorno_fac_cre)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_buscar_facturas(self):
        self.hide()
        self.close()

class emerValTot(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(emerValTot, self).__init__(parent)
        uic.loadUi('Front/comunes/emerValTot.ui', self)

        self.botPagar.clicked.connect(self.funcion_ok)

    def imprimir_retorno_2 (self, retorno_emer, variable_ok):
        print('llegue a imprimir_retorno_2')
        print(retorno_emer)
        print(variable_ok)
        self.LValTot.setText(variable_ok)
        self.documento = variable_ok

    def funcion_ok (self):
        self.def_pag_facturas = Facturas()
        self.retorno_pago = self.def_pag_facturas.pagar_facturas_documento_aceptar(self.documento)
        if self.retorno_pago:
            self.crear_ventana(self.retorno_pago)

    def crear_ventana(self, retorno):
        self.hide()
        self.emer_retorno = emerRetorno()
        self.emer_retorno.imprimir_retorno(retorno)
        self.emer_retorno.show()

class emerPagFacDoc(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(emerPagFacDoc, self).__init__(parent)
        uic.loadUi('Front/comunes/emerGenPagDoc.ui', self)

        self.botGenPag.clicked.connect(self.generar_pago_funcion)
        self.botCanGenPag.clicked.connect(self.cancelar_generar_pago)
        self.callback = None

    def generar_pago_funcion(self):
        self.doc_fac_pag = self.LDocFacPag.text()
        self.hide()
        self.factura = Facturas()
        self.retorno_fac_pag = self.factura.pagar_facturas_documento(self.doc_fac_pag)
        self.crear_ventana_valor_total(self.retorno_fac_pag[0])

        #if self.callback:
            #self.callback(self.retorno_fac_cre)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_generar_pago(self):
        self.hide()
        self.close()

    def crear_ventana_valor_total(self, retorno):
        print('llegue crear_ventana_total')
        print(self.retorno_fac_pag[0])
        print(self.retorno_fac_pag[1])
        self.hide()
        self.emer_val_tol = emerValTot()
        self.emer_val_tol.imprimir_retorno_2(retorno, self.retorno_fac_pag[1])
        self.emer_val_tol.show()'''




