import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Set Window Title
        self.setWindowTitle('Chess App')

        # Label
        self.text = QtWidgets.QLabel("Chess App",
                                     alignment=QtCore.Qt.AlignTop)
        # Layout
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)

if __name__ == "__main__":
    
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(1280, 720)
    widget.show()

    sys.exit(app.exec())