from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import random

class ResultWindow(QMainWindow):

    def __init__(self, parent, PlotWindow, DataTable, params):
        super(ResultWindow, self).__init__(parent)
        self.title = 'PyQt5 tabs - pythonspot.com'
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

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = PlotWindow(self.tabs, **params)
        self.tab2 = DataTable(self.tabs, **params)

        # Add tabs
        self.tabs.addTab(self.tab1, "Plot")
        self.tabs.addTab(self.tab2, "Results")

        # Create first tab
        self.tab1.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("PyQt5 button")
        self.tab1.layout.addWidget(self.pushButton1)
        self.tab1.setLayout(self.tab1.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)