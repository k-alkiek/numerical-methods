import random

from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import numpy as np
import matplotlib.pyplot as plt

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
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Interpolated f(x)"

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

        # Just some button connected to `plot` method
        self.button = QPushButton('Plot')
        self.button.clicked.connect(self.plot)

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.f = kwargs["f"]
        self.queries = kwargs["queries"]
        self.plot()


    def plot(self):
        ''' plot some random stuff '''



        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        # ax.clear()

        xpts = np.linspace(0, 100, 1000)
        ax.plot(xpts, self.f(xpts))

        # refresh canvas
        self.canvas.draw()
