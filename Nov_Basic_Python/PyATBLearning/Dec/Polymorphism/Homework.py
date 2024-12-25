'''
Create a Program
Class - PC
Class - MotherBoard
ab → start MotherBoard

Class - RAM
abstractMethod → start ram

Class - Processor
abstractMethod → start processor

Class - Storage
abstractMethod → storage data,

static method
loadOS

non static
startMouse
UseHeadPhone

'''
from abc import ABC,abstractmethod

class PC():
    def __init__(self):
        print("Started PC")

    @staticmethod
    def loadOS():
        print("start to Load OS")

    def startMouse(self):
        print("start using mouse")

    def UseHeadPhone(self):
        print("Start to UseHeadPhone")


class MotherBoard():

    def start(self):
        print("motherboard is started")

class RAM(ABC):

    @abstractmethod
    def start_ram(self):
        pass

class Processor(ABC):

    @abstractmethod
    def start_processor(self):
        pass

class Storage(ABC):
    @abstractmethod
    def data_storage(self):
        pass

obj1=PC()
obj1.loadOS()
obj1.startMouse()
obj1.UseHeadPhone()