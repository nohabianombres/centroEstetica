from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication

class emerModSer(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerModSer, self).__init__(parent)
        uic.loadUi('Front/administrador/emeAdm/emerModSer.ui', self)


class emerModPro(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerModPro, self).__init__(parent)
        uic.loadUi('Front/administrador/emeAdm/emerModPro.ui', self)

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

class emerAgrSer(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerAgrSer, self).__init__(parent)
        uic.loadUi('Front/administrador/emeAdm/emerAgrSer.ui', self)
