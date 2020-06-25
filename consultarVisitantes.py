from PyQt5 import QtCore, QtGui, QtWidgets
#from conectabanco import ConectaBanco
import MySQLdb

class Ui_janelaConsultarVisitantes(object):

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

        elif suaBusca == "RG da Visita":

            suaBusca="rg_visi"
            return suaBusca

        else:                       #Se nenhuma opção for dessas escolhidas, então por lógica, é a nome visita 
            suaBusca="nome_visi"
            return suaBusca

    def funCarregarVisi(self):

        suaEscolha = self.campoPesqVisi(self.comboBoxConsultarVisitantes.currentText())
        vlrPesquisa = self.inputConsultarVisitantes.text()
        self.conecta()
        self.sqlCursor = self.con.cursor()
        query = "SELECT nome_visi, CASE autorizado WHEN FALSE THEN 'NÃO' ELSE 'SIM' END autorizado,"\
                "CASE data_fim_visi WHEN !NULL THEN data_fim_visi ELSE 'Sem limite' END data_fim_visi,"\
                "bloco_ap, num_ap, rg_visi, dt_registro_visi FROM visi_apt JOIN agen_visi ON visi_apt.id_visi"\
                "= agen_visi.visi_apt_id_visi JOIN tbl_pessoa ON agen_visi.tbl_pessoa_id_pessoa = tbl_pessoa.id_pessoa "\
                "JOIN tbl_moradia ON tbl_pessoa.id_pessoa = tbl_moradia.tbl_pessoa_id_pessoa1 "\
                "WHERE %s = '%s';" % (suaEscolha, vlrPesquisa)

        print(query)
        self.sqlCursor.execute(query)
        self.result = self.sqlCursor.fetchall()

        self.tblConsultarVisitantes.setRowCount(0)
                
        for linhas_numeros, linhas_dados in enumerate(self.result):

                    self.tblConsultarVisitantes.insertRow(linhas_numeros)

                    for numero_coluna, data in enumerate(linhas_dados):
                            
                            self.tblConsultarVisitantes.setItem(linhas_numeros, numero_coluna, QtWidgets.QTableWidgetItem(str(data)))

        self.con.close()


    def setupUi(self, janelaConsultarVisitantes):
        janelaConsultarVisitantes.setObjectName("janelaConsultarVisitantes")
        janelaConsultarVisitantes.setWindowModality(QtCore.Qt.WindowModal)
        janelaConsultarVisitantes.resize(725, 610)
        janelaConsultarVisitantes.setMinimumSize(QtCore.QSize(725, 610))
        janelaConsultarVisitantes.setMaximumSize(QtCore.QSize(725, 610))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        janelaConsultarVisitantes.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(janelaConsultarVisitantes)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBoxConsultarVisitantes = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxConsultarVisitantes.setEnabled(True)
        self.comboBoxConsultarVisitantes.setGeometry(QtCore.QRect(30, 110, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBoxConsultarVisitantes.setFont(font)
        self.comboBoxConsultarVisitantes.setObjectName("comboBoxConsultarVisitantes")
        self.comboBoxConsultarVisitantes.addItem("")
        self.comboBoxConsultarVisitantes.addItem("")
        self.comboBoxConsultarVisitantes.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 80, 271, 16))
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
        self.tblConsultarVisitantes = QtWidgets.QTableWidget(self.centralwidget)
        self.tblConsultarVisitantes.setEnabled(True)
        self.tblConsultarVisitantes.setGeometry(QtCore.QRect(30, 160, 671, 361))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.tblConsultarVisitantes.setFont(font)
        self.tblConsultarVisitantes.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tblConsultarVisitantes.setAutoFillBackground(False)
        self.tblConsultarVisitantes.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tblConsultarVisitantes.setMidLineWidth(0)
        self.tblConsultarVisitantes.setAutoScroll(False)
        self.tblConsultarVisitantes.setAutoScrollMargin(16)
        self.tblConsultarVisitantes.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tblConsultarVisitantes.setTabKeyNavigation(True)
        self.tblConsultarVisitantes.setDragEnabled(False)
        self.tblConsultarVisitantes.setDragDropOverwriteMode(True)
        self.tblConsultarVisitantes.setAlternatingRowColors(True)
        self.tblConsultarVisitantes.setShowGrid(True)
        self.tblConsultarVisitantes.setGridStyle(QtCore.Qt.SolidLine)
        self.tblConsultarVisitantes.setWordWrap(True)
        self.tblConsultarVisitantes.setCornerButtonEnabled(True)
        self.tblConsultarVisitantes.setRowCount(11)
        self.tblConsultarVisitantes.setColumnCount(7)
        self.tblConsultarVisitantes.setObjectName("tblConsultarVisitantes")
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarVisitantes.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarVisitantes.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarVisitantes.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarVisitantes.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarVisitantes.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarVisitantes.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarVisitantes.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarVisitantes.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarVisitantes.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarVisitantes.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarVisitantes.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Nome visitante")
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tblConsultarVisitantes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarVisitantes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarVisitantes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarVisitantes.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarVisitantes.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarVisitantes.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblConsultarVisitantes.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        item.setFont(font)
        self.tblConsultarVisitantes.setItem(0, 0, item)
        self.tblConsultarVisitantes.horizontalHeader().setVisible(True)
        self.tblConsultarVisitantes.horizontalHeader().setCascadingSectionResizes(False)
        self.tblConsultarVisitantes.horizontalHeader().setDefaultSectionSize(166)
        self.tblConsultarVisitantes.horizontalHeader().setHighlightSections(False)
        self.tblConsultarVisitantes.horizontalHeader().setMinimumSectionSize(43)
        self.tblConsultarVisitantes.horizontalHeader().setSortIndicatorShown(False)
        self.tblConsultarVisitantes.horizontalHeader().setStretchLastSection(True)
        self.tblConsultarVisitantes.verticalHeader().setVisible(False)
        self.tblConsultarVisitantes.verticalHeader().setSortIndicatorShown(False)
        self.tblConsultarVisitantes.verticalHeader().setStretchLastSection(False)
        self.inputConsultarVisitantes = QtWidgets.QLineEdit(self.centralwidget)
        self.inputConsultarVisitantes.setGeometry(QtCore.QRect(170, 110, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.inputConsultarVisitantes.setFont(font)
        self.inputConsultarVisitantes.setObjectName("inputConsultarVisitantes")
        self.btnConsultarVisitante = QtWidgets.QPushButton(self.centralwidget)
        self.btnConsultarVisitante.setGeometry(QtCore.QRect(650, 109, 51, 33))
        self.btnConsultarVisitante.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnConsultarVisitante.setIcon(icon1)
        self.btnConsultarVisitante.setObjectName("btnConsultarVisitante")
        self.btnConsultarVisitante.clicked.connect(self.funCarregarVisi)
        janelaConsultarVisitantes.setCentralWidget(self.centralwidget)

        self.retranslateUi(janelaConsultarVisitantes)
        self.btnLimpar.clicked.connect(self.tblConsultarVisitantes.clearContents)
        self.btnLimpar.clicked.connect(self.inputConsultarVisitantes.clear)
        QtCore.QMetaObject.connectSlotsByName(janelaConsultarVisitantes)
        janelaConsultarVisitantes.setTabOrder(self.comboBoxConsultarVisitantes, self.inputConsultarVisitantes)
        janelaConsultarVisitantes.setTabOrder(self.inputConsultarVisitantes, self.tblConsultarVisitantes)
        janelaConsultarVisitantes.setTabOrder(self.tblConsultarVisitantes, self.btnLimpar)

    def retranslateUi(self, janelaConsultarVisitantes):
        _translate = QtCore.QCoreApplication.translate
        janelaConsultarVisitantes.setWindowTitle(_translate("janelaConsultarVisitantes", "Prime Condo"))
        self.comboBoxConsultarVisitantes.setItemText(0, _translate("janelaConsultarVisitantes", "Nome do Morador"))
        self.comboBoxConsultarVisitantes.setItemText(1, _translate("janelaConsultarVisitantes", "RG da Visita"))
        self.comboBoxConsultarVisitantes.setItemText(2, _translate("janelaConsultarVisitantes", "Nome da Visita"))
        self.label.setText(_translate("janelaConsultarVisitantes", "Escolha uma opção de consulta e digite o nome:"))
        self.lblTituloConsultarVisitantes.setText(_translate("janelaConsultarVisitantes", "Consultar Visitantes"))
        self.btnLimpar.setText(_translate("janelaConsultarVisitantes", "LIMPAR"))
        self.tblConsultarVisitantes.setSortingEnabled(False)
        item = self.tblConsultarVisitantes.verticalHeaderItem(0)
        item.setText(_translate("janelaConsultarVisitantes", "1"))
        item = self.tblConsultarVisitantes.verticalHeaderItem(1)
        item.setText(_translate("janelaConsultarVisitantes", "2"))
        item = self.tblConsultarVisitantes.verticalHeaderItem(2)
        item.setText(_translate("janelaConsultarVisitantes", "3"))
        item = self.tblConsultarVisitantes.verticalHeaderItem(3)
        item.setText(_translate("janelaConsultarVisitantes", "4"))
        item = self.tblConsultarVisitantes.verticalHeaderItem(4)
        item.setText(_translate("janelaConsultarVisitantes", "5"))
        item = self.tblConsultarVisitantes.verticalHeaderItem(5)
        item.setText(_translate("janelaConsultarVisitantes", "6"))
        item = self.tblConsultarVisitantes.verticalHeaderItem(6)
        item.setText(_translate("janelaConsultarVisitantes", "7"))
        item = self.tblConsultarVisitantes.verticalHeaderItem(7)
        item.setText(_translate("janelaConsultarVisitantes", "8"))
        item = self.tblConsultarVisitantes.verticalHeaderItem(8)
        item.setText(_translate("janelaConsultarVisitantes", "9"))
        item = self.tblConsultarVisitantes.verticalHeaderItem(9)
        item.setText(_translate("janelaConsultarVisitantes", "10"))
        item = self.tblConsultarVisitantes.verticalHeaderItem(10)
        item.setText(_translate("janelaConsultarVisitantes", "11"))
        item = self.tblConsultarVisitantes.horizontalHeaderItem(1)
        item.setText(_translate("janelaConsultarVisitantes", "Autorizado ?"))
        item = self.tblConsultarVisitantes.horizontalHeaderItem(2)
        item.setText(_translate("janelaConsultarVisitantes", "Nº apt"))
        item = self.tblConsultarVisitantes.horizontalHeaderItem(3)
        item.setText(_translate("janelaConsultarVisitantes", "Bloco Destino"))
        item = self.tblConsultarVisitantes.horizontalHeaderItem(4)
        item.setText(_translate("janelaConsultarVisitantes", "Fim da visita em"))
        item = self.tblConsultarVisitantes.horizontalHeaderItem(5)
        item.setText(_translate("janelaConsultarVisitantes", "RG"))
        item = self.tblConsultarVisitantes.horizontalHeaderItem(6)
        item.setText(_translate("janelaConsultarVisitantes", "Agendado em"))
        __sortingEnabled = self.tblConsultarVisitantes.isSortingEnabled()
        self.tblConsultarVisitantes.setSortingEnabled(False)
        self.tblConsultarVisitantes.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    janelaConsultarVisitantes = QtWidgets.QMainWindow()
    ui = Ui_janelaConsultarVisitantes()
    ui.setupUi(janelaConsultarVisitantes)
    janelaConsultarVisitantes.show()
    sys.exit(app.exec_())
