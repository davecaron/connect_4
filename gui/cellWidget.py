from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QMouseEvent, QPaintEvent, QPainter, QPen
from PyQt6.QtCore import QSize, pyqtSignal as Signal

from defines.gameDefines import PlayerId
from defines.uiDefines import CellDefines, TokenDefines


class CellWidget(QLabel):

    mouseReleasedSignal = Signal()

    def __init__(self, minimumWidth=CellDefines.CELL_WIDTH_PX, minimumHeight=CellDefines.CELL_HEIGHT_PX):
        super().__init__()
        self.setFixedSize(QSize(minimumWidth, minimumHeight))
        self.setStyleSheet("background-color:rgb(0,162,232)")
        self._color = TokenDefines.EMPTY_COLOR

    def mouseReleaseEvent(self, ev: QMouseEvent) -> None:
        self.mouseReleasedSignal.emit()

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter()
        painter.begin(self)
        painter.setBrush(self._color)
        pen = QPen()
        pen.setWidth(0)
        pen.setBrush(CellDefines.BACKGROUND_COLOR)
        painter.setPen(pen)
        painter.drawEllipse(10, 10, 80, 80)
        painter.end()

        self.update()

    def setTokenColor(self, playerId: PlayerId):
        if playerId == PlayerId.PLAYER1:
            self._color = TokenDefines.PLAYER1_COLOR
        elif playerId == PlayerId.PLAYER2:
            self._color = TokenDefines.PLAYER2_COLOR
