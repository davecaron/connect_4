from managers.threadsManager import ThreadsManager
from gui.mainWindow import MainWindow
from PyQt6.QtWidgets import QApplication


def main():
    print("Main Running")

    threadsManager = ThreadsManager()

    threadsManager.createThreads()
    threadsManager.startThreads()

    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()

    threadsManager.stopThreads()

    print("Main Finished")


if __name__ == '__main__':
    main()
