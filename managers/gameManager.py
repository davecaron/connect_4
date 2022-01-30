import threading
from logic.connect_4 import connect4Game, PlayerId
from time import sleep

class GameManager(threading.Thread):

    SLEEPING_TIME_SEC = 0.1

    def __init__(self):
        super().__init__()
        self.game = connect4Game()
        self.winningPlayer = PlayerId.INVALID_PLAYER.value
        self.stopFlag = threading.Event()

    def run(self):
        while not self.__isStopped():

            self.game.update()

            if self.game.isFinished():
                self.winningPlayer = self.game.getWinningPlayerId()

            sleep(self.SLEEPING_TIME_SEC)

    def stop(self):
        self.stopFlag.set()

    def __isStopped(self):
        return self.stopFlag.is_set()


if __name__ == "__main__":
    print("gameManager")
