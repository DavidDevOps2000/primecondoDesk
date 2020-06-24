from PyQt5 import QtCore, QtGui, QtWidgets
from funcMorador import FuncoesMorador
from tkinter import messagebox
from tkinter import *
import serial


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_janelaCadastrarMoradores(object):

    def funcSalvarMorador(self):
                # Morador
                self.vlrNomeMorador          = self.inputNomeCompleto.text()     #
                self.vlrCpfMorador           = self.inputCpf.text()
                self.vlrSenha                = self.inputSenha.text()
                self.vlrApelido              = self.inputNomeApelido.text()
                self.vlrTipoMorador          = str(self.comboBoxTipoMorador.currentText())#Pegando o valor do comboBox e convertendo em string
                self.vlrDataNasc             = self.inputDataNascimento.text()

                self.setsMorador             = ("'%s','%s','%s','%s','%s','%s'" % (self.vlrCpfMorador, self.vlrNomeMorador, self.vlrSenha, self.vlrApelido, self.vlrTipoMorador, self.vlrDataNasc))

                #Contatos
                self.vlrTelefone             = self.inputTelefone.text()
                self.vlrEmail                = self.inputEmail.text()
                
                #Identificadores
                self.vlrRfid                 = self.inputRfid.text()
                self.vlrBiometria            = self.inputDigitalBiometria.text()
                
                #Moradia
                self.vlrNumApt               = self.inputNumeroApartamento.text()
                self.vlrBloco                = str(self.comboBoxBloco.currentText())
                self.vlrVaga                 = self.inputNumeroVaga.text()

                #Vericulo
                self.vlrTipoVeiculo          = str(self.comboBoxTipoVeiculo.currentText())
                self.vlrCorVeiculo           = str(self.comboBoxCorVeiculo.currentText())
                self.vlrPlaca                = self.inputPlaca.text()  
                self.vlrVagaCarro            = self.vlrVaga
                self.vlridMoradia :int

                self.cmdBanco = FuncoesMorador()

                self.conexaoRfid             = FuncoesMorador()

                self.cmdBanco = FuncoesMorador()

                try:                                    #o try executa uma função
                        self.cmdBanco.insertMorador(self.setsMorador)

                        self.IDmorador = self.cmdBanco.buscarIdMorador(self.vlrNomeMorador, self.vlrCpfMorador)

                        self.cmdBanco.insertMoradia(self.vlrNumApt, self.vlrBloco, self.IDmorador[0], self.vlrVagaCarro)

                        self.IDmoradia = self.cmdBanco.buscarIdMoradia(self.IDmorador[0], self.vlrBloco, self.vlrNumApt)

                        self.cmdBanco.insertVeiculo(self.comboBoxCorVeiculo, self.vlrTipoVeiculo, self.inputModeloVeiculo, self.inputPlaca, self.IDmoradia[0])

                        
                        if not self.cmdBanco:

                                print("Deu errado")
                        else:

                                print("Funcionou")
                except:
                        print('Erro de Conexao')

        

    def abrirMsgBox(self):
             top = Tk()  
             top.geometry("0x0")
             top.overrideredirect(True)  
             ok = messagebox.askokcancel("Cadastrar Morador","Você tem que certeza que cadastrá-lo(a) ?") 
        
             if ok:                          #Se a pessoa clicar em OK ....
                    try:
                       self.funcSalvarMorador()
       
                       if not self.funcSalvarMorador:
                            self.lblResultado.setText("Não funcionou")

                       else:
                           self.lblResultado.setText("funcionou")
                        
                    except:
                        self.lblResultado.setText("Erro no Banco")
              
                
    def setupUi(self, janelaCadastrarMoradores):
        janelaCadastrarMoradores.setObjectName("janelaCadastrarMoradores")
        janelaCadastrarMoradores.resize(725, 650)
        janelaCadastrarMoradores.setMinimumSize(QtCore.QSize(725, 650))
        janelaCadastrarMoradores.setMaximumSize(QtCore.QSize(725, 650))
        janelaCadastrarMoradores.setBaseSize(QtCore.QSize(725, 650))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        janelaCadastrarMoradores.setWindowIcon(icon)
        janelaCadastrarMoradores.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(janelaCadastrarMoradores)
        self.centralwidget.setObjectName("centralwidget")
        self.lblNomeCompleto = QtWidgets.QLabel(self.centralwidget)
        self.lblNomeCompleto.setGeometry(QtCore.QRect(30, 90, 151, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setItalic(False)
        self.lblNomeCompleto.setFont(font)
        self.lblNomeCompleto.setObjectName("lblNomeCompleto")
        self.lblCpf = QtWidgets.QLabel(self.centralwidget)
        self.lblCpf.setGeometry(QtCore.QRect(30, 150, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblCpf.setFont(font)
        self.lblCpf.setObjectName("lblCpf")
        self.lblEmail = QtWidgets.QLabel(self.centralwidget)
        self.lblEmail.setGeometry(QtCore.QRect(260, 210, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblEmail.setFont(font)
        self.lblEmail.setObjectName("lblEmail")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(570, 130, 55, 16))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.lblBloco = QtWidgets.QLabel(self.centralwidget)
        self.lblBloco.setGeometry(QtCore.QRect(410, 150, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblBloco.setFont(font)
        self.lblBloco.setObjectName("lblBloco")
        self.lblDataNascimento = QtWidgets.QLabel(self.centralwidget)
        self.lblDataNascimento.setGeometry(QtCore.QRect(530, 90, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblDataNascimento.setFont(font)
        self.lblDataNascimento.setObjectName("lblDataNascimento")
        self.lblNumeroApartamento = QtWidgets.QLabel(self.centralwidget)
        self.lblNumeroApartamento.setGeometry(QtCore.QRect(260, 150, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblNumeroApartamento.setFont(font)
        self.lblNumeroApartamento.setObjectName("lblNumeroApartamento")
        self.comboBoxBloco = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxBloco.setEnabled(True)
        self.comboBoxBloco.setGeometry(QtCore.QRect(410, 170, 71, 26))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBoxBloco.setFont(font)
        self.comboBoxBloco.setObjectName("comboBoxBloco")
        self.comboBoxBloco.addItem("")
        self.comboBoxBloco.addItem("")
        self.comboBoxBloco.addItem("")
        self.comboBoxBloco.addItem("")
        self.comboBoxTipoMorador = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxTipoMorador.setEnabled(True)
        self.comboBoxTipoMorador.setGeometry(QtCore.QRect(530, 170, 181, 26))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBoxTipoMorador.setFont(font)
        self.comboBoxTipoMorador.setObjectName("comboBoxTipoMorador")
        self.comboBoxTipoMorador.addItem("")
        self.comboBoxTipoMorador.addItem("")
        self.comboBoxTipoMorador.addItem("")
        self.lblTipoMorador = QtWidgets.QLabel(self.centralwidget)
        self.lblTipoMorador.setGeometry(QtCore.QRect(530, 150, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblTipoMorador.setFont(font)
        self.lblTipoMorador.setObjectName("lblTipoMorador")
        self.lblTelefone = QtWidgets.QLabel(self.centralwidget)
        self.lblTelefone.setGeometry(QtCore.QRect(30, 210, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblTelefone.setFont(font)
        self.lblTelefone.setObjectName("lblTelefone")
        self.radioButtonOpcaoSim = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonOpcaoSim.setGeometry(QtCore.QRect(120, 420, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButtonOpcaoSim.setFont(font)
        self.radioButtonOpcaoSim.setObjectName("radioButtonOpcaoSim")
        self.lblPossuiVeiculo = QtWidgets.QLabel(self.centralwidget)
        self.lblPossuiVeiculo.setGeometry(QtCore.QRect(30, 420, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblPossuiVeiculo.setFont(font)
        self.lblPossuiVeiculo.setObjectName("lblPossuiVeiculo")
        self.lblTipoVeiculo = QtWidgets.QLabel(self.centralwidget)
        self.lblTipoVeiculo.setGeometry(QtCore.QRect(30, 450, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblTipoVeiculo.setFont(font)
        self.lblTipoVeiculo.setObjectName("lblTipoVeiculo")
        self.comboBoxTipoVeiculo = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxTipoVeiculo.setEnabled(True)
        self.comboBoxTipoVeiculo.setGeometry(QtCore.QRect(30, 470, 121, 26))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBoxTipoVeiculo.setFont(font)
        self.comboBoxTipoVeiculo.setObjectName("comboBoxTipoVeiculo")
        self.comboBoxTipoVeiculo.addItem("")
        self.comboBoxTipoVeiculo.addItem("")
        self.comboBoxTipoVeiculo.addItem("")
        self.lblModeloVeiculo = QtWidgets.QLabel(self.centralwidget)
        self.lblModeloVeiculo.setGeometry(QtCore.QRect(210, 450, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblModeloVeiculo.setFont(font)
        self.lblModeloVeiculo.setObjectName("lblModeloVeiculo")
        self.lblCorVeiculo = QtWidgets.QLabel(self.centralwidget)
        self.lblCorVeiculo.setGeometry(QtCore.QRect(530, 450, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblCorVeiculo.setFont(font)
        self.lblCorVeiculo.setObjectName("lblCorVeiculo")
        self.comboBoxCorVeiculo = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxCorVeiculo.setEnabled(True)
        self.comboBoxCorVeiculo.setGeometry(QtCore.QRect(530, 470, 181, 26))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBoxCorVeiculo.setFont(font)
        self.comboBoxCorVeiculo.setObjectName("comboBoxCorVeiculo")
        self.comboBoxCorVeiculo.addItem("")
        self.comboBoxCorVeiculo.setItemText(0, "")
        self.comboBoxCorVeiculo.addItem("")
        self.comboBoxCorVeiculo.addItem("")
        self.comboBoxCorVeiculo.addItem("")
        self.comboBoxCorVeiculo.addItem("")
        self.comboBoxCorVeiculo.addItem("")
        self.lblPlaca = QtWidgets.QLabel(self.centralwidget)
        self.lblPlaca.setGeometry(QtCore.QRect(210, 520, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblPlaca.setFont(font)
        self.lblPlaca.setObjectName("lblPlaca")
        self.btnSalvar = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalvar.setGeometry(QtCore.QRect(560, 590, 131, 31))
        self.btnSalvar.setAutoDefault(False)
        self.btnSalvar.setObjectName("btnSalvar")
        self.lblNumeroVaga = QtWidgets.QLabel(self.centralwidget)
        self.lblNumeroVaga.setGeometry(QtCore.QRect(30, 520, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblNumeroVaga.setFont(font)
        self.lblNumeroVaga.setObjectName("lblNumeroVaga")
        self.lblNomeApelido = QtWidgets.QLabel(self.centralwidget)
        self.lblNomeApelido.setGeometry(QtCore.QRect(30, 270, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblNomeApelido.setFont(font)
        self.lblNomeApelido.setObjectName("lblNomeApelido")
        self.lblSenha = QtWidgets.QLabel(self.centralwidget)
        self.lblSenha.setGeometry(QtCore.QRect(260, 270, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblSenha.setFont(font)
        self.lblSenha.setObjectName("lblSenha")
        self.lblConfirmarSenha = QtWidgets.QLabel(self.centralwidget)
        self.lblConfirmarSenha.setGeometry(QtCore.QRect(530, 270, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblConfirmarSenha.setFont(font)
        self.lblConfirmarSenha.setObjectName("lblConfirmarSenha")
        self.lblRfid = QtWidgets.QLabel(self.centralwidget)
        self.lblRfid.setGeometry(QtCore.QRect(30, 340, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblRfid.setFont(font)
        self.lblRfid.setObjectName("lblRfid")
        self.lblDigital = QtWidgets.QLabel(self.centralwidget)
        self.lblDigital.setGeometry(QtCore.QRect(260, 340, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblDigital.setFont(font)
        self.lblDigital.setObjectName("lblDigital")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(30, 400, 681, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.radioButtonOpcaoNao = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonOpcaoNao.setGeometry(QtCore.QRect(170, 420, 51, 20))
        self.radioButtonOpcaoNao.setCheckable(True)
        self.radioButtonOpcaoNao.setChecked(True)
        self.radioButtonOpcaoNao.setObjectName("radioButtonOpcaoNao")
        self.lblTituloCadastrarMoradores = QtWidgets.QLabel(self.centralwidget)
        self.lblTituloCadastrarMoradores.setGeometry(QtCore.QRect(30, 20, 271, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblTituloCadastrarMoradores.setFont(font)
        self.lblTituloCadastrarMoradores.setObjectName("lblTituloCadastrarMoradores")
        self.btnLimpar = QtWidgets.QPushButton(self.centralwidget)
        self.btnLimpar.setGeometry(QtCore.QRect(390, 590, 131, 31))
        self.btnLimpar.setObjectName("btnLimpar")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 50, 671, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.inputNomeCompleto = QtWidgets.QLineEdit(self.centralwidget)
        self.inputNomeCompleto.setGeometry(QtCore.QRect(30, 110, 451, 26))
        self.inputNomeCompleto.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
"")
        self.inputNomeCompleto.setMaxLength(85)
        self.inputNomeCompleto.setObjectName("inputNomeCompleto")
        self.inputDataNascimento = QtWidgets.QLineEdit(self.centralwidget)
        self.inputDataNascimento.setGeometry(QtCore.QRect(530, 110, 181, 26))
        self.inputDataNascimento.setMaxLength(10)
        self.inputDataNascimento.setPlaceholderText("")
        self.inputDataNascimento.setObjectName("inputDataNascimento")
        self.inputCpf = QtWidgets.QLineEdit(self.centralwidget)
        self.inputCpf.setGeometry(QtCore.QRect(30, 170, 181, 26))
        self.inputCpf.setMaxLength(14)
        self.inputCpf.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.inputCpf.setCursorPosition(0)
        self.inputCpf.setObjectName("inputCpf")
        self.inputNumeroApartamento = QtWidgets.QLineEdit(self.centralwidget)
        self.inputNumeroApartamento.setGeometry(QtCore.QRect(260, 170, 111, 26))
        self.inputNumeroApartamento.setMaxLength(4)
        self.inputNumeroApartamento.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.inputNumeroApartamento.setCursorPosition(0)
        self.inputNumeroApartamento.setObjectName("inputNumeroApartamento")
        self.inputTelefone = QtWidgets.QLineEdit(self.centralwidget)
        self.inputTelefone.setGeometry(QtCore.QRect(30, 230, 181, 26))
        self.inputTelefone.setMaxLength(16)
        self.inputTelefone.setCursorPosition(0)
        self.inputTelefone.setObjectName("inputTelefone")
        self.inputEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.inputEmail.setGeometry(QtCore.QRect(260, 230, 451, 26))
        self.inputEmail.setMaxLength(56)
        self.inputEmail.setDragEnabled(False)
        self.inputEmail.setObjectName("inputEmail")
        self.inputNomeApelido = QtWidgets.QLineEdit(self.centralwidget)
        self.inputNomeApelido.setGeometry(QtCore.QRect(30, 290, 181, 26))
        self.inputNomeApelido.setMaxLength(20)
        self.inputNomeApelido.setObjectName("inputNomeApelido")
        self.inputPlaca = QtWidgets.QLineEdit(self.centralwidget)
        self.inputPlaca.setEnabled(True)
        self.inputPlaca.setGeometry(QtCore.QRect(210, 540, 111, 26))
        self.inputPlaca.setMaxLength(7)
        self.inputPlaca.setObjectName("inputPlaca")
        self.inputSenha = QtWidgets.QLineEdit(self.centralwidget)
        self.inputSenha.setGeometry(QtCore.QRect(260, 290, 181, 26))
        self.inputSenha.setMaxLength(20)
        self.inputSenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputSenha.setObjectName("inputSenha")
        self.inputConfirmarSenha = QtWidgets.QLineEdit(self.centralwidget)
        self.inputConfirmarSenha.setGeometry(QtCore.QRect(530, 290, 181, 26))
        self.inputConfirmarSenha.setMaxLength(20)
        self.inputConfirmarSenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputConfirmarSenha.setObjectName("inputConfirmarSenha")
        self.inputRfid = QtWidgets.QLineEdit(self.centralwidget)
        self.inputRfid.setGeometry(QtCore.QRect(30, 360, 151, 26))
        self.inputRfid.setMaxLength(20)
        self.inputRfid.setReadOnly(True)
        self.inputRfid.setObjectName("inputRfid")
        self.inputDigitalBiometria = QtWidgets.QLineEdit(self.centralwidget)
        self.inputDigitalBiometria.setGeometry(QtCore.QRect(260, 360, 151, 26))
        self.inputDigitalBiometria.setMaxLength(100)
        self.inputDigitalBiometria.setReadOnly(True)
        self.inputDigitalBiometria.setObjectName("inputDigitalBiometria")
        self.inputModeloVeiculo = QtWidgets.QLineEdit(self.centralwidget)
        self.inputModeloVeiculo.setEnabled(True)
        self.inputModeloVeiculo.setGeometry(QtCore.QRect(210, 470, 271, 26))
        self.inputModeloVeiculo.setMaxLength(25)
        self.inputModeloVeiculo.setObjectName("inputModeloVeiculo")
        self.inputNumeroVaga = QtWidgets.QLineEdit(self.centralwidget)
        self.inputNumeroVaga.setEnabled(True)
        self.inputNumeroVaga.setGeometry(QtCore.QRect(30, 540, 111, 26))
        self.inputNumeroVaga.setMaxLength(4)
        self.inputNumeroVaga.setCursorPosition(0)
        self.inputNumeroVaga.setObjectName("inputNumeroVaga")
        self.btnBuscarRfid = QtWidgets.QPushButton(self.centralwidget)
        self.btnBuscarRfid.setGeometry(QtCore.QRect(180, 359, 31, 28))
        self.btnBuscarRfid.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBuscarRfid.setIcon(icon1)
        self.btnBuscarRfid.setAutoDefault(False)
        self.btnBuscarRfid.setObjectName("btnBuscarRfid")
        self.btnBuscarDigitalBiometria = QtWidgets.QPushButton(self.centralwidget)
        self.btnBuscarDigitalBiometria.setGeometry(QtCore.QRect(410, 359, 31, 28))
        self.btnBuscarDigitalBiometria.setText("")
        self.btnBuscarDigitalBiometria.setIcon(icon1)
        self.btnBuscarDigitalBiometria.setAutoDefault(False)
        self.btnBuscarDigitalBiometria.setObjectName("btnBuscarDigitalBiometria")
        self.lblResultado = QtWidgets.QLabel(self.centralwidget)
        self.lblResultado.setGeometry(QtCore.QRect(510, 375, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lblResultado.setFont(font)
        self.lblResultado.setText("")
        self.lblResultado.setObjectName("lblResultado")
        janelaCadastrarMoradores.setCentralWidget(self.centralwidget)
        self.lblNomeCompleto.setBuddy(self.inputNomeCompleto)
        self.lblCpf.setBuddy(self.inputCpf)
        self.lblEmail.setBuddy(self.inputEmail)
        self.lblBloco.setBuddy(self.comboBoxBloco)
        self.lblDataNascimento.setBuddy(self.inputDataNascimento)
        self.lblNumeroApartamento.setBuddy(self.inputNumeroApartamento)
        self.lblTipoMorador.setBuddy(self.comboBoxTipoMorador)
        self.lblTelefone.setBuddy(self.inputTelefone)
        self.lblPossuiVeiculo.setBuddy(self.radioButtonOpcaoSim)
        self.lblTipoVeiculo.setBuddy(self.comboBoxTipoVeiculo)
        self.lblModeloVeiculo.setBuddy(self.inputModeloVeiculo)
        self.lblCorVeiculo.setBuddy(self.comboBoxCorVeiculo)
        self.lblPlaca.setBuddy(self.inputPlaca)
        self.lblNumeroVaga.setBuddy(self.inputNumeroVaga)
        self.lblNomeApelido.setBuddy(self.inputNomeApelido)
        self.lblSenha.setBuddy(self.inputSenha)
        self.lblConfirmarSenha.setBuddy(self.inputConfirmarSenha)
        self.lblRfid.setBuddy(self.inputRfid)
        self.lblDigital.setBuddy(self.inputDigitalBiometria)

        self.retranslateUi(janelaCadastrarMoradores)
        self.btnLimpar.clicked.connect(self.inputNomeCompleto.clear)
        self.btnLimpar.clicked.connect(self.inputDataNascimento.clear)
        self.btnLimpar.clicked.connect(self.inputCpf.clear)
        self.btnLimpar.clicked.connect(self.inputNumeroApartamento.clear)
        self.btnLimpar.clicked.connect(self.inputTelefone.clear)
        self.btnLimpar.clicked.connect(self.inputEmail.clear)
        self.btnLimpar.clicked.connect(self.inputNomeApelido.clear)
        self.btnLimpar.clicked.connect(self.inputSenha.clear)
        self.btnLimpar.clicked.connect(self.inputConfirmarSenha.clear)
        self.btnLimpar.clicked.connect(self.inputRfid.clear)
        self.btnLimpar.clicked.connect(self.inputDigitalBiometria.clear)
        self.btnLimpar.clicked.connect(self.inputModeloVeiculo.clear)
        self.btnLimpar.clicked.connect(self.inputNumeroVaga.clear)
        self.btnLimpar.clicked.connect(self.inputPlaca.clear)
        QtCore.QMetaObject.connectSlotsByName(janelaCadastrarMoradores)
        janelaCadastrarMoradores.setTabOrder(self.inputNomeCompleto, self.inputDataNascimento)
        janelaCadastrarMoradores.setTabOrder(self.inputDataNascimento, self.inputCpf)
        janelaCadastrarMoradores.setTabOrder(self.inputCpf, self.inputNumeroApartamento)
        janelaCadastrarMoradores.setTabOrder(self.inputNumeroApartamento, self.comboBoxBloco)
        janelaCadastrarMoradores.setTabOrder(self.comboBoxBloco, self.comboBoxTipoMorador)
        janelaCadastrarMoradores.setTabOrder(self.comboBoxTipoMorador, self.inputTelefone)
        janelaCadastrarMoradores.setTabOrder(self.inputTelefone, self.inputEmail)
        janelaCadastrarMoradores.setTabOrder(self.inputEmail, self.inputNomeApelido)
        janelaCadastrarMoradores.setTabOrder(self.inputNomeApelido, self.inputSenha)
        janelaCadastrarMoradores.setTabOrder(self.inputSenha, self.inputConfirmarSenha)
        janelaCadastrarMoradores.setTabOrder(self.inputConfirmarSenha, self.inputRfid)
        janelaCadastrarMoradores.setTabOrder(self.inputRfid, self.inputDigitalBiometria)
        janelaCadastrarMoradores.setTabOrder(self.inputDigitalBiometria, self.radioButtonOpcaoSim)
        janelaCadastrarMoradores.setTabOrder(self.radioButtonOpcaoSim, self.radioButtonOpcaoNao)
        janelaCadastrarMoradores.setTabOrder(self.radioButtonOpcaoNao, self.comboBoxTipoVeiculo)
        janelaCadastrarMoradores.setTabOrder(self.comboBoxTipoVeiculo, self.inputModeloVeiculo)
        janelaCadastrarMoradores.setTabOrder(self.inputModeloVeiculo, self.comboBoxCorVeiculo)
        janelaCadastrarMoradores.setTabOrder(self.comboBoxCorVeiculo, self.inputNumeroVaga)
        janelaCadastrarMoradores.setTabOrder(self.inputNumeroVaga, self.inputPlaca)
        janelaCadastrarMoradores.setTabOrder(self.inputPlaca, self.btnLimpar)
        janelaCadastrarMoradores.setTabOrder(self.btnLimpar, self.btnSalvar)

    def retranslateUi(self, janelaCadastrarMoradores):
        _translate = QtCore.QCoreApplication.translate
        janelaCadastrarMoradores.setWindowTitle(_translate("janelaCadastrarMoradores", "PrimeCondo"))
        self.lblNomeCompleto.setText(_translate("janelaCadastrarMoradores", "&Nome Completo:"))
        self.lblCpf.setText(_translate("janelaCadastrarMoradores", "&CPF:"))
        self.lblEmail.setText(_translate("janelaCadastrarMoradores", "&E-mail:"))
        self.lblBloco.setText(_translate("janelaCadastrarMoradores", "&Bloco:"))
        self.lblDataNascimento.setText(_translate("janelaCadastrarMoradores", "&Data de Nascimento:"))
        self.lblNumeroApartamento.setText(_translate("janelaCadastrarMoradores", "Nº apt:"))
        self.comboBoxBloco.setItemText(0, _translate("janelaCadastrarMoradores", "A"))
        self.comboBoxBloco.setItemText(1, _translate("janelaCadastrarMoradores", "B"))
        self.comboBoxBloco.setItemText(2, _translate("janelaCadastrarMoradores", "C"))
        self.comboBoxBloco.setItemText(3, _translate("janelaCadastrarMoradores", "D"))
        self.comboBoxTipoMorador.setItemText(0, _translate("janelaCadastrarMoradores", "Proprietário"))
        self.comboBoxTipoMorador.setItemText(1, _translate("janelaCadastrarMoradores", "Morador"))
        self.comboBoxTipoMorador.setItemText(2, _translate("janelaCadastrarMoradores", "Dependente"))
        self.lblTipoMorador.setText(_translate("janelaCadastrarMoradores", "&Tipo de Morador:"))
        self.lblTelefone.setText(_translate("janelaCadastrarMoradores", "&Tefone:"))
        self.radioButtonOpcaoSim.setText(_translate("janelaCadastrarMoradores", "Sim"))
        self.lblPossuiVeiculo.setText(_translate("janelaCadastrarMoradores", "&Possui Veiculo"))
        self.lblTipoVeiculo.setText(_translate("janelaCadastrarMoradores", "&Tipo"))
        self.comboBoxTipoVeiculo.setItemText(0, _translate("janelaCadastrarMoradores", "Carro"))
        self.comboBoxTipoVeiculo.setItemText(1, _translate("janelaCadastrarMoradores", "Moto"))
        self.comboBoxTipoVeiculo.setItemText(2, _translate("janelaCadastrarMoradores", "Outros"))
        self.lblModeloVeiculo.setText(_translate("janelaCadastrarMoradores", "&Modelo:"))
        self.lblCorVeiculo.setText(_translate("janelaCadastrarMoradores", "&Cor:"))
        self.comboBoxCorVeiculo.setItemText(1, _translate("janelaCadastrarMoradores", "Preto"))
        self.comboBoxCorVeiculo.setItemText(2, _translate("janelaCadastrarMoradores", "Vermelho"))
        self.comboBoxCorVeiculo.setItemText(3, _translate("janelaCadastrarMoradores", "Azul"))
        self.comboBoxCorVeiculo.setItemText(4, _translate("janelaCadastrarMoradores", "Branco"))
        self.comboBoxCorVeiculo.setItemText(5, _translate("janelaCadastrarMoradores", "Outros"))
        self.lblPlaca.setText(_translate("janelaCadastrarMoradores", "&Placa:"))
        self.btnSalvar.setText(_translate("janelaCadastrarMoradores", "SALVAR"))
        self.lblNumeroVaga.setText(_translate("janelaCadastrarMoradores", "&Nº da Vaga:"))
        self.lblNomeApelido.setText(_translate("janelaCadastrarMoradores", "&Nome / Apelido"))
        self.lblSenha.setText(_translate("janelaCadastrarMoradores", "&Senha:"))
        self.lblConfirmarSenha.setText(_translate("janelaCadastrarMoradores", "&Confirmar Senha:"))
        self.lblRfid.setText(_translate("janelaCadastrarMoradores", "&RFID (Tag ou Cartão)"))
        self.lblDigital.setText(_translate("janelaCadastrarMoradores", "&Digital | Biometria"))
        self.radioButtonOpcaoNao.setText(_translate("janelaCadastrarMoradores", "Não"))
        self.lblTituloCadastrarMoradores.setText(_translate("janelaCadastrarMoradores", "Cadastro de Moradores"))
        self.btnLimpar.setText(_translate("janelaCadastrarMoradores", "LIMPAR"))
        self.inputDataNascimento.setInputMask(_translate("janelaCadastrarMoradores", "00/00/0000"))
        self.inputCpf.setInputMask(_translate("janelaCadastrarMoradores", "000.000.000-00"))
        self.inputCpf.setPlaceholderText(_translate("janelaCadastrarMoradores", "Digite só números"))
        self.inputNumeroApartamento.setInputMask(_translate("janelaCadastrarMoradores", "0000"))
        self.inputTelefone.setInputMask(_translate("janelaCadastrarMoradores", "(000) 00000-0000"))
        self.inputNumeroVaga.setInputMask(_translate("janelaCadastrarMoradores", "0000"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    janelaCadastrarMoradores = QtWidgets.QMainWindow()
    ui = Ui_janelaCadastrarMoradores()
    ui.setupUi(janelaCadastrarMoradores)
    janelaCadastrarMoradores.show()
    sys.exit(app.exec_())