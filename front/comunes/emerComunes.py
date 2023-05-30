
from Back.Facturas import *
from Back.Informes import *
from Back.Servicios import *
from Back.Usuarios import *
from Back.Inventario import *
from BD.Conexion import *
from Back.Agenda import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import os
import sys

# Obtener la ruta absoluta del directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Obtener la ruta absoluta del directorio "Back" dentro de "centrodeestetica"
back_dir = os.path.join(current_dir, "...", "Back")

# Agregar el directorio "Back" al path de búsqueda de módulos
sys.path.append(back_dir)

# Importar la clase "Clientes" desde el archivo "Clientes.py" dentro de "Back"
from Back.Clientes import *

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication
basedatos = Database("postgres", "00112233", "centroestetica.ccwkcz7cjsk2.us-east-2.rds.amazonaws.com")
conexion= basedatos.conectar()
#clientes = Clientes()

class emerAdiFal(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerAdiFal, self).__init__(parent)
        uic.loadUi('Front/comunes/emerAdiFalta.ui', self)

        self.EmerAdiFalta.clicked.connect(self.llamar_funcion)
        self.documento_falta = None

    def llamar_funcion (self):
        print('entre a la funcion llamar_funcion')
        self.documento_falta = self.lineEdit.text()
        self.hide()
        print(self.documento_falta)
        #print(clientes)
        #clientes.verificar_cliente(self.documento_falta)

class emerAgrCita(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerAgrCita, self).__init__(parent)
        uic.loadUi('Front/comunes/emerAgrCita.ui', self)

class emerAgrCli(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerAgrCli, self).__init__(parent)
        uic.loadUi('Front/comunes/emerAgrCli.ui', self)


class emerConfirmar(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerConfirmar, self).__init__(parent)
        uic.loadUi('Front/comunes/emerConfirmar.ui', self)


class emerBuscClien(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerBuscClien, self).__init__(parent)
        uic.loadUi('Front/comunes/emerBuscClien.ui', self)

class emerBusCita(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerBusCita, self).__init__(parent)
        uic.loadUi('Front/comunes/emerBusCita.ui', self)

class emerBuscPro(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerBuscPro, self).__init__(parent)
        uic.loadUi('Front/comunes/emerBuscPro.ui', self)

class emerBuscSer(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerBuscSer, self).__init__(parent)
        uic.loadUi('Front/comunes/emerBuscSer.ui', self)

class emerBuscUsu(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerBuscUsu, self).__init__(parent)
        uic.loadUi('Front/comunes/emerBuscUsu.ui', self)


class emerCamCita(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerCamCita, self).__init__(parent)
        uic.loadUi('Front/comunes/emerCamCita.ui', self)

class emerModClien(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerModClien, self).__init__(parent)
        uic.loadUi('Front/comunes/emerModClien.ui', self)