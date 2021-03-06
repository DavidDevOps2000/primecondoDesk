# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastrarVisitante.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_janelaCadastrarMoradores(object):
    def setupUi(self, janelaCadastrarMoradores):
        janelaCadastrarMoradores.setObjectName("janelaCadastrarMoradores")
        janelaCadastrarMoradores.resize(730, 600)
        janelaCadastrarMoradores.setMinimumSize(QtCore.QSize(730, 600))
        janelaCadastrarMoradores.setMaximumSize(QtCore.QSize(730, 650))
        janelaCadastrarMoradores.setBaseSize(QtCore.QSize(725, 650))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        janelaCadastrarMoradores.setWindowIcon(icon)
        janelaCadastrarMoradores.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(janelaCadastrarMoradores)
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
        self.lblTituloCadastrarMoradores = QtWidgets.QLabel(self.centralwidget)
        self.lblTituloCadastrarMoradores.setGeometry(QtCore.QRect(30, 20, 271, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblTituloCadastrarMoradores.setFont(font)
        self.lblTituloCadastrarMoradores.setObjectName("lblTituloCadastrarMoradores")
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
        self.btnAtualizarMorador = QtWidgets.QPushButton(self.centralwidget)
        self.btnAtualizarMorador.setGeometry(QtCore.QRect(630, 100, 75, 26))
        self.btnAtualizarMorador.setObjectName("btnAtualizarMorador")
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
        self.lblPossuiVeiculo_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblPossuiVeiculo_2.setGeometry(QtCore.QRect(610, 180, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblPossuiVeiculo_2.setFont(font)
        self.lblPossuiVeiculo_2.setObjectName("lblPossuiVeiculo_2")
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
        self.lblPossuiVeiculo_3 = QtWidgets.QLabel(self.centralwidget)
        self.lblPossuiVeiculo_3.setGeometry(QtCore.QRect(600, 210, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblPossuiVeiculo_3.setFont(font)
        self.lblPossuiVeiculo_3.setObjectName("lblPossuiVeiculo_3")
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
        self.lblTituloCadastrarMoradores_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblTituloCadastrarMoradores_2.setGeometry(QtCore.QRect(30, 270, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lblTituloCadastrarMoradores_2.setFont(font)
        self.lblTituloCadastrarMoradores_2.setObjectName("lblTituloCadastrarMoradores_2")
        janelaCadastrarMoradores.setCentralWidget(self.centralwidget)
        self.lblNomeCompleto.setBuddy(self.inputNomeCompleto)
        self.lblCpf.setBuddy(self.inputCpf)
        self.lblTipoMorador.setBuddy(self.comboBoxNumDias)
        self.lblBloco.setBuddy(self.comboBoxBloco)
        self.lblNumeroVaga.setBuddy(self.inputNumeroVaga)
        self.lblPossuiVeiculo_2.setBuddy(janelaCadastrarMoradores.radioButtonOpcaoSim)
        self.lblNumeroApartamento.setBuddy(self.inputNumeroApartamento)
        self.lblPossuiVeiculo_3.setBuddy(janelaCadastrarMoradores.radioButtonOpcaoSim)
        self.lblNomeCompleto_3.setBuddy(self.inputNomeCompleto)
        self.lblNomeCompleto_4.setBuddy(self.inputNomeCompleto)

        self.retranslateUi(janelaCadastrarMoradores)
        self.btnLimpar.clicked.connect(self.inputNomeCompleto.clear)
        self.btnLimpar.clicked.connect(self.inputCpf.clear)
        QtCore.QMetaObject.connectSlotsByName(janelaCadastrarMoradores)
        janelaCadastrarMoradores.setTabOrder(self.inputNomeCompleto, self.inputCpf)
        janelaCadastrarMoradores.setTabOrder(self.inputCpf, self.btnAtualizarMorador)
        janelaCadastrarMoradores.setTabOrder(self.btnAtualizarMorador, self.inputNumeroApartamento)
        janelaCadastrarMoradores.setTabOrder(self.inputNumeroApartamento, self.inputNumeroVaga)
        janelaCadastrarMoradores.setTabOrder(self.inputNumeroVaga, self.comboBoxBloco)
        janelaCadastrarMoradores.setTabOrder(self.comboBoxBloco, self.inputNomeVisitante)
        janelaCadastrarMoradores.setTabOrder(self.inputNomeVisitante, self.comboBoxNumDias)
        janelaCadastrarMoradores.setTabOrder(self.comboBoxNumDias, self.inputRgVisitante)
        janelaCadastrarMoradores.setTabOrder(self.inputRgVisitante, self.btnLimpar)
        janelaCadastrarMoradores.setTabOrder(self.btnLimpar, self.btnSalvarVisi)

    def retranslateUi(self, janelaCadastrarMoradores):
        _translate = QtCore.QCoreApplication.translate
        janelaCadastrarMoradores.setWindowTitle(_translate("janelaCadastrarMoradores", "PrimeCondo"))
        self.lblNomeCompleto.setText(_translate("janelaCadastrarMoradores", "Visitar quem ? (Nome morador)"))
        self.lblCpf.setText(_translate("janelaCadastrarMoradores", "&CPF:"))
        self.comboBoxNumDias.setItemText(0, _translate("janelaCadastrarMoradores", "Sem limite"))
        self.comboBoxNumDias.setItemText(1, _translate("janelaCadastrarMoradores", "1"))
        self.comboBoxNumDias.setItemText(2, _translate("janelaCadastrarMoradores", "2"))
        self.comboBoxNumDias.setItemText(3, _translate("janelaCadastrarMoradores", "3"))
        self.comboBoxNumDias.setItemText(4, _translate("janelaCadastrarMoradores", "4"))
        self.comboBoxNumDias.setItemText(5, _translate("janelaCadastrarMoradores", "5"))
        self.comboBoxNumDias.setItemText(6, _translate("janelaCadastrarMoradores", "6"))
        self.lblTipoMorador.setText(_translate("janelaCadastrarMoradores", "Quantos dias de Acesso:"))
        self.btnSalvarVisi.setText(_translate("janelaCadastrarMoradores", "SALVAR"))
        self.lblTituloCadastrarMoradores.setText(_translate("janelaCadastrarMoradores", "Cadastrar Visitantes"))
        self.btnLimpar.setText(_translate("janelaCadastrarMoradores", "LIMPAR"))
        self.inputCpf.setInputMask(_translate("janelaCadastrarMoradores", "000.000.000-00"))
        self.inputCpf.setPlaceholderText(_translate("janelaCadastrarMoradores", "Digite só números"))
        self.btnAtualizarMorador.setText(_translate("janelaCadastrarMoradores", "Buscar"))
        self.label.setText(_translate("janelaCadastrarMoradores", "ou"))
        self.lblBloco.setText(_translate("janelaCadastrarMoradores", "&Bloco:"))
        self.comboBoxBloco.setItemText(0, _translate("janelaCadastrarMoradores", "A"))
        self.comboBoxBloco.setItemText(1, _translate("janelaCadastrarMoradores", "B"))
        self.comboBoxBloco.setItemText(2, _translate("janelaCadastrarMoradores", "C"))
        self.comboBoxBloco.setItemText(3, _translate("janelaCadastrarMoradores", "D"))
        self.lblNumeroVaga.setText(_translate("janelaCadastrarMoradores", "&Nº da Vaga Veiculo:"))
        self.inputNumeroVaga.setInputMask(_translate("janelaCadastrarMoradores", "0000"))
        self.lblPossuiVeiculo_2.setText(_translate("janelaCadastrarMoradores", "Status Morador"))
        self.inputNumeroApartamento.setInputMask(_translate("janelaCadastrarMoradores", "0000"))
        self.lblNumeroApartamento.setText(_translate("janelaCadastrarMoradores", "Nº apt:"))
        self.lblPossuiVeiculo_3.setText(_translate("janelaCadastrarMoradores", "Ativo/ Desativado"))
        self.lblNomeCompleto_3.setText(_translate("janelaCadastrarMoradores", "Nome do(a) Visitante:"))
        self.inputRgVisitante.setInputMask(_translate("janelaCadastrarMoradores", "00.000.000-00"))
        self.inputRgVisitante.setText(_translate("janelaCadastrarMoradores", "..-"))
        self.lblNomeCompleto_4.setText(_translate("janelaCadastrarMoradores", "RG:(Opcional)"))
        self.lblTituloCadastrarMoradores_2.setText(_translate("janelaCadastrarMoradores", "Área do Visitante:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    janelaCadastrarMoradores = QtWidgets.QMainWindow()
    ui = Ui_janelaCadastrarMoradores()
    ui.setupUi(janelaCadastrarMoradores)
    janelaCadastrarMoradores.show()
    sys.exit(app.exec_())
