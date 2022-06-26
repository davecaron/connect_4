from PyQt6.QtWidgets import QMainWindow, QVBoxLayout

from gui.opponentsChoiceWidget import OpponentsChoiceWidget
from gui.boardWidget import BoardWidget
from controller.controllerABC import ControllerABC
from factories.packetBuilder import PacketBuilder
from logic.gameData import GameData
from defines.commandDefines import GameCommands
from defines.gameDefines import OpponentType
from defines.packetDefines import GamePacket
from version.versionDefines import getNameAndVersion


class MainWindow(QMainWindow):

    def __init__(self, controller: ControllerABC, packetBuilder: PacketBuilder):
        super().__init__()
        self._gameData = GameData()
        self._verticalLayout = QVBoxLayout()
        self._opponentsWidget = None
        self._boardWidget: BoardWidget = None
        self._isGameFinished = False
        self._commandsCallbackMap = {GameCommands.ACK_ADD_PLAYER_MOVE: self._ackAddPlayerMove,
                                     GameCommands.FINISH_GAME: self._finishGame}
        self._controller = controller
        self._controller.setCommandsCallbackMap(self._commandsCallbackMap)
        self._packetBuilder = packetBuilder

        self.__initWindow()
        self.__addOpponentsChoiceWidget()

    def __initWindow(self):
        nameAndVersion = getNameAndVersion()
        self.setWindowTitle(nameAndVersion)

    def __addOpponentsChoiceWidget(self):
        self._opponentsWidget = OpponentsChoiceWidget()
        self._opponentsWidget.opponentTypeSignal.connect(self.receiveOpponentType)
        self._opponentsWidget.closeRequestSignal.connect(self.receiveCloseRequest)

        self._verticalLayout.addWidget(self._opponentsWidget)
        self.setLayout(self._verticalLayout)

        self.setCentralWidget(self._opponentsWidget)

    def __addBoardWidget(self):
        self._verticalLayout.setSpacing(0)

        self._boardWidget = BoardWidget(self._gameData, self.sendPlayerMove)
        self._verticalLayout.addWidget(self._boardWidget)

        self.setCentralWidget(self._boardWidget)
        self.setFixedSize(self._boardWidget.size())

    def __startNewGame(self):
        self._isGameFinished = False
        gamePacket = self._packetBuilder.getPacket(command=GameCommands.START_NEW_GAME, gameData=self._gameData)
        self._controller.addPacketToSend(gamePacket)

    def receiveOpponentType(self, opponentType: OpponentType):
        self._gameData.opponentType = OpponentType(opponentType)

        self._opponentsWidget.close()
        self._opponentsWidget.destroy()

        self.__addBoardWidget()
        self.__startNewGame()

    def receiveCloseRequest(self):
        self.close()

    def sendPlayerMove(self, playedColumn: int):
        if not self._isGameFinished:
            gamePacket = self._packetBuilder.getPacket(command=GameCommands.ADD_PLAYER_MOVE, playedColumn=playedColumn)
            self._controller.addPacketToSend(gamePacket)

    def _ackAddPlayerMove(self, packet: GamePacket):
        if self._boardWidget is not None:
            self._boardWidget.addPlayerMove(packet)

    def _finishGame(self, packet: GamePacket):
        self._isGameFinished = True
        self._boardWidget.finishGame(packet)


if __name__ == "__main__":
    print("mainWindow")
