from PyQt6.QtWidgets import QWidget, QHBoxLayout

from logic.gameData import GameData
from gui.columnWidget import ColumnWidget


class BoardWidget(QWidget):

    DEFAULT_WIDTH_PX = 1200
    DEFAULT_HEIGHT_PX = 800

    def __init__(self, gameData: GameData, playerMoveCallback):
        super().__init__()
        self.resize(self.DEFAULT_WIDTH_PX, self.DEFAULT_HEIGHT_PX)

        self._opponentType = gameData.opponentType
        self._numberColumns = gameData.numberColumns
        self._numberRow = gameData.numberLines
        self._playerMoveCallback = playerMoveCallback
        self._board = []

        self.__initBoard()

    def __initBoard(self):
        horizontalLayout = QHBoxLayout()

        for i in range(self._numberColumns):
            columnWidget = ColumnWidget(i, self._numberRow, self._playerMoveCallback)
            horizontalLayout.addWidget(columnWidget)
            self._board.append(columnWidget)

        self.setLayout(horizontalLayout)


if __name__ == "__main__":
    print("boardWidget")
