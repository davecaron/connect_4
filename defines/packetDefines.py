from dataclasses import dataclass
from logic.gameData import GameData
from defines.gameDefines import PlayerId
from defines.commandDefines import GameCommands


@dataclass
class GamePacket:
    command: int = GameCommands.NO_COMMAND
    gameData: GameData = GameData()
    playedColumn: int = -1
    playedRow: int = -1
    gameFinished: bool = False
    winningPlayer: PlayerId = PlayerId.NO_PLAYER
