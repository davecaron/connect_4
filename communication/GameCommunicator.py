from queue import Queue
from _queue import Empty
from communication.Communicator import Communicator
from defines.packetDefines import GamePacket


class GameCommunicator(Communicator):

    def __init__(self, queue: Queue):
        super().__init__()
        self._gameDataQueue = queue

    def getLastPacket(self) -> GamePacket:
        packet: GamePacket = GamePacket()

        try:
            packet = self._gameDataQueue.get_nowait()
            self._gameDataQueue.task_done()
        except Empty:
            pass

        return packet

    def addPacket(self, packet: GamePacket):
        self._gameDataQueue.put(packet)
