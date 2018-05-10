from ast import literal_eval

import sympy
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

from src.interpolation.interpolation import interpolate
from ui_main_window import Ui_MainWindow
from result_window import ResultWindow
from controllers import interpolation_controller

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Make some local modifications.
        # self.ui.colorDepthCombo.addItem("2 colors (1 bit per pixel)")

        # Initial stuff
        self.ui.rootX0.setEnabled(False)
        self.ui.rootX1.setEnabled(False)

        # Connect up the buttons.
        self.ui.rootComboBox.activated.connect(self.changeRootMethod)
        self.ui.rootSolveBtn.clicked.connect(self.rootSolve)
        self.ui.interpolationSolveBtn.clicked.connect(self.interpolationSolve)
        self.ui.sysAddBtn.clicked.connect(self.sysAdd)
        self.ui.sysRemoveBtn.clicked.connect(self.sysRemove)
        self.ui.rootLoadBtn.clicked.connect(self.loadFile)
        self.ui.interpolationLoadBtn.clicked.connect(self.loadFile)
        self.ui.sysLoadBtn.clicked.connect(self.loadFile)

    def changeRootMethod(self):
        index = self.ui.rootComboBox.currentIndex()

        if index == 0:
            self.ui.rootX0.setEnabled(False)
            self.ui.rootX1.setEnabled(False)
        elif index in [1, 2, 5]:
            self.ui.rootX0.setEnabled(True)
            self.ui.rootX1.setEnabled(False)
        elif index in [3, 4, 6]:
            self.ui.rootX0.setEnabled(True)
            self.ui.rootX1.setEnabled(True)

    def rootSolve(self):
        aw = ResultWindow(self)     # this method should take plots and table data
        aw.show()
        # msg = QtWidgets.QMessageBox(self)
        # msg.setIcon(QtWidgets.QMessageBox.Critical)
        # msg.setText("Error")
        # msg.setInformativeText("Oh no! Something went wrong.")
        # msg.setWindowTitle("Error")
        # msg.show()

    def interpolationSolve(self):

        sample_points = literal_eval(self.ui.interpolationSampleLineEdit.text())
        queries = self.ui.interpolationQueryLineEdit.text().split(',')
        interpolation = interpolate(sample_points)
        method_index = self.ui.interpolationComboBox.currentIndex()

        if method_index == 0:
            sym_function = interpolation.newoten_method()
        else:
            sym_function = interpolation.lagrange()
        f = sympy.lambdify('x', sym_function)

        aw = ResultWindow(self, interpolation_controller.PlotWindow, interpolation_controller.DataTable,
                          {"f": f, "queries": queries})
        aw.show()

    def sysAdd(self):

        if self.ui.sysEqnsForm.rowCount() < 10:
            eqn_number = str(self.ui.sysEqnsForm.rowCount() + 1)
            label = QtWidgets.QLabel("  Equation " + eqn_number)
            label.setObjectName("sysEqn" + eqn_number + "Label")
            lineEdit = QtWidgets.QLineEdit()
            lineEdit.setObjectName("sysEqn" + eqn_number + "LineEdit")
            lineEdit.setPlaceholderText("Example: 2a + 5b - 3c = 5")
            self.ui.sysEqnsForm.addRow(label, lineEdit)

    def sysRemove(self):
        if self.ui.sysEqnsForm.rowCount() > 2:
            self.ui.sysEqnsForm.removeRow(self.ui.sysEqnsForm.rowCount() - 1)

    def loadFile(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName()
        if fileName:
            print(fileName)
