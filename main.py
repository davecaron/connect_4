from queue import Queue
from gui.mainWindow import MainWindow
from PyQt6.QtWidgets import QApplication

from managers.gameManager import GameManager
from controller.gameController import GameController


def main():
    print("Main Running")

    modelQueue = Queue()
    uiQueue = Queue()

    gameManager = GameManager(modelQueue, uiQueue)
    gameManager.start()

    app = QApplication([])

    gameController = GameController(modelQueue, uiQueue)

    mainWindow = MainWindow(gameController)
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
