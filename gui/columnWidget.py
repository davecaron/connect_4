from PyQt6.QtWidgets import QWidget, QVBoxLayout
from gui.cellWidget import CellWidget


class ColumnWidget(QWidget):

    def __init__(self, index: int, numberCells: int, playerMoveCallback):
        super().__init__()
        self._index = index
        self._numberCells = numberCells
        self._playerMoveCallback = playerMoveCallback
        self._cells = []

        self.__initCellWidgets()

    def __initCellWidgets(self):
        verticalLayout = QVBoxLayout()

        for i in range(self._numberCells):
            cellWidget = CellWidget()
            cellWidget.clicked.connect(lambda index=int(i): self.sendPlayerMove(index))
            verticalLayout.addWidget(cellWidget)
            self._cells.append(cellWidget)

        self.setLayout(verticalLayout)

    def sendPlayerMove(self, playedRow: int):
        self._playerMoveCallback(self._index, playedRow)
