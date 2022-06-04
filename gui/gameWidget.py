from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt

from gui.guiCommon import getOpponentName, setLabelFontSize, LabelAlignFlag
from defines.gameDefines import OpponentType


class GameWidget(QWidget):

    DEFAULT_WIDTH_PX = 1200
    DEFAULT_HEIGHT_PX = 800

    def __init__(self, opponentType: OpponentType):
        super().__init__()
        self.resize(self.DEFAULT_WIDTH_PX, self.DEFAULT_HEIGHT_PX)

        dummyLabel = QLabel("Playing Connect4 against %s" % getOpponentName(opponentType))
        setLabelFontSize(dummyLabel, 60)
        dummyLabel.setAlignment(Qt.AlignmentFlag(LabelAlignFlag.AlignCenter.value))

        verticalLayout = QVBoxLayout()
        verticalLayout.addWidget(dummyLabel)

        self.setLayout(verticalLayout)


if __name__ == "__main__":
    print("gameWidget")
