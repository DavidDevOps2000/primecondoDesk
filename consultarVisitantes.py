from PyQt5 import QtCore, QtGui, QtWidgets
from conectabanco import ConectaBanco
import serial                                           #Obs IMPORTANTE, sempre use ".self" no começo nos parametros das funcoes ->(self), e no começo de toda Variavel self.nomeVariavel dentro das Classes 


class Ui_janelaConsultarVisitantes(object):
    def setupUi(self, janelaConsultarVisitantes):
        janelaConsultarVisitantes.setObjectName("janelaConsultarVisitantes")
        janelaConsultarVisitantes.resize(725, 610)
        janelaConsultarVisitantes.setMinimumSize(QtCore.QSize(725, 610))
        janelaConsultarVisitantes.setMaximumSize(QtCore.QSize(725, 610))
        self.centralwidget = QtWidgets.QWidget(janelaConsultarVisitantes)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBoxConsultarVisitantes = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxConsultarVisitantes.setEnabled(True)
        self.comboBoxConsultarVisitantes.setGeometry(QtCore.QRect(30, 110, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBoxConsultarVisitantes.setFont(font)
        self.comboBoxConsultarVisitantes.setObjectName("comboBoxConsultarVisitantes")
        self.comboBoxConsultarVisitantes.addItem("")
        self.comboBoxConsultarVisitantes.addItem("")
        self.inputConsultarVisitantes = QtWidgets.QTextEdit(self.centralwidget)
        self.inputConsultarVisitantes.setGeometry(QtCore.QRect(190, 110, 511, 31))
        self.inputConsultarVisitantes.setTabChangesFocus(True)
        self.inputConsultarVisitantes.setObjectName("inputConsultarVisitantes")
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
        self.btnLimpar.setGeometry(QtCore.QRect(430, 540, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnLimpar.setFont(font)
        self.btnLimpar.setAutoDefault(False)
        self.btnLimpar.setObjectName("btnLimpar")
        self.tblConsultarVisitantes = QtWidgets.QTableWidget(self.centralwidget)
        self.tblConsultarVisitantes.setGeometry(QtCore.QRect(30, 160, 671, 351))
        self.tblConsultarVisitantes.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tblConsultarVisitantes.setObjectName("tblConsultarVisitantes")
        self.tblConsultarVisitantes.setColumnCount(5)
        self.tblConsultarVisitantes.setRowCount(12)
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
        self.tblConsultarVisitantes.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Nome ")
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
        self.btnAlterar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAlterar.setGeometry(QtCore.QRect(570, 540, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnAlterar.setFont(font)
        self.btnAlterar.setObjectName("btnAlterar")
        self.btnConsultarVisitantes = QtWidgets.QPushButton(self.centralwidget)
        self.btnConsultarVisitantes.setGeometry(QtCore.QRect(600, 110, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnConsultarVisitantes.setFont(font)
        self.btnConsultarVisitantes.setObjectName("btnConsultarVisitantes")
        janelaConsultarVisitantes.setCentralWidget(self.centralwidget)

        self.retranslateUi(janelaConsultarVisitantes)
        self.btnLimpar.clicked.connect(self.tblConsultarVisitantes.clearContents)
        self.btnLimpar.clicked.connect(self.inputConsultarVisitantes.clear)
        QtCore.QMetaObject.connectSlotsByName(janelaConsultarVisitantes)
        janelaConsultarVisitantes.setTabOrder(self.comboBoxConsultarVisitantes, self.inputConsultarVisitantes)
        janelaConsultarVisitantes.setTabOrder(self.inputConsultarVisitantes, self.btnConsultarVisitantes)
        janelaConsultarVisitantes.setTabOrder(self.btnConsultarVisitantes, self.tblConsultarVisitantes)
        janelaConsultarVisitantes.setTabOrder(self.tblConsultarVisitantes, self.btnLimpar)
        janelaConsultarVisitantes.setTabOrder(self.btnLimpar, self.btnAlterar)

    def retranslateUi(self, janelaConsultarVisitantes):
        _translate = QtCore.QCoreApplication.translate
        janelaConsultarVisitantes.setWindowTitle(_translate("janelaConsultarVisitantes", "Prime Condo"))
        self.comboBoxConsultarVisitantes.setItemText(0, _translate("janelaConsultarVisitantes", "Nome"))
        self.comboBoxConsultarVisitantes.setItemText(1, _translate("janelaConsultarVisitantes", "RG"))
        self.label.setText(_translate("janelaConsultarVisitantes", "Selecione o Campo que deseja pesquisar"))
        self.lblTituloConsultarVisitantes.setText(_translate("janelaConsultarVisitantes", "Consultar Visitantes"))
        self.btnLimpar.setText(_translate("janelaConsultarVisitantes", "LIMPAR"))
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
        item = self.tblConsultarVisitantes.verticalHeaderItem(11)
        item.setText(_translate("janelaConsultarVisitantes", "12"))
        item = self.tblConsultarVisitantes.horizontalHeaderItem(1)
        item.setText(_translate("janelaConsultarVisitantes", "Rg"))
        item = self.tblConsultarVisitantes.horizontalHeaderItem(2)
        item.setText(_translate("janelaConsultarVisitantes", "Data Cadastro"))
        item = self.tblConsultarVisitantes.horizontalHeaderItem(3)
        item.setText(_translate("janelaConsultarVisitantes", "Última Visita"))
        item = self.tblConsultarVisitantes.horizontalHeaderItem(4)
        item.setText(_translate("janelaConsultarVisitantes", "Status"))
        self.btnAlterar.setText(_translate("janelaConsultarVisitantes", "ALTERAR"))
        self.btnConsultarVisitantes.setText(_translate("janelaConsultarVisitantes", "Buscar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    janelaConsultarVisitantes = QtWidgets.QMainWindow()
    ui = Ui_janelaConsultarVisitantes()
    ui.setupUi(janelaConsultarVisitantes)
    janelaConsultarVisitantes.show()
    sys.exit(app.exec_())