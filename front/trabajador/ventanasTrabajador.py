
from Front.comunes.emerComunes import *
from PyQt5 import QtWidgets, uic
from datetime import datetime

class TrabajadorVentana(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(TrabajadorVentana, self).__init__(parent)
        uic.loadUi('Front/trabajador/Trabajador.ui', self)

        self.botAgenPers.clicked.connect(self.open_view_tra_2)
        self.botSerProc.clicked.connect(self.open_view_tra_2)
        self.botCerRec.clicked.connect(self.cerrar_sesion)

        self.traAgenda = None
        self.traSerPro = None

    def open_view_tra_2(self):
        sender_button_tra_2 = self.sender()
        if sender_button_tra_2 == self.botAgenPers:
            self.hide()
            self.traAgenda = TrabajadorAgenda()
            self.traAgenda.recibir_datos(self.datos_usuario)
            self.traAgenda.show()
        elif sender_button_tra_2 == self.botSerProc:
            self.hide()
            self.traSerPro = TrabajadorProceso()
            self.traSerPro.recibir_datos(self.datos_usuario)
            self.traSerPro.show()

    def recibir_datos (self, usuario_validar):
        self.datos_usuario = usuario_validar

    def cerrar_sesion(self):
        quit()

class TrabajadorAgenda(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(TrabajadorAgenda, self).__init__(parent)
        uic.loadUi('Front/trabajador/TrabajadorAgenda.ui', self)

        self.botAgenPers.clicked.connect(self.open_view_tra_age)
        self.botSerProc.clicked.connect(self.open_view_tra_age)
        self.botCerRec.clicked.connect(self.cerrar_sesion)

        self.traAgenda = None
        self.traSerPro = None

    def open_view_tra_age(self):
        sender_button_tra_age = self.sender()
        if sender_button_tra_age == self.botAgenPers:
            self.hide()
            self.traAgenda = TrabajadorAgenda()
            self.traAgenda.recibir_datos(self.datos_usuario)
            self.traAgenda.show()
        elif sender_button_tra_age == self.botSerProc:
            self.hide()
            self.traSerPro = TrabajadorProceso()
            self.traSerPro.recibir_datos(self.datos_usuario)
            self.traSerPro.show()

    def open_view_tab_personal (self):
        self.agenda_perso = self.trabajador.consultar_agenda_personal()
        self.imprimir_tabla_filas(self.agenda_perso)

    def imprimir_tabla_filas(self, listas):
        self.TabAgenda.clearContents()
        print(listas)
        self.TabAgenda.show()
        if listas != None:
            fila = 0
            self.TabAgenda.setRowCount(len(listas))
            for elementos in listas:
                print(elementos)
                self.TabAgenda.setItem(fila, 0, QtWidgets.QTableWidgetItem((str(elementos[0]))))
                self.TabAgenda.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(elementos[1].strftime("%H:%M"))))
                self.TabAgenda.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(elementos[2].strftime("%Y-%m-%d"))))
                self.TabAgenda.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(elementos[3])))
                self.TabAgenda.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(elementos[4])))
                self.TabAgenda.setItem(fila, 5, QtWidgets.QTableWidgetItem(str(elementos[5])))
                self.TabAgenda.setItem(fila, 6, QtWidgets.QTableWidgetItem(str(elementos[6])))
                self.TabAgenda.setItem(fila, 7, QtWidgets.QTableWidgetItem(str(elementos[7])))
                self.TabAgenda.setItem(fila, 8, QtWidgets.QTableWidgetItem(str(elementos[8])))
                self.TabAgenda.setItem(fila, 9, QtWidgets.QTableWidgetItem(str(elementos[9])))
                fila = fila + 1
        else:
            print('no encontre')

    def recibir_datos (self, usuario_validar):
        self.datos_usuario = usuario_validar
        self.trabajador = Trabajadores(usuario_validar[0], usuario_validar[1], usuario_validar[2], usuario_validar[3],
                                       usuario_validar[4], usuario_validar[5], usuario_validar[6], usuario_validar[7])
        self.open_view_tab_personal()

    def cerrar_sesion(self):
        quit()

class TrabajadorProceso(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(TrabajadorProceso, self).__init__(parent)
        uic.loadUi('Front/trabajador/TrabajadorProceso.ui', self)

        self.botAgenPers.clicked.connect(self.open_view_tra_pro)
        self.botSerProc.clicked.connect(self.open_view_tra_pro)
        self.botIniFin.clicked.connect(self.open_view_IniFin)
        self.botBusCit.clicked.connect(self.open_view_eme_BusCita)
        self.botCerRec.clicked.connect(self.cerrar_sesion)

        self.traAgenda = None
        self.traSerPro = None

    def open_view_tra_pro(self):
        sender_button_tra_pro = self.sender()

        if sender_button_tra_pro == self.botAgenPers:
            self.hide()
            self.traAgenda = TrabajadorAgenda()
            self.traAgenda.recibir_datos(self.datos_usuario)
            self.traAgenda.show()
        elif sender_button_tra_pro == self.botSerProc:
            self.hide()
            self.traSerPro = TrabajadorProceso()
            self.traSerPro.recibir_datos(self.datos_usuario)
            self.traSerPro.show()

    def open_view_eme_BusCita(self):
        self.BusCit = emerBusCitas()
        self.BusCit.set_callback(self.imprimir_tabla_filas)
        self.BusCit.show()

    def imprimir_tabla_filas(self, listas):
        self.TabAgenda.clearContents()
        print(listas)
        self.TabAgenda.show()
        if listas != None:
            fila = 0
            self.TabAgenda.setRowCount(len(listas))
            for elementos in listas:
                print(elementos)
                self.TabAgenda.setItem(fila, 0, QtWidgets.QTableWidgetItem((str(elementos[0]))))
                self.TabAgenda.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(elementos[1].strftime("%H:%M"))))
                self.TabAgenda.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(elementos[2].strftime("%Y-%m-%d"))))
                self.TabAgenda.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(elementos[3])))
                self.TabAgenda.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(elementos[4])))
                self.TabAgenda.setItem(fila, 5, QtWidgets.QTableWidgetItem(str(elementos[5])))
                self.TabAgenda.setItem(fila, 6, QtWidgets.QTableWidgetItem(str(elementos[6])))
                self.TabAgenda.setItem(fila, 7, QtWidgets.QTableWidgetItem(str(elementos[7])))
                self.TabAgenda.setItem(fila, 8, QtWidgets.QTableWidgetItem(str(elementos[8])))
                self.TabAgenda.setItem(fila, 9, QtWidgets.QTableWidgetItem(str(elementos[9])))
                fila = fila + 1
        else:
            print('no encontre')

    def open_view_IniFin (self):
        self.emerIniFin = emerIniFin()
        self.emerIniFin.recibir_datos(self.datos_usuario)
        self.emerIniFin.set_callback(self.crear_ventana)
        self.emerIniFin.show()

    def recibir_datos (self, usuario_validar):
        self.datos_usuario = usuario_validar

    def crear_ventana(self, retorno):
        self.emer_retorno = emerRetorno()
        self.emer_retorno.imprimir_retorno(retorno)
        self.emer_retorno.show()

    def cerrar_sesion(self):
        quit()


class emerIniFin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(emerIniFin, self).__init__(parent)
        uic.loadUi('Front/trabajador/emerIniFin.ui', self)

        self.botAceIniFin.clicked.connect(self.iniciar_finalizar_funcion)
        self.botCanIniFin.clicked.connect(self.cancelar_iniciar_finalizar)
        self.hora_inicio.clicked.connect(self.agregar_hora_inicio)
        self.hora_fin.clicked.connect(self.agregar_hora_fin)

    def iniciar_finalizar_funcion(self):
        self.id_cita = self.LIdCita.text()
        self.hide()
        self.trabajador = Trabajadores(self.datos_usuario[0], self.datos_usuario[1], self.datos_usuario[2], self.datos_usuario[3],
                                       self.datos_usuario[4], self.datos_usuario[5], self.datos_usuario[6], self.datos_usuario[7])
        self.retorno_ini_fin = self.trabajador.inicializar_finalizar_cita_(self.id_cita, self.hora_inicio, self.hora_fin)

        if self.callback:
            self.callback(self.retorno_ini_fin)

    def agregar_hora_inicio (self):
        self.hora_inicio = datetime.now().strftime('%H:%M:%S')

    def agregar_hora_fin (self):
        self.hora_fin = datetime.now().strftime('%H:%M:%S')


    def set_callback(self, callback):
        self.callback = callback

    def cancelar_iniciar_finalizar(self):
        self.hide()
        self.close()

    def recibir_datos (self, usuario_validar):
        self.datos_usuario = usuario_validar

#self.btnMiBoton.setEnabled(False)