from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import QSize

from gui.cellWidget import CellWidget
from defines.gameDefines import PlayerId
from defines.uiDefines import CellDefines


class ColumnWidget(QWidget):

    def __init__(self, index: int, numberCells: int, playerMoveCallback):
        super().__init__()
        self._index = index
        self._numberCells = numberCells
        self._columnHeightPx = self._numberCells * CellDefines.CELL_HEIGHT_PX
        self._playerMoveCallback = playerMoveCallback
        self._cells = []

        self.__initCellWidgets()

    def __initCellWidgets(self):
        cellsLayout = QVBoxLayout()
        cellsLayout.setSpacing(0)
        cellsLayout.setContentsMargins(0, 0, 0, 0)

        for i in range(self._numberCells):
            cellWidget = CellWidget()
            cellWidget.mouseReleasedSignal.connect(self.sendPlayerMove)
            cellsLayout.addWidget(cellWidget)
            self._cells.append(cellWidget)

        self.setLayout(cellsLayout)
        self.setFixedSize(QSize(CellDefines.CELL_WIDTH_PX, self._columnHeightPx))

    def sendPlayerMove(self):
        self._playerMoveCallback(self._index)

    def setTokenColor(self, playerId: PlayerId, row: int):
        if row < len(self._cells):
            self._cells[row].setTokenColor(playerId)
