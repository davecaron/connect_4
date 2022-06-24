from PyQt6.QtWidgets import QWidget, QHBoxLayout
from PyQt6.QtCore import QSize

from logic.gameData import GameData
from defines.gameDefines import PlayerId
from gui.columnWidget import ColumnWidget


class BoardWidget(QWidget):

    def __init__(self, gameData: GameData, playerMoveCallback):
        super().__init__()

        self._opponentType = gameData.opponentType
        self._numberColumns = gameData.numberColumns
        self._numberRow = gameData.numberLines
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

    def setTokenColor(self, playerId: PlayerId, column: int, row: int):
        if column <= len(self._board):
            self._board[column].setCellColor(playerId, row)


if __name__ == "__main__":
    print("boardWidget")
