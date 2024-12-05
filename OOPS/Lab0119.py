class Dog:

    # Attributes - Instance variables | Data variables
    name = None
    breed = None
    height = None
    weight = None
    race = None

def _init_(self,name,breed):
    print("PC")
    self.name=name
    self.breed=breed

def bark(self):
    print("Barking")

def sleep(self):
    print("who is sleep -> "+self.name)

def talk(self):
    pass


# Object Ref
chow_ref = Dog("chow","mastiff")
print(chow_ref.name)
chow_ref.sleep()
print(id(chow_ref))


mow_ref = Dog("mow","husky")
print(mow_ref.name)
mow_ref.sleep()
print(id(mow_ref))
