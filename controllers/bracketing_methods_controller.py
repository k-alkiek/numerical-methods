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

        self.number_of_iterations= kwargs["results"][0]
        self.execution_time = kwargs["results"][1]
        self.iterations = kwargs["results"][2]
        self.approximate_root = kwargs["results"][3]
        self.error = kwargs["results"][4]
        self.f = kwargs["results"][5]

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
            header = self.tableWidget.horizontalHeader()
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)


        for i in range(0, len(self.iterations)):
            iteration = self.iterations[i]
            for j in range (0, len(headers)):
                header = headers[j]
                item = str(iteration[header])
                self.tableWidget.setItem(i, j, QTableWidgetItem(item))


class PlotWindow(QDialog):
    def __init__(self, parent, **kwargs):
        super(PlotWindow, self).__init__(parent)

        self.number_of_iterations = kwargs["results"][0]
        self.execution_time = kwargs["results"][1]
        self.iterations = kwargs["results"][2]
        self.approximate_root = kwargs["results"][3]
        self.error = kwargs["results"][4]
        self.f = kwargs["results"][5]
        self.pos = 0;

        # a figure instance to plot on
        self.figure = Figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = MyNavigationToolbar(self.canvas, self)

        self.pos_label = QLabel(str(self.pos + 1) + '/' + str(len(self.iterations)))
        self.pos_label.setAlignment(Qt.AlignCenter)
        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.init_buttons()
        layout.addLayout(self.btns_layout)
        layout.addWidget(self.pos_label)
        self.setLayout(layout)


        self.plot()


    def plot(self):
        iteration = self.iterations[self.pos]
        self.pos_label.setText(str(self.pos + 1) + '/' + str(len(self.iterations)))

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


        xl = iteration['xl']
        xu = iteration['xu']
        xr = iteration['xr']

        diff = xu - xl
        start = xl-0.5*diff
        end = xu+0.5*diff
        if diff == 0:
            start = -10
            end = 10
        xpts = np.linspace(start, end, 100)
        ax.plot(xpts, self.f(xpts), label='f(x)')


        bx.plot([xl, xl], [0, self.f(xl)], color='r', label='xl')
        bx.plot([xr, xr], [0, self.f(xr)], color='g', label='xr')
        bx.plot([xu, xu], [0, self.f(xu)], color='r', label='xu')
        ax.legend()
        # refresh canvas
        self.canvas.draw()
        # x ^ 2 - 25

    def init_buttons(self):
        self.jump_to_first_btn = QPushButton("<< Jump to Start")
        self.previous_btn = QPushButton("< Previous")
        self.next_btn = QPushButton("Next >")
        self.jump_to_last_btn = QPushButton("Jump to End >>")

        # connect buttons
        self.jump_to_first_btn.clicked.connect(self.jump_to_first)
        self.previous_btn.clicked.connect(self.previous)
        self.next_btn.clicked.connect(self.next)
        self.jump_to_last_btn.clicked.connect(self.jump_to_last)

        self.btns_layout = QHBoxLayout()
        self.btns_layout.addWidget(self.jump_to_first_btn)
        self.btns_layout.addWidget(self.previous_btn)
        self.btns_layout.addWidget(self.next_btn)
        self.btns_layout.addWidget(self.jump_to_last_btn)

    def jump_to_first(self):
        if self.pos > 0:
            self.pos = 0
            self.plot()

    def previous(self):
        if self.pos > 0:
            self.pos -= 1
            self.plot()

    def next(self):
        if self.pos < len(self.iterations) - 1:
            self.pos += 1
            self.plot()

    def jump_to_last(self):
        if self.pos < len(self.iterations) - 1:
            self.pos = len(self.iterations) - 1
            self.plot()
