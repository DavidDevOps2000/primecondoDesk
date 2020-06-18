from conectabanco import ConectaBanco
from PyQt5 import QtCore, QtGui, QtWidgets
                                            #Obs IMPORTANTE, sempre use ".self" no começo nos parametros das funcoes ->(self), e no começo de toda Variavel self.nomeVariavel dentro das Classes 

class Ui_janelaCadastroMorador(object):

    def funcSalvarMorador(self):
        self.vlrNomeCompletoMorador  = self.inputNomeCompleto.toPlainText()
        self.vlrCpfMorador           = self.inputCpf.toPlainText()
        self.vlrSenha                = self.inputSenha.toPlainText()
        self.vlrApelido              = self.inputNomeApelido.toPlainText()
        self.vlrTipo                 = str(self.comboBoxTipoMorador.currentText())#Pegando o valor do comboBox e convertendo em string

        self.sets = ("'%s','%s','%s','%s','%s'" % (self.vlrCpfMorador, self.vlrNomeCompletoMorador, self.vlrSenha, self.vlrApelido, self.vlrTipo))

        self.insertar = ConectaBanco()
        
        try:
                self.insertar.insertMorador(self.sets)
                
                print(self.sets)
                
                if not self.insertar:
                        print("Deu errado")
                else: 
                        print("Funcionou")
        except:
                print('Erro de Conexao')





    def setupUi(self, janelaCadastroMorador):
########################################################################
        janelaCadastroMorador.setObjectName("janelaCadastroMorador")# Aqui é as configurações de Janela
        janelaCadastroMorador.resize(725, 610)
        janelaCadastroMorador.setMinimumSize(QtCore.QSize(725, 610))
        janelaCadastroMorador.setMaximumSize(QtCore.QSize(725, 610))
###########################################################################

        self.centralwidget = QtWidgets.QWidget(janelaCadastroMorador)                       #Aqui definimos os Nomes das Labels da Tela Morador
        self.centralwidget.setObjectName("centralwidget")

        self.lblNomeCompleto = QtWidgets.QLabel(self.centralwidget)
        self.lblNomeCompleto.setGeometry(QtCore.QRect(20, 80, 111, 21))
        self.lblNomeCompleto.setObjectName("lblNomeCompleto")
        self.lblCpf = QtWidgets.QLabel(self.centralwidget)
        self.lblCpf.setGeometry(QtCore.QRect(20, 140, 55, 16))
        self.lblCpf.setObjectName("lblCpf")
        self.lblEmail = QtWidgets.QLabel(self.centralwidget)
        self.lblEmail.setGeometry(QtCore.QRect(250, 200, 55, 16))
        self.lblEmail.setObjectName("lblEmail")
        self.lblBloco = QtWidgets.QLabel(self.centralwidget)
        self.lblBloco.setGeometry(QtCore.QRect(400, 140, 55, 16))
        self.lblBloco.setObjectName("lblBloco")
        self.lblDataNascimento = QtWidgets.QLabel(self.centralwidget)
        self.lblDataNascimento.setGeometry(QtCore.QRect(520, 80, 131, 16))
        self.lblDataNascimento.setObjectName("lblDataNascimento")
        self.lblNumeroApartamento = QtWidgets.QLabel(self.centralwidget)
        self.lblNumeroApartamento.setGeometry(QtCore.QRect(250, 140, 101, 16))
        self.lblNumeroApartamento.setObjectName("lblNumeroApartamento")
        self.lblTipoMorador = QtWidgets.QLabel(self.centralwidget)
        self.lblTipoMorador.setGeometry(QtCore.QRect(520, 140, 101, 16))
        self.lblTipoMorador.setObjectName("lblTipoMorador")
        self.lblTelefone = QtWidgets.QLabel(self.centralwidget)
        self.lblTelefone.setGeometry(QtCore.QRect(20, 200, 55, 16))
        self.lblTelefone.setObjectName("lblTelefone")
        self.lblPossuiVeiculo = QtWidgets.QLabel(self.centralwidget)
        self.lblPossuiVeiculo.setGeometry(QtCore.QRect(20, 400, 91, 16))
        self.lblPossuiVeiculo.setObjectName("lblPossuiVeiculo")
        self.lblMarca = QtWidgets.QLabel(self.centralwidget)
        self.lblMarca.setGeometry(QtCore.QRect(20, 430, 55, 16))
        self.lblMarca.setObjectName("lblMarca")
        self.lblModelo = QtWidgets.QLabel(self.centralwidget)
        self.lblModelo.setGeometry(QtCore.QRect(170, 430, 55, 16))
        self.lblModelo.setObjectName("lblModelo")
        self.lblCorVeiculo = QtWidgets.QLabel(self.centralwidget)
        self.lblCorVeiculo.setGeometry(QtCore.QRect(20, 500, 55, 16))
        self.lblCorVeiculo.setObjectName("lblCorVeiculo")
        self.lblFabricacaoVeiculo = QtWidgets.QLabel(self.centralwidget)
        self.lblFabricacaoVeiculo.setGeometry(QtCore.QRect(570, 430, 121, 16))
        self.lblFabricacaoVeiculo.setObjectName("lblFabricacaoVeiculo")
        self.lblNumeroVaga = QtWidgets.QLabel(self.centralwidget)
        self.lblNumeroVaga.setGeometry(QtCore.QRect(170, 500, 81, 16))
        self.lblNumeroVaga.setObjectName("lblNumeroVaga")
        self.lblPlaca = QtWidgets.QLabel(self.centralwidget)
        self.lblPlaca.setGeometry(QtCore.QRect(400, 430, 55, 16))
        self.lblPlaca.setObjectName("lblPlaca")
        self.lblNomeApelido = QtWidgets.QLabel(self.centralwidget)
        self.lblNomeApelido.setGeometry(QtCore.QRect(20, 260, 101, 16))
        self.lblNomeApelido.setObjectName("lblNomeApelido")
        self.lblSenha = QtWidgets.QLabel(self.centralwidget)
        self.lblSenha.setGeometry(QtCore.QRect(250, 260, 55, 16))
        self.lblSenha.setObjectName("lblSenha")
        self.lblConfirmarSenha = QtWidgets.QLabel(self.centralwidget)
        self.lblConfirmarSenha.setGeometry(QtCore.QRect(520, 260, 111, 16))
        self.lblConfirmarSenha.setObjectName("lblConfirmarSenha")
        self.lblRfid = QtWidgets.QLabel(self.centralwidget)
        self.lblRfid.setGeometry(QtCore.QRect(20, 320, 101, 16))
        self.lblRfid.setObjectName("lblRfid")
        self.lblDigital = QtWidgets.QLabel(self.centralwidget)
        self.lblDigital.setGeometry(QtCore.QRect(130, 320, 101, 16))
        self.lblDigital.setObjectName("lblDigital")
        self.lblTituloCadastroMorador = QtWidgets.QLabel(self.centralwidget)
        self.lblTituloCadastroMorador.setGeometry(QtCore.QRect(20, 10, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblTituloCadastroMorador.setFont(font)
        self.lblTituloCadastroMorador.setObjectName("lblTituloCadastroMorador")
##################################################################################

        self.inputNomeCompleto = QtWidgets.QTextEdit(self.centralwidget)                      # Aqui definimos os inputs (Entrada de dados) da tela Morador
        self.inputNomeCompleto.setGeometry(QtCore.QRect(20, 100, 451, 31))
        self.inputNomeCompleto.setObjectName("inputNomeCompleto")
        self.inputCpf = QtWidgets.QTextEdit(self.centralwidget)
        self.inputCpf.setGeometry(QtCore.QRect(20, 160, 181, 31))
        self.inputCpf.setObjectName("inputCpf")
        self.inputDataNascimento = QtWidgets.QTextEdit(self.centralwidget)
        self.inputDataNascimento.setGeometry(QtCore.QRect(520, 100, 181, 31))
        self.inputDataNascimento.setObjectName("inputDataNascimento")
        self.inputEmail = QtWidgets.QTextEdit(self.centralwidget)
        self.inputEmail.setGeometry(QtCore.QRect(250, 220, 451, 31))
        self.inputEmail.setObjectName("inputEmail")
        self.inputNumeroApartamento = QtWidgets.QTextEdit(self.centralwidget)
        self.inputNumeroApartamento.setGeometry(QtCore.QRect(250, 160, 111, 31))
        self.inputNumeroApartamento.setObjectName("inputNumeroApartamento")
        self.inputTelefone = QtWidgets.QTextEdit(self.centralwidget)
        self.inputTelefone.setGeometry(QtCore.QRect(20, 220, 181, 31))
        self.inputTelefone.setObjectName("inputTelefone")
        self.inputFabricacaoVeiculo = QtWidgets.QTextEdit(self.centralwidget)
        self.inputFabricacaoVeiculo.setGeometry(QtCore.QRect(570, 450, 121, 31))
        self.inputFabricacaoVeiculo.setObjectName("inputFabricacaoVeiculo")
        self.inputNumeroVaga = QtWidgets.QTextEdit(self.centralwidget)
        self.inputNumeroVaga.setGeometry(QtCore.QRect(170, 520, 111, 31))
        self.inputNumeroVaga.setObjectName("inputNumeroVaga")
        self.inputNomeApelido = QtWidgets.QTextEdit(self.centralwidget)
        self.inputNomeApelido.setGeometry(QtCore.QRect(20, 280, 181, 31))
        self.inputNomeApelido.setObjectName("inputNomeApelido")
        self.inputModeloVeiculo = QtWidgets.QTextEdit(self.centralwidget)
        self.inputModeloVeiculo.setGeometry(QtCore.QRect(170, 450, 181, 31))
        self.inputModeloVeiculo.setObjectName("inputModeloVeiculo")
        self.inputPlacaVeiculo = QtWidgets.QTextEdit(self.centralwidget)
        self.inputPlacaVeiculo.setGeometry(QtCore.QRect(400, 450, 111, 31))
        self.inputPlacaVeiculo.setObjectName("inputPlacaVeiculo")
        self.inputDigital = QtWidgets.QTextEdit(self.centralwidget)
        self.inputDigital.setGeometry(QtCore.QRect(130, 340, 71, 31))
        self.inputDigital.setObjectName("inputDigital")
        self.inputSenha = QtWidgets.QTextEdit(self.centralwidget)
        self.inputSenha.setGeometry(QtCore.QRect(250, 280, 181, 31))
        self.inputSenha.setObjectName("inputSenha")
        self.inputConfirmarSenha = QtWidgets.QTextEdit(self.centralwidget)
        self.inputConfirmarSenha.setGeometry(QtCore.QRect(520, 280, 181, 31))
        self.inputConfirmarSenha.setObjectName("inputConfirmarSenha")
        self.inputRfid = QtWidgets.QTextEdit(self.centralwidget)
        self.inputRfid.setGeometry(QtCore.QRect(20, 340, 71, 31))
        self.inputRfid.setObjectName("inputRfid")        
##################################################################################

        self.comboBoxBloco = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxBloco.setEnabled(True)                                                     # Aqui sao sao os comboBox do BLOCO
        self.comboBoxBloco.setGeometry(QtCore.QRect(400, 160, 71, 31))
        self.comboBoxBloco.setObjectName("comboBoxBloco")
        self.comboBoxBloco.addItem("")
        self.comboBoxBloco.addItem("")
        self.comboBoxBloco.addItem("")
        self.comboBoxBloco.addItem("")
##################################################################################

        self.comboBoxTipoMorador = QtWidgets.QComboBox(self.centralwidget)                      # Aqui sao sao os comboBox do TIPO MORADOR
        self.comboBoxTipoMorador.setEnabled(True)
        self.comboBoxTipoMorador.setGeometry(QtCore.QRect(520, 160, 181, 31))
        self.comboBoxTipoMorador.setObjectName("comboBoxTipoMorador")
        self.comboBoxTipoMorador.addItem("")
        self.comboBoxTipoMorador.addItem("")
        self.comboBoxTipoMorador.addItem("")
##################################################################################

        self.radioBoxOpcaoSim = QtWidgets.QRadioButton(self.centralwidget) # RadioBox OPção Veiculo 
        self.radioBoxOpcaoSim.setGeometry(QtCore.QRect(110, 400, 95, 20))
        self.radioBoxOpcaoSim.setObjectName("radioBoxOpcaoSim")
        self.radioBoxOpcaoNao = QtWidgets.QRadioButton(self.centralwidget)
        self.radioBoxOpcaoNao.setGeometry(QtCore.QRect(160, 400, 95, 20))
        self.radioBoxOpcaoNao.setObjectName("radioBoxOpcaoNao")
###################################################################################

        self.comboBoxMarcaVeiculo = QtWidgets.QComboBox(self.centralwidget) # ComboBox Veiculo
        self.comboBoxMarcaVeiculo.setEnabled(True)
        self.comboBoxMarcaVeiculo.setGeometry(QtCore.QRect(20, 450, 121, 31))
        self.comboBoxMarcaVeiculo.setObjectName("comboBoxMarcaVeiculo")
        self.comboBoxMarcaVeiculo.addItem("")
        self.comboBoxMarcaVeiculo.setItemText(0, "")
        self.comboBoxMarcaVeiculo.addItem("")
        self.comboBoxMarcaVeiculo.addItem("")
        self.comboBoxMarcaVeiculo.addItem("")
        self.comboBoxMarcaVeiculo.addItem("")
        self.comboBoxMarcaVeiculo.addItem("")
        self.comboBoxMarcaVeiculo.addItem("")
        self.comboBoxMarcaVeiculo.addItem("")
        self.comboBoxMarcaVeiculo.addItem("")
        self.comboBoxMarcaVeiculo.addItem("")
        self.comboBoxMarcaVeiculo.addItem("")
        self.comboBoxMarcaVeiculo.addItem("")
        self.comboBoxCorVeiculo = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxCorVeiculo.setEnabled(True)
        self.comboBoxCorVeiculo.setGeometry(QtCore.QRect(20, 520, 121, 31))
        self.comboBoxCorVeiculo.setObjectName("comboBoxCorVeiculo")
        self.comboBoxCorVeiculo.addItem("")
        self.comboBoxCorVeiculo.setItemText(0, "")
        self.comboBoxCorVeiculo.addItem("")
        self.comboBoxCorVeiculo.addItem("")
        self.comboBoxCorVeiculo.addItem("")

###################################################################################

        self.btnSalvar = QtWidgets.QPushButton(self.centralwidget)              # Botao salvar
        self.btnSalvar.setGeometry(QtCore.QRect(570, 550, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btnSalvar.setFont(font)
        self.btnSalvar.setAutoDefault(False)
        self.btnSalvar.setObjectName("btnSalvar")
        self.btnSalvar.clicked.connect(self.funcSalvarMorador)
##################################################################################

        self.linha = QtWidgets.QFrame(self.centralwidget)                       #Linhas
        self.linha.setGeometry(QtCore.QRect(20, 380, 671, 20))
        self.linha.setFrameShape(QtWidgets.QFrame.HLine)
        self.linha.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.linha.setObjectName("linha")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 50, 681, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
##################################################################################

        janelaCadastroMorador.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(janelaCadastroMorador)
        self.statusbar.setObjectName("statusbar")
        janelaCadastroMorador.setStatusBar(self.statusbar)
        self.retranslateUi(janelaCadastroMorador)
        QtCore.QMetaObject.connectSlotsByName(janelaCadastroMorador)
###################################################################################
    def retranslateUi(self, janelaCadastroMorador):                                                                 #Daqui pra baixo Apenas estamos jogando tudo na tela pelo SET
######################################################
        _translate = QtCore.QCoreApplication.translate
        janelaCadastroMorador.setWindowTitle(_translate("janelaCadastroMorador", "MainWindow"))
        self.lblNomeCompleto.setText(_translate("janelaCadastroMorador", "Nome Completo:"))
        self.lblCpf.setText(_translate("janelaCadastroMorador", "CPF:"))
        self.lblEmail.setText(_translate("janelaCadastroMorador", "E-mail:"))
        self.lblBloco.setText(_translate("janelaCadastroMorador", "Bloco:"))
######################################################

        self.lblDataNascimento.setText(_translate("janelaCadastroMorador", "Data de Nascimento:"))
        self.lblNumeroApartamento.setText(_translate("janelaCadastroMorador", "Nº apartamento:"))
        self.comboBoxBloco.setItemText(0, _translate("janelaCadastroMorador", "A"))
        self.comboBoxBloco.setItemText(1, _translate("janelaCadastroMorador", "B"))
        self.comboBoxBloco.setItemText(2, _translate("janelaCadastroMorador", "C"))
        self.comboBoxBloco.setItemText(3, _translate("janelaCadastroMorador", "D"))
######################################################

        self.comboBoxTipoMorador.setItemText(0, _translate("janelaCadastroMorador", "Proprietário"))
        self.comboBoxTipoMorador.setItemText(1, _translate("janelaCadastroMorador", "Morador"))
        self.comboBoxTipoMorador.setItemText(2, _translate("janelaCadastroMorador", "Dependente"))
######################################################

        self.lblTipoMorador.setText(_translate("janelaCadastroMorador", "Tipo de Morador:"))
        self.lblTelefone.setText(_translate("janelaCadastroMorador", "Tefone:"))
        self.radioBoxOpcaoSim.setText(_translate("janelaCadastroMorador", "Sim"))
        self.radioBoxOpcaoNao.setText(_translate("janelaCadastroMorador", "Não"))
        self.lblPossuiVeiculo.setText(_translate("janelaCadastroMorador", "Possui Veiculo"))
        self.lblMarca.setText(_translate("janelaCadastroMorador", "Marca"))
######################################################

        self.comboBoxMarcaVeiculo.setItemText(1, _translate("janelaCadastroMorador", "Audi"))
        self.comboBoxMarcaVeiculo.setItemText(2, _translate("janelaCadastroMorador", "Agrale"))
        self.comboBoxMarcaVeiculo.setItemText(3, _translate("janelaCadastroMorador", "Aston Matin"))
        self.comboBoxMarcaVeiculo.setItemText(4, _translate("janelaCadastroMorador", "Bentley"))
        self.comboBoxMarcaVeiculo.setItemText(5, _translate("janelaCadastroMorador", "BMW"))
        self.comboBoxMarcaVeiculo.setItemText(6, _translate("janelaCadastroMorador", "BYD"))
        self.comboBoxMarcaVeiculo.setItemText(7, _translate("janelaCadastroMorador", "Caoa"))
        self.comboBoxMarcaVeiculo.setItemText(8, _translate("janelaCadastroMorador", "Ferrari"))
        self.comboBoxMarcaVeiculo.setItemText(9, _translate("janelaCadastroMorador", "Volskvagen"))
        self.comboBoxMarcaVeiculo.setItemText(10, _translate("janelaCadastroMorador", "Fiat"))
        self.comboBoxMarcaVeiculo.setItemText(11, _translate("janelaCadastroMorador", "Chevrolet"))
######################################################

        self.lblModelo.setText(_translate("janelaCadastroMorador", "Modelo"))
        self.lblCorVeiculo.setText(_translate("janelaCadastroMorador", "Cor:"))
        self.comboBoxCorVeiculo.setItemText(1, _translate("janelaCadastroMorador", "Preto"))
        self.comboBoxCorVeiculo.setItemText(2, _translate("janelaCadastroMorador", "Vermelho"))
        self.comboBoxCorVeiculo.setItemText(3, _translate("janelaCadastroMorador", "Azul"))
######################################################

        self.lblPlaca.setText(_translate("janelaCadastroMorador", "Placa:"))
        self.btnSalvar.setText(_translate("janelaCadastroMorador", "Salvar"))
        self.lblFabricacaoVeiculo.setText(_translate("janelaCadastroMorador", "Data de Fabricação:"))
        self.lblNumeroVaga.setText(_translate("janelaCadastroMorador", "Nº da Vaga:"))
        self.lblNomeApelido.setText(_translate("janelaCadastroMorador", "Nome / Apelido"))
        self.lblSenha.setText(_translate("janelaCadastroMorador", "Senha:"))
        self.lblConfirmarSenha.setText(_translate("janelaCadastroMorador", "Confirmar Senha:"))
        self.lblRfid.setText(_translate("janelaCadastroMorador", "RFID"))
        self.lblDigital.setText(_translate("janelaCadastroMorador", "DIGITAL"))
        self.lblTituloCadastroMorador.setText(_translate("janelaCadastroMorador", "Cadastro de Moradores"))
########################################################################


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    janelaCadastroMorador = QtWidgets.QMainWindow()
    ui = Ui_janelaCadastroMorador()
    ui.setupUi(janelaCadastroMorador)
    janelaCadastroMorador.show()
    sys.exit(app.exec_())
