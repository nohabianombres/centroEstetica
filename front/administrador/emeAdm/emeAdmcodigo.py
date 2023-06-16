from PyQt5.QtWidgets import QApplication, QMainWindow


import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication
from Back.Inventario import Inventario
from Back.Servicios import Servicios
from Back.Informes import Informe
from Back.Usuarios import Administracion

class emerModSer(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerModSer, self).__init__(parent)
        uic.loadUi('Front/administrador/emeAdm/emerModSer.ui', self)

        self.botModSer.clicked.connect(self.modificar_precio_servicio_funcion)
        self.botCanModSer.clicked.connect(self.cancelar_agregar_producto)

    def modificar_precio_servicio_funcion(self):
        self.id_ser = self.LIdSerMod.text()
        self.pre_nue = self.LPreNueSer.text()
        self.hide()
        self.servicio = Servicios ()
        self.retorno_mod_ser = self.servicio.modificar_servicios(self.id_ser, self.pre_nue)
        if self.callback:
            self.callback(self.retorno_mod_ser)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_agregar_producto(self):
        self.hide()
        self.close()

class emerModProCan(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerModProCan, self).__init__(parent)
        uic.loadUi('Front/administrador/emeAdm/emerModProCan.ui', self)

        self.botModPro.clicked.connect(self.modificar_cantidad_prodcuto_funcion)
        self.botCanModPro.clicked.connect(self.cancelar_modificar_producto)

    def modificar_cantidad_prodcuto_funcion(self):
        self.id_pro = self.LIdProMod.text()
        self.can_nue = self.LCanNuePro.text()
        self.hide()
        self.inventario = Inventario ()
        self.retorno_mod_can_pro = self.inventario.agregar_cantidad_inventario(self.id_pro, self.can_nue)
        if self.callback:
            self.callback(self.retorno_mod_can_pro)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_modificar_producto(self):
        self.hide()
        self.close()

class emerModProPre(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerModProPre, self).__init__(parent)
        uic.loadUi('Front/administrador/emeAdm/emerModProPre.ui', self)

        self.botModPro.clicked.connect(self.modificar_precio_producto_funcion)
        self.botCanModPro.clicked.connect(self.cancelar_modificar_producto)

    def modificar_precio_producto_funcion(self):
        self.id_pro = self.LIdProMod.text()
        self.pre_nue = self.LPreNuePro.text()
        self.hide()
        self.inventario = Inventario()
        self.retorno_mod_pre_pro = self.inventario.cambiar_precio_producto(self.id_pro, self.pre_nue)
        if self.callback:
            self.callback(self.retorno_mod_pre_pro)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_modificar_producto(self):
        self.hide()
        self.close()

class emerCamCon(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerCamCon, self).__init__(parent)
        uic.loadUi('Front/administrador/emeAdm/emerCamCon.ui', self)

        self.CamCon.clicked.connect(self.cambiar_contrasena_funcion)
        self.CanCamCon.clicked.connect(self.cancelar_cambiar_contrasena)

    def cambiar_contrasena_funcion(self):
        print('entre a agregar usuario funcion')
        self.id_usu = self.LUsuCamCon.text()
        self.nue_con = self.LConNue.text()
        self.hide()
        self.retorno_cam_con = self.instancia.cambiar_contrasena(self.id_usu, self.nue_con)

        if self.callback:
            self.callback(self.retorno_cam_con)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_cambiar_contrasena(self):
        self.hide()
        self.close()

    def recibir_datos(self, usuario_validar):
        self.datos_usuario = usuario_validar
        self.instancia = Administracion(self.datos_usuario[0], self.datos_usuario[1], self.datos_usuario[2],self.datos_usuario[3], self.datos_usuario[4], self.datos_usuario[5],self.datos_usuario[6], self.datos_usuario[7])


class emerAgrUsu(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerAgrUsu, self).__init__(parent)
        uic.loadUi('Front/administrador/emeAdm/emerAgrUsu.ui', self)

        self.botAgrUsu.clicked.connect(self.agregar_usuario_funcion)
        self.botCanAgrUsu.clicked.connect(self.cancelar_agregar_usuario)

    def agregar_usuario_funcion(self):
        print('entre a agregar usuario funcion')
        self.nom_usu = self.LNomUsuAgr.text()
        self.ape_usu = self.LApeUsuAgr.text()
        self.doc_usu = self.LDocUsuAgr.text()
        self.pasw_usu = self.LConUsuAgr.text()
        self.cor_usu = self.LCorUsuAgr.text()
        self.rol_usu = self.LRolUsuAgr.text()
        self.tel_usu = self.LTelUsuAgr.text()
        self.hide()
        self.retorno_agregar_usu = self.instancia.crear_usuarios(self.pasw_usu,self.doc_usu, self.nom_usu, self.ape_usu, self.tel_usu, self.cor_usu, self.rol_usu)


        if self.callback:
            self.callback(self.retorno_agregar_usu)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_agregar_usuario(self):
        self.hide()
        self.close()

    def recibir_datos(self, usuario_validar):
        self.datos_usuario = usuario_validar
        self.instancia = Administracion(self.datos_usuario[0], self.datos_usuario[1], self.datos_usuario[2], self.datos_usuario[3], self.datos_usuario[4], self.datos_usuario[5], self.datos_usuario[6], self.datos_usuario[7])
        print(self.instancia)

class emerAgrPro(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerAgrPro, self).__init__(parent)
        uic.loadUi('Front/administrador/emeAdm/emerAgrPro.ui', self)

        self.botAgrPro.clicked.connect(self.agregar_producto_funcion)
        self.botCanAgrPro.clicked.connect(self.cancelar_agregar_producto)

    def agregar_producto_funcion(self):
        self.nom_pro = self.LAgrNomPro.text()
        self.pre_pro = self.LAgrPrePro.text()
        self.can_pro = self.LAgrCanPro.text()
        self.hide()
        self.inventario = Inventario()
        self.retorno_agre_inv = self.inventario.agregar_nuevo_producto(self.nom_pro, self.can_pro, self.pre_pro)
        if self.callback:
            self.callback(self.retorno_agre_inv)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_agregar_producto(self):
        self.hide()
        self.close()

class emerAgrSer(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerAgrSer, self).__init__(parent)
        uic.loadUi('Front/administrador/emeAdm/emerAgrSer.ui', self)

        self.AgrSer.clicked.connect(self.agregar_servicio_funcion)
        self.CanAgrSer.clicked.connect(self.cancelar_agregar_servicio)

    def agregar_servicio_funcion(self):
        self.nom_ser = self.LNomSerAgr.text()
        self.pre_ser = self.LPreSerAgr.text()
        self.tie_pro = self.LTiePro.text()
        self.hide()
        self.servicio = Servicios ()
        self.retorno_agr_ser = self.servicio.agregar_servicio(self.nom_ser, self.tie_pro, self.pre_ser)
        if self.callback:
            self.callback(self.retorno_agr_ser)

    def set_callback(self, callback):
        self.callback = callback

    def cancelar_agregar_servicio(self):
        self.hide()
        self.close()

class emerBusInfPro(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerBusInfPro, self).__init__(parent)
        uic.loadUi('Front/administrador/emeAdm/emerDiaDes.ui', self)

        self.botBusInf.clicked.connect(self.buscar_informe_pro)
        self.botCanBusInf.clicked.connect(self.cancelar_buscar_informe_pro)

    def buscar_informe_pro(self):
        print('llegue a buscar informe productos')
        self.dia_bus_inf = self.LNumDiaInf.text()
        self.hide()
        self.mostrar_informe(self.dia_bus_inf)

    def cancelar_buscar_informe_pro(self):
        self.hide()
        self.close()

    def mostrar_informe (self, dias):
        self.mosPro = emerProductos()
        self.mosPro.buscar_informe_pro(dias)
        self.mosPro.show()


class emerProductos(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerProductos, self).__init__(parent)
        uic.loadUi('Front/administrador/emeAdm/emerProductos.ui', self)

    def buscar_informe_pro(self, dias):
        print('llegue a inf_des')
        self.informe = Informe()
        self.retorno_bus_inf = self.informe.informe_productos(dias)
        print(self.retorno_bus_inf)

        self.imprimir_tabla_pro(self.retorno_bus_inf)

    def imprimir_tabla_pro(self, listas):
        self.TabProductos.clearContents()
        print(listas)
        self.TabProductos.show()
        if listas != None:
            fila = 0
            self.TabProductos.setRowCount(len(listas))
            for elementos in listas:
                print(elementos)
                self.TabProductos.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(elementos[0])))
                self.TabProductos.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(elementos[1])))
                self.TabProductos.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(elementos[2])))
                self.TabProductos.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(elementos[3])))
                self.TabProductos.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(elementos[4])))
                self.TabProductos.setItem(fila, 5, QtWidgets.QTableWidgetItem(str(elementos[5])))
                self.TabProductos.setItem(fila, 6, QtWidgets.QTableWidgetItem(str(elementos[6])))
                self.TabProductos.setItem(fila, 7, QtWidgets.QTableWidgetItem(str(elementos[7])))
                fila = fila + 1
        else:
            print('no encontre')

class emerBusInfSer(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerBusInfSer, self).__init__(parent)
        uic.loadUi('Front/administrador/emeAdm/emerDiaDes.ui', self)

        self.botBusInf.clicked.connect(self.buscar_informe_ser)
        self.botCanBusInf.clicked.connect(self.cancelar_buscar_informe_ser)

    def buscar_informe_ser(self):
        print('llegue a buscar informe productos')
        self.dia_bus_inf = self.LNumDiaInf.text()
        self.hide()
        self.mostrar_informe(self.dia_bus_inf)

    def cancelar_buscar_informe_ser(self):
        self.hide()
        self.close()

    def mostrar_informe (self, dias):
        self.mosPro = emerServicios()
        self.mosPro.buscar_informe_ser(dias)
        self.mosPro.show()

class emerServicios(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerServicios, self).__init__(parent)
        uic.loadUi('Front/administrador/emeAdm/emerServicios.ui', self)

    def buscar_informe_ser(self, dias):
        self.informe = Informe()
        self.retorno_bus_inf = self.informe.informe_servicios(dias)
        print(self.retorno_bus_inf)

        self.imprimir_tabla_ser(self.retorno_bus_inf)

    def imprimir_tabla_ser(self, listas):
        self.TabServicios.clearContents()
        print(listas)
        self.TabServicios.show()
        if listas != None:
            fila = 0
            self.TabServicios.setRowCount(len(listas))
            for elementos in listas:
                print(elementos)
                self.TabServicios.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(elementos[0])))
                self.TabServicios.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(elementos[1])))
                self.TabServicios.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(elementos[2])))
                self.TabServicios.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(elementos[3])))
                self.TabServicios.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(elementos[4])))
                self.TabServicios.setItem(fila, 5, QtWidgets.QTableWidgetItem(str(elementos[5])))
                self.TabServicios.setItem(fila, 6, QtWidgets.QTableWidgetItem(str(elementos[6])))

                fila = fila + 1
        else:
            print('no encontre')

class emerDesempeno(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerDesempeno, self).__init__(parent)
        uic.loadUi('Front/administrador/emeAdm/emerDesem.ui', self)

        self.botAct.clicked.connect(self.buscar_informe_des)

    def buscar_informe_des(self):
        print('llegue a inf_des')
        self.informe = Informe()
        self.retorno_bus_inf = self.informe.mostrar_desempeno()
        print(self.retorno_bus_inf)

        self.imprimir_tabla_des(self.retorno_bus_inf)

    def imprimir_tabla_des(self, listas):
        self.TabDesempeno.clearContents()
        print(listas)
        self.TabDesempeno.show()
        if listas != None:
            fila = 0
            self.TabDesempeno.setRowCount(len(listas))
            for elementos in listas:
                print(elementos)
                self.TabDesempeno.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(elementos[0])))
                self.TabDesempeno.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(elementos[1])))
                self.TabDesempeno.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(elementos[2])))
                self.TabDesempeno.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(elementos[3])))
                self.TabDesempeno.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(elementos[4])))
                self.TabDesempeno.setItem(fila, 5, QtWidgets.QTableWidgetItem(str(elementos[5])))
                fila = fila + 1
        else:
            print('no encontre')
