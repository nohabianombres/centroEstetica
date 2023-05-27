from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication

class Cajero(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Cajero, self).__init__(parent)
        uic.loadUi('Front/cajero/Cajero.ui', self)

class CajeroFacturacion(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(CajeroFacturacion, self).__init__(parent)
        uic.loadUi('Front/cajero/Cajero.ui', self)

class CajeroInventario(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(CajeroInventario, self).__init__(parent)
        uic.loadUi('Front/cajero/CajeroInventario.ui', self)
