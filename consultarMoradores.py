from PyQt5 import QtCore, QtGui, QtWidgets
import MySQLdb

class Ui_janelaConsultarMoradores(object):

    def __init__(self):
        self.con = ""

    def conecta(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.db = "bd_cond"
        self.port = 3306
        self.con = MySQLdb.connect(self.host, self.user, self.password, self.db, self.port)


  

    def campoPesqVisi(self, suaBusca):
        
        if suaBusca == "Nome do Morador":

            suaBusca="nome_pessoa"
            return suaBusca

        else:                       #Se nenhuma opção for dessas escolhidas, então por lógica, é a nome visita 
            suaBusca="cpf_pessoa"
            return suaBusca
            

    def funCarregarMorador(self):

        suaEscolha = self.campoPesqVisi(self.comboBoxConsultarMoradores.currentText())
        vlrPesquisa = self.inputConsultarMoradores.text()
        self.conecta()
        self.sqlCursor = self.con.cursor()
        query ="SELECT nome_pessoa, bloco_ap, num_ap, tipo_pessoa, CASE status_pess WHEN TRUE THEN 'ATIVO' ELSE 'DESATIVADO' END status_pess, dt_reg FROM tbl_pessoa "\
                "JOIN tbl_moradia ON tbl_pessoa.id_pessoa = tbl_moradia.tbl_pessoa_id_pessoa1 WHERE %s ='%s'" % (suaEscolha, vlrPesquisa)

        print(query)
        self.sqlCursor.execute(query)
        self.result = self.sqlCursor.fetchall()

        self.tblConsultarMoradores.setRowCount(0)
                
        for linhas_numeros, linhas_dados in enumerate(self.result):

                    self.tblConsultarMoradores.insertRow(linhas_numeros)

                    for numero_coluna, data in enumerate(linhas_dados):
                            
                            self.tblConsultarMoradores.setItem(linhas_numeros, numero_coluna, QtWidgets.QTableWidgetItem(str(data)))

        self.con.close()


    def setupUi(self, janelaConsultarMoradores):
        janelaConsultarMoradores.setObjectName("janelaConsultarMoradores")
        janelaConsultarMoradores.setWindowModality(QtCore.Qt.WindowModal)
        janelaConsultarMoradores.resize(725, 610)
        janelaConsultarMoradores.setMinimumSize(QtCore.QSize(725, 610))
        janelaConsultarMoradores.setMaximumSize(QtCore.QSize(725, 610))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        janelaConsultarMoradores.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(janelaConsultarMoradores)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBoxConsultarMoradores = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxConsultarMoradores.setEnabled(True)
        self.comboBoxConsultarMoradores.setGeometry(QtCore.QRect(30, 110, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBoxConsultarMoradores.setFont(font)
        self.comboBoxConsultarMoradores.setObjectName("comboBoxConsultarMoradores")
        self.comboBoxConsultarMoradores.addItem("")
        self.comboBoxConsultarMoradores.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 80, 351, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 50, 671, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lblTituloConsultarVisitantes = QtWidgets.QLabel(self.centralwidget)
        self.lblTituloConsultarVisitantes.setGeometry(QtCore.QRect(30, 20, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblTituloConsultarVisitantes.setFont(font)
        self.lblTituloConsultarVisitantes.setObjectName("lblTituloConsultarVisitantes")
        self.btnLimpar = QtWidgets.QPushButton(self.centralwidget)
        self.btnLimpar.setGeometry(QtCore.QRect(570, 530, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnLimpar.setFont(font)
        self.btnLimpar.setAutoDefault(False)
        self.btnLimpar.setObjectName("btnLimpar")
        self.tblConsultarMoradores = QtWidgets.QTableWidget(self.centralwidget)
        self.tblConsultarMoradores.setEnabled(True)
        self.tblConsultarMoradores.setGeometry(QtCore.QRect(30, 160, 671, 361))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.tblConsultarMoradores.setFont(font)
        self.tblConsultarMoradores.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tblConsultarMoradores.setAutoFillBackground(False)
        self.tblConsultarMoradores.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tblConsultarMoradores.setMidLineWidth(0)
        self.tblConsultarMoradores.setAutoScroll(False)
        self.tblConsultarMoradores.setAutoScrollMargin(16)
        self.tblConsultarMoradores.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tblConsultarMoradores.setTabKeyNavigation(True)
        self.tblConsultarMoradores.setDragEnabled(False)
        self.tblConsultarMoradores.setDragDropOverwriteMode(True)
        self.tblConsultarMoradores.setAlternatingRowColors(True)
        self.tblConsultarMoradores.setShowGrid(True)
        self.tblConsultarMoradores.setGridStyle(QtCore.Qt.SolidLine)
        self.tblConsultarMoradores.setWordWrap(True)
        self.tblConsultarMoradores.setCornerButtonEnabled(True)
        self.tblConsultarMoradores.setRowCount(11)
        self.tblConsultarMoradores.setColumnCount(6)
        self.tblConsultarMoradores.setObjectName("tblConsultarMoradores")
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarMoradores.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarMoradores.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarMoradores.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarMoradores.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarMoradores.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarMoradores.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarMoradores.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarMoradores.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarMoradores.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarMoradores.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarMoradores.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Nome")
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tblConsultarMoradores.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarMoradores.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarMoradores.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarMoradores.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarMoradores.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarMoradores.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        item.setFont(font)
        self.tblConsultarMoradores.setItem(0, 0, item)
        self.tblConsultarMoradores.horizontalHeader().setVisible(True)
        self.tblConsultarMoradores.horizontalHeader().setCascadingSectionResizes(False)
        self.tblConsultarMoradores.horizontalHeader().setDefaultSectionSize(166)
        self.tblConsultarMoradores.horizontalHeader().setHighlightSections(False)
        self.tblConsultarMoradores.horizontalHeader().setMinimumSectionSize(43)
        self.tblConsultarMoradores.horizontalHeader().setSortIndicatorShown(False)
        self.tblConsultarMoradores.horizontalHeader().setStretchLastSection(True)
        self.tblConsultarMoradores.verticalHeader().setVisible(False)
        self.tblConsultarMoradores.verticalHeader().setSortIndicatorShown(False)
        self.tblConsultarMoradores.verticalHeader().setStretchLastSection(False)
        self.inputConsultarMoradores = QtWidgets.QLineEdit(self.centralwidget)
        self.inputConsultarMoradores.setGeometry(QtCore.QRect(170, 110, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.inputConsultarMoradores.setFont(font)
        self.inputConsultarMoradores.setObjectName("inputConsultarMoradores")
        self.btnConsultarMoradores = QtWidgets.QPushButton(self.centralwidget)
        self.btnConsultarMoradores.setGeometry(QtCore.QRect(650, 109, 51, 33))
        self.btnConsultarMoradores.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnConsultarMoradores.setIcon(icon1)
        self.btnConsultarMoradores.setObjectName("btnConsultarMoradores")
        self.btnConsultarMoradores.clicked.connect(self.funCarregarMorador)

        janelaConsultarMoradores.setCentralWidget(self.centralwidget)

        self.retranslateUi(janelaConsultarMoradores)
        self.btnLimpar.clicked.connect(self.tblConsultarMoradores.clearContents)
        self.btnLimpar.clicked.connect(self.inputConsultarMoradores.clear)
        QtCore.QMetaObject.connectSlotsByName(janelaConsultarMoradores)
        janelaConsultarMoradores.setTabOrder(self.comboBoxConsultarMoradores, self.inputConsultarMoradores)
        janelaConsultarMoradores.setTabOrder(self.inputConsultarMoradores, self.tblConsultarMoradores)
        janelaConsultarMoradores.setTabOrder(self.tblConsultarMoradores, self.btnLimpar)

    def retranslateUi(self, janelaConsultarMoradores):
        _translate = QtCore.QCoreApplication.translate
        janelaConsultarMoradores.setWindowTitle(_translate("janelaConsultarMoradores", "Prime Condo"))
        self.comboBoxConsultarMoradores.setItemText(0, _translate("janelaConsultarMoradores", "Nome do Morador"))
        self.comboBoxConsultarMoradores.setItemText(1, _translate("janelaConsultarMoradores", "CPF (com pontos e hífen)"))
        self.label.setText(_translate("janelaConsultarMoradores", "Digite o nome da morador(a) ou os dados referente à pesquisa:"))
        self.lblTituloConsultarVisitantes.setText(_translate("janelaConsultarMoradores", "Consultar Moradores"))
        self.btnLimpar.setText(_translate("janelaConsultarMoradores", "LIMPAR"))
        self.tblConsultarMoradores.setSortingEnabled(False)
        item = self.tblConsultarMoradores.verticalHeaderItem(0)
        item.setText(_translate("janelaConsultarMoradores", "1"))
        item = self.tblConsultarMoradores.verticalHeaderItem(1)
        item.setText(_translate("janelaConsultarMoradores", "2"))
        item = self.tblConsultarMoradores.verticalHeaderItem(2)
        item.setText(_translate("janelaConsultarMoradores", "3"))
        item = self.tblConsultarMoradores.verticalHeaderItem(3)
        item.setText(_translate("janelaConsultarMoradores", "4"))
        item = self.tblConsultarMoradores.verticalHeaderItem(4)
        item.setText(_translate("janelaConsultarMoradores", "5"))
        item = self.tblConsultarMoradores.verticalHeaderItem(5)
        item.setText(_translate("janelaConsultarMoradores", "6"))
        item = self.tblConsultarMoradores.verticalHeaderItem(6)
        item.setText(_translate("janelaConsultarMoradores", "7"))
        item = self.tblConsultarMoradores.verticalHeaderItem(7)
        item.setText(_translate("janelaConsultarMoradores", "8"))
        item = self.tblConsultarMoradores.verticalHeaderItem(8)
        item.setText(_translate("janelaConsultarMoradores", "9"))
        item = self.tblConsultarMoradores.verticalHeaderItem(9)
        item.setText(_translate("janelaConsultarMoradores", "10"))
        item = self.tblConsultarMoradores.verticalHeaderItem(10)
        item.setText(_translate("janelaConsultarMoradores", "11"))
        item = self.tblConsultarMoradores.horizontalHeaderItem(1)
        item.setText(_translate("janelaConsultarMoradores", "Bloco"))
        item = self.tblConsultarMoradores.horizontalHeaderItem(2)
        item.setText(_translate("janelaConsultarMoradores", "Nº apt"))
        item = self.tblConsultarMoradores.horizontalHeaderItem(3)
        item.setText(_translate("janelaConsultarMoradores", "Tipo"))
        item = self.tblConsultarMoradores.horizontalHeaderItem(4)
        item.setText(_translate("janelaConsultarMoradores", "Status"))
        item = self.tblConsultarMoradores.horizontalHeaderItem(5)
        item.setText(_translate("janelaConsultarMoradores", "Data de Registro:"))
        __sortingEnabled = self.tblConsultarMoradores.isSortingEnabled()
        self.tblConsultarMoradores.setSortingEnabled(False)
        self.tblConsultarMoradores.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    janelaConsultarMoradores = QtWidgets.QMainWindow()
    ui = Ui_janelaConsultarMoradores()
    ui.setupUi(janelaConsultarMoradores)
    janelaConsultarMoradores.show()
    sys.exit(app.exec_())
