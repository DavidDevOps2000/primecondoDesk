from funcVisitante import FuncoesVisitante
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from tkinter import messagebox
from tkinter import Tk


class Ui_janelaCadastrarVisitantes(object):

    def blockCampo(self):
        self.inputRgVisitante.setEnabled(False)
        self.inputNomeVisitante.setEnabled(False)
        self.comboBoxNumDias.setEnabled(False)
        self.btnSalvarVisi.setEnabled(False)
        self.btnSalvarVisi.setEnabled(False)

    def limparCampos(self):
        self.btnLimpar.clicked.connect(self.inputNomeCompleto.clear)
        self.btnLimpar.clicked.connect(self.inputCpf.clear)
        self.btnLimpar.clicked.connect(self.inputNomeVisitante.clear)
        self.btnLimpar.clicked.connect(self.inputRgVisitante.clear)
        self.btnLimpar.clicked.connect(self.inputNomeCompleto.clear)
        self.btnLimpar.clicked.connect(self.inputCpf.clear)
        self.btnLimpar.clicked.connect(self.inputNumeroApartamento.clear)
        self.btnLimpar.clicked.connect(self.inputNumeroVaga.clear)
        self.lblResultadoStatus.setText("Ativo/ Desativado")
        self.lblResultado.setText("")
        self.btnLimpar.clicked.connect(self.blockCampo)

    def consulMorador(self):
        self.conexao = FuncoesVisitante()
        self.conexao.conecta()

        self.cpfMorador  = self.inputCpf.text()
        self.nomeMorador = self.inputNomeCompleto.text()
        self.cmdBancoVisi = FuncoesVisitante()

        try:
            
            self.result = self.cmdBancoVisi.consulMoradorToVisi(self.nomeMorador, self.cpfMorador)
            self.lblResultado.setText("")

            if len(self.result) > 0: #Se a condição vier TRUE(1) é pq existe esse morador vai passar, e se for False(0) vai dizer que não

                    self.statusVer = str(self.result[0][2])
                    if self.statusVer == 'ATIVO':#Se o Morador estiver ativado poderá avançar
                                
                                print(self.statusVer)

                                if not self.cmdBancoVisi:
                                        self.lblResultado.setText("Erro")

                                else:
                                        self.inputNomeCompleto.setText(str(self.result[0][3]))
                                        self.inputNumeroApartamento.setText(str(self.result[0][0]))
                                        self.comboBoxBloco.setCurrentText(str(self.result[0][1]))
                                        self.inputNumeroVaga.setText(str(self.result[0][4]))
                                        self.lblResultadoStatus.setText(str(self.result[0][2]))#Seu Status atuaal
                                        self.lblResultado.setText("Encontrado")
                                        self.inputRgVisitante.setEnabled(True)
                                        self.inputNomeVisitante.setEnabled(True)
                                        self.comboBoxNumDias.setEnabled(True)
                                        self.btnSalvarVisi.setEnabled(True)
                    else:
                                self.lblResultado.setText("Morador Desativado")
                                self.blockCampo()
                                self.lblResultadoStatus.setText("Ativo/ Desativado")
            else:
                        self.lblResultado.setText("Morador não encontrado")
                        self.blockCampo()
                        self.lblResultadoStatus.setText("Ativo/ Desativado")
        except:
                self.lblResultado.setText("Erro banco")
                self.blockCampo()


    def salvarVisi(self):
        self.conexao.conecta()
        self.cpfMorador  = self.inputCpf.text()
        self.visiNome    = self.inputNomeVisitante.text()
        self.rgVisi      = self.inputRgVisitante.text()
        self.vlrDias     = self.comboBoxNumDias.currentText()

        try:
                if self.visiNome != '':

                        self.result = self.cmdBancoVisi.buscarIdMoradorToVisi(self.cpfMorador)
            
                        if not self.cmdBancoVisi:
                                self.lblResultado.setText("Não foi encontrado morador")
                                print("Aqui 1")
                        else:
                                self.idMoradorVisi = int(self.result[0][0])
                                print(self.idMoradorVisi)
                                self.verificarVisi = self.cmdBancoVisi.verificarVisiExiste(self.idMoradorVisi, self.visiNome)
                                print(len(self.verificarVisi))
                                print("Aqui 2")

                                if len(self.verificarVisi) == 0:
                                        self.cmdBancoVisi.insertVisi1(self.visiNome, self.rgVisi)
                                        print("Aqui 3")

                                        if not self.cmdBancoVisi:
                                                self.lblResultado.setText("Erro inserir dados")
                                                print("Aqui 4")
                                        else:
                                                self.idVisita = self.cmdBancoVisi.idVisi(self.visiNome, self.rgVisi)
                                                print("Aqui 5")

                                                if self.vlrDias == 'Sem limite':# Caso escolham sem data definida
                                                        print("Aqui 6")

                                                        if not self.cmdBancoVisi:
                                                                self.lblResultado.setText("Erro ao pegar id")

                                                        else:
                                                                self.idVisita = int(self.idVisita[0][0])
                                                                self.cmdBancoVisi.insertVisi2(self.idMoradorVisi, self.idVisita)
                                                                self.lblResultado.setText("Cadastrado com sucesso")
                                                                print("Aqui 7")

                                                                self.blockCampo()
                                                else:
                                                        if not self.cmdBancoVisi:
                                                                self.lblResultado.setText("Erro ao pegar id")
                                                                print("Aqui 8")

                                                        else:
                                                                self.vlrDias  = int(self.comboBoxNumDias.currentText())
                                                                self.idVisita = int(self.idVisita[0][0])
                                                                self.cmdBancoVisi.insertVisi3(self.idMoradorVisi, self.idVisita, self.vlrDias)
                                                                print("Aqui 9")

                                                                if not self.cmdBancoVisi:
                                                                        self.lblResultado.setText("Erro ao inserir dados")
                                                                else:
                                                                        self.lblResultado.setText("Cadastrado com sucesso")
                                                                        self.blockCampo()
                                else:
                                         self.lblResultado.setText("Visitante já existe")
                else:
                        self.lblResultado.setText("Campos Vazios")
        except:
                self.lblResultado.setText("Erro banco")


    def abrirMsgBox(self):
             top = Tk()  
             top.geometry("0x0")
             top.overrideredirect(True)  
             ok = messagebox.askokcancel("Cadastrar Visitante","Você tem certeza que quer cadastrá-lo(a) ?") 
        
             if ok:                          #Se a pessoa clicar em OK ....
                       self.salvarVisi()


        
    def setupUi(self, janelaCadastrarVisitantes):
        janelaCadastrarVisitantes.setObjectName("janelaCadastrarVisitantes")
        janelaCadastrarVisitantes.resize(730, 600)
        janelaCadastrarVisitantes.setMinimumSize(QtCore.QSize(730, 600))
        janelaCadastrarVisitantes.setMaximumSize(QtCore.QSize(730, 650))
        janelaCadastrarVisitantes.setBaseSize(QtCore.QSize(725, 650))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        janelaCadastrarVisitantes.setWindowIcon(icon)
        janelaCadastrarVisitantes.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(janelaCadastrarVisitantes)
        self.centralwidget.setObjectName("centralwidget")
        self.lblNomeCompleto = QtWidgets.QLabel(self.centralwidget)
        self.lblNomeCompleto.setGeometry(QtCore.QRect(30, 80, 181, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setItalic(False)
        self.lblNomeCompleto.setFont(font)
        self.lblNomeCompleto.setObjectName("lblNomeCompleto")
        self.lblCpf = QtWidgets.QLabel(self.centralwidget)
        self.lblCpf.setGeometry(QtCore.QRect(440, 80, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblCpf.setFont(font)
        self.lblCpf.setObjectName("lblCpf")
        self.comboBoxNumDias = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxNumDias.setEnabled(True)
        self.comboBoxNumDias.setGeometry(QtCore.QRect(560, 330, 141, 26))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBoxNumDias.setFont(font)
        self.comboBoxNumDias.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBoxNumDias.setObjectName("comboBoxNumDias")
        self.comboBoxNumDias.addItem("")
        self.comboBoxNumDias.addItem("")
        self.comboBoxNumDias.addItem("")
        self.comboBoxNumDias.addItem("")
        self.comboBoxNumDias.addItem("")
        self.comboBoxNumDias.addItem("")
        self.comboBoxNumDias.addItem("")
        self.lblTipoMorador = QtWidgets.QLabel(self.centralwidget)
        self.lblTipoMorador.setGeometry(QtCore.QRect(560, 310, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblTipoMorador.setFont(font)
        self.lblTipoMorador.setObjectName("lblTipoMorador")
        self.btnSalvarVisi = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalvarVisi.setGeometry(QtCore.QRect(570, 510, 131, 31))
        self.btnSalvarVisi.setAutoDefault(False)
        self.btnSalvarVisi.setObjectName("btnSalvarVisi")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(30, 240, 671, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lblTituloCadastrarVisitantes = QtWidgets.QLabel(self.centralwidget)
        self.lblTituloCadastrarVisitantes.setGeometry(QtCore.QRect(30, 20, 271, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblTituloCadastrarVisitantes.setFont(font)
        self.lblTituloCadastrarVisitantes.setObjectName("lblTituloCadastrarVisitantes")
        self.btnLimpar = QtWidgets.QPushButton(self.centralwidget)
        self.btnLimpar.setGeometry(QtCore.QRect(380, 510, 131, 31))
        self.btnLimpar.setObjectName("btnLimpar")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 50, 671, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.inputNomeCompleto = QtWidgets.QLineEdit(self.centralwidget)
        self.inputNomeCompleto.setGeometry(QtCore.QRect(30, 100, 381, 26))
        self.inputNomeCompleto.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
"")
        self.inputNomeCompleto.setMaxLength(85)
        self.inputNomeCompleto.setObjectName("inputNomeCompleto")
        self.inputCpf = QtWidgets.QLineEdit(self.centralwidget)
        self.inputCpf.setGeometry(QtCore.QRect(440, 100, 181, 26))
        self.inputCpf.setMaxLength(14)
        self.inputCpf.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.inputCpf.setCursorPosition(0)
        self.inputCpf.setObjectName("inputCpf")
        self.lblResultado = QtWidgets.QLabel(self.centralwidget)
        self.lblResultado.setGeometry(QtCore.QRect(450, 400, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lblResultado.setFont(font)
        self.lblResultado.setText("")
        self.lblResultado.setObjectName("lblResultado")
        self.btnBuscarVisi = QtWidgets.QPushButton(self.centralwidget)
        self.btnBuscarVisi.setGeometry(QtCore.QRect(630, 100, 75, 26))
        self.btnBuscarVisi.setObjectName("btnBuscarVisi")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 100, 21, 16))
        self.label.setObjectName("label")
        self.lblBloco = QtWidgets.QLabel(self.centralwidget)
        self.lblBloco.setGeometry(QtCore.QRect(440, 150, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblBloco.setFont(font)
        self.lblBloco.setObjectName("lblBloco")
        self.comboBoxBloco = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxBloco.setEnabled(True)
        self.comboBoxBloco.setGeometry(QtCore.QRect(440, 170, 71, 26))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBoxBloco.setFont(font)
        self.comboBoxBloco.setObjectName("comboBoxBloco")
        self.comboBoxBloco.addItem("")
        self.comboBoxBloco.addItem("")
        self.comboBoxBloco.addItem("")
        self.comboBoxBloco.addItem("")
        self.lblNumeroVaga = QtWidgets.QLabel(self.centralwidget)
        self.lblNumeroVaga.setGeometry(QtCore.QRect(230, 150, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblNumeroVaga.setFont(font)
        self.lblNumeroVaga.setObjectName("lblNumeroVaga")
        self.inputNumeroVaga = QtWidgets.QLineEdit(self.centralwidget)
        self.inputNumeroVaga.setEnabled(True)
        self.inputNumeroVaga.setGeometry(QtCore.QRect(230, 170, 111, 26))
        self.inputNumeroVaga.setMaxLength(4)
        self.inputNumeroVaga.setCursorPosition(0)
        self.inputNumeroVaga.setObjectName("inputNumeroVaga")
        self.lblStatusMorador = QtWidgets.QLabel(self.centralwidget)
        self.lblStatusMorador.setGeometry(QtCore.QRect(580, 180, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblStatusMorador.setFont(font)
        self.lblStatusMorador.setObjectName("lblStatusMorador")
        self.inputNumeroApartamento = QtWidgets.QLineEdit(self.centralwidget)
        self.inputNumeroApartamento.setGeometry(QtCore.QRect(30, 170, 111, 26))
        self.inputNumeroApartamento.setMaxLength(4)
        self.inputNumeroApartamento.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.inputNumeroApartamento.setCursorPosition(0)
        self.inputNumeroApartamento.setObjectName("inputNumeroApartamento")
        self.lblNumeroApartamento = QtWidgets.QLabel(self.centralwidget)
        self.lblNumeroApartamento.setGeometry(QtCore.QRect(30, 150, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblNumeroApartamento.setFont(font)
        self.lblNumeroApartamento.setObjectName("lblNumeroApartamento")
        self.lblResultadoStatus = QtWidgets.QLabel(self.centralwidget)
        self.lblResultadoStatus.setGeometry(QtCore.QRect(580, 210, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblResultadoStatus.setFont(font)
        self.lblResultadoStatus.setObjectName("lblResultadoStatus")
        self.inputNomeVisitante = QtWidgets.QLineEdit(self.centralwidget)
        self.inputNomeVisitante.setGeometry(QtCore.QRect(30, 330, 381, 26))
        self.inputNomeVisitante.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
"")
        self.inputNomeVisitante.setMaxLength(85)
        self.inputNomeVisitante.setObjectName("inputNomeVisitante")
        self.lblNomeCompleto_3 = QtWidgets.QLabel(self.centralwidget)
        self.lblNomeCompleto_3.setGeometry(QtCore.QRect(30, 310, 181, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setItalic(False)
        self.lblNomeCompleto_3.setFont(font)
        self.lblNomeCompleto_3.setObjectName("lblNomeCompleto_3")
        self.inputRgVisitante = QtWidgets.QLineEdit(self.centralwidget)
        self.inputRgVisitante.setGeometry(QtCore.QRect(30, 410, 141, 26))
        self.inputRgVisitante.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
"")
        self.inputRgVisitante.setMaxLength(13)
        self.inputRgVisitante.setCursorPosition(0)
        self.inputRgVisitante.setObjectName("inputRgVisitante")

        self.inputRgVisitante.setEnabled(False)
        self.inputNomeVisitante.setEnabled(False)
        self.comboBoxNumDias.setEnabled(False)
        self.btnSalvarVisi.setEnabled(False)
        
        self.lblNomeCompleto_4 = QtWidgets.QLabel(self.centralwidget)
        self.lblNomeCompleto_4.setGeometry(QtCore.QRect(30, 390, 151, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setItalic(False)
        self.lblNomeCompleto_4.setFont(font)
        self.lblNomeCompleto_4.setObjectName("lblNomeCompleto_4")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(30, 450, 671, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.lblTituloCadastrarVisitantes_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblTituloCadastrarVisitantes_2.setGeometry(QtCore.QRect(30, 270, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lblTituloCadastrarVisitantes_2.setFont(font)
        self.lblTituloCadastrarVisitantes_2.setObjectName("lblTituloCadastrarVisitantes_2")
        janelaCadastrarVisitantes.setCentralWidget(self.centralwidget)
        self.lblNomeCompleto.setBuddy(self.inputNomeCompleto)
        self.lblCpf.setBuddy(self.inputCpf)
        self.lblTipoMorador.setBuddy(self.comboBoxNumDias)
        self.lblBloco.setBuddy(self.comboBoxBloco)
        self.lblNumeroVaga.setBuddy(self.inputNumeroVaga)
        self.lblNumeroApartamento.setBuddy(self.inputNumeroApartamento)
        self.lblNomeCompleto_3.setBuddy(self.inputNomeCompleto)
        self.lblNomeCompleto_4.setBuddy(self.inputNomeCompleto)
        self.btnBuscarVisi.clicked.connect(self.consulMorador)

        self.retranslateUi(janelaCadastrarVisitantes)
        self.btnLimpar.clicked.connect(self.limparCampos)

        self.inputNumeroApartamento.setReadOnly(True)
        self.inputNumeroVaga.setReadOnly(True)
        

        self.btnSalvarVisi.clicked.connect(self.abrirMsgBox)
        QtCore.QMetaObject.connectSlotsByName(janelaCadastrarVisitantes)
        janelaCadastrarVisitantes.setTabOrder(self.inputNomeCompleto, self.inputCpf)
        janelaCadastrarVisitantes.setTabOrder(self.inputCpf, self.btnBuscarVisi)
        janelaCadastrarVisitantes.setTabOrder(self.btnBuscarVisi, self.inputNumeroApartamento)
        janelaCadastrarVisitantes.setTabOrder(self.inputNumeroApartamento, self.inputNumeroVaga)
        janelaCadastrarVisitantes.setTabOrder(self.inputNumeroVaga, self.comboBoxBloco)
        janelaCadastrarVisitantes.setTabOrder(self.comboBoxBloco, self.inputNomeVisitante)
        janelaCadastrarVisitantes.setTabOrder(self.inputNomeVisitante, self.comboBoxNumDias)
        janelaCadastrarVisitantes.setTabOrder(self.comboBoxNumDias, self.inputRgVisitante)
        janelaCadastrarVisitantes.setTabOrder(self.inputRgVisitante, self.btnLimpar)
        janelaCadastrarVisitantes.setTabOrder(self.btnLimpar, self.btnSalvarVisi)


    def retranslateUi(self, janelaCadastrarVisitantes):
        _translate = QtCore.QCoreApplication.translate
        janelaCadastrarVisitantes.setWindowTitle(_translate("janelaCadastrarVisitantes", "Prime Condo"))
        self.lblNomeCompleto.setText(_translate("janelaCadastrarVisitantes", "Visitar quem ? (Nome morador)"))
        self.lblCpf.setText(_translate("janelaCadastrarVisitantes", "&CPF:"))
        self.comboBoxNumDias.setItemText(0, _translate("janelaCadastrarVisitantes", "Sem limite"))
        self.comboBoxNumDias.setItemText(1, _translate("janelaCadastrarVisitantes", "1"))
        self.comboBoxNumDias.setItemText(2, _translate("janelaCadastrarVisitantes", "2"))
        self.comboBoxNumDias.setItemText(3, _translate("janelaCadastrarVisitantes", "3"))
        self.comboBoxNumDias.setItemText(4, _translate("janelaCadastrarVisitantes", "4"))
        self.comboBoxNumDias.setItemText(5, _translate("janelaCadastrarVisitantes", "5"))
        self.comboBoxNumDias.setItemText(6, _translate("janelaCadastrarVisitantes", "6"))
        self.lblTipoMorador.setText(_translate("janelaCadastrarVisitantes", "Quantos dias de Acesso:"))
        self.btnSalvarVisi.setText(_translate("janelaCadastrarVisitantes", "SALVAR"))
        self.lblTituloCadastrarVisitantes.setText(_translate("janelaCadastrarVisitantes", "Cadastrar Visitantes"))
        self.btnLimpar.setText(_translate("janelaCadastrarVisitantes", "LIMPAR"))
        self.inputCpf.setInputMask(_translate("janelaCadastrarVisitantes", "000.000.000-00"))
        self.inputCpf.setPlaceholderText(_translate("janelaCadastrarVisitantes", "Digite só números"))
        self.btnBuscarVisi.setText(_translate("janelaCadastrarVisitantes", "Buscar"))
        self.label.setText(_translate("janelaCadastrarVisitantes", "ou"))
        self.lblBloco.setText(_translate("janelaCadastrarVisitantes", "&Bloco:"))
        self.comboBoxBloco.setItemText(0, _translate("janelaCadastrarVisitantes", "A"))
        self.comboBoxBloco.setItemText(1, _translate("janelaCadastrarVisitantes", "B"))
        self.comboBoxBloco.setItemText(2, _translate("janelaCadastrarVisitantes", "C"))
        self.comboBoxBloco.setItemText(3, _translate("janelaCadastrarVisitantes", "D"))
        self.lblNumeroVaga.setText(_translate("janelaCadastrarVisitantes", "&Nº da Vaga Veiculo:"))
        self.inputNumeroVaga.setInputMask(_translate("janelaCadastrarVisitantes", "0000"))
        self.lblStatusMorador.setText(_translate("janelaCadastrarVisitantes", "Status Morador"))
        self.inputNumeroApartamento.setInputMask(_translate("janelaCadastrarVisitantes", "0000"))
        self.lblNumeroApartamento.setText(_translate("janelaCadastrarVisitantes", "Nº apt:"))
        self.lblResultadoStatus.setText(_translate("janelaCadastrarVisitantes", "Ativo/ Desativado"))
        self.lblNomeCompleto_3.setText(_translate("janelaCadastrarVisitantes", "Nome do(a) Visitante:"))
        self.inputRgVisitante.setInputMask(_translate("janelaCadastrarVisitantes", "0000000000"))
        self.inputRgVisitante.setText(_translate("janelaCadastrarVisitantes", "..-"))
        self.lblNomeCompleto_4.setText(_translate("janelaCadastrarVisitantes", "RG:(Opcional)"))
        self.lblTituloCadastrarVisitantes_2.setText(_translate("janelaCadastrarVisitantes", "Área do Visitante:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    janelaCadastrarVisitantes = QtWidgets.QMainWindow()
    ui = Ui_janelaCadastrarVisitantes()
    ui.setupUi(janelaCadastrarVisitantes)
    janelaCadastrarVisitantes.show()
    sys.exit(app.exec_())
