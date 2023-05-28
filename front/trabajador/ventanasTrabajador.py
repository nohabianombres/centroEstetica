from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication





class TrabajadorVentana(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(TrabajadorVentana, self).__init__(parent)
        uic.loadUi('Front/trabajador/Trabajador.ui', self)

class TrabajadorAgenda(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(TrabajadorAgenda, self).__init__(parent)
        uic.loadUi('Front/trabajador/TrabajadorAgenda.ui', self)

class TrabajadorProceso(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(TrabajadorProceso, self).__init__(parent)
        uic.loadUi('Front/trabajador/TrabajadorProceso.ui', self)

class emerIniFin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerIniFin, self).__init__(parent)
        uic.loadUi('Front/trabajador/emerIniFin.ui', self)

