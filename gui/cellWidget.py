from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QMouseEvent, QPaintEvent, QPainter, QPen
from PyQt6.QtCore import QSize, pyqtSignal as Signal

from gui.guiCommon import getQColor
from defines.gameDefines import PlayerId
from defines.uiDefines import CellDefines, TokenDefines


class CellWidget(QLabel):

    mouseReleasedSignal = Signal()

    def __init__(self, minimumWidth=CellDefines.CELL_WIDTH_PX, minimumHeight=CellDefines.CELL_HEIGHT_PX):
        super().__init__()
        self.setFixedSize(QSize(minimumWidth, minimumHeight))
        self.setStyleSheet(f"background-color:rgb{CellDefines.BACKGROUND_COLOR_STR}")
        self._currentColor = getQColor(TokenDefines.EMPTY_COLOR)
        self._backgroundColor = getQColor(CellDefines.BACKGROUND_COLOR)
        self._tokenOffsetPx = int((minimumWidth - TokenDefines.TOKEN_DIAMETER_PX) / 2)

    def setEmptyTokenColor(self):
        self._currentColor = getQColor(TokenDefines.EMPTY_COLOR)

    def setPlayableTokenAlpha(self, currentPlayerId: PlayerId, alpha: int = TokenDefines.PLAYABLE_TOKEN_ALPHA):
        self.setPlayerTokenColor(currentPlayerId)
        self._currentColor.setAlpha(alpha)

    def setPlayerTokenColor(self, playerId: PlayerId):
        if playerId == PlayerId.PLAYER1:
            self._currentColor = getQColor(TokenDefines.PLAYER1_COLOR)
        elif playerId == PlayerId.PLAYER2:
            self._currentColor = getQColor(TokenDefines.PLAYER2_COLOR)
        self._currentColor.setAlpha(TokenDefines.PLAYED_TOKEN_ALPHA)

    def setAlpha(self, alpha: int):
        self._currentColor.setAlpha(alpha)
        self._backgroundColor.setAlpha(alpha)
        self.setStyleSheet(f"background-color:rgba({CellDefines.BACKGROUND_COLOR_STR}, {alpha})")

    def mouseReleaseEvent(self, ev: QMouseEvent) -> None:
        self.mouseReleasedSignal.emit()

    def paintEvent(self, a0: QPaintEvent) -> None:
        self.__updateColor()
        self.update()

    def __updateColor(self):
        painter = QPainter()
        painter.begin(self)
        painter.setBrush(self._currentColor)
        pen = QPen()
        pen.setWidth(0)
        pen.setBrush(self._backgroundColor)
        painter.setPen(pen)
        painter.drawEllipse(self._tokenOffsetPx, self._tokenOffsetPx, TokenDefines.TOKEN_DIAMETER_PX, TokenDefines.TOKEN_DIAMETER_PX)
        painter.end()
