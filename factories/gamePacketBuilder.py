from factories.packetBuilder import PacketBuilder
import dataclasses
from defines.packetDefines import GamePacket


class GamePacketBuilder(PacketBuilder):

    def __init__(self):
        super().__init__()

    def getPacket(self, **arguments):
        validArguments = self._getValidArguments(**arguments)

        return GamePacket(**validArguments)

    def _getValidArguments(self, **arguments):
        gamePacketDict = dataclasses.asdict(GamePacket())
        validArguments = dict()

        for argument, value in arguments.items():
            if argument in gamePacketDict:
                validArguments[argument] = value

        return validArguments
