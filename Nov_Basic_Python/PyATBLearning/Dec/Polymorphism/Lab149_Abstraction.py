# Abstraction
# Hide the details and show what is required.
from abc import ABC,abstractmethod

# Car - with key _ __private, tyres -> public,

# Car -> multiple - Engine, GearBox
# Car -> driver -> Engine, gearbox?

class Animal(ABC):
    def __init__(self,name):
        self.name=name

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Bark Bark........")


object_ref=Dog("Puppy")
object_ref.make_sound()


