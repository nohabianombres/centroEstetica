from PyQt5.QtWidgets import QApplication, QMainWindow

import sys
from Front.cajero import *
from Front.comunes.emerComunes import emerRetorno, emerBuscPro, emerAgrCli, emerBusFac, emerCreFac, emerPagFacId, emerPagFacDoc, emerBuscClien, emerAdiFal,emerAgrProFac
from Back.Inventario import Inventario
from Back.Facturas import Facturas
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
        self.botCerCaj.clicked.connect(self.cerrar_sesion)

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
        self.CreFac = emerCreFac()
        self.CreFac.set_callback(self.proceso_factura)
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
        self.BusFac = emerBusFac()
        self.BusFac.set_callback(self.imprimir_tablas)
        self.BusFac.show()

    def imprimir_tablas(self, listas):
        self.TabFacturas.clearContents()
        print(listas)
        self.TabFacturas.show()
        if listas != None:
            fila = 0
            self.TabFacturas.setRowCount(len(listas))
            for elementos in listas:
                print(elementos)
                self.TabFacturas.setItem(fila, 0, QtWidgets.QTableWidgetItem((str(elementos[0]))))
                self.TabFacturas.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(elementos[1].strftime("%H:%M"))))
                self.TabFacturas.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(elementos[2].strftime("%Y-%m-%d"))))
                self.TabFacturas.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(elementos[3])))
                self.TabFacturas.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(elementos[4])))
                self.TabFacturas.setItem(fila, 5, QtWidgets.QTableWidgetItem(str(elementos[5])))
                self.TabFacturas.setItem(fila, 6, QtWidgets.QTableWidgetItem(str(elementos[6])))
                self.TabFacturas.setItem(fila, 7, QtWidgets.QTableWidgetItem(str(elementos[7])))
                self.TabFacturas.setItem(fila, 8, QtWidgets.QTableWidgetItem(str(elementos[8])))
                self.TabFacturas.setItem(fila, 9, QtWidgets.QTableWidgetItem(str(elementos[9])))
                self.TabFacturas.setItem(fila, 10, QtWidgets.QTableWidgetItem(str(elementos[10].strftime("%Y-%m-%d"))))
                self.TabFacturas.setItem(fila, 11, QtWidgets.QTableWidgetItem(str(elementos[11].strftime("%H:%M"))))
                fila = fila + 1
        else:
            print('no encontre')

    def crear_ventana(self, retorno):
        self.emer_retorno = emerRetorno()
        self.emer_retorno.imprimir_retorno(retorno)
        self.emer_retorno.show()

    def recibir_datos(self, usuario_validar):
        self.datos_usuario = usuario_validar

    def proceso_factura(self, datos):
        self.cliente_cobrar = datos[0]
        self.id_citas_cobrar = datos[1]
        self.nombres_servicio = datos[2]
        self.precios_servicio = datos[3]
        print('llegue a proceso factura')
        self.hide()
        self.facProceso = AdminProcesoFactura()
        self.facProceso.recibir_datos(self.datos_usuario, self.cliente_cobrar, self.id_citas_cobrar,
                                      self.nombres_servicio, self.precios_servicio)
        self.facProceso.show()

    def cerrar_sesion(self):
        quit()


class AdminProcesoFactura(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(AdminProcesoFactura, self).__init__(parent)
        uic.loadUi('Front/cajero/cajeroFacturacionAgregarPro.ui', self)


        self.botCliCaj.clicked.connect(self.open_view_caj_fac)
        self.botFacCaj.clicked.connect(self.open_view_caj_fac)
        self.botInvCaj.clicked.connect(self.open_view_caj_fac)
        self.botCerCaj.clicked.connect(self.cerrar_sesion)

        self.botAgrProFac.clicked.connect(self.agregar_producto_factura)
        self.botCreFac.clicked.connect(self.generar_factura)
        self.botCerAdm.clicked.connect(self.cerrar_sesion)

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
            self.cajClien = CajeroClientes()
            self.cajClien.recibir_datos(self.datos_usuario)
            self.cajClien.show()

    def recibir_datos(self, usuario_validar, cliente_cobrar, id_citas_cobrar, nombres_servicio, precios_servicio):
        self.datos_usuario = usuario_validar
        self.cliente_facturar = cliente_cobrar
        self.id_citas = id_citas_cobrar
        self.nom_ser = nombres_servicio
        self.pre_ser = precios_servicio
        self.imprimir_tabla_ser(cliente_cobrar, id_citas_cobrar, nombres_servicio, precios_servicio)
        self.fila = 0

    def imprimir_tabla_ser (self, cliente_cobrar, id_citas_cobrar, nombres_servicio, precios_servicio ):
        self.TabServicios.clearContents()
        self.TabServicios.show()
        if cliente_cobrar != None:
            fila = 0
            self.TabServicios.setRowCount(len(nombres_servicio))
            for citas, nombres, precios in zip(id_citas_cobrar, nombres_servicio, precios_servicio):
                self.TabServicios.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(cliente_cobrar)))
                self.TabServicios.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(nombres)))
                self.TabServicios.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(precios)))
                fila = fila + 1
        else:
            print('no encontre')


    def imprimir_tabla_pro(self, datos):

        self.TabInventario.clearContents()
        self.pres_pro = []
        self.pres_pro.append(datos[3])
        self.noms_pro = []
        self.noms_pro.append(datos[2])
        self.cans_pro = []
        self.cans_pro.append(datos[4])
        self.ids_pro = []
        self.ids_pro.append(datos[1])
        self.fila = 0
        self.TabInventario.setRowCount(len(self.ids_pro))
        for id, nombre, precio, cantidad  in zip(self.ids_pro, self.noms_pro, self.pres_pro, self.cans_pro):
            self.TabInventario.setItem(self.fila, 0, QtWidgets.QTableWidgetItem(str(id)))
            self.TabInventario.setItem(self.fila, 1, QtWidgets.QTableWidgetItem(str(nombre)))
            self.TabInventario.setItem(self.fila, 2, QtWidgets.QTableWidgetItem(str(precio)))
            self.TabInventario.setItem(self.fila, 3, QtWidgets.QTableWidgetItem(str(cantidad)))
            self.fila = self.fila + 1
        else:
            print('no encontre')

    def agregar_producto_factura (self):
        self.agr_pro_fac = emerAgrProFac()
        self.agr_pro_fac.set_callback(self.imprimir_tabla_pro)
        self.agr_pro_fac.show()


    def generar_factura (self):
        self.ids_pro = []
        self.facturas = Facturas()
        self.retorno_creacion = self.facturas.agr_fac_con_ser(self.pres_pro, self.noms_pro, self.cans_pro, self.id_pro, self.id_citas, self.cliente_facturar, self.nom_ser, self.pre_ser)
        self.crear_ventana(self.retorno_creacion)

    def crear_ventana(self, retorno):
        self.emer_retorno = emerRetorno()
        self.emer_retorno.imprimir_retorno(retorno)
        self.emer_retorno.show()

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
        self.BusPro.set_callback(self.imprimir_tabla)
        self.BusPro.show()

    def open_view_eme_MosTodPro(self):
        self.inventario = Inventario()
        inv_comp = self.inventario.consultar_inverntario()
        self.imprimir_tabla_filas(inv_comp)

    def crear_ventana(self, retorno):
        self.emer_retorno = emerRetorno()
        self.emer_retorno.imprimir_retorno(retorno)
        self.emer_retorno.show()

    def imprimir_tabla(self, lista):
        self.TabInventario.clearContents()
        print(lista)
        self.TabInventario.show()
        self.TabInventario.setRowCount(1)
        if lista != None:
            fila = 0
            self.TabInventario.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(lista[0])))
            self.TabInventario.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(lista[1])))
            self.TabInventario.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(lista[2])))
            self.TabInventario.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(lista[3])))

        else:
            print('no encontre')

    def imprimir_tabla_filas(self, listas):
        print(listas)
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
