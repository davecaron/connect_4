from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import QSize, QEvent
from PyQt6.QtGui import QMouseEvent

from gui.cellWidget import CellWidget
from defines.gameDefines import PlayerId
from defines.uiDefines import CellDefines


class ColumnWidget(QWidget):

    def __init__(self, index: int, numberCells: int, playerMoveCallback):
        super().__init__()
        self._index = index
        self._currentPlayerId = PlayerId.PLAYER1
        self._numberCells = numberCells
        self._columnHeightPx = self._numberCells * CellDefines.CELL_HEIGHT_PX
        self._playerMoveCallback = playerMoveCallback
        self._cells = []
        self._numberTokens = 0

        self.__init()

    def __init(self):
        self.__setSize()
        self.__initCellWidgets()
        self.setMouseTracking(True)
        self.installEventFilter(self)

    def __setSize(self):
        self.setFixedSize(QSize(CellDefines.CELL_WIDTH_PX, self._columnHeightPx))

    def __initCellWidgets(self):
        cellsLayout = QVBoxLayout()
        cellsLayout.setSpacing(0)
        cellsLayout.setContentsMargins(0, 0, 0, 0)

        for i in range(self._numberCells):
            cell = self.__createCellWidget()
            self._cells.append(cell)
            cellsLayout.addWidget(cell)

        self.setLayout(cellsLayout)

    def __createCellWidget(self):
        cellWidget = CellWidget()
        cellWidget.mouseReleasedSignal.connect(self.sendPlayerMove)

        return cellWidget

    def sendPlayerMove(self):
        self._playerMoveCallback(self._index)

    def setCurrentPlayerId(self, currentPlayerId: PlayerId):
        self._currentPlayerId = currentPlayerId

    def setPlayerTokenColor(self, playerId: PlayerId,  rowIndex: int):
        if rowIndex < len(self._cells):
            self._cells[rowIndex].setPlayerTokenColor(playerId)
        self.setFocus()

    def setAllCellsAlpha(self, alpha: int):
        for i in range(len(self._cells)):
            self._cells[i].setAlpha(alpha)
        self.setFocus()

    def incrementNumberTokens(self):
        self._numberTokens += 1

    def removeEventFilters(self):
        self.removeEventFilter(self)

    def eventFilter(self, source: 'QObject', event: 'QEvent') -> bool:
        if event.type() == QEvent.Type.Enter:
            self.showCurrentPlayableToken()
        elif event.type() == QEvent.Type.Leave:
            self.hideCurrentPlayableToken()

        return super(ColumnWidget, self).eventFilter(source, event)

    def showCurrentPlayableToken(self):
        playableTokenIndex = len(self._cells) - self._numberTokens - 1

        if playableTokenIndex >= 0:
            self._cells[playableTokenIndex].setPlayableTokenAlpha(self._currentPlayerId)

    def hideCurrentPlayableToken(self):
        playableTokenIndex = len(self._cells) - self._numberTokens - 1

        if playableTokenIndex >= 0:
            self._cells[playableTokenIndex].setEmptyTokenColor()
