from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import random

class ResultWindow(QMainWindow):

    def __init__(self, parent, PlotWindow, DataTable, params):
        super(ResultWindow, self).__init__(parent)
        self.title = 'Results'
        self.left = 0
        self.top = 0
        self.width = 800
        self.height = 500
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.table_widget = TabWidget(self, PlotWindow, DataTable ,params)
        self.setCentralWidget(self.table_widget)

        self.show()


class TabWidget(QWidget):

    def __init__(self, parent, PlotWindow, DataTable, params):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        if "general_results" in params.keys():
            number_of_iterations = params["general_results"][0]
            roots = params["general_results"][1]
            execution_time = params["general_results"][2]

            self.summary = QLabel("Found {:d} Roots \t \t {:d} iterations \t {:f} seconds"
                                  .format(len(roots), number_of_iterations, execution_time))
            self.layout.addWidget(self.summary)

        if PlotWindow is not None and "results" in params.keys():
            number_of_iterations = params["results"][0]
            execution_time = params["results"][1]
            approximate_root = params["results"][3]
            error = params["results"][4]

            self.summary = QLabel("Root: {:.5f} \t Error: {:.5f} \t {:d} iterations \t {:.5f} seconds"
                                                 .format(approximate_root, error, number_of_iterations, execution_time))
            self.layout.addWidget(self.summary)
        # Initialize tab screen
        self.tabs = QTabWidget()
        if PlotWindow is not None:
            self.tab1 = PlotWindow(self.tabs, **params)
        self.tab2 = DataTable(self.tabs, **params)

        # Add tabs
        if PlotWindow is not None:
            self.tabs.addTab(self.tab1, "Plot")
        self.tabs.addTab(self.tab2, "Results")

        # Create first tab
        # if PlotWindow is not None:
        # self.tab1.layout = QVBoxLayout(self)
        # self.pushButton1 = QPushButton("PyQt5 button")
        # self.tab1.layout.addWidget(self.pushButton1)
        # self.tab1.setLayout(self.tab1.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)