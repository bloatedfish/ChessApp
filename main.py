import sys
import random
import webbrowser
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QMenuBar, QMenu
from PySide6.QtGui import QPainter, QBrush, QPen, QPixmap
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
        howToPlayMenu.triggered.connect(self.openURL)

        # Layout
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(menuBar)
        self.layout.setAlignment(menuBar, Qt.AlignTop)
        
    def openURL(self):
        webbrowser.open('https://en.wikipedia.org/wiki/Rules_of_chess')

    def paintEvent(self, e):
        # Draw Chess Board
        painter = QPainter(self)
        pen = QPen(Qt.lightGray, Qt.SolidLine)
        pen2 = QPen(Qt.darkGray, Qt.SolidLine)
        brush = QBrush(Qt.lightGray, Qt.SolidPattern)
        brush2 = QBrush(Qt.darkGray, Qt.SolidPattern)
        for x in range(0, 8):
            for y in range(0, 8):
                # Draw Grid
                if((x+y)%2 == 0):
                    painter.setPen(pen)
                    painter.setBrush(brush)
                    painter.drawRect(x*80, y*80+40, 80, 80)
                else:
                    painter.setPen(pen2)
                    painter.setBrush(brush2)
                    painter.drawRect(x*80, y*80+40, 80, 80)

                # Draw Chess Pieces    
                if(y == 0):
                    if(x == 0 or x == 7):
                        pixmap = QPixmap('art/rookB.png')
                        painter.drawPixmap(x*80, y*80+40, 80, 80, pixmap)
                    elif(x == 1 or x == 6):
                        pixmap = QPixmap('art/knightB.png')
                        painter.drawPixmap(x*80, y*80+40, 80, 80, pixmap)
                    elif(x == 2 or x == 5):
                        pixmap = QPixmap('art/bishopB.png')
                        painter.drawPixmap(x*80, y*80+40, 80, 80, pixmap)
                    elif(x == 3):
                        pixmap = QPixmap('art/queenB.png')
                        painter.drawPixmap(x*80, y*80+40, 80, 80, pixmap)
                    else:
                        pixmap = QPixmap('art/kingB.png')
                        painter.drawPixmap(x*80, y*80+40, 80, 80, pixmap)
                elif(y == 1):
                    pixmap = QPixmap('art/pawnB.png')
                    painter.drawPixmap(x*80, y*80+40, 80, 80, pixmap)
                elif(y == 6):
                    pixmap = QPixmap('art/pawnW.png')
                    painter.drawPixmap(x*80, y*80+40, 80, 80, pixmap)
                elif(y == 7):
                    if(x == 0 or x == 7):
                        pixmap = QPixmap('art/rookW.png')
                        painter.drawPixmap(x*80, y*80+40, 80, 80, pixmap)
                    elif(x == 1 or x == 6):
                        pixmap = QPixmap('art/knightW.png')
                        painter.drawPixmap(x*80, y*80+40, 80, 80, pixmap)
                    elif(x == 2 or x == 5):
                        pixmap = QPixmap('art/bishopW.png')
                        painter.drawPixmap(x*80, y*80+40, 80, 80, pixmap)
                    elif(x == 3):
                        pixmap = QPixmap('art/queenW.png')
                        painter.drawPixmap(x*80, y*80+40, 80, 80, pixmap)
                    else:
                        pixmap = QPixmap('art/kingW.png')
                        painter.drawPixmap(x*80, y*80+40, 80, 80, pixmap)
        
        painter.end()

if __name__ == "__main__":
    
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(640, 680)
    widget.setMinimumSize(640, 680)
    widget.setMaximumSize(640, 680)
    widget.show()

    sys.exit(app.exec())