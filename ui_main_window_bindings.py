

def connectUi(self):
    self.sysAddBtn.clicked.connect(self.sysAdd)
    self.sysRemoveBtn.clicked.connect(self.sysRemove)


def sysAdd(self):
    if self.sysEqnsForm.rowCount() < 10:
        eqn_number = str(self.sysEqnsForm.rowCount() + 1)
        label = QtWidgets.QLabel("  Equation " + eqn_number)
        label.setObjectName("sysEqn" + eqn_number + "Label")
        lineEdit = QtWidgets.QLineEdit()
        lineEdit.setObjectName("sysEqn" + eqn_number + "LineEdit")
        lineEdit.setPlaceholderText("Example: 2a + 5b - 3c = 5")
        self.sysEqnsForm.addRow(label, lineEdit)


def sysRemove(self):
    if self.sysEqnsForm.rowCount() > 2:
        self.sysEqnsForm.removeRow(self.sysEqnsForm.rowCount() - 1)
        # self.sysEqnsForm.removeRow()