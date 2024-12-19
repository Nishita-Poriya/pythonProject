from abc import ABC,abstractmethod
from tkinter.font import names


class Father(ABC):
    def __init__(self,name):
        self.name= name

    @abstractmethod
    def loan(self):
        pass

class Son(Father):
    def loan(self):
        print("1L given")


nishita_obj = Son("Nishita")
nishita_obj.loan()