from PyQt6.QtWidgets import QMainWindow, QVBoxLayout

from gui.opponentsChoiceWidget import OpponentsChoiceWidget
from gui.gameWidget import GameWidget
from gui.guiCommon import OpponentType
from version.versionDefines import getNameAndVersion


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.opponentType = OpponentType.Invalid.value
        self.verticalLayout = QVBoxLayout()
        self.opponentsWidget = None
        self.gameWidget = None

        self.__initWindow()
        self.__addOpponentsChoiceWidget()

    def __initWindow(self):
        nameAndVersion = getNameAndVersion()
        self.setWindowTitle(nameAndVersion)

    def __addOpponentsChoiceWidget(self):
        self.opponentsWidget = OpponentsChoiceWidget()
        self.opponentsWidget.opponentTypeSignal.connect(self.receiveOpponentType)
        self.opponentsWidget.closeRequestSignal.connect(self.receiveCloseRequest)

        self.verticalLayout.addWidget(self.opponentsWidget)
        self.setLayout(self.verticalLayout)

        self.setCentralWidget(self.opponentsWidget)

    def receiveOpponentType(self, opponentType):
        self.opponentType = opponentType

        self.opponentsWidget.close()
        self.opponentsWidget.destroy()

        self.__addGameWidget()

    def __addGameWidget(self):
        self.gameWidget = GameWidget(self.opponentType)

        self.verticalLayout.addWidget(self.gameWidget)
        self.setLayout(self.verticalLayout)

        self.setCentralWidget(self.gameWidget)

    def receiveCloseRequest(self):
        self.close()


if __name__ == "__main__":
    print("mainWindow")
