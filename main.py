from queue import Queue
from managers.gameManager import GameManager
from gui.mainWindow import MainWindow
from PyQt6.QtWidgets import QApplication


def main():
    print("Main Running")

    modelQueue = Queue()
    uiQueue = Queue()

    gameManager = GameManager(modelQueue, uiQueue)
    gameManager.start()

    app = QApplication([])

    mainWindow = MainWindow(modelQueue, uiQueue)
    mainWindow.show()

    app.exec()

    modelQueue.join()
    uiQueue.join()

    gameManager.stop()
    gameManager.join()

    print("Main Finished")


if __name__ == '__main__':
    main()
