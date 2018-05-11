from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QDialog, QTableWidget, QVBoxLayout, QTableWidgetItem


class DataTable(QDialog):
    def __init__(self, parent, **kwargs):
        super(DataTable, self).__init__(parent)

        self.values = kwargs["results"][0]

        # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(self.values))
        self.tableWidget.setColumnCount(2)

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.tableWidget.move(0, 0)
        self.setLayout(layout)

        print()

        self.fill()


    def fill(self):
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem('Variable'))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem('Value'))
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        for i in range(0, len(self.values)):
            value = self.values[i]
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(value[0])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(value[1])))
