from PyQt5.QtWidgets import QApplication, QMainWindow


import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication

from Back.Inventario import *
from Back.Servicios import *
from Back.Informes import *

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

class emerAgrUsu(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerAgrUsu, self).__init__(parent)
        uic.loadUi('Front/administrador/emeAdm/emerAgrUsu.ui', self)

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
