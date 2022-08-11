from PyQt6.QtWidgets import QMainWindow, QDialog
from PyQt6.QtCore import QTimer

from gui.playAgainWindow import PlayAgainWindow
from gui.opponentsChoiceWindow import OpponentsChoiceWindow
from gui.boardWidget import BoardWidget
from controller.controllerABC import ControllerABC
from factories.packetBuilder import PacketBuilder
from logic.gameConfig import GameConfig
from defines.commandDefines import GameCommands
from defines.gameDefines import OpponentType
from defines.packetDefines import GamePacket
from version.versionDefines import getNameAndVersion


class MainWindow(QMainWindow):

    GAME_FINISHED_UPDATE_TIME_MS = 100

    def __init__(self, controller: ControllerABC, packetBuilder: PacketBuilder):
        super().__init__()
        self._gameConfig = GameConfig()
        self._opponentsWindow = None
        self._boardWidget: BoardWidget = None
        self._playAgainWindow = None
        self._isGameFinished = False
        self._commandsCallbackMap = {GameCommands.ACK_ADD_PLAYER_MOVE: self._ackAddPlayerMove,
                                     GameCommands.FINISH_GAME: self._finishGame}
        self._controller = controller
        self._controller.setCommandsCallbackMap(self._commandsCallbackMap)
        self._packetBuilder = packetBuilder

        self.__initTimer()
        self.__initWindow()
        self.__addOpponentsChoiceWindow()

    def __initTimer(self):
        self._timer = QTimer()
        self._timer.setInterval(self.GAME_FINISHED_UPDATE_TIME_MS)
        self._timer.timeout.connect(self._checkIsGameFinished)
        self._timer.start()

    def __initWindow(self):
        nameAndVersion = getNameAndVersion()
        self.setWindowTitle(nameAndVersion)

    def __addOpponentsChoiceWindow(self):
        self._opponentsWindow = OpponentsChoiceWindow()
        self._opponentsWindow.opponentTypeSignal.connect(self.receiveOpponentType)
        self._opponentsWindow.closeRequestSignal.connect(self.receiveCloseRequest)
        self.setCentralWidget(self._opponentsWindow)

    def __addBoardWidget(self):
        self._boardWidget = BoardWidget(self._gameConfig, self.sendPlayerMove)
        self.setCentralWidget(self._boardWidget)
        self.setFixedSize(self._boardWidget.size())

    def __startNewGame(self):
        self._isGameFinished = False
        gamePacket = self._packetBuilder.getPacket(command=GameCommands.START_NEW_GAME, gameConfig=self._gameConfig)
        self._controller.addPacketToSend(gamePacket)

    def receiveOpponentType(self, opponentType: OpponentType):
        self._gameConfig.opponentType = OpponentType(opponentType)

        self._opponentsWindow.close()
        self._opponentsWindow.destroy()

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

    def _checkIsGameFinished(self):
        if self._isGameFinished and not self._playAgainWindow:
            execValue = self._showPlayAgainWindow()
            self.__processShowPlayAgainExecValue(execValue)

    def _showPlayAgainWindow(self) -> int:
        self._playAgainWindow = PlayAgainWindow()
        execValue = self._playAgainWindow.exec()
        self._playAgainWindow = None

        return execValue

    def __processShowPlayAgainExecValue(self, execValue: int):
        if execValue == PlayAgainWindow.PLAY_AGAIN_EXEC_VALUE:
            self.__restartGame()
        elif execValue == PlayAgainWindow.QUIT_EXEC_VALUE:
            self.close()

    def __restartGame(self):
        self._boardWidget.destroy()
        self.__addBoardWidget()
        self.__startNewGame()


if __name__ == "__main__":
    print("mainWindow")
