from queue import Queue
from _queue import Empty
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout
from PyQt6.QtCore import QTimer

from gui.opponentsChoiceWidget import OpponentsChoiceWidget
from gui.gameWidget import GameWidget
from logic.gameData import GameData
from defines.gameDefines import OpponentType
from version.versionDefines import getNameAndVersion


class MainWindow(QMainWindow):

    GAME_STATE_TIMER_UPDATE_TIME_MS = 100

    def __init__(self, gameStateQueue: Queue, gameDataQueue: Queue):
        super().__init__()
        self._gameStateQueue = gameStateQueue
        self._gameDataQueue = gameDataQueue
        self._gameData = GameData()
        self.verticalLayout = QVBoxLayout()
        self.opponentsWidget = None
        self.gameWidget = None
        self._gameStateTimer = QTimer()
        self._gameStateTimer.setInterval(self.GAME_STATE_TIMER_UPDATE_TIME_MS)
        self._gameStateTimer.timeout.connect(self.checkGameState)

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

    def receiveOpponentType(self, opponentType: OpponentType):
        self._gameData.opponentType = OpponentType(opponentType)

        self.opponentsWidget.close()
        self.opponentsWidget.destroy()

        self.__addGameWidget()
        self.__updateGameDataQueue()
        self._gameStateTimer.start()

    def __addGameWidget(self):
        self.gameWidget = GameWidget(self._gameData.opponentType)

        self.verticalLayout.addWidget(self.gameWidget)
        self.setLayout(self.verticalLayout)

        self.setCentralWidget(self.gameWidget)

    def receiveCloseRequest(self):
        self.close()

    def __updateGameDataQueue(self):
        self._gameDataQueue.put(self._gameData)

    def checkGameState(self):
        if not self._gameStateQueue.empty():
            try:
                gameState = self._gameStateQueue.get_nowait()
                self._gameStateQueue.task_done()
            except Empty:
                pass


if __name__ == "__main__":
    print("mainWindow")
