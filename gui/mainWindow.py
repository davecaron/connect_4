from queue import Queue
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout
from PyQt6.QtCore import QTimer

from gui.opponentsChoiceWidget import OpponentsChoiceWidget
from gui.boardWidget import BoardWidget
from communication.PacketProcessor import PacketProcessor
from communication.GameCommunicator import GameCommunicator
from factories.GamePacketFactory import GamePacketFactory as PacketFactory
from logic.gameData import GameData
from defines.commandDefines import GameCommands
from defines.gameDefines import OpponentType
from version.versionDefines import getNameAndVersion


class MainWindow(QMainWindow):

    GAME_STATE_TIMER_UPDATE_TIME_MS = 100

    def __init__(self, modelQueue: Queue, uiQueue: Queue):
        super().__init__()
        self._gameData = GameData()
        self.verticalLayout = QVBoxLayout()
        self.opponentsWidget = None
        self.boardWidget = None
        self._commandsCallbackMap = {GameCommands.FINISH_GAME: self.finishGame}
        self._packetProcessor = PacketProcessor(uiQueue, self._commandsCallbackMap)
        self._modelCommunicator = GameCommunicator(modelQueue)

        self.__initTimer()
        self.__initWindow()

        self.__addOpponentsChoiceWidget()

    def __initTimer(self):
        self._gameStateTimer = QTimer()
        self._gameStateTimer.setInterval(self.GAME_STATE_TIMER_UPDATE_TIME_MS)
        self._gameStateTimer.timeout.connect(self.processGamePacket)

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

        self.__addBoardWidget()
        self.__startNewGame()
        self._gameStateTimer.start()

    def __addBoardWidget(self):
        self.boardWidget = BoardWidget(self._gameData, self.sendPlayerMove)

        self.verticalLayout.addWidget(self.boardWidget)
        self.setLayout(self.verticalLayout)

        self.setCentralWidget(self.boardWidget)

    def sendPlayerMove(self, playedColumn: int, playedRow: int):
        gamePacket = PacketFactory.getPacket(command=GameCommands.ADD_PLAYER_MOVE, playedColumn=playedColumn, playedRow=playedRow)
        self._modelCommunicator.addPacket(gamePacket)

    def receiveCloseRequest(self):
        self.close()

    def processGamePacket(self):
        self._packetProcessor.executeLastCommand()

    def __startNewGame(self):
        gamePacket = PacketFactory.getPacket(command=GameCommands.START_NEW_GAME, gameData=self._gameData)
        self._modelCommunicator.addPacket(gamePacket)

    def finishGame(self, packet):
        pass


if __name__ == "__main__":
    print("mainWindow")
