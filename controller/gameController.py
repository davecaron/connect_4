from time import sleep
from queue import Queue
from threading import Thread, Event, Lock

from controller.controllerABC import ControllerABC
from communication.PacketProcessor import PacketProcessor
from communication.GameCommunicator import GameCommunicator
from defines.packetDefines import GamePacket


class GameController(Thread, ControllerABC):

    REFRESH_TIME_SEC = 0.01

    def __init__(self, modelQueue: Queue, uiQueue: Queue):
        super().__init__()
        self._uiQueue = uiQueue
        self._packetProcessor = None
        self._modelCommunicator = GameCommunicator(modelQueue)
        self._commandsCallbackMap = {}
        self._packetsToSend = []
        self._lock = Lock()
        self._stopFlag = Event()

    def setCommandsCallbackMap(self, commandsCallbackMap):
        self._commandsCallbackMap = commandsCallbackMap

    def addPacketToSend(self, packet: GamePacket):
        with self._lock:
            self._packetsToSend.append(packet)

    def _needToSendPacket(self) -> bool:
        with self._lock:
            return len(self._packetsToSend) > 0

    def _sendLastPacketReceived(self):
        with self._lock:
            if len(self._packetsToSend) > 0:
                packet = self._packetsToSend.pop()
                self._modelCommunicator.addPacket(packet)

    def _initPacketProcessor(self):
        self._packetProcessor = PacketProcessor(self._uiQueue, self._commandsCallbackMap)

    def __isStopped(self) -> bool:
        return self._stopFlag.is_set()

    def stop(self):
        self._stopFlag.set()

    def run(self):
        self._initPacketProcessor()

        while not self.__isStopped():
            self._packetProcessor.executeLastCommand()
            self._sendLastPacketReceived()

            sleep(self.REFRESH_TIME_SEC)
