from PyQt5 import QtWidgets, uic
import main

app = QtWidgets.QApplication([])

login = uic.loadUi('Front/login.ui')

name = login.varUsu.text()
password = login.varPass.text()
main.validacion(name, password)

login.show()
app.exec()
