from logic.gameData import GameData
from defines.commandDefines import GameCommands
from defines.packetDefines import GamePacket
from defines.gameDefines import PlayerId


class GamePacketBuilder:

    @staticmethod
    def getPacket(command: GameCommands = None, gameData: GameData = None, playedColumn: int = -1, playedRow: int = -1,
                  gameFinished=False, currentPlayerId: PlayerId = PlayerId.NO_PLAYER, winningPlayerId: PlayerId = PlayerId.NO_PLAYER) -> GamePacket:
        return GamePacket(command=command, gameData=gameData, playedColumn=playedColumn, playedRow=playedRow,
                          currentPlayerId=currentPlayerId, gameFinished=gameFinished, winningPlayerId=winningPlayerId)
