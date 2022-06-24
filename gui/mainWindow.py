from PyQt6.QtWidgets import QMainWindow, QVBoxLayout

from gui.opponentsChoiceWidget import OpponentsChoiceWidget
from gui.boardWidget import BoardWidget
from controller.controllerABC import ControllerABC
from factories.gamePacketBuilder import GamePacketBuilder as PacketBuilder
from logic.gameData import GameData
from defines.commandDefines import GameCommands
from defines.gameDefines import OpponentType
from defines.packetDefines import GamePacket
from version.versionDefines import getNameAndVersion


class MainWindow(QMainWindow):

    def __init__(self, controller: ControllerABC):
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
        gamePacket = PacketBuilder.getPacket(command=GameCommands.START_NEW_GAME, gameData=self._gameData)
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
            gamePacket = PacketBuilder.getPacket(command=GameCommands.ADD_PLAYER_MOVE, playedColumn=playedColumn)
            self._controller.addPacketToSend(gamePacket)

    def _ackAddPlayerMove(self, packet: GamePacket):
        currentPlayerId = packet.currentPlayerId
        playedColumn = packet.playedColumn
        playedRow = packet.playedRow

        if self._boardWidget is not None:
            self._boardWidget.setTokenColor(currentPlayerId, playedColumn, playedRow)

    def _finishGame(self, packet: GamePacket):
        self._isGameFinished = True
        winningPlayerId = packet.winningPlayerId


if __name__ == "__main__":
    print("mainWindow")
