# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(717, 589)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Roboto [GOOG]")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_10.addWidget(self.label_26)
        self.tab_4 = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_4.sizePolicy().hasHeightForWidth())
        self.tab_4.setSizePolicy(sizePolicy)
        self.tab_4.setObjectName("tab_4")
        self.tab_0 = QtWidgets.QWidget()
        self.tab_0.setAccessibleName("")
        self.tab_0.setObjectName("tab_0")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.tab_0)
        font = QtGui.QFont()
        font.setFamily("Roboto [pyrs]")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_0)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.memeText = QtWidgets.QTextBrowser(self.tab_0)
        self.memeText.setObjectName("memeText")
        self.horizontalLayout.addWidget(self.memeText)
        self.memeLabel = QtWidgets.QLabel(self.tab_0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.memeLabel.sizePolicy().hasHeightForWidth())
        self.memeLabel.setSizePolicy(sizePolicy)
        self.memeLabel.setObjectName("memeLabel")
        self.horizontalLayout.addWidget(self.memeLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.memeBtn = QtWidgets.QPushButton(self.tab_0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.memeBtn.sizePolicy().hasHeightForWidth())
        self.memeBtn.setSizePolicy(sizePolicy)
        self.memeBtn.setText("")
        self.memeBtn.setObjectName("memeBtn")
        self.verticalLayout.addWidget(self.memeBtn)
        self.tab_4.addTab(self.tab_0, "")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.tab_1)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_14.addItem(spacerItem)
        self.label_8 = QtWidgets.QLabel(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_14.addWidget(self.label_8)
        self.rootComboBox = QtWidgets.QComboBox(self.tab_1)
        self.rootComboBox.setObjectName("rootComboBox")
        self.rootComboBox.addItem("")
        self.rootComboBox.addItem("")
        self.rootComboBox.addItem("")
        self.rootComboBox.addItem("")
        self.rootComboBox.addItem("")
        self.rootComboBox.addItem("")
        self.rootComboBox.addItem("")
        self.rootComboBox.addItem("")
        self.rootComboBox.addItem("")
        self.verticalLayout_14.addWidget(self.rootComboBox)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_19 = QtWidgets.QLabel(self.tab_1)
        self.label_19.setObjectName("label_19")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.rootFx = QtWidgets.QLineEdit(self.tab_1)
        self.rootFx.setObjectName("rootFx")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.rootFx)
        self.rootX0Label = QtWidgets.QLabel(self.tab_1)
        self.rootX0Label.setObjectName("rootX0Label")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.rootX0Label)
        self.rootX0 = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.rootX0.setDecimals(10)
        self.rootX0.setMinimum(-1000000000.0)
        self.rootX0.setMaximum(1000000000.0)
        self.rootX0.setObjectName("rootX0")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.rootX0)
        self.rootX1Label = QtWidgets.QLabel(self.tab_1)
        self.rootX1Label.setObjectName("rootX1Label")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.rootX1Label)
        self.rootX1 = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.rootX1.setDecimals(10)
        self.rootX1.setMinimum(-1000000000.0)
        self.rootX1.setMaximum(1000000000.0)
        self.rootX1.setProperty("value", 1.0)
        self.rootX1.setObjectName("rootX1")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.rootX1)
        self.verticalLayout_14.addLayout(self.formLayout_4)
        self.line = QtWidgets.QFrame(self.tab_1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_14.addWidget(self.line)
        self.label_27 = QtWidgets.QLabel(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_14.addWidget(self.label_27)
        self.formLayout_8 = QtWidgets.QFormLayout()
        self.formLayout_8.setObjectName("formLayout_8")
        self.label_28 = QtWidgets.QLabel(self.tab_1)
        self.label_28.setObjectName("label_28")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_28)
        self.rootMaxIterations = QtWidgets.QSpinBox(self.tab_1)
        self.rootMaxIterations.setMinimum(1)
        self.rootMaxIterations.setMaximum(1000)
        self.rootMaxIterations.setProperty("value", 50)
        self.rootMaxIterations.setObjectName("rootMaxIterations")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.rootMaxIterations)
        self.label_29 = QtWidgets.QLabel(self.tab_1)
        self.label_29.setObjectName("label_29")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_29)
        self.rootPercision = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.rootPercision.setDecimals(10)
        self.rootPercision.setMinimum(1e-06)
        self.rootPercision.setMaximum(1000000000.0)
        self.rootPercision.setSingleStep(0.0001)
        self.rootPercision.setProperty("value", 0.0001)
        self.rootPercision.setObjectName("rootPercision")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.rootPercision)
        self.verticalLayout_14.addLayout(self.formLayout_8)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem2)
        self.rootLoadBtn = QtWidgets.QPushButton(self.tab_1)
        self.rootLoadBtn.setObjectName("rootLoadBtn")
        self.horizontalLayout_12.addWidget(self.rootLoadBtn)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem3)
        self.rootSolveBtn = QtWidgets.QPushButton(self.tab_1)
        self.rootSolveBtn.setObjectName("rootSolveBtn")
        self.horizontalLayout_12.addWidget(self.rootSolveBtn)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem4)
        self.verticalLayout_14.addLayout(self.horizontalLayout_12)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_14.addItem(spacerItem5)
        self.tab_4.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_15.addItem(spacerItem6)
        self.label_25 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_15.addWidget(self.label_25)
        self.interpolationComboBox = QtWidgets.QComboBox(self.tab_2)
        self.interpolationComboBox.setObjectName("interpolationComboBox")
        self.interpolationComboBox.addItem("")
        self.interpolationComboBox.addItem("")
        self.verticalLayout_15.addWidget(self.interpolationComboBox)
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_22 = QtWidgets.QLabel(self.tab_2)
        self.label_22.setObjectName("label_22")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.label_23 = QtWidgets.QLabel(self.tab_2)
        self.label_23.setObjectName("label_23")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.interpolationSampleLineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.interpolationSampleLineEdit.setObjectName("interpolationSampleLineEdit")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.interpolationSampleLineEdit)
        self.label_24 = QtWidgets.QLabel(self.tab_2)
        self.label_24.setObjectName("label_24")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.interpolationQueryLineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.interpolationQueryLineEdit.setObjectName("interpolationQueryLineEdit")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.interpolationQueryLineEdit)
        self.interpolationOrderLineEdit = QtWidgets.QSpinBox(self.tab_2)
        self.interpolationOrderLineEdit.setObjectName("interpolationOrderLineEdit")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.interpolationOrderLineEdit)
        self.verticalLayout_15.addLayout(self.formLayout_5)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem7)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem8)
        self.interpolationLoadBtn = QtWidgets.QPushButton(self.tab_2)
        self.interpolationLoadBtn.setObjectName("interpolationLoadBtn")
        self.horizontalLayout_13.addWidget(self.interpolationLoadBtn)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem9)
        self.interpolationSolveBtn = QtWidgets.QPushButton(self.tab_2)
        self.interpolationSolveBtn.setObjectName("interpolationSolveBtn")
        self.horizontalLayout_13.addWidget(self.interpolationSolveBtn)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem10)
        self.verticalLayout_15.addLayout(self.horizontalLayout_13)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_15.addItem(spacerItem11)
        self.tab_4.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_17.addItem(spacerItem12)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.sysEqnsLabel = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sysEqnsLabel.setFont(font)
        self.sysEqnsLabel.setObjectName("sysEqnsLabel")
        self.horizontalLayout_15.addWidget(self.sysEqnsLabel)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem13)
        self.sysAddBtn = QtWidgets.QPushButton(self.tab_3)
        self.sysAddBtn.setObjectName("sysAddBtn")
        self.horizontalLayout_15.addWidget(self.sysAddBtn)
        self.sysRemoveBtn = QtWidgets.QPushButton(self.tab_3)
        self.sysRemoveBtn.setObjectName("sysRemoveBtn")
        self.horizontalLayout_15.addWidget(self.sysRemoveBtn)
        self.verticalLayout_17.addLayout(self.horizontalLayout_15)
        self.sysEqnsForm = QtWidgets.QFormLayout()
        self.sysEqnsForm.setObjectName("sysEqnsForm")
        self.sysEqn1Label = QtWidgets.QLabel(self.tab_3)
        self.sysEqn1Label.setObjectName("sysEqn1Label")
        self.sysEqnsForm.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.sysEqn1Label)
        self.sysEqn1LineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.sysEqn1LineEdit.setObjectName("sysEqn1LineEdit")
        self.sysEqnsForm.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sysEqn1LineEdit)
        self.sysEqn2Label = QtWidgets.QLabel(self.tab_3)
        self.sysEqn2Label.setObjectName("sysEqn2Label")
        self.sysEqnsForm.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.sysEqn2Label)
        self.sysEqn2LineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.sysEqn2LineEdit.setObjectName("sysEqn2LineEdit")
        self.sysEqnsForm.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sysEqn2LineEdit)
        self.verticalLayout_17.addLayout(self.sysEqnsForm)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_17.addItem(spacerItem14)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem15)
        self.sysLoadBtn = QtWidgets.QPushButton(self.tab_3)
        self.sysLoadBtn.setObjectName("sysLoadBtn")
        self.horizontalLayout_14.addWidget(self.sysLoadBtn)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem16)
        self.sysSolveBtn = QtWidgets.QPushButton(self.tab_3)
        self.sysSolveBtn.setObjectName("sysSolveBtn")
        self.horizontalLayout_14.addWidget(self.sysSolveBtn)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem17)
        self.verticalLayout_17.addLayout(self.horizontalLayout_14)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_17.addItem(spacerItem18)
        self.tab_4.addTab(self.tab_3, "")
        self.verticalLayout_10.addWidget(self.tab_4)
        self.tab_4.raise_()
        self.label_26.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 717, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab_4.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_26.setText(_translate("MainWindow", "Numerical Methods Project"))
        self.tab_4.setToolTip(_translate("MainWindow", "<html><head/><body><p>Solves a system of equations using Gauss Jordan method.</p></body></html>"))
        self.tab_4.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Solves a system of equations using Gauss Jordan method.</p></body></html>"))
        self.label.setText(_translate("MainWindow", "Hello World!"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This project is made as the final project for the course CS213: Numerical Analysis and Computer Applications, Spring 2018.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The aim of the project is to implement some of the numerical methods taught during the course which include root finding techniques, interpolation and solving systems of linear equations.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The source code for the project is avialable on Github here:<br /><a href=\"https://github.com/k-alkiek/numerical-methods\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/k-alkiek/numerical-methods</span></a></p></body></html>"))
        self.memeText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">much numbers</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">very accuracy</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">so error</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p></body></html>"))
        self.memeLabel.setText(_translate("MainWindow", "TextLabel"))
        self.tab_4.setTabText(self.tab_4.indexOf(self.tab_0), _translate("MainWindow", "Welcome"))
        self.label_8.setText(_translate("MainWindow", "  Choose Method"))
        self.rootComboBox.setCurrentText(_translate("MainWindow", "General Algorithm"))
        self.rootComboBox.setItemText(0, _translate("MainWindow", "General Algorithm"))
        self.rootComboBox.setItemText(1, _translate("MainWindow", "Bisection"))
        self.rootComboBox.setItemText(2, _translate("MainWindow", "False Position"))
        self.rootComboBox.setItemText(3, _translate("MainWindow", "Fixed Point"))
        self.rootComboBox.setItemText(4, _translate("MainWindow", "Newton-Raphson"))
        self.rootComboBox.setItemText(5, _translate("MainWindow", "First modified Newton"))
        self.rootComboBox.setItemText(6, _translate("MainWindow", "Second modified Newton"))
        self.rootComboBox.setItemText(7, _translate("MainWindow", "Secant"))
        self.rootComboBox.setItemText(8, _translate("MainWindow", "Birge Vieta"))
        self.label_19.setText(_translate("MainWindow", "  f(x)"))
        self.rootX0Label.setText(_translate("MainWindow", "  X0"))
        self.rootX1Label.setText(_translate("MainWindow", "  X1"))
        self.label_27.setText(_translate("MainWindow", "  Conditions"))
        self.label_28.setText(_translate("MainWindow", "  Max Iterations"))
        self.label_29.setText(_translate("MainWindow", "  Percision"))
        self.rootLoadBtn.setText(_translate("MainWindow", "Load from file"))
        self.rootSolveBtn.setText(_translate("MainWindow", "Solve"))
        self.tab_4.setTabText(self.tab_4.indexOf(self.tab_1), _translate("MainWindow", "Root Finding"))
        self.label_25.setText(_translate("MainWindow", "  Choose Method"))
        self.interpolationComboBox.setCurrentText(_translate("MainWindow", "Newton"))
        self.interpolationComboBox.setItemText(0, _translate("MainWindow", "Newton"))
        self.interpolationComboBox.setItemText(1, _translate("MainWindow", "Lagrange"))
        self.label_22.setText(_translate("MainWindow", "  Polynomial Order"))
        self.label_23.setText(_translate("MainWindow", "  Sample Points"))
        self.interpolationSampleLineEdit.setPlaceholderText(_translate("MainWindow", "Enter points as comma sepearted tuples: (x1, y1), (x2, y2), (x3, y3)..."))
        self.label_24.setText(_translate("MainWindow", "  Query Points"))
        self.interpolationQueryLineEdit.setPlaceholderText(_translate("MainWindow", "Enter points as a comma seperated list of integers: 1, 2.25, 3.4 ..."))
        self.interpolationLoadBtn.setText(_translate("MainWindow", "Load from file"))
        self.interpolationSolveBtn.setText(_translate("MainWindow", "Solve"))
        self.tab_4.setTabText(self.tab_4.indexOf(self.tab_2), _translate("MainWindow", "Interpolation"))
        self.sysEqnsLabel.setText(_translate("MainWindow", "  Equations"))
        self.sysAddBtn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Add new equation to the system</p></body></html>"))
        self.sysAddBtn.setText(_translate("MainWindow", "Add"))
        self.sysRemoveBtn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Remove last equation from the system</p></body></html>"))
        self.sysRemoveBtn.setText(_translate("MainWindow", "Remove"))
        self.sysEqn1Label.setText(_translate("MainWindow", "  Equation 1"))
        self.sysEqn1LineEdit.setPlaceholderText(_translate("MainWindow", "Example: 2a + 5b - 3c = 5"))
        self.sysEqn2Label.setText(_translate("MainWindow", "  Equation 2"))
        self.sysEqn2LineEdit.setPlaceholderText(_translate("MainWindow", "Example: 2a + 5b - 3c = 5"))
        self.sysLoadBtn.setText(_translate("MainWindow", "Load from file"))
        self.sysSolveBtn.setText(_translate("MainWindow", "Solve"))
        self.tab_4.setTabText(self.tab_4.indexOf(self.tab_3), _translate("MainWindow", "System of Equations"))

