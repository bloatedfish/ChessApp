import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QMenuBar, QMenu
from PySide6.QtGui import QPainter, QBrush, QPen
from PySide6.QtCore import Qt
class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Set Window Title
        self.setWindowTitle('Chess App')
        self.setGeometry(0,0,640,640)

        # MenuBar
        menuBar = QMenuBar(self)
        fileMenu = menuBar.addMenu('Game')
        newGameMenu = fileMenu.addAction('New Game')
        exitMenu = fileMenu.addAction('Exit')
        exitMenu.triggered.connect(self.close)
        helpMenu = menuBar.addMenu('Help')
        howToPlayMenu = helpMenu.addAction('How to Play')
        #self.setMenuBar(menuBar)

        # Layout
        self.layout = QtWidgets.QVBoxLayout(self)
        #self.layout.addStretch()
        self.layout.addWidget(menuBar)
        self.layout.setAlignment(menuBar, Qt.AlignTop)
        

    def paintEvent(self, e):
        # Draw Chess Board
        painter = QPainter(self)
        pen = QPen(Qt.lightGray, Qt.SolidLine)
        pen2 = QPen(Qt.darkGray, Qt.SolidLine)
        brush = QBrush(Qt.lightGray, Qt.SolidPattern)
        brush2 = QBrush(Qt.darkGray, Qt.SolidPattern)
        for x in range(0, 8):
            for y in range(0, 8):
                if((x+y)%2 == 0):
                    painter.setPen(pen)
                    painter.setBrush(brush)
                    painter.drawRect(x*80, y*80+40, 80, 80)
                else:
                    painter.setPen(pen2)
                    painter.setBrush(brush2)
                    painter.drawRect(x*80, y*80+40, 80, 80)
        painter.end()

if __name__ == "__main__":
    
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(640, 680)
    widget.setMinimumSize(640, 680)
    widget.setMaximumSize(640, 680)
    widget.show()

    sys.exit(app.exec())