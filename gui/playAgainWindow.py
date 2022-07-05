from PyQt6.QtWidgets import QDialog, QPushButton, QHBoxLayout

from defines.uiDefines import PlayAgainWindow as Config


class PlayAgainWindow(QDialog):

    PLAY_AGAIN_EXEC_VALUE = 1
    QUIT_EXEC_VALUE = 2

    def __init__(self, title=Config.DEFAULT_TITLE, width=Config.DEFAULT_WIDTH_PX, height=Config.DEFAULT_HEIGHT_PX):
        super().__init__()
        self.horizontalLayout = QHBoxLayout()

        self.setWindowTitle(title)
        self.setFixedSize(width, height)

        self.__initButtons()
        self.__setLayout()

    def __initButtons(self):
        buttonsLayout = QHBoxLayout()

        self._playAgainButton = QPushButton("Play Again", self)
        self._playAgainButton.clicked.connect(lambda value: self._returnExecValue(value=self.PLAY_AGAIN_EXEC_VALUE))
        buttonsLayout.addWidget(self._playAgainButton)

        self._quitButton = QPushButton("Quit", self)
        self._quitButton.clicked.connect(lambda value: self._returnExecValue(value=self.QUIT_EXEC_VALUE))
        buttonsLayout.addWidget(self._quitButton)

        self.horizontalLayout.addLayout(buttonsLayout)

    def __setLayout(self):
        self.setLayout(self.horizontalLayout)

    def _returnExecValue(self, value: int):
        self.done(value)
