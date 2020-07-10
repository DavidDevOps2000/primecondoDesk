from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from funcMorador import FuncoesMorador
from tkinter import messagebox
from tkinter import Tk

class Ui_janelaAtualizarMoradores(object):

    def buscarMorador(self):
        self.conexao = FuncoesMorador()
        self.conexao.conecta()

        self.cpfMorador  = self.inputPesquisarCpf.text()
        self.nomeMorador = self.inputPesquisarMorador.text()
        
        self.cmdMoradorConsult = FuncoesMorador()

        try:
            self.result = self.cmdMoradorConsult.consulMoradorUpdate(self.nomeMorador, self.cpfMorador)
            
            if not self.cmdMoradorConsult:
                    self.lblResultado.setText("Não Encontrado")
            else:
                    self.lblResultado.setText("Encontrado")
                    self.inputPesquisarMorador.setText(str(self.result[0][14]))
                    self.nomeMoradorAntigo = self.inputPesquisarMorador.text()
                    self.inputDataNascimento.setText(self.result[0][0])
                    self.inputNumeroApartamento.setText(str(self.result[0][1]))
                    self.inputTelefone.setText(str(self.result[0][4]))
                    self.inputEmail.setText(str(self.result[0][5]))
                    self.inputNomeApelido.setText(str(self.result[0][6]))
                    self.inputSenha.setText(str(self.result[0][7]))
                    self.seuStatus = self.result[0][9] #Seu Status atuaal
                    self.inputNumeroVaga.setText(str(self.result[0][8]))
                    self.inputPlaca.setText(str(self.result[0][11]))        
                    self.inputModeloVeiculo.setText(str(self.result[0][11]))
                    self.inputPlaca.setText(str(self.result[0][13]))
                    self.comboBoxBloco.setCurrentText(str(self.result[0][2]))
                    self.comboBoxTipoVeiculo.setCurrentText(str(self.result[0][10]))
                    self.comboBoxCorVeiculo.setCurrentText(str(self.result[0][12]))

                    if self.seuStatus == 1:# Converendo em True
                        self.radioOpcaoAtivo.setChecked(True)
                    else:
                        self.radioOpcaoDesativado.setChecked(True)  
        except:
            self.lblResultado.setText("Não encontrado")

    def salvarUpdate(self):
        self.conexao = FuncoesMorador()
        self.conexao.conecta()

        self.vlrSenha = self.inputSenha.text()
        self.vlrConfirmarSenha =self.inputConfirmarSenha.text()

        newNomeMorador          = self.inputPesquisarMorador.text()
        newSenha                = self.inputSenha.text()
        newApelido              = self.inputNomeApelido.text()
        newTipoMorador          = str(self.comboBoxTipoMorador.currentText())#Pegando o valor do comboBox e convertendo em string
        newDataNasc             = self.inputDataNascimento.text()
    
        #Contatos
        newTel                  = self.inputTelefone.text()
        newEmail                = self.inputEmail.text()

        #Moradia
        newNumApt               = self.inputNumeroApartamento.text()
        newBloco                = str(self.comboBoxBloco.currentText())
        newVaga                 = self.inputNumeroVaga.text()

        #Veiculo
        newTipoVei              = str(self.comboBoxTipoVeiculo.currentText())
        newCorVei               = str(self.comboBoxCorVeiculo.currentText())
        newPlaca                = self.inputPlaca.text()
        newModelo               = self.inputModeloVeiculo.text()
     
        if self.radioOpcaoAtivo.isChecked():
            newStatus = True
        else:
            newStatus = False

        self.cmdUpdate = FuncoesMorador()

        if self.vlrSenha == self.vlrConfirmarSenha: #Se as senhas forem as mesmas
            try:
                
                self.cmdUpdate.atualizarMoradores(newDataNasc, newNumApt, newBloco, newTipoMorador, newTel, newEmail, newApelido, newSenha, newVaga, newStatus, newTipoVei, newModelo, newCorVei, newPlaca, newNomeMorador, self.nomeMoradorAntigo, self.cpfMorador)

                if not self.cmdUpdate:
                  self.lblResultado.setText("Não foi Atualizado(a)")

                else:
                        self.lblResultado.setText("Atualizado com Sucesso")
            except:
                    self.lblResultado.setText("Verifique corretamente os campos")
        else:
            self.lblResultado.setText("Campos de senha não conferem")
    
    def abrirMsgBox(self):
             top = Tk()  
             top.geometry("0x0")
             top.overrideredirect(True)  
             ok = messagebox.askokcancel("Cadastrar Morador","Você tem que certeza que cadastrá-lo(a) ?") 
        
             if ok:                      #Se a pessoa clicar em OK ....
                    self.salvarUpdate()

    def setupUi(self, janelaAtualizarMoradores):
        janelaAtualizarMoradores.setObjectName("janelaAtualizarMoradores")
        janelaAtualizarMoradores.resize(725, 650)
        janelaAtualizarMoradores.setMinimumSize(QtCore.QSize(725, 650))
        janelaAtualizarMoradores.setMaximumSize(QtCore.QSize(725, 650))
        janelaAtualizarMoradores.setBaseSize(QtCore.QSize(725, 650))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        janelaAtualizarMoradores.setWindowIcon(icon)
        janelaAtualizarMoradores.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(janelaAtualizarMoradores)
        self.centralwidget.setObjectName("centralwidget")
        self.lblNomeCompleto = QtWidgets.QLabel(self.centralwidget)
        self.lblNomeCompleto.setGeometry(QtCore.QRect(30, 70, 151, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setItalic(False)
        self.lblNomeCompleto.setFont(font)
        self.lblNomeCompleto.setObjectName("lblNomeCompleto")
        self.lblCpf = QtWidgets.QLabel(self.centralwidget)
        self.lblCpf.setGeometry(QtCore.QRect(440, 74, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblCpf.setFont(font)
        self.lblCpf.setObjectName("lblCpf")
        self.lblEmail = QtWidgets.QLabel(self.centralwidget)
        self.lblEmail.setGeometry(QtCore.QRect(260, 220, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblEmail.setFont(font)
        self.lblEmail.setObjectName("lblEmail")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(570, 130, 55, 16))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.lblBloco = QtWidgets.QLabel(self.centralwidget)
        self.lblBloco.setGeometry(QtCore.QRect(420, 160, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblBloco.setFont(font)
        self.lblBloco.setObjectName("lblBloco")
        self.lblDataNascimento = QtWidgets.QLabel(self.centralwidget)
        self.lblDataNascimento.setGeometry(QtCore.QRect(30, 160, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblDataNascimento.setFont(font)
        self.lblDataNascimento.setObjectName("lblDataNascimento")
        self.lblNumeroApartamento = QtWidgets.QLabel(self.centralwidget)
        self.lblNumeroApartamento.setGeometry(QtCore.QRect(260, 160, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblNumeroApartamento.setFont(font)
        self.lblNumeroApartamento.setObjectName("lblNumeroApartamento")
        self.comboBoxBloco = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxBloco.setEnabled(True)
        self.comboBoxBloco.setGeometry(QtCore.QRect(420, 180, 71, 26))
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
        self.comboBoxTipoMorador.setGeometry(QtCore.QRect(520, 180, 181, 26))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBoxTipoMorador.setFont(font)
        self.comboBoxTipoMorador.setObjectName("comboBoxTipoMorador")
        self.comboBoxTipoMorador.addItem("")
        self.comboBoxTipoMorador.addItem("")
        self.comboBoxTipoMorador.addItem("")
        self.lblTipoMorador = QtWidgets.QLabel(self.centralwidget)
        self.lblTipoMorador.setGeometry(QtCore.QRect(520, 160, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblTipoMorador.setFont(font)
        self.lblTipoMorador.setObjectName("lblTipoMorador")
        self.lblTelefone = QtWidgets.QLabel(self.centralwidget)
        self.lblTelefone.setGeometry(QtCore.QRect(30, 220, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblTelefone.setFont(font)
        self.lblTelefone.setObjectName("lblTelefone")
        font = QtGui.QFont()
        font.setPointSize(9)
        font = QtGui.QFont()
        font.setPointSize(9)
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
        self.lblModeloVeiculo.setGeometry(QtCore.QRect(260, 450, 55, 16))
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
        self.comboBoxCorVeiculo.addItem("")
        self.comboBoxCorVeiculo.addItem("")
        self.comboBoxCorVeiculo.addItem("")
        self.comboBoxCorVeiculo.addItem("")
        self.comboBoxCorVeiculo.addItem("")
        self.comboBoxCorVeiculo.addItem("")
        self.comboBoxCorVeiculo.addItem("")
        self.lblPlaca = QtWidgets.QLabel(self.centralwidget)
        self.lblPlaca.setGeometry(QtCore.QRect(30, 520, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblPlaca.setFont(font)
        self.lblPlaca.setObjectName("lblPlaca")
        self.btnAtualizar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAtualizar.setGeometry(QtCore.QRect(580, 590, 131, 31))
        self.btnAtualizar.setAutoDefault(False)
        self.btnAtualizar.setObjectName("btnAtualizar")
        self.btnAtualizar.clicked.connect(self.abrirMsgBox)

        self.lblNumeroVaga = QtWidgets.QLabel(self.centralwidget)
        self.lblNumeroVaga.setGeometry(QtCore.QRect(30, 340, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblNumeroVaga.setFont(font)
        self.lblNumeroVaga.setObjectName("lblNumeroVaga")
        self.lblNomeApelido = QtWidgets.QLabel(self.centralwidget)
        self.lblNomeApelido.setGeometry(QtCore.QRect(30, 280, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblNomeApelido.setFont(font)
        self.lblNomeApelido.setObjectName("lblNomeApelido")
        self.lblSenha = QtWidgets.QLabel(self.centralwidget)
        self.lblSenha.setGeometry(QtCore.QRect(260, 280, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblSenha.setFont(font)
        self.lblSenha.setObjectName("lblSenha")
        self.lblConfirmarSenha = QtWidgets.QLabel(self.centralwidget)
        self.lblConfirmarSenha.setGeometry(QtCore.QRect(520, 280, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblConfirmarSenha.setFont(font)
        self.lblConfirmarSenha.setObjectName("lblConfirmarSenha")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(30, 400, 681, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
    
        self.lblTituloAtualizarMoradores = QtWidgets.QLabel(self.centralwidget)
        self.lblTituloAtualizarMoradores.setGeometry(QtCore.QRect(30, 20, 271, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblTituloAtualizarMoradores.setFont(font)
        self.lblTituloAtualizarMoradores.setObjectName("lblTituloAtualizarMoradores")
        self.btnLimpar = QtWidgets.QPushButton(self.centralwidget)
        self.btnLimpar.setGeometry(QtCore.QRect(390, 590, 131, 31))
        self.btnLimpar.setObjectName("btnLimpar")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 50, 671, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.inputPesquisarMorador = QtWidgets.QLineEdit(self.centralwidget)
        self.inputPesquisarMorador.setGeometry(QtCore.QRect(30, 90, 381, 26))
        self.inputPesquisarMorador.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
"")
        self.inputPesquisarMorador.setMaxLength(85)
        self.inputPesquisarMorador.setObjectName("inputPesquisarMorador")
        self.inputDataNascimento = QtWidgets.QLineEdit(self.centralwidget)
        self.inputDataNascimento.setGeometry(QtCore.QRect(30, 180, 181, 26))
        self.inputDataNascimento.setMaxLength(10)
        self.inputDataNascimento.setPlaceholderText("")
        self.inputDataNascimento.setObjectName("inputDataNascimento")
        self.inputPesquisarCpf = QtWidgets.QLineEdit(self.centralwidget)
        self.inputPesquisarCpf.setGeometry(QtCore.QRect(440, 90, 181, 26))
        self.inputPesquisarCpf.setMaxLength(14)
        self.inputPesquisarCpf.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.inputPesquisarCpf.setCursorPosition(0)
        self.inputPesquisarCpf.setObjectName("inputPesquisarCpf")
        self.inputNumeroApartamento = QtWidgets.QLineEdit(self.centralwidget)
        self.inputNumeroApartamento.setGeometry(QtCore.QRect(260, 180, 111, 26))
        self.inputNumeroApartamento.setMaxLength(4)
        self.inputNumeroApartamento.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.inputNumeroApartamento.setCursorPosition(0)
        self.inputNumeroApartamento.setObjectName("inputNumeroApartamento")
        self.inputTelefone = QtWidgets.QLineEdit(self.centralwidget)
        self.inputTelefone.setGeometry(QtCore.QRect(30, 240, 181, 26))
        self.inputTelefone.setMaxLength(16)
        self.inputTelefone.setCursorPosition(0)
        self.inputTelefone.setObjectName("inputTelefone")
        self.inputEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.inputEmail.setGeometry(QtCore.QRect(260, 240, 441, 26))
        self.inputEmail.setMaxLength(56)
        self.inputEmail.setDragEnabled(False)
        self.inputEmail.setObjectName("inputEmail")
        self.inputNomeApelido = QtWidgets.QLineEdit(self.centralwidget)
        self.inputNomeApelido.setGeometry(QtCore.QRect(30, 300, 181, 26))
        self.inputNomeApelido.setMaxLength(20)
        self.inputNomeApelido.setObjectName("inputNomeApelido")
        self.inputPlaca = QtWidgets.QLineEdit(self.centralwidget)
        self.inputPlaca.setEnabled(True)
        self.inputPlaca.setGeometry(QtCore.QRect(30, 540, 111, 26))
        self.inputPlaca.setMaxLength(7)
        self.inputPlaca.setObjectName("inputPlaca")
        self.inputSenha = QtWidgets.QLineEdit(self.centralwidget)
        self.inputSenha.setGeometry(QtCore.QRect(260, 300, 181, 26))
        self.inputSenha.setMaxLength(20)
        self.inputSenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputSenha.setObjectName("inputSenha")
        self.inputConfirmarSenha = QtWidgets.QLineEdit(self.centralwidget)
        self.inputConfirmarSenha.setGeometry(QtCore.QRect(520, 300, 181, 26))
        self.inputConfirmarSenha.setMaxLength(20)
        self.inputConfirmarSenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputConfirmarSenha.setObjectName("inputConfirmarSenha")
        self.inputModeloVeiculo = QtWidgets.QLineEdit(self.centralwidget)
        self.inputModeloVeiculo.setEnabled(True)
        self.inputModeloVeiculo.setGeometry(QtCore.QRect(260, 470, 181, 26))
        self.inputModeloVeiculo.setMaxLength(25)
        self.inputModeloVeiculo.setObjectName("inputModeloVeiculo")
        self.inputNumeroVaga = QtWidgets.QLineEdit(self.centralwidget)
        self.inputNumeroVaga.setEnabled(True)
        self.inputNumeroVaga.setGeometry(QtCore.QRect(30, 360, 111, 26))
        self.inputNumeroVaga.setMaxLength(4)
        self.inputNumeroVaga.setCursorPosition(0)
        self.inputNumeroVaga.setObjectName("inputNumeroVaga")
        self.lblResultado = QtWidgets.QLabel(self.centralwidget)
        self.lblResultado.setGeometry(QtCore.QRect(470, 340, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lblResultado.setFont(font)
        self.lblResultado.setText("")
        self.lblResultado.setObjectName("lblResultado")

        self.btnBuscarMorador = QtWidgets.QPushButton(self.centralwidget)
        self.btnBuscarMorador.setGeometry(QtCore.QRect(626, 90, 75, 26))
        self.btnBuscarMorador.setObjectName("btnBuscarMorador")

        self.btnBuscarMorador.clicked.connect(self.buscarMorador)


        self.radioOpcaoDesativado = QtWidgets.QRadioButton(self.centralwidget)
        self.radioOpcaoDesativado.setGeometry(QtCore.QRect(330, 370, 81, 20))
        self.radioOpcaoDesativado.setCheckable(True)
        self.radioOpcaoDesativado.setChecked(False)
        self.radioOpcaoDesativado.setObjectName("radioOpcaoDesativado")
        self.radioOpcaoAtivo = QtWidgets.QRadioButton(self.centralwidget)
        self.radioOpcaoAtivo.setGeometry(QtCore.QRect(280, 370, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioOpcaoAtivo.setFont(font)
        self.radioOpcaoAtivo.setObjectName("radioOpcaoAtivo")
        self.lblPossuiVeiculo_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblPossuiVeiculo_2.setGeometry(QtCore.QRect(290, 340, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblPossuiVeiculo_2.setFont(font)
        self.lblPossuiVeiculo_2.setObjectName("lblPossuiVeiculo_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 100, 21, 16))
        self.label.setObjectName("label")
        janelaAtualizarMoradores.setCentralWidget(self.centralwidget)
        self.lblNomeCompleto.setBuddy(self.inputPesquisarMorador)
        self.lblCpf.setBuddy(self.inputPesquisarCpf)
        self.lblEmail.setBuddy(self.inputEmail)
        self.lblBloco.setBuddy(self.comboBoxBloco)
        self.lblDataNascimento.setBuddy(self.inputDataNascimento)
        self.lblNumeroApartamento.setBuddy(self.inputNumeroApartamento)
        self.lblTipoMorador.setBuddy(self.comboBoxTipoMorador)
        self.lblTelefone.setBuddy(self.inputTelefone)
        self.lblTipoVeiculo.setBuddy(self.comboBoxTipoVeiculo)
        self.lblModeloVeiculo.setBuddy(self.inputModeloVeiculo)
        self.lblCorVeiculo.setBuddy(self.comboBoxCorVeiculo)
        self.lblPlaca.setBuddy(self.inputPlaca)
        self.lblNumeroVaga.setBuddy(self.inputNumeroVaga)
        self.lblNomeApelido.setBuddy(self.inputNomeApelido)
        self.lblSenha.setBuddy(self.inputSenha)
        self.lblConfirmarSenha.setBuddy(self.inputConfirmarSenha)

        self.inputPesquisarMorador.setFocus()

        self.retranslateUi(janelaAtualizarMoradores)
        self.btnLimpar.clicked.connect(self.inputPesquisarMorador.clear)
        self.btnLimpar.clicked.connect(self.inputDataNascimento.clear)
        self.btnLimpar.clicked.connect(self.inputPesquisarCpf.clear)
        self.btnLimpar.clicked.connect(self.inputConfirmarSenha.clear)
        self.btnLimpar.clicked.connect(self.inputModeloVeiculo.clear)
        self.btnLimpar.clicked.connect(self.inputNumeroVaga.clear)
        self.btnLimpar.clicked.connect(self.inputPlaca.clear)
        self.btnLimpar.clicked.connect(self.inputSenha.clear)
        self.btnLimpar.clicked.connect(self.inputNomeApelido.clear)
        self.btnLimpar.clicked.connect(self.inputTelefone.clear)
        self.btnLimpar.clicked.connect(self.inputNumeroApartamento.clear)
        self.btnLimpar.clicked.connect(self.inputEmail.clear)

        QtCore.QMetaObject.connectSlotsByName(janelaAtualizarMoradores)
        janelaAtualizarMoradores.setTabOrder(self.inputPesquisarMorador, self.inputPesquisarCpf)
        janelaAtualizarMoradores.setTabOrder(self.inputPesquisarCpf, self.btnBuscarMorador)
        janelaAtualizarMoradores.setTabOrder(self.inputDataNascimento, self.inputNumeroApartamento)
        janelaAtualizarMoradores.setTabOrder(self.inputNumeroApartamento, self.comboBoxBloco)
        janelaAtualizarMoradores.setTabOrder(self.comboBoxBloco, self.comboBoxTipoMorador)
        janelaAtualizarMoradores.setTabOrder(self.comboBoxTipoMorador, self.inputTelefone)
        janelaAtualizarMoradores.setTabOrder(self.inputTelefone, self.inputEmail)
        janelaAtualizarMoradores.setTabOrder(self.inputEmail, self.inputNomeApelido)
        janelaAtualizarMoradores.setTabOrder(self.inputNomeApelido, self.inputSenha)
        janelaAtualizarMoradores.setTabOrder(self.inputSenha, self.inputConfirmarSenha)
        janelaAtualizarMoradores.setTabOrder(self.inputConfirmarSenha, self.inputNumeroVaga)
        janelaAtualizarMoradores.setTabOrder(self.comboBoxTipoVeiculo, self.inputModeloVeiculo)
        janelaAtualizarMoradores.setTabOrder(self.inputModeloVeiculo, self.comboBoxCorVeiculo)
        janelaAtualizarMoradores.setTabOrder(self.comboBoxCorVeiculo, self.inputPlaca)
        janelaAtualizarMoradores.setTabOrder(self.inputPlaca, self.btnLimpar)
        janelaAtualizarMoradores.setTabOrder(self.btnLimpar, self.btnAtualizar)

    def retranslateUi(self, janelaAtualizarMoradores):
        _translate = QtCore.QCoreApplication.translate
        janelaAtualizarMoradores.setWindowTitle(_translate("janelaAtualizarMoradores", "PrimeCondo"))
        self.lblNomeCompleto.setText(_translate("janelaAtualizarMoradores", "&Nome Completo:"))
        self.lblCpf.setText(_translate("janelaAtualizarMoradores", "&CPF:"))
        self.lblEmail.setText(_translate("janelaAtualizarMoradores", "&E-mail:"))
        self.lblBloco.setText(_translate("janelaAtualizarMoradores", "&Bloco:"))
        self.lblDataNascimento.setText(_translate("janelaAtualizarMoradores", "&Data de Nascimento:"))
        self.lblNumeroApartamento.setText(_translate("janelaAtualizarMoradores", "Nº apt:"))
        self.comboBoxBloco.setItemText(0, _translate("janelaAtualizarMoradores", "A"))
        self.comboBoxBloco.setItemText(1, _translate("janelaAtualizarMoradores", "B"))
        self.comboBoxBloco.setItemText(2, _translate("janelaAtualizarMoradores", "C"))
        self.comboBoxBloco.setItemText(3, _translate("janelaAtualizarMoradores", "D"))
        self.comboBoxTipoMorador.setItemText(0, _translate("janelaAtualizarMoradores", "Proprietário"))
        self.comboBoxTipoMorador.setItemText(1, _translate("janelaAtualizarMoradores", "Morador"))
        self.comboBoxTipoMorador.setItemText(2, _translate("janelaAtualizarMoradores", "Dependente"))
        self.lblTipoMorador.setText(_translate("janelaAtualizarMoradores", "&Tipo de Morador:"))
        self.lblTelefone.setText(_translate("janelaAtualizarMoradores", "&Tefone:"))
        self.lblTipoVeiculo.setText(_translate("janelaAtualizarMoradores", "&Tipo"))
        self.comboBoxTipoVeiculo.setItemText(0, _translate("janelaAtualizarMoradores", "Carro"))
        self.comboBoxTipoVeiculo.setItemText(1, _translate("janelaAtualizarMoradores", "Moto"))
        self.comboBoxTipoVeiculo.setItemText(2, _translate("janelaAtualizarMoradores", "Outros"))
        self.lblModeloVeiculo.setText(_translate("janelaAtualizarMoradores", "&Modelo:"))
        self.lblCorVeiculo.setText(_translate("janelaAtualizarMoradores", "&Cor:"))
        self.comboBoxCorVeiculo.setItemText(0, _translate("janelaAtualizarMoradores", "Outros"))
        self.comboBoxCorVeiculo.setItemText(1, _translate("janelaAtualizarMoradores", "Prata"))
        self.comboBoxCorVeiculo.setItemText(2, _translate("janelaAtualizarMoradores", "Amarelo"))
        self.comboBoxCorVeiculo.setItemText(3, _translate("janelaAtualizarMoradores", "Roxo"))
        self.comboBoxCorVeiculo.setItemText(4, _translate("janelaAtualizarMoradores", "Preto"))
        self.comboBoxCorVeiculo.setItemText(5, _translate("janelaAtualizarMoradores", "Vermelho"))
        self.comboBoxCorVeiculo.setItemText(6, _translate("janelaAtualizarMoradores", "Azul"))
        self.comboBoxCorVeiculo.setItemText(7, _translate("janelaAtualizarMoradores", "Branco"))
        self.lblPlaca.setText(_translate("janelaAtualizarMoradores", "&Placa:"))
        self.btnAtualizar.setText(_translate("janelaAtualizarMoradores", "ATUALIZAR"))
        self.lblNumeroVaga.setText(_translate("janelaAtualizarMoradores", "&Nº da Vaga Veiculo:"))
        self.lblNomeApelido.setText(_translate("janelaAtualizarMoradores", "&Nome / Apelido"))
        self.lblSenha.setText(_translate("janelaAtualizarMoradores", "&Senha:"))
        self.lblConfirmarSenha.setText(_translate("janelaAtualizarMoradores", "&Confirmar Senha:"))
        self.lblTituloAtualizarMoradores.setText(_translate("janelaAtualizarMoradores", "Atualizar Moradores"))
        self.btnLimpar.setText(_translate("janelaAtualizarMoradores", "LIMPAR"))
        self.inputDataNascimento.setInputMask(_translate("janelaAtualizarMoradores", "00/00/0000"))
        self.inputPesquisarCpf.setInputMask(_translate("janelaAtualizarMoradores", "000.000.000-00"))
        self.inputPesquisarCpf.setPlaceholderText(_translate("janelaAtualizarMoradores", "Digite só números"))
        self.inputNumeroApartamento.setInputMask(_translate("janelaAtualizarMoradores", "0000"))
        self.inputTelefone.setInputMask(_translate("janelaAtualizarMoradores", "(000) 00000-0000"))
        self.inputNumeroVaga.setInputMask(_translate("janelaAtualizarMoradores", "0000"))
        self.btnBuscarMorador.setText(_translate("janelaAtualizarMoradores", "Buscar"))
        self.radioOpcaoDesativado.setText(_translate("janelaAtualizarMoradores", "Desativado"))
        self.radioOpcaoAtivo.setText(_translate("janelaAtualizarMoradores", "Ativo"))
        self.lblPossuiVeiculo_2.setText(_translate("janelaAtualizarMoradores", "Status Pessoa"))
        self.label.setText(_translate("janelaAtualizarMoradores", "ou"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    janelaAtualizarMoradores = QtWidgets.QMainWindow()
    ui = Ui_janelaAtualizarMoradores()
    ui.setupUi(janelaAtualizarMoradores)
    janelaAtualizarMoradores.show()
    sys.exit(app.exec_())
