from PyQt5 import QtWidgets, uic



app = QtWidgets.QApplication([])

login = uic.loadUi('prueba carpeta/login2.ui')
login.show()
app.exec()