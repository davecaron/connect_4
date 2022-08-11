from abc import ABCMeta, abstractmethod


class ControllerABC(metaclass=ABCMeta):

    @abstractmethod
    def setCommandsCallbackMap(self, commandsCallbackMap):
        pass

    @abstractmethod
    def addPacketToSend(self, packet):
        pass
