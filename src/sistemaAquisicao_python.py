# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sistemaAquisicao.ui'
#
# Created: Mon Aug 18 13:25:07 2014
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(684, 850)
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.formLayout = QtGui.QFormLayout(self.centralwidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_4.addWidget(self.label_10, 3, 0, 1, 1)
        self.spinBox = QtGui.QSpinBox(self.groupBox)
        self.spinBox.setEnabled(True)
        self.spinBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(99)
        self.spinBox.setProperty("value", 30)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.gridLayout_4.addWidget(self.spinBox, 1, 2, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout_4.addWidget(self.lineEdit_2, 3, 2, 1, 1)
        self.checkBox = QtGui.QCheckBox(self.groupBox)
        self.checkBox.setChecked(False)
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout_4.addWidget(self.checkBox, 4, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_4.addWidget(self.lineEdit, 2, 2, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setWordWrap(False)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_4.addWidget(self.label_9, 0, 2, 1, 1)
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_4.addWidget(self.pushButton, 0, 3, 1, 1)
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.groupBox)
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_30 = QtGui.QLabel(self.groupBox_3)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.gridLayout_2.addWidget(self.label_30, 3, 0, 1, 1)
        self.line = QtGui.QFrame(self.groupBox_3)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 6, 0, 1, 1)
        self.label_31 = QtGui.QLabel(self.groupBox_3)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.gridLayout_2.addWidget(self.label_31, 3, 1, 1, 1)
        self.line_4 = QtGui.QFrame(self.groupBox_3)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout_2.addWidget(self.line_4, 2, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox_3)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_2.addWidget(self.label_12, 7, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox_3)
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setScaledContents(False)
        self.label_7.setWordWrap(False)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 4, 1, 1, 1)
        self.label_19 = QtGui.QLabel(self.groupBox_3)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_2.addWidget(self.label_19, 8, 0, 1, 1)
        self.line_3 = QtGui.QFrame(self.groupBox_3)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout_2.addWidget(self.line_3, 2, 0, 1, 1)
        self.label_28 = QtGui.QLabel(self.groupBox_3)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.gridLayout_2.addWidget(self.label_28, 8, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.groupBox_3)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_2.addWidget(self.label_11, 7, 0, 1, 1)
        self.line_2 = QtGui.QFrame(self.groupBox_3)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_2.addWidget(self.line_2, 6, 1, 1, 1)
        self.formLayout.setWidget(3, QtGui.QFormLayout.SpanningRole, self.groupBox_3)
        self.groupBox_5 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.gridLayout_10 = QtGui.QGridLayout(self.groupBox_5)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.pushAnalisar = QtGui.QPushButton(self.groupBox_5)
        self.pushAnalisar.setObjectName(_fromUtf8("pushAnalisar"))
        self.gridLayout_10.addWidget(self.pushAnalisar, 0, 0, 1, 1)
        self.progressBar = QtGui.QProgressBar(self.groupBox_5)
        self.progressBar.setEnabled(False)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout_10.addWidget(self.progressBar, 0, 2, 1, 1)
        self.pushCancelar = QtGui.QPushButton(self.groupBox_5)
        self.pushCancelar.setObjectName(_fromUtf8("pushCancelar"))
        self.gridLayout_10.addWidget(self.pushCancelar, 0, 1, 1, 1)
        self.formLayout.setWidget(1, QtGui.QFormLayout.SpanningRole, self.groupBox_5)
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_9 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.label_17 = QtGui.QLabel(self.groupBox_4)
        self.label_17.setMaximumSize(QtCore.QSize(150, 100))
        self.label_17.setText(_fromUtf8(""))
        self.label_17.setPixmap(QtGui.QPixmap(_fromUtf8("figuras/esquema_ligacao.svg")))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_9.addWidget(self.label_17, 0, 0, 1, 1)
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.label_22 = QtGui.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_22.setFont(font)
        self.label_22.setWordWrap(True)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_8.addWidget(self.label_22, 5, 0, 1, 1)
        self.label_21 = QtGui.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_21.setFont(font)
        self.label_21.setWordWrap(True)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_8.addWidget(self.label_21, 4, 0, 1, 1)
        self.label_20 = QtGui.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_20.setFont(font)
        self.label_20.setWordWrap(True)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_8.addWidget(self.label_20, 3, 0, 1, 1)
        self.label_27 = QtGui.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_27.setFont(font)
        self.label_27.setWordWrap(True)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_8.addWidget(self.label_27, 2, 0, 1, 1)
        self.label_25 = QtGui.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_25.setFont(font)
        self.label_25.setWordWrap(True)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_8.addWidget(self.label_25, 0, 0, 1, 1)
        self.label_26 = QtGui.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_26.setFont(font)
        self.label_26.setWordWrap(True)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout_8.addWidget(self.label_26, 1, 0, 1, 1)
        self.label_23 = QtGui.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_23.setFont(font)
        self.label_23.setWordWrap(True)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_8.addWidget(self.label_23, 7, 0, 1, 1)
        self.label_24 = QtGui.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_24.setFont(font)
        self.label_24.setWordWrap(True)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout_8.addWidget(self.label_24, 6, 0, 1, 1)
        self.label_29 = QtGui.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_29.setFont(font)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.gridLayout_8.addWidget(self.label_29, 8, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_8, 0, 1, 1, 1)
        self.formLayout.setWidget(4, QtGui.QFormLayout.SpanningRole, self.groupBox_4)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_7 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.label_13 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMaximumSize(QtCore.QSize(100, 40))
        self.label_13.setText(_fromUtf8(""))
        self.label_13.setPixmap(QtGui.QPixmap(_fromUtf8("figuras/Logo coelce endesa brasil12.jpg")))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_7.addWidget(self.label_13, 0, 0, 1, 1)
        self.label_15 = QtGui.QLabel(self.groupBox_2)
        self.label_15.setMaximumSize(QtCore.QSize(100, 40))
        self.label_15.setText(_fromUtf8(""))
        self.label_15.setPixmap(QtGui.QPixmap(_fromUtf8("figuras/LOGO P&D ANEEL (horizontal).jpg")))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_7.addWidget(self.label_15, 0, 4, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMaximumSize(QtCore.QSize(100, 40))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8("figuras/logo2.png")))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_7.addWidget(self.label_6, 0, 5, 1, 1)
        self.label_14 = QtGui.QLabel(self.groupBox_2)
        self.label_14.setMaximumSize(QtCore.QSize(100, 40))
        self.label_14.setText(_fromUtf8(""))
        self.label_14.setPixmap(QtGui.QPixmap(_fromUtf8("figuras/concema.png")))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_7.addWidget(self.label_14, 0, 3, 1, 1)
        self.label_16 = QtGui.QLabel(self.groupBox_2)
        self.label_16.setMaximumSize(QtCore.QSize(100, 60))
        self.label_16.setText(_fromUtf8(""))
        self.label_16.setPixmap(QtGui.QPixmap(_fromUtf8("figuras/labterra.png")))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_7.addWidget(self.label_16, 0, 2, 1, 1)
        self.formLayout.setWidget(6, QtGui.QFormLayout.SpanningRole, self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 684, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuArquivo = QtGui.QMenu(self.menubar)
        self.menuArquivo.setObjectName(_fromUtf8("menuArquivo"))
        self.menuAvan_ado = QtGui.QMenu(self.menubar)
        self.menuAvan_ado.setObjectName(_fromUtf8("menuAvan_ado"))
        self.menuInjetar_pulso_unico = QtGui.QMenu(self.menuAvan_ado)
        self.menuInjetar_pulso_unico.setObjectName(_fromUtf8("menuInjetar_pulso_unico"))
        self.menuSobre = QtGui.QMenu(self.menubar)
        self.menuSobre.setObjectName(_fromUtf8("menuSobre"))
        self.menuU2531A = QtGui.QMenu(self.menubar)
        self.menuU2531A.setObjectName(_fromUtf8("menuU2531A"))
        self.menuAnalise = QtGui.QMenu(self.menubar)
        self.menuAnalise.setObjectName(_fromUtf8("menuAnalise"))
        self.menu_Plotar_Graficos = QtGui.QMenu(self.menuAnalise)
        self.menu_Plotar_Graficos.setObjectName(_fromUtf8("menu_Plotar_Graficos"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbrir = QtGui.QAction(MainWindow)
        self.actionAbrir.setObjectName(_fromUtf8("actionAbrir"))
        self.actionSalvar = QtGui.QAction(MainWindow)
        self.actionSalvar.setObjectName(_fromUtf8("actionSalvar"))
        self.actionNovo = QtGui.QAction(MainWindow)
        self.actionNovo.setObjectName(_fromUtf8("actionNovo"))
        self.actionSair = QtGui.QAction(MainWindow)
        self.actionSair.setObjectName(_fromUtf8("actionSair"))
        self.actionLamotriz = QtGui.QAction(MainWindow)
        self.actionLamotriz.setObjectName(_fromUtf8("actionLamotriz"))
        self.actionLer_tens_o = QtGui.QAction(MainWindow)
        self.actionLer_tens_o.setObjectName(_fromUtf8("actionLer_tens_o"))
        self.actionLer_corrente = QtGui.QAction(MainWindow)
        self.actionLer_corrente.setObjectName(_fromUtf8("actionLer_corrente"))
        self.actionResetar = QtGui.QAction(MainWindow)
        self.actionResetar.setObjectName(_fromUtf8("actionResetar"))
        self.actionO_Projeto = QtGui.QAction(MainWindow)
        self.actionO_Projeto.setObjectName(_fromUtf8("actionO_Projeto"))
        self.actionSobre_o_Software = QtGui.QAction(MainWindow)
        self.actionSobre_o_Software.setObjectName(_fromUtf8("actionSobre_o_Software"))
        self.actionE_ler_corrente = QtGui.QAction(MainWindow)
        self.actionE_ler_corrente.setObjectName(_fromUtf8("actionE_ler_corrente"))
        self.actionCom_leitura_de_Corrente = QtGui.QAction(MainWindow)
        self.actionCom_leitura_de_Corrente.setObjectName(_fromUtf8("actionCom_leitura_de_Corrente"))
        self.actionCom_leitura_da_imped_ncia = QtGui.QAction(MainWindow)
        self.actionCom_leitura_da_imped_ncia.setObjectName(_fromUtf8("actionCom_leitura_da_imped_ncia"))
        self.actionLer_imped_ncia = QtGui.QAction(MainWindow)
        self.actionLer_imped_ncia.setObjectName(_fromUtf8("actionLer_imped_ncia"))
        self.actionConectar = QtGui.QAction(MainWindow)
        self.actionConectar.setObjectName(_fromUtf8("actionConectar"))
        self.actionDesconectar = QtGui.QAction(MainWindow)
        self.actionDesconectar.setObjectName(_fromUtf8("actionDesconectar"))
        self.actionStatus = QtGui.QAction(MainWindow)
        self.actionStatus.setObjectName(_fromUtf8("actionStatus"))
        self.actionArvore = QtGui.QAction(MainWindow)
        self.actionArvore.setObjectName(_fromUtf8("actionArvore"))
        self.actionAnalisar = QtGui.QAction(MainWindow)
        self.actionAnalisar.setObjectName(_fromUtf8("actionAnalisar"))
        self.actionTreinar = QtGui.QAction(MainWindow)
        self.actionTreinar.setObjectName(_fromUtf8("actionTreinar"))
        self.actionAnalisar_Amostras = QtGui.QAction(MainWindow)
        self.actionAnalisar_Amostras.setObjectName(_fromUtf8("actionAnalisar_Amostras"))
        self.actionPlot_V_I_transiente = QtGui.QAction(MainWindow)
        self.actionPlot_V_I_transiente.setObjectName(_fromUtf8("actionPlot_V_I_transiente"))
        self.actionPlot_V_I_raw = QtGui.QAction(MainWindow)
        self.actionPlot_V_I_raw.setObjectName(_fromUtf8("actionPlot_V_I_raw"))
        self.actionCANCELAR = QtGui.QAction(MainWindow)
        self.actionCANCELAR.setObjectName(_fromUtf8("actionCANCELAR"))
        self.menuArquivo.addAction(self.actionAbrir)
        self.menuArquivo.addSeparator()
        self.menuArquivo.addAction(self.actionSair)
        self.menuInjetar_pulso_unico.addAction(self.actionE_ler_corrente)
        self.menuInjetar_pulso_unico.addAction(self.actionCom_leitura_de_Corrente)
        self.menuInjetar_pulso_unico.addAction(self.actionCom_leitura_da_imped_ncia)
        self.menuAvan_ado.addAction(self.actionAnalisar)
        self.menuAvan_ado.addAction(self.actionTreinar)
        self.menuAvan_ado.addAction(self.menuInjetar_pulso_unico.menuAction())
        self.menuAvan_ado.addAction(self.actionLer_tens_o)
        self.menuAvan_ado.addAction(self.actionLer_corrente)
        self.menuAvan_ado.addAction(self.actionLer_imped_ncia)
        self.menuAvan_ado.addAction(self.actionCANCELAR)
        self.menuSobre.addAction(self.actionLamotriz)
        self.menuSobre.addAction(self.actionO_Projeto)
        self.menuSobre.addAction(self.actionSobre_o_Software)
        self.menuU2531A.addAction(self.actionConectar)
        self.menuU2531A.addAction(self.actionDesconectar)
        self.menuU2531A.addAction(self.actionStatus)
        self.menuU2531A.addAction(self.actionResetar)
        self.menu_Plotar_Graficos.addAction(self.actionPlot_V_I_transiente)
        self.menu_Plotar_Graficos.addAction(self.actionPlot_V_I_raw)
        self.menuAnalise.addAction(self.actionAnalisar_Amostras)
        self.menuAnalise.addAction(self.actionArvore)
        self.menuAnalise.addAction(self.menu_Plotar_Graficos.menuAction())
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuAvan_ado.menuAction())
        self.menubar.addAction(self.menuU2531A.menuAction())
        self.menubar.addAction(self.menuAnalise.menuAction())
        self.menubar.addAction(self.menuSobre.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Sistema de Aquisição", None))
        self.groupBox.setTitle(_translate("MainWindow", "Entrada", None))
        self.label_2.setText(_translate("MainWindow", "Nome do Terreno", None))
        self.label.setText(_translate("MainWindow", "Número de Amostras", None))
        self.label_10.setText(_translate("MainWindow", "Nome do Arranjo / Rótulo", None))
        self.lineEdit_2.setText(_translate("MainWindow", "haste4", None))
        self.checkBox.setText(_translate("MainWindow", "Plotar o transiente após análise", None))
        self.lineEdit.setText(_translate("MainWindow", "Formigueiro", None))
        self.label_8.setText(_translate("MainWindow", "Área de Trabalho:", None))
        self.label_9.setText(_translate("MainWindow", "Selecione uma área de trabalho", None))
        self.pushButton.setText(_translate("MainWindow", "...", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Resultados", None))
        self.label_4.setText(_translate("MainWindow", "Parado", None))
        self.label_3.setText(_translate("MainWindow", "Status:", None))
        self.label_30.setText(_translate("MainWindow", "Número exato:", None))
        self.label_31.setText(_translate("MainWindow", "Siga as instruções abaixo", None))
        self.label_12.setText(_translate("MainWindow", "0", None))
        self.label_5.setText(_translate("MainWindow", "Número aproximado:", None))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p>Siga as instruções abaixo.</p></body></html>", None))
        self.label_19.setText(_translate("MainWindow", "Tempo estimado (seg):", None))
        self.label_28.setText(_translate("MainWindow", "0", None))
        self.label_11.setText(_translate("MainWindow", "Tempo total (seg):", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "Ações", None))
        self.pushAnalisar.setText(_translate("MainWindow", "Iniciar", None))
        self.pushCancelar.setText(_translate("MainWindow", "Cancelar", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Instruções", None))
        self.label_22.setText(_translate("MainWindow", "6. Conecte a haste auxiliar-retorno no borne preto.", None))
        self.label_21.setText(_translate("MainWindow", "5. Conecte a haste auxiliar-central no borne verde.", None))
        self.label_20.setText(_translate("MainWindow", "4. Conecte a malha a ser analisada no borne/conector vermelho.", None))
        self.label_27.setText(_translate("MainWindow", "3. Insira o nome do arranjo/rótulo.", None))
        self.label_25.setText(_translate("MainWindow", "1. Insira o número de amostras a ser adquirido (Default: 30)", None))
        self.label_26.setText(_translate("MainWindow", "2. Insira o nome do Terreno a ser analisado. ", None))
        self.label_23.setText(_translate("MainWindow", "8. Pressione o botão \"Iniciar\".", None))
        self.label_24.setText(_translate("MainWindow", "7. Certifique-se que as distâncias entre as hastes auxiliares estejam corretas.", None))
        self.label_29.setText(_translate("MainWindow", "9. Pressione o botão \"Cancelar\" para cancelar o ensaio.", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Desenvolvimento", None))
        self.menuArquivo.setTitle(_translate("MainWindow", "&Arquivo", None))
        self.menuAvan_ado.setTitle(_translate("MainWindow", "Açõe&s", None))
        self.menuInjetar_pulso_unico.setTitle(_translate("MainWindow", "&Injetar pulso unico", None))
        self.menuSobre.setTitle(_translate("MainWindow", "&Sobre", None))
        self.menuU2531A.setTitle(_translate("MainWindow", "&U2531A", None))
        self.menuAnalise.setTitle(_translate("MainWindow", "Aná&lise", None))
        self.menu_Plotar_Graficos.setTitle(_translate("MainWindow", "&Plotar Graficos", None))
        self.actionAbrir.setText(_translate("MainWindow", "Área &Trabalho", None))
        self.actionAbrir.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionSalvar.setText(_translate("MainWindow", "Sa&lvar", None))
        self.actionNovo.setText(_translate("MainWindow", "&Novo", None))
        self.actionSair.setText(_translate("MainWindow", "&Sair", None))
        self.actionLamotriz.setText(_translate("MainWindow", "&Lamotriz", None))
        self.actionLer_tens_o.setText(_translate("MainWindow", "Ler &tensão", None))
        self.actionLer_corrente.setText(_translate("MainWindow", "Ler &corrente", None))
        self.actionResetar.setText(_translate("MainWindow", "&Resetar", None))
        self.actionO_Projeto.setText(_translate("MainWindow", "O &Projeto", None))
        self.actionSobre_o_Software.setText(_translate("MainWindow", "&Sobre o Software", None))
        self.actionE_ler_corrente.setText(_translate("MainWindow", "Com leitura de tensão", None))
        self.actionCom_leitura_de_Corrente.setText(_translate("MainWindow", "Com leitura de corrente", None))
        self.actionCom_leitura_da_imped_ncia.setText(_translate("MainWindow", "Com leitura da impedância", None))
        self.actionLer_imped_ncia.setText(_translate("MainWindow", "Ler &impedância", None))
        self.actionConectar.setText(_translate("MainWindow", "&Conectar", None))
        self.actionDesconectar.setText(_translate("MainWindow", "&Desconectar", None))
        self.actionStatus.setText(_translate("MainWindow", "&Status", None))
        self.actionArvore.setText(_translate("MainWindow", "A&rvore", None))
        self.actionAnalisar.setText(_translate("MainWindow", "Analisar", None))
        self.actionAnalisar.setShortcut(_translate("MainWindow", "Ctrl+R", None))
        self.actionTreinar.setText(_translate("MainWindow", "Treinar", None))
        self.actionAnalisar_Amostras.setText(_translate("MainWindow", "A&nalisar Amostras", None))
        self.actionPlot_V_I_transiente.setText(_translate("MainWindow", "Plot V I transiente", None))
        self.actionPlot_V_I_transiente.setShortcut(_translate("MainWindow", "Ctrl+P", None))
        self.actionPlot_V_I_raw.setText(_translate("MainWindow", "Plot V I raw", None))
        self.actionPlot_V_I_raw.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionCANCELAR.setText(_translate("MainWindow", "CANCELAR", None))
        self.actionCANCELAR.setShortcut(_translate("MainWindow", "Ctrl+W", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
