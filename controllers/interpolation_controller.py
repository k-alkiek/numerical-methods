from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QDialog, QTableWidget, QVBoxLayout, QTableWidgetItem, QPushButton, QHeaderView
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np

class DataTable(QDialog):
    def __init__(self, parent, **kwargs):
        super(DataTable, self).__init__(parent)

        # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.tableWidget.move(0, 0)
        self.setLayout(layout)

        self.f = kwargs["f"]
        self.queries = kwargs["queries"]
        self.fill()


    def fill(self):
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Query x"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Interpolated f(x)"))
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        for i in range(0, len(self.queries)):
            x = float(self.queries[i])
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(x)))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(self.f(x))))


class PlotWindow(QDialog):
    def __init__(self, parent, **kwargs):
        super(PlotWindow, self).__init__(parent)

        # a figure instance to plot on
        self.figure = Figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        self.f = kwargs["f"]
        self.queries = kwargs["queries"]
        self.plot()


    def plot(self):

        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        # ax.clear()

        xpts = np.linspace(0, 100, 1000)
        ax.plot(xpts, self.f(xpts))

        # refresh canvas
        self.canvas.draw()
