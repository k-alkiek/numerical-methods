from ast import literal_eval

import sympy
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

from src.interpolation.interpolation import interpolate
from src.roots_finder.root_finder_factory import RootFinderFactory
from src.system_of_equations.Gauss_Jordan import GaussJordan
from ui_main_window import Ui_MainWindow
from result_window import ResultWindow
from controllers import interpolation_controller, gauss_jordan_controller
from src.file_parser.file_parser import *

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
        self.ui.sysSolveBtn.clicked.connect(self.sysSolve)
        self.ui.rootLoadBtn.clicked.connect(self.rootLoadFile)
        self.ui.interpolationLoadBtn.clicked.connect(self.interpolationLoadFile)
        self.ui.sysLoadBtn.clicked.connect(self.sysLoadFile)

    def changeRootMethod(self):
        index = self.ui.rootComboBox.currentIndex()

        if index == 0:
            self.ui.rootX0.setEnabled(False)
            self.ui.rootX1.setEnabled(False)
        elif index in [1, 2, 5, 7]:
            self.ui.rootX0.setEnabled(True)
            self.ui.rootX1.setEnabled(True)
        else:
            self.ui.rootX0.setEnabled(True)
            self.ui.rootX1.setEnabled(False)

        if index == 5:
            self.ui.rootX1Label.setText("  Multiplicity")
        else:
            self.ui.rootX1Label.setText("  X1")

    def rootSolve(self):
        try:
            expression = self.ui.rootFx.text()
            method_name = self.ui.rootComboBox.currentText()

            inital_points = []
            if self.ui.rootX0.isEnabled():
                inital_points.append(self.ui.rootX0.value())
            if self.ui.rootX1.isEnabled():
                inital_points.append(self.ui.rootX1.value())

            max_iterations = self.ui.rootMaxIterations.value()
            percision = self.ui.rootPercision.value()

            f = sympy.lambdify('x', expression)

            if method_name == "General Algorithm":
                pass
            else:
                factory = RootFinderFactory()
                results, PlotWindow, Datatable = factory.solve(method_name, expression, *inital_points, max_iterations, percision)
                rw = ResultWindow(self, PlotWindow, Datatable, {"results": results})
                rw.show()
        except Exception as e:
            self.errorDialog(e.args[0])

    def interpolationSolve(self):
        try:
            sample_points = literal_eval(self.ui.interpolationSampleLineEdit.text())
            queries = self.ui.interpolationQueryLineEdit.text().split(',')
            interpolation = interpolate(sample_points)
            method_index = self.ui.interpolationComboBox.currentIndex()

            if method_index == 0:
                sym_function = interpolation.newoten_method()
            else:
                sym_function = interpolation.lagrange()
            f = sympy.lambdify('x', sym_function)

            rw = ResultWindow(self, interpolation_controller.PlotWindow, interpolation_controller.DataTable,
                              {"f": f, "queries": queries})
            rw.show()
        except Exception as e:
            self.errorDialog(e.args[0])

    def sysSolve(self):
        try:
            equations = []
            for i in range(1, self.ui.sysEqnsForm.rowCount()*2, 2):
                equations.append(self.ui.sysEqnsForm.itemAt(i).widget().text())

            solver = GaussJordan()
            results = solver.solve(equations)
            print(results)


            rw = ResultWindow(self, None, gauss_jordan_controller.DataTable, {"results": results})
            rw.show()
        except Exception as e:
            self.errorDialog(e.args[0])

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

    def open_file(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName()
        if file_name:
            return file_name

    def rootLoadFile(self):
        file = self.open_file()
        if file:
            try:
                params = parse_root_finder_file(file)
                method_number = params['method']
                self.ui.rootFx.setText(params['equation'])
                self.ui.rootX0.setValue(params['parameters'][0])
                if len(params['parameters']) > 1:
                    self.ui.rootX1.setValue(params['parameters'][1])
                self.ui.rootMaxIterations.setValue(params['iterations'])
                self.ui.rootPercision.setValue(params['tolerance'])

                if method_number > 4:
                    method_number += 2
                self.ui.rootComboBox.setCurrentIndex(method_number)
                self.changeRootMethod()
            except Exception as e:
                self.errorDialog(e.args[0])


    def interpolationLoadFile(self):
        file = self.open_file()
        if file:
            try:
                params = parse_interpolation_file(file)
                print(params)
            except Exception as e:
                self.errorDialog(e.args[0])

    def sysLoadFile(self):
        file = self.open_file()
        if file:
            try:
                params = parse_equations_file(file)
                print(params)
            except Exception as e:
                self.errorDialog(e.args[0])

    def errorDialog(self, text="Oh no! Something went wrong."):
        msg = QtWidgets.QMessageBox(self)
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(text)
        msg.setWindowTitle("Error")
        msg.resize(500, msg.height())
        msg.show()
