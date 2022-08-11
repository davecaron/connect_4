from enum import IntEnum


class BoardConfig:
    DEFAULT_NUMBER_COLUMNS = 7
    DEFAULT_NUMBER_LINES = 6
    DEFAULT_NUMBER_PIECES_TO_WIN = 4


class OpponentType(IntEnum):
    INVALID = -1
    HUMAN = 0
    AI    = 1


class PlayerId(IntEnum):
    NO_PLAYER = -1
    PLAYER1 = 0
    PLAYER2 = 1
