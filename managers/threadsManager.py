from gameManager import GameManager

class ThreadsManager:

    def __init__(self):
        self.threads = []

    def createThreads(self):
        print("Creating thread %s" % GameManager.__name__)
        thread = GameManager()
        thread.daemon = True
        print("Thread created")
        self.threads.append(thread)

    def startThreads(self):
        for thread in self.threads:
            if (thread != None):
                thread.start()

    def stopThreads(self):
        for thread in self.threads:
            if (thread != None):
                thread.stop()
                thread.join()


if __name__ == "__main__":
    print("threadsManager")
