from enum import IntEnum


class GameCommands(IntEnum):
    NO_COMMAND = -1
    START_NEW_GAME = 0
    ADD_PLAYER_MOVE = 1
    ACK_ADD_PLAYER_MOVE = 2
    FINISH_GAME = 3
