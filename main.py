from queue import Queue
from gui.mainWindow import MainWindow
from PyQt6.QtWidgets import QApplication

from managers.gameManager import GameManager
from controller.gameController import GameController
from factories.gamePacketBuilder import GamePacketBuilder


def main():
    print("Main Running")

    modelQueue = Queue()
    uiQueue = Queue()

    gamePacketBuilder = GamePacketBuilder()
    gameManager = GameManager(modelQueue, uiQueue, gamePacketBuilder)
    gameManager.start()

    app = QApplication([])

    gameController = GameController(modelQueue, uiQueue)
    gamePacketBuilder = GamePacketBuilder()

    mainWindow = MainWindow(gameController, gamePacketBuilder)
    mainWindow.show()

    gameController.start()
    app.exec()

    modelQueue.join()
    uiQueue.join()

    gameManager.stop()
    gameManager.join()
    gameController.stop()
    gameController.join()

    print("Main Finished")


if __name__ == '__main__':
    main()
