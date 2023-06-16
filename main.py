
from Front.trabajador.ventanasTrabajador import *
from Back.Usuarios import *
from Front.cajero.ventanasCajero import *
from Front.administrador.ventanasAdmin import *
from Front.recepcionista.ventanasRecepcionista import *
from Front.comunes.emerComunes import emerRetorno

basedatos = Database("postgres", "00112233", "centroestetica.ccwkcz7cjsk2.us-east-2.rds.amazonaws.com")
conexion = basedatos.conectar()


def validacion(user_log, contrasena_log, instancia_log):
    print(user_log)
    var_control = True
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM usuario WHERE usuario = " + str(user_log))
            usuario = cursor.fetchone()
            if usuario:
                usuario_contrasena = usuario[1]
                if usuario_contrasena == contrasena_log:
                    rol_usuario = usuario[7]
                    list_validacion = [usuario[2], usuario[3], int(usuario[0]), usuario[1], usuario[4], usuario[5], usuario[6], usuario[7]]
                else:
                    print('hpta')
            else:
                print('gonorrea')
    except psycopg2.Error as e:
        return ("Ocurrio un error al consultar")

    return list_validacion

class Login(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        uic.loadUi('Front/login.ui', self)
        self.BorraPrograma.clicked.connect(self.borrar)
        self.BotEntrar.clicked.connect(self.obtener_datos)

    def obtener_datos (self):
        self.user = self.VarUsu.text()
        self.contrasena = self.VarPass.text()
        self.usuario_validacion = validacion(self.user, self.contrasena, login)
        #usuario_validacion = validacion(self.user, self.contrasena, login)
        if self.usuario_validacion == "Ocurrio un error al consultar":
            print('entre')
            self.error = emerRetorno()
            self.error.imprimir_retorno(self.usuario_validacion)
            self.error.show()
            self.user = None
            self.contrasena = None
        else:
            if self.usuario_validacion[7] == 'Admin':
                self.open_view_adm()
            elif self.usuario_validacion[7] == 'Recepcion':
                self.open_view_rec()
            elif self.usuario_validacion[7] == 'Cajero':
                self.open_view_caj()
            else:
                print('voy en el if')
                self.open_view_tra()

    def borrar(self):
        for line_edit in self.findChildren(QtWidgets.QLineEdit):
            line_edit.clear()

    def open_view_rec(self):
        print('entre rec')
        self.close()
        self.hide()
        self.recepcionista = Recepcionista()
        self.recepcionista.recibir_datos(self.usuario_validacion)
        self.recepcionista.show()

    def open_view_adm(self):
        self.close()
        self.hide()
        self.admin = Admin()
        self.admin.recibir_datos(self.usuario_validacion)
        self.admin.show()


    def open_view_caj(self):
        self.close()
        self.hide()
        self.cajero = Cajero()
        self.cajero.recibir_datos(self.usuario_validacion)
        self.cajero.show()

    def open_view_tra(self):
        print('llegue a la funcion')
        self.close()
        self.hide()
        self.trabajador_ins = TrabajadorVentana()
        self.trabajador_ins.recibir_datos(self.usuario_validacion)
        self.trabajador_ins.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec_())

