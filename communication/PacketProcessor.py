from queue import Queue
from communication.GameCommunicator import GameCommunicator
from defines.packetDefines import GamePacket


class PacketProcessor:

    def __init__(self, queue: Queue, commandsCallbackMap):
        self._communicator = GameCommunicator(queue)
        self._commandsCallbackMap = commandsCallbackMap

    def executeLastCommand(self):
        lastCommand = None
        gamePacket = self._communicator.getLastPacket()

        if self._isPacketValid(gamePacket):
            lastCommand = gamePacket.command

        if lastCommand in self._commandsCallbackMap:
            self._commandsCallbackMap[lastCommand](gamePacket)

    def _isPacketValid(self, packet: GamePacket) -> bool:
        return isinstance(packet, GamePacket)
