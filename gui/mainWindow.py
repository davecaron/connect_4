from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from version.versionDefines import getNameAndVersion


class MainWindow(QMainWindow):
    DEFAULT_WIDTH_PX = 600
    DEFAULT_HEIGHT_PX = 400

    def __init__(self):
        super().__init__()

        self.__initMainWindow()
        self.__addMenuButtons()

    def __initMainWindow(self):
        nameAndVersion = getNameAndVersion()
        self.setWindowTitle(nameAndVersion)
        self.resize(self.DEFAULT_WIDTH_PX, self.DEFAULT_HEIGHT_PX)
        self.menuWidget = QWidget()

    def __addMenuButtons(self):
        verticalLayout = QVBoxLayout()
        horizontalLayout = QHBoxLayout()
        horizontalLayout.addStretch(1)

        playButton = QPushButton("Play", self)
        playButton.clicked.connect(self.__play)
        horizontalLayout.addWidget(playButton)

        quitButton = QPushButton("Quit", self)
        quitButton.clicked.connect(self.__quit)
        horizontalLayout.addWidget(quitButton)

        verticalLayout.addLayout(horizontalLayout)
        self.menuWidget.setLayout(verticalLayout)
        self.setCentralWidget(self.menuWidget)

    def __play(self):
        print("play")

    def __quit(self):
        self.close()
