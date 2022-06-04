from queue import Queue
from _queue import Empty
from threading import Thread, Event
from time import sleep

from logic.connect_4 import connect4Game, PlayerId
from logic.gameData import GameData


class GameManager(Thread):
    SLEEPING_TIME_SEC = 0.1

    def __init__(self, gameState: Queue, gameDataQueue: Queue):
        super().__init__()
        self._gameStateQueue = gameState
        self._gameDataQueue = gameDataQueue
        self._gameData: GameData = None
        self._game = None
        self._isGameStarted = False
        self._winningPlayer = PlayerId.NO_PLAYER
        self._stopFlag = Event()

    def run(self):
        while not self.__isStopped():
            if self._needStartNewGame():
                self._startNewGame()
            elif self._canUpdateGame():
                self._game.update()
                self._checkGameFinished()

            sleep(self.SLEEPING_TIME_SEC)

    def _needStartNewGame(self) -> bool:
        if not self._gameDataQueue.empty():
            try:
                self._gameData = self._gameDataQueue.get_nowait()
                self._gameDataQueue.task_done()
            except Empty:
                pass

        return self._gameData is not None

    def _canUpdateGame(self) -> bool:
        canUpdateGame = self._isGameStarted
        canUpdateGame &= not self._isGameFinished()

        return canUpdateGame

    def _isGameFinished(self) -> bool:
        isGameFinished = False

        if self._game is not None:
            isGameFinished = self._game.isFinished()

        return isGameFinished

    def _startNewGame(self):
        self._game = connect4Game(self._gameData)
        self._gameData = None
        self._isGameStarted = True

    def _checkGameFinished(self):
        if self._game.isFinished():
            self._winningPlayer = self._game.getWinningPlayerId()
            self._gameStateQueue.put(self._winningPlayer)

    def stop(self):
        self._stopFlag.set()

    def __isStopped(self):
        return self._stopFlag.is_set()


if __name__ == "__main__":
    print("gameManager")
