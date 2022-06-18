from logic.gameData import GameData
from defines.commandDefines import GameCommands
from defines.packetDefines import GamePacket
from defines.gameDefines import PlayerId


class GamePacketFactory:

    @staticmethod
    def getPacket(command: GameCommands = None, gameData: GameData = None, playedColumn: int = -1, playedRow: int = -1,
                  gameFinished=False, winningPlayer: PlayerId = None) -> GamePacket:
        return GamePacket(command=command, gameData=gameData, playedColumn=playedColumn, playedRow=playedRow,
                          gameFinished=gameFinished, winningPlayer=winningPlayer)
