import threading
from logic.connect_4 import connect4Game, PlayerId
from time import sleep


class GameManager(threading.Thread):
    SLEEPING_TIME_SEC = 0.1

    def __init__(self):
        super().__init__()
        self._game = connect4Game()
        self._winningPlayer = PlayerId.NO_PLAYER.value
        self._stopFlag = threading.Event()

    def run(self):
        while not self.__isStopped():

            self._game.update()

            if self._game.isFinished():
                self._winningPlayer = self._game.getWinningPlayerId()

            sleep(self.SLEEPING_TIME_SEC)

    def stop(self):
        self._stopFlag.set()

    def __isStopped(self):
        return self._stopFlag.is_set()


if __name__ == "__main__":
    print("gameManager")
