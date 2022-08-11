from abc import ABCMeta, abstractmethod


class PacketBuilder(metaclass=ABCMeta):

    @abstractmethod
    def getPacket(self, **arguments):
        pass

    @abstractmethod
    def _getValidArguments(self, **arguments):
        pass
