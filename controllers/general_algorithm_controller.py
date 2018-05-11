from PyQt5 import QtWidgets

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QTableWidget, QVBoxLayout, QTableWidgetItem, QPushButton, QHBoxLayout, QLabel
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

from controllers.my_navigation_toolbar import MyNavigationToolbar


class DataTable(QDialog):
    def __init__(self, parent, **kwargs):
        super(DataTable, self).__init__(parent)

        self.number_of_iterations = kwargs["general_results"][0]
        self.roots = kwargs["general_results"][1]
        self.execution_time = kwargs["general_results"][2]
        self.f = kwargs["general_results"][3]
        self.maclorin_f = kwargs["general_results"][4]

        # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(self.roots))
        self.tableWidget.setColumnCount(1)

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.tableWidget.move(0, 0)
        self.setLayout(layout)

        print()

        self.fill()

    def fill(self):

        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Roots found"))
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        for i in range(0, len(self.roots)):
            self.tableWidget.setItem(0, i, QTableWidgetItem(str(self.roots[i])))


class PlotWindow(QDialog):
    def __init__(self, parent, **kwargs):
        super(PlotWindow, self).__init__(parent)

        self.number_of_iterations = kwargs["general_results"][0]
        self.roots = kwargs["general_results"][1]
        self.execution_time = kwargs["general_results"][2]
        self.f = kwargs["general_results"][3]
        self.maclaurin_f = kwargs["general_results"][4]

        # a figure instance to plot on
        self.figure = Figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = MyNavigationToolbar(self.canvas, self)

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        self.plot()

    def plot(self):

        # create an axis
        ax = self.figure.add_subplot(111)
        bx = self.figure.add_subplot(111)

        # discards the old graph
        ax.clear()
        bx.clear()

        ax.grid(True, which='both')

        ax.axhline(y=0, color='k')
        ax.axvline(x=0, color='k')
        ax.grid(True, which='both')

        diff = max(self.roots) - min(self.roots)
        start = min(self.roots) - diff
        end = max(self.roots) + diff
        if diff == 0:
            start = -100
            end = 100
        xpts = np.linspace(start, end, 1000)
        ax.plot(xpts, self.f(xpts), label='f(x)')
        ax.plot(xpts, self.maclaurin_f(xpts), label='Maclaurin Polynomial of f(x)', color='g')

        ax.scatter(self.roots, [0 for i in self.roots], marker='x', color='r', label="Roots")


        ax.legend()
        # refresh canvas
        self.canvas.draw()
        # x ^ 2 - 25
