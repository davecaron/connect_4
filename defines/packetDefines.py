from dataclasses import dataclass
from logic.gameConfig import GameConfig
from defines.gameDefines import PlayerId
from defines.commandDefines import GameCommands


@dataclass
class GamePacket:
    command: int = GameCommands.NO_COMMAND
    gameConfig: GameConfig = GameConfig()
    playedColumn: int = -1
    playedRow: int = -1
    lastPlayerId: PlayerId = PlayerId.NO_PLAYER
    currentPlayerId: PlayerId = PlayerId.NO_PLAYER
    gameFinished: bool = False
    winningPlayerId: PlayerId = PlayerId.NO_PLAYER
