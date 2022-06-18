from abc import ABC, abstractmethod


class Communicator(ABC):

    @abstractmethod
    def getLastPacket(self):
        pass

    @abstractmethod
    def addPacket(self, packet):
        pass
