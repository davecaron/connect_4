from gameManager import GameManager


class ThreadsManager:

    def __init__(self):
        self._threads = []

    def createThreads(self):
        print("Creating thread %s" % GameManager.__name__)
        thread = GameManager()
        thread.daemon = True
        print("Thread created")
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
