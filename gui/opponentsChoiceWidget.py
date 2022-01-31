from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt, pyqtSignal

from gui.guiCommon import setLabelFontSize, LabelAlignFlag, OpponentType


class OpponentsChoiceWidget(QWidget):

    opponentTypeSignal = pyqtSignal(int)
    closeRequestSignal = pyqtSignal()

    DEFAULT_WIDTH_PX = 600
    DEFAULT_HEIGHT_PX = 400
    OPPONENTS_CHOICE_FONT_SIZE = 30

    def __init__(self):
        super().__init__()
        self.verticalLayout = QVBoxLayout()

        self.__addOpponentsChoiceLabel()
        self.__addOpponentsButtons()
        self.__addQuitButtons()
        self.__addElementsToWidget()

    def __addOpponentsChoiceLabel(self):
        chooseOpponentLabel = QLabel("Choose Your Opponent")
        setLabelFontSize(chooseOpponentLabel, self.OPPONENTS_CHOICE_FONT_SIZE)
        chooseOpponentLabel.setAlignment(Qt.AlignmentFlag(LabelAlignFlag.AlignCenter.value))

        self.verticalLayout.addWidget(chooseOpponentLabel)

    def __addOpponentsButtons(self):
        opponentButtonsLayout = QHBoxLayout()

        humanButton = QPushButton("Human", self)
        humanButton.clicked.connect(lambda opponentType: self.__sendOpponentTypeSignal(opponentType=OpponentType.Human.value))
        opponentButtonsLayout.addWidget(humanButton)

        aiButton = QPushButton("AI", self)
        aiButton.clicked.connect(lambda opponentType: self.__sendOpponentTypeSignal(opponentType=OpponentType.Ai.value))
        opponentButtonsLayout.addWidget(aiButton)

        self.verticalLayout.addLayout(opponentButtonsLayout)

    def __addQuitButtons(self):
        quitButton = QPushButton("Quit", self)
        quitButton.clicked.connect(self.__sendCloseRequest)

        self.verticalLayout.addWidget(quitButton)

    def __addElementsToWidget(self):
        self.setLayout(self.verticalLayout)
        self.resize(self.DEFAULT_WIDTH_PX, self.DEFAULT_HEIGHT_PX)

    def __sendOpponentTypeSignal(self, opponentType):
        self.opponentTypeSignal.emit(opponentType)

    def __sendCloseRequest(self):
        self.closeRequestSignal.emit()


if __name__ == "__main__":
    print("opponentsChoiceWidget")
