from PyQt5.QtWidgets import QDialog, QTableWidget, QVBoxLayout, QTableWidgetItem, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np

class DataTable(QDialog):
    def __init__(self, parent, **kwargs):
        super(DataTable, self).__init__(parent)

        self.f = kwargs["f"]
        self.number_of_iterations= kwargs["results"][0]
        self.execution_time = kwargs["results"][1]
        self.iterations = kwargs["results"][2]
        self.approximate_root = kwargs["results"][3]
        self.error = kwargs["results"][4]


        # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(self.iterations))
        self.tableWidget.setColumnCount(len(self.iterations[0].dtype.names))

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.tableWidget.move(0, 0)
        self.setLayout(layout)

        print()

        self.fill()


    def fill(self):
        headers = self.iterations[0].dtype.names

        for i in range (0, len(headers)):
            self.tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem(headers[i]))

        for i in range(0, len(self.iterations)):
            iteration = self.iterations[i]
            for j in range (0, len(headers)):
                header = headers[j]
                item = str(iteration[header])
                self.tableWidget.setItem(i, j, QTableWidgetItem(item))


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


        self.plot()


    def plot(self):
        pass
        # # create an axis
        # ax = self.figure.add_subplot(111)
        #
        # # discards the old graph
        # # ax.clear()
        #
        # xpts = np.linspace(0, 100, 1000)
        # ax.plot(xpts, self.f(xpts))
        #
        # # refresh canvas
        # self.canvas.draw()
