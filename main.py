import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

from bienvenida import Ui_Dialog1
from add_paciente import Ui_Dialog2



class bienvenida(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog1()
        self.ui.setupUi(self)
        self.ui.bt_paciente.clicked.connect(self.irAAddPaciente)

    def irAAddPaciente(self):

        self.add_paciente_window = add_paciente()
        self.add_paciente_window.show()
        self.close()  # Cierra la ventana de bienvenida

class add_paciente(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog2()
        self.ui.setupUi(self)
        self.ui.bt_regresar.clicked.connect(
        self.regresarABienvenida)  # Conecta el botón a la función regresarABienvenida

    def regresarABienvenida(self):

        self.bienvenida_window = bienvenida()
        self.bienvenida_window.show()
        self.close()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Main Window')

        # Crear instancias de las ventanas de las interfaces
        self.bienvenida_window = bienvenida()
        self.add_paciente_window = add_paciente()

        # Configurar las señales para abrir las interfaces

        self.add_paciente_window.ui.boton_add_paciente.clicked.connect(self.mostrarAddPaciente)

    def mostrarBienvenida(self):
        self.bienvenida_window.show()

    def mostrarAddPaciente(self):
        self.add_paciente_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = bienvenida()
    mi_app.show()
    sys.exit(app.exec_())
