from queue import Queue
from managers.threadsManager import ThreadsManager
from gui.mainWindow import MainWindow
from PyQt6.QtWidgets import QApplication


def main():
    print("Main Running")

    gameStateQueue = Queue()
    gameDataQueue = Queue()

    threadsManager = ThreadsManager(gameStateQueue, gameDataQueue)

    threadsManager.createThreads()
    threadsManager.startThreads()

    app = QApplication([])

    mainWindow = MainWindow(gameStateQueue, gameDataQueue)
    mainWindow.show()

    app.exec()

    gameStateQueue.join()
    gameDataQueue.join()
    threadsManager.stopThreads()

    print("Main Finished")


if __name__ == '__main__':
    main()
