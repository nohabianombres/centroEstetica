from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication





class Recepcionista(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Recepcionista, self).__init__(parent)
        uic.loadUi('Front/recepcionista/Recepcionista.ui', self)

class RecepcionistaClientes(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(RecepcionistaClientes, self).__init__(parent)
        uic.loadUi('Front/recepcionista/RecepcionistaClientes.ui', self)

class RecepcionistaAgenda(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(RecepcionistaAgenda, self).__init__(parent)
        uic.loadUi('Front/recepcionista/RecepcionistaAgenda.ui', self)

class RecepcionistaServicios(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(RecepcionistaServicios, self).__init__(parent)
        uic.loadUi('Front/recepcionista/RecepcionistaServicios.ui', self)

class RecepcionistaUsuarios(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(RecepcionistaUsuarios, self).__init__(parent)
        uic.loadUi('Front/recepcionista/RecepcionistaUsuarios.ui', self)