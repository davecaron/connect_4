from queue import Queue
from threading import Thread, Event
from time import sleep

from factories.packetBuilder import PacketBuilder
from logic.connect_4 import Connect4Game
from communication.PacketProcessor import PacketProcessor
from communication.GameCommunicator import GameCommunicator
from defines.commandDefines import GameCommands as Commands
from defines.packetDefines import GamePacket


class GameManager(Thread):
    SLEEPING_TIME_SEC = 0.01

    def __init__(self, modelQueue: Queue, uiQueue: Queue, packetBuilder: PacketBuilder):
        super().__init__()
        self._game: Connect4Game = None
        self._isGameStarted = False
        self._isGameFinished = False
        self._stopFlag = Event()
        self._commandsCallbackMap = {Commands.START_NEW_GAME: self._startNewGame,
                                     Commands.ADD_PLAYER_MOVE: self._addPlayerMove}
        self._packetProcessor = PacketProcessor(modelQueue, self._commandsCallbackMap)
        self._uiCommunicator = GameCommunicator(uiQueue)
        self._packetBuilder = packetBuilder

    def _canUpdateGame(self) -> bool:
        canUpdateGame = self._isGameStarted
        canUpdateGame &= not self._isGameFinished

        return canUpdateGame

    def _isGameFinished(self) -> bool:
        isGameFinished = False

        if self._game is not None:
            isGameFinished = self._game.isFinished()

        return isGameFinished

    def _checkGameFinished(self):
        if self._game.isFinished():
            self._isGameFinished = True
            winningPlayerId = self._game.getWinningPlayerId()
            gamePacket = self._packetBuilder.getPacket(command=Commands.FINISH_GAME, winningPlayerId=winningPlayerId)
            self._uiCommunicator.addPacket(gamePacket)

    def _startNewGame(self, packet: GamePacket):
        gameData = packet.gameData
        self._game = Connect4Game(gameData)
        self._isGameStarted = True

    def _addPlayerMove(self, packet: GamePacket):
        column = packet.playedColumn
        lastPlayerId, playedRow = self._game.add_move_column(column)
        currentPlayerId = self._game.getCurrentPlayerId()

        if playedRow != -1:
            gamePacket = self._packetBuilder.getPacket(command=Commands.ACK_ADD_PLAYER_MOVE,
                                                       playedColumn=column,
                                                       playedRow=playedRow,
                                                       lastPlayerId=lastPlayerId,
                                                       currentPlayerId=currentPlayerId)
            self._uiCommunicator.addPacket(gamePacket)

    def __isStopped(self):
        return self._stopFlag.is_set()

    def stop(self):
        self._stopFlag.set()

    def run(self):
        while not self.__isStopped():
            self._packetProcessor.executeLastCommand()

            if self._canUpdateGame():
                self._game.update()
                self._checkGameFinished()

            sleep(self.SLEEPING_TIME_SEC)


if __name__ == "__main__":
    print("gameManager")
