from PyQt6.QtWidgets import QWidget, QHBoxLayout
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QCursor

from logic.gameConfig import GameConfig
from defines.packetDefines import GamePacket
from defines.gameDefines import PlayerId
from defines.uiDefines import BoardDefines
from gui.columnWidget import ColumnWidget


class BoardWidget(QWidget):

    def __init__(self, gameConfig: GameConfig, playerMoveCallback):
        super().__init__()
        self._winningPlayerId = PlayerId.NO_PLAYER
        self._opponentType = gameConfig.opponentType
        self._numberColumns = gameConfig.numberColumns
        self._numberRow = gameConfig.numberLines
        self._playerMoveCallback = playerMoveCallback
        self._columnWidthPx = 0
        self._columnHeightPx = 0
        self._board = []

        self.__initBoard()
        self.__setSize()

    def __initBoard(self):
        columnsLayout = QHBoxLayout()
        columnsLayout.setSpacing(0)
        columnsLayout.setContentsMargins(0, 0, 0, 0)

        for i in range(self._numberColumns):
            columnWidget = ColumnWidget(i, self._numberRow, self._playerMoveCallback)
            columnsLayout.addWidget(columnWidget)
            self._board.append(columnWidget)
            self._columnWidthPx = columnWidget.size().width()
            self._columnHeightPx = columnWidget.size().height()

        self.setLayout(columnsLayout)

    def __setSize(self):
        boardWidthPx = self._numberColumns * self._columnWidthPx
        boardHeightPx = self._columnHeightPx

        self.setFixedSize(QSize(boardWidthPx, boardHeightPx))

    def finishGame(self, packet: GamePacket):
        self._winningPlayerId = packet.winningPlayerId
        self.__hideAllCurrentPlayableToken()
        self.__setAllColumnsAlpha()
        self.__removeEventFilters()

    def __setAllColumnsAlpha(self, alpha: int = BoardDefines.FINISHED_GAME_ALPHA):
        for column in range(len(self._board)):
            self._board[column].setAllCellsAlpha(alpha)

    def __removeEventFilters(self):
        for column in range(len(self._board)):
            self._board[column].removeEventFilters()

    def addPlayerMove(self, packet: GamePacket):
        lastPlayerId = packet.lastPlayerId
        currentPlayerId = packet.currentPlayerId
        playedColumn = packet.playedColumn
        playedRow = packet.playedRow

        self.__incrementNumberTokens(playedColumn)
        self.__setPlayerTokenColor(lastPlayerId, playedColumn, playedRow)
        self.__setColumnsCurrentPlayerId(currentPlayerId)
        self.__showCurrentPlayableToken()

    def __setPlayerTokenColor(self, playerId: PlayerId, columnIndex: int, rowIndex: int):
        if columnIndex <= len(self._board):
            self._board[columnIndex].setPlayerTokenColor(playerId, rowIndex)

    def __setColumnsCurrentPlayerId(self, currentPlayerId: PlayerId):
        for i in range(len(self._board)):
            self._board[i].setCurrentPlayerId(currentPlayerId)

    def __incrementNumberTokens(self, columnIndex: int):
        if columnIndex <= len(self._board):
            self._board[columnIndex].incrementNumberTokens()

    def __showCurrentPlayableToken(self):
        mouseXPosition = QCursor.pos()
        mouseXPosition = self.mapFromGlobal(mouseXPosition).x()

        for columnIndex in range(len(self._board)):
            if self.__isMouseWithinColumn(mouseXPosition, columnIndex):
                self._board[columnIndex].showCurrentPlayableToken()

    def __isMouseWithinColumn(self, mouseXPosition: int, columnIndex: int) -> bool:
        columnWidth = self.__getColumnWidth(columnIndex)
        isWithinColumn = mouseXPosition >= (columnIndex * columnWidth)
        isWithinColumn &= mouseXPosition <= ((columnIndex * columnWidth) + columnWidth)

        return isWithinColumn

    def __getColumnWidth(self, columnIndex: int) -> int:
        columnWidth = -1

        if columnIndex < len(self._board):
            columWidgetGeometry = self._board[columnIndex].geometry()
            columnWidth = columWidgetGeometry.width()

        return columnWidth

    def __hideAllCurrentPlayableToken(self):
        for i in range(len(self._board)):
            self._board[i].hideCurrentPlayableToken()
