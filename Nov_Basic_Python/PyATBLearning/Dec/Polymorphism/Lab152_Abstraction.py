from abc import ABC,abstractmethod

class ExcelReader(ABC):
    @abstractmethod
    def readFromExcel(self):
        pass

class Browser(ExcelReader):
    @abstractmethod
    def startBrowser(self):
        pass

class TC1():
    def startBrowser(self):
        print("starting")

    def stopBrowser(self):
        print("stop")

    def readFromExcel(self):
        print("readFromExcel is ready")

    def runTC(self):
        self.startBrowser()
        self.readFromExcel()
        self.stopBrowser()

tc1=TC1()
tc1.runTC()