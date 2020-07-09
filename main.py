from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
import sys
from principal import Ui_Principal
from login import Ui_janelaLogin
from cadastrarMorador import Ui_janelaCadastrarMoradores
from consultarVisitantes import Ui_janelaConsultarVisitantes
from consultarMoradores import Ui_janelaConsultarMoradores
from atualizarMoradores import Ui_janelaAtualizarMoradores
class Home(QMainWindow):

    def __init__(self,*args,**argvs):
        super(Home,self).__init__(*args,**argvs)
        self.ui = Ui_Principal()
        self.ui.setupUi(self)
        self.ui.btnActCadastrarMoradores.triggered.connect(self.abrirCadastroMoradores) # btn Cadastrar Morador da Tela Principal
        self.ui.btnActConsultarVisitantes.triggered.connect(self.abrirConsultaVisitantes) # btn Consultar Visitantes da TelaVisitantes
        self.ui.btnActConsultarMoradores.triggered.connect(self.abrirConsultaMoradores) # btn Consultar Moradores da telaMoradores
        self.ui.btnActAtualizarMoradores.triggered.connect(self.abrirAtualizarMoradores)
        self.ui.btnActSair.triggered.connect(self.sair)

    def abrirCadastroMoradores(self):
        self.janela = GuiaCadastrarMoradores()
        self.janela.show()
    
    def abrirConsultaVisitantes(self):
        self.janela = GuiaConsultarVisitantes()
        self.janela.show()

    def abrirConsultaMoradores(self):
        self.janela = GuiaConsultarMoradores()
        self.janela.show()

    def abrirAtualizarMoradores(self):
        self.janela = GuiaAtualizarMoradores()
        self.janela.show()

    def sair(self):
        self.ui = Login()
        self.ui.show()

        self.destroy()

class GuiaCadastrarMoradores(QMainWindow): #Contrui a janela aqui, e chamei a page externa pra ligar com essa
    def __init__(self,*args,**argvs):
        super(GuiaCadastrarMoradores,self).__init__(*args,**argvs)
        self.telaCadastrarMoradores = Ui_janelaCadastrarMoradores()
        self.telaCadastrarMoradores.setupUi(self)
class GuiaConsultarVisitantes(QMainWindow): #Contrui a janela aqui, e chamei a page externa pra ligar com essa
    def __init__(self,*args,**argvs):
        super(GuiaConsultarVisitantes,self).__init__(*args,**argvs)
        self.telaConsultarVisitantes = Ui_janelaConsultarVisitantes()
        self.telaConsultarVisitantes.setupUi(self)
class GuiaConsultarMoradores(QMainWindow): #Contrui a janela aqui, e chamei a page externa pra ligar com essa
    def __init__(self,*args,**argvs):
        super(GuiaConsultarMoradores,self).__init__(*args,**argvs)
        self.telaConsultarMoradores = Ui_janelaConsultarMoradores()
        self.telaConsultarMoradores.setupUi(self)
class GuiaAtualizarMoradores(QMainWindow): #Contrui a janela aqui, e chamei a page externa pra ligar com essa
    def __init__(self,*args,**argvs):
        super(GuiaAtualizarMoradores,self).__init__(*args,**argvs)
        self.telaConsultarMoradores = Ui_janelaAtualizarMoradores()
        self.telaConsultarMoradores.setupUi(self)
class Login (QMainWindow):

    def __init__(self,*args,**argvs):
        super(Login,self).__init__(*args,**argvs)
        self.ui = Ui_janelaLogin()
        self.ui.setupUi(self)
        self.ui.btnEntrar.clicked.connect(self.login)

    def login(self):
        admin = "admin"
        senha = "admin"
        user = self.ui.inputLogin.text()
        passw = self.ui.inputSenha.text()

        if user == admin and passw == senha:
            self.janela = Home()
            self.janela.show()
            self.destroy()
           
        else:
            QMessageBox.warning(QMessageBox(),"Login errado!", "Volte e Digite Novamente!")

app = QApplication(sys.argv)
if (QDialog.Accepted == True):
    janela = Login()
    janela.show()
    sys.exit(app.exec_())