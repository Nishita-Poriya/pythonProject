class Person:

#attributes
    id =None
    name = None
    age=None
    email=None
    height=None
    gender=None
    phone_no=None
    address=None

#behaviour
def talk(self):
    print("I can talk")

def sleep(self,name):
    print("I am method:")
    print("sleep",name)

def sleep2(self,name):
    print("I am a method")

def walk(self):
    print("I am walking")

def walk_return(self):
    return "I am Walking"

#creat an Object of the class
#objectRef=ClassName()->Object

geeta=Person()
geeta.name="Geeta sharma"
geeta.gender="Female"
