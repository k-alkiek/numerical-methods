from PyQt5 import QtWidgets
from main_window import MainWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.setWindowTitle("Numerical Methods")
    main.show()
    sys.exit(app.exec_())