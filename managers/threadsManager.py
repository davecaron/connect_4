from queue import Queue
from gameManager import GameManager


class ThreadsManager:

    def __init__(self, gameStateQueue: Queue, gameDataQueue: Queue):
        self._threads = []
        self._gameStateQueue = gameStateQueue
        self._gameDataQueue = gameDataQueue

    def createThreads(self):
        print("Creating thread %s" % GameManager.__name__)
        thread = GameManager(self._gameStateQueue, self._gameDataQueue)
        thread.daemon = True
        print("Thread %s created" % GameManager.__name__)
        self._threads.append(thread)

    def startThreads(self):
        for thread in self._threads:
            if thread is not None:
                thread.start()

    def stopThreads(self):
        for thread in self._threads:
            if thread is not None:
                thread.stop()
                thread.join()


if __name__ == "__main__":
    print("threadsManager")
