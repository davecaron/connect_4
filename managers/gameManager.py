from queue import Queue
from threading import Thread, Event
from time import sleep

from factories.GamePacketFactory import GamePacketFactory as PacketFactory
from logic.connect_4 import Connect4Game, PlayerId
from communication.PacketProcessor import PacketProcessor
from communication.GameCommunicator import GameCommunicator
from defines.commandDefines import GameCommands as Commands
from defines.packetDefines import GamePacket


class GameManager(Thread):
    SLEEPING_TIME_SEC = 0.1

    def __init__(self, modelQueue: Queue, uiQueue: Queue):
        super().__init__()
        self._game: Connect4Game = None
        self._isGameStarted = False
        self._isGameFinished = False
        self._winningPlayer = PlayerId.NO_PLAYER
        self._stopFlag = Event()
        self._commandsCallbackMap = {Commands.START_NEW_GAME: self.startNewGame,
                                     Commands.ADD_PLAYER_MOVE: self.addPlayerMove}
        self._packetProcessor = PacketProcessor(modelQueue, self._commandsCallbackMap)
        self._uiCommunicator = GameCommunicator(uiQueue)

    def run(self):
        while not self.__isStopped():
            self._packetProcessor.executeLastCommand()

            if self._canUpdateGame():
                self._game.update()
                self._checkGameFinished()

            sleep(self.SLEEPING_TIME_SEC)

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
            self._winningPlayer = self._game.getWinningPlayerId()
            gamePacket = PacketFactory.getPacket(command=Commands.FINISH_GAME, winningPlayer=self._winningPlayer)
            self._uiCommunicator.addPacket(gamePacket)

    def stop(self):
        self._stopFlag.set()

    def __isStopped(self):
        return self._stopFlag.is_set()

    def startNewGame(self, packet: GamePacket):
        gameData = packet.gameData
        self._game = Connect4Game(gameData)
        self._isGameStarted = True

    def addPlayerMove(self, packet: GamePacket):
        column = packet.playedColumn
        row = packet.playedRow

        self._game.add_move(column, row)


if __name__ == "__main__":
    print("gameManager")
